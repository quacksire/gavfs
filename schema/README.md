# JSON Schemas

Schemas use JSON Schema Draft 2020-12. Each file validates a complete GAVFS response envelope, not only the `data` payload.

Run `pip install -r requirements-dev.txt && python scripts/validate.py` to validate the examples.

These schemas cover basic structural validation. Cross-feed references, service-area geometry validity, unique IDs, surge-area overlap, and fare range ordering require additional semantic checks.
