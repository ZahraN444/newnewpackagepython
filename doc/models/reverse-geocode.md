
# Reverse Geocode

## Structure

`ReverseGeocode`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Unique identifier prefixed with `us_reverse_geocode_`.<br>**Constraints**: *Pattern*: `^us_reverse_geocode_[a-zA-Z0-9_]+$` |
| `addresses` | [`List[Addresses]`](../../doc/models/addresses.md) | Optional | list of addresses |
| `object` | [`Object15Enum`](../../doc/models/object-15-enum.md) | Optional | - |

## Example (as JSON)

```json
{
  "id": "id2",
  "addresses": [
    {
      "components": {
        "zip_code": "zip_code0",
        "zip_code_plus_4": "zip_code_plus_48"
      },
      "location_analysis": {
        "latitude": 102.1,
        "longitude": 99.9,
        "distance": 58.56
      }
    }
  ],
  "object": "us_reverse_geocode_lookup"
}
```

