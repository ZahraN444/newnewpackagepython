
# Intl Verification Base

## Structure

`IntlVerificationBase`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient` | `str` | Optional | The intended recipient, typically a person's or firm's name.<br>**Constraints**: *Maximum Length*: `500` |
| `primary_line` | `str` | Optional | The primary delivery line (usually the street address) of the address.<br>**Constraints**: *Maximum Length*: `200` |
| `secondary_line` | `str` | Optional | The secondary delivery line of the address. This field is typically empty but may contain information if `primary_line` is too long.<br>**Constraints**: *Maximum Length*: `500` |

## Example (as JSON)

```json
{
  "recipient": "recipient6",
  "primary_line": "primary_line4",
  "secondary_line": "secondary_line0"
}
```

