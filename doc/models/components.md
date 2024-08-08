
# Components

A nested object containing a breakdown of each component of a reverse geocoded response.

## Structure

`Components`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `zip_code` | `str` | Required | The 5-digit ZIP code<br>**Constraints**: *Pattern*: `^\d{5}$` |
| `zip_code_plus_4` | `str` | Required | **Constraints**: *Pattern*: `^\d{4}$` |

## Example (as JSON)

```json
{
  "zip_code": "zip_code0",
  "zip_code_plus_4": "zip_code_plus_48"
}
```

