# Example GAVFS payloads

Examples are illustrative and use fictional providers, coordinates and prices. They are not live services.

## provider.json
```json
{
  "last_updated": "2026-09-26T08:30:00Z",
  "data": {
    "provider_id": "example_av",
    "name": "Example AV",
    "url": "https://example.com",
    "timezone": "America/Los_Angeles",
    "language": "en",
    "support": {"url": "https://example.com/support"},
    "booking": {
      "deep_link": "exampleav://ride",
      "web_url": "https://example.com/ride"
    }
  }
}
```

## service_areas.json
```json
{
  "last_updated": "2026-09-26T08:30:00Z",
  "data": {
    "service_areas": [{
      "area_id": "sf",
      "name": "San Francisco",
      "geometry": {
        "type": "Polygon",
        "coordinates": [[[-122.52,37.70],[-122.35,37.70],[-122.35,37.83],[-122.52,37.83],[-122.52,37.70]]]
      },
      "pickup_allowed": true,
      "dropoff_allowed": true,
      "has_surge": false
    }]
  }
}
```

## products.json
```json
{
  "last_updated": "2026-09-26T08:30:00Z",
  "data": {
    "products": [{
      "product_id": "standard",
      "name": "Standard",
      "description": "Private autonomous ride",
      "capacity": {"passengers": 4},
      "amenities": ["climate_control", "usb_charging"],
      "accessibility": {"wheelchair_accessible": false, "service_animals_allowed": true}
    }]
  }
}
```

## GET /eta?lat=37.77&lon=-122.42
```json
{
  "last_updated": "2026-09-26T08:30:00Z",
  "data": {
    "location": {"lat": 37.77, "lon": -122.42},
    "estimates": [{"product_id": "standard", "pickup_eta_seconds": 240}]
  }
}
```

## GET /trip_planning?start_lat=37.77&start_lon=-122.42&end_lat=37.78&end_lon=-122.40
```json
{
  "last_updated": "2026-09-26T08:30:00Z",
  "data": {
    "trips": [{
      "product_id": "standard",
      "pickup_eta_seconds": 240,
      "duration_seconds": 900,
      "fare": {"currency": "USD", "amount": 18.72, "type": "estimated"},
      "booking": {
        "deep_link": "exampleav://ride?origin=37.77,-122.42&destination=37.78,-122.40&product=standard",
        "web_url": "https://example.com/ride?origin=37.77,-122.42&destination=37.78,-122.40"
      }
    }]
  }
}
```
