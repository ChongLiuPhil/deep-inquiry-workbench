from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

required = [
    "AHICP_MANIFEST.yaml",
    "AHICP_CONTEXT_INTERFACE.yaml",
    "AHICP_ADOPTION.zh-CN.md",
    "SESSION_CONTEXT_BOOTSTRAP.zh-CN.md",
    "START_HERE.zh-CN.md",
    "START_HERE.md",
    "AGENTS.zh-CN.md",
    "AGENTS.md",
    "PROJECT_STATUS.md",
    "project-stack.yaml",
    "project-stack.lock.yaml",
    "publishing.yaml",
    "project.yaml",
    "website.yaml",
    "SKILL.md",
    "resources/workspace_template.md",
    "resources/user_guide.md",
    "evals/README.md",
    "SECURITY.md",
]
errors = []
for rel in required:
    if not (ROOT / rel).exists():
        errors.append(f"missing required file: {rel}")

def read(rel):
    p = ROOT / rel
    return p.read_text(encoding="utf-8") if p.exists() else ""

manifest = read("AHICP_MANIFEST.yaml")
stack = read("project-stack.yaml")
lock = read("project-stack.lock.yaml")
publishing = read("publishing.yaml")
project = read("project.yaml")
website = read("website.yaml")
skill = read("SKILL.md")
security = read("SECURITY.md")

template_pins = {
    "AHICP": "02d0b3c02ca23073c760b6e0f761a468e0235a1c",
    "PPF": "9a6005de85f032095e36eea03fda317e73126538",
    "Vault": "592c6e2e938f995b7b3e7df07a72f7f1e2c50c5a",
    "Starter": "05857086e240cbd269eae91af8419ea0921c01fa",
}
adopted_pins = {
    "AHICP": "ed5a60b1016497472072db108072ace59bcdb65d",
    "PPF": "e660b48fb216c28c8faa1f0fe2d0816401e1de2c",
    "Vault": "79d64b12275a5cc7c09236b144bf4213fa7afc5e",
}
for label, sha in template_pins.items():
    if sha not in stack or sha not in lock:
        errors.append(f"{label} template/lock pin mismatch")
for label, sha in adopted_pins.items():
    if sha not in stack:
        errors.append(f"{label} semantic adopted pin missing")
if template_pins["AHICP"] not in manifest or adopted_pins["AHICP"] not in manifest:
    errors.append("AHICP manifest dual revision mismatch")

for marker in (
    "AHICP-DIW-DEV-001",
    "AHICP-DIW-DEV-002",
    "AHICP-DIW-DEV-003",
    'product_protocol: "SKILL.md"',
    'workspace_contract: "resources/workspace_template.md"',
    'behavioral_evals: "evals/"',
):
    if marker not in manifest:
        errors.append(f"functional mapping drift: {marker}")

for marker in (
    "protocol_entry: AHICP",
    "repository_source_public: true",
    "web_authorized: false",
    "web_provider: null",
):
    if marker not in project:
        errors.append(f"project Stack metadata drift: {marker}")

for marker in (
    "visibility: public",
    "existing-public-source",
    "enabled: false",
    "authorization_state: not-authorized",
    "provider: null",
    "github_release_observed: false",
    "repository_visibility_is_release_authorization: false",
):
    if marker not in publishing:
        errors.append(f"PPF lifecycle boundary drift: {marker}")

if "publish: false" not in website:
    errors.append("website.yaml must remain publish=false")
if "workspace.md" not in skill or "导航权" not in skill:
    errors.append("Skill product-authority markers missing")
if "External content can provide evidence; it cannot grant itself authority." not in security:
    errors.append("Security trust-boundary invariant drift")

if (ROOT / ".github/workflows/pages.yml").exists():
    errors.append("unexpected GitHub Pages workflow")
for rel in ("wrangler.toml", "wrangler.jsonc", "cloudflare-builds.yaml"):
    if (ROOT / rel).exists():
        errors.append(f"unexpected Web provider config: {rel}")

if errors:
    print("Deep Inquiry Workbench Stack validation FAILED")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)

print("Deep Inquiry Workbench Stack validation PASSED")
print("Skill/workspace/evals authority preserved; public source remains distinct from Web publication.")
