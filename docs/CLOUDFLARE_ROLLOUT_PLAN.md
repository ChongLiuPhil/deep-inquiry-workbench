# Cloudflare rollout plan — management-only

Status: **planning only**. Public source visibility does not authorize a public standalone Web deployment.

## Current-state preservation
- Preserve the public source repository and existing skill/tool release semantics.
- No production Web provider is treated as verified by this plan.
- Do not change repository visibility, releases, package/skill content, or canonical identity.

## Target management state
- Target provider for a future standalone Web surface: Cloudflare Workers / Static Assets.
- Planned Worker: `deep-inquiry-workbench`.
- Target Web visibility: restricted by default while source remains public.
- Reader policy reference: `shared-reader-access`.
- Preview visibility: private; previews disabled until Access acceptance.
- Production branch: `main`; commit-triggered only; no scheduled polling.
- Public bypass: disabled; no custom domain selected.
- Paid services: not authorized.

## Content/build boundary
This phase does not select or publish skill definitions, resources, evals, examples, documentation, or any other project content. Existing `publishing.yaml`, `website.yaml`, package/skill structure, and CI remain unchanged. A later phase must separately decide whether any Web surface is actually needed and, if so, approve its build/output contract.

## Manual/provider gates
Cloudflare login/MFA, Access baseline, reader approval, GitHub App authorization, Web-surface necessity/build choice, Worker/Builds reconciliation, runtime verification, and final release/cutover remain separate gates.

## Rollback
No provider state is changed here. Repository rollback is an ordinary revert PR. No paid upgrade, DNS change, or publication transition is authorized.
