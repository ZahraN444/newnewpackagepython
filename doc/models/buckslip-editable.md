
# Buckslip Editable

## Structure

`BuckslipEditable`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | Description of the buckslip.<br>**Constraints**: *Maximum Length*: `255` |
| `size` | [`SizeEnum`](../../doc/models/size-enum.md) | Optional | - |
| `front` | str | Required | This is a container for one-of cases. |
| `back` | str \| None | Optional | This is a container for one-of cases. |

## Example (as JSON)

```json
{
  "description": "description2",
  "size": "8.75x3.75",
  "front": "String9",
  "back": "String5"
}
```

