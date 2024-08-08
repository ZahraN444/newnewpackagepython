
# Buckslip Updatable

## Structure

`BuckslipUpdatable`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | Description of the buckslip.<br>**Constraints**: *Maximum Length*: `255` |
| `auto_reorder` | `bool` | Optional | Allows for auto reordering |
| `reorder_quantity` | `float` | Optional | The quantity of items to be reordered (only required when auto_reorder is true).<br>**Constraints**: `>= 5000`, `<= 10000000` |

## Example (as JSON)

```json
{
  "description": "description0",
  "auto_reorder": false,
  "reorder_quantity": 114.28
}
```

