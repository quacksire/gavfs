# GAVFS — General Autonomous Vehicle Feed Specification

**Draft 1.0 — Work in progress**

GAVFS is an open JSON specification for autonomous ride-hailing discovery, trip planning and booking handoff. Inspired by GBFS and GTFS, it lets mapping and transit applications integrate multiple autonomous mobility providers.

## Why GAVFS?

Autonomous ride-hailing is becoming part of the transportation network, but information about these services is often available only through each provider's own application or proprietary integrations. This makes it difficult for riders to discover whether a service operates where they need to travel, compare it with other transportation options, or include it in a multimodal journey.

Public transportation has benefited from common data specifications such as GTFS, while shared mobility services use GBFS to make service information available across many applications. Autonomous ride-hailing needs a similar, provider-neutral way to share rider-facing information.

GAVFS aims to make autonomous ride-hailing discoverable and usable from the maps, transit planners, and other mobility applications people already use. With a common format, a consumer can identify providers, display service coverage, retrieve pickup times and estimated fares, and hand a rider off to the provider to complete a booking.

The specification is intended to support interoperability without requiring providers to expose their dispatch systems or give third parties control over bookings. Providers remain responsible for the ride experience, while consumers can help riders understand how autonomous services fit into a broader trip.

## Principles

- One provider per feed, identified by `provider.json`.
- No rider authentication required for discovery, ETA or trip planning. Providers may require consumer app keys for rate limiting.
- Trip planning returns provider-generated deep links. Booking, payments and identity checks happen in the provider's app.
- Trip fares and pickup times are estimates unless expressly guaranteed.
- `service_areas.json` includes `has_surge`, indicating whether surge pricing may occur in a service area.

## Resources

| Resource | Description |
| --- | --- |
| `gavfs.json` | Feed discovery |
| `provider.json` | Provider identity and booking support |
| `service_areas.json` | Geographic coverage and surge policy |
| `products.json` | Ride products, amenities and accessibility |
| `eta` | Pickup time estimates |
| `trip_planning` | Trip estimates and deep-link handoff |
| `service_status.json` | Optional operating status |

Read the [draft 1.0 specification](spec/1.0.md), [example payloads](examples/README.md), and [contribution guidelines](CONTRIBUTING.md).

This is an early draft, not a ratified standard. Field names and requirements may change before release.

## Validation

The repository includes [JSON Schemas](schema/README.md), [standalone example responses](examples/README.md), and a [GitHub Actions workflow](.github/workflows/validate.yml) for pull-request validation.

```bash
pip install -r requirements-dev.txt
python scripts/validate.py
```

**Current limitations:** Schemas validate payload structure, but do not yet verify cross-feed IDs, GeoJSON topology, overlapping areas or all fare consistency rules. The draft is not yet implementation-certified.
