# AGENTS.md

## Project

GAVFS (General Autonomous Vehicle Feed Specification) is a draft open, provider-neutral format for autonomous ride-hailing discovery, coverage, products, pickup ETAs, fare estimates and booking handoff. Its goal is to help mapping and transit applications include autonomous services in multimodal planning.

This repository is a **specification**, not a production API or client application. Keep its documentation in Markdown for now. The canonical normative document is [spec/1.0.md](spec/1.0.md).

## Read these first

- [README.md](README.md): project motivation, overview, resource list and validation instructions
- [spec/1.0.md](spec/1.0.md): normative requirements and field reference
- [schema/README.md](schema/README.md) and [schema/](schema/): JSON Schema Draft 2020-12 definitions
- [examples/README.md](examples/README.md) and [examples/](examples/): illustrative payloads
- [CONTRIBUTING.md](CONTRIBUTING.md): contribution guidance

## How to contribute

1. Read the relevant section of the normative specification before editing.
2. Prefer GTFS/GBFS-style reference documentation: clear definitions, tables of fields, type, presence and description, and examples.
3. Use MUST, SHOULD and MAY consistently. State whether fields are REQUIRED, OPTIONAL or CONDITIONAL.
4. When adding or changing a field, update the specification, matching JSON Schema and example response together.
5. Run `pip install -r requirements-dev.txt && python scripts/validate.py`. Do not claim validation passed unless you ran it.
6. Keep examples fictional and avoid secrets, actual rider data or proprietary provider endpoints.
7. Preserve the one-provider-per-feed model and provider-owned booking handoff. Do not introduce rider authentication, dispatch or payments into the core specification without explicit design discussion.
8. Flag unresolved interoperability questions instead of silently inventing new normative behavior.

## Conventions

- `gavfs.json` is the manifest; `provider.json` is singular.
- A provider MAY advertise a manifest URL through `/.well-known/gavfs.json` on its public domain; see the normative hosting section.
- `has_surge` indicates whether surge pricing can occur in a service area, not whether it is active now.
- `fare.expires_at` is an optional price validity timestamp, not a booking reservation or guarantee.
- All feed URLs use HTTPS. Coordinates use WGS 84. GeoJSON positions are longitude-first.
- Keep the draft implementation-neutral and avoid creating a documentation site unless requested.
