
# Card Editable

## Structure

`CardEditable`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | Description of the card.<br>**Constraints**: *Maximum Length*: `255` |
| `size` | [`Size1Enum`](../../doc/models/size-1-enum.md) | Optional | - |
| `front` | str | Required | This is a container for one-of cases. |
| `back` | str \| None | Optional | This is a container for one-of cases. |

## Example (as JSON)

```json
{
  "description": "description8",
  "size": "3.375x2.125",
  "front": "String9",
  "back": "String7"
}
```

