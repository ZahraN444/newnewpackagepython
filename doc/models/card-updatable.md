
# Card Updatable

## Structure

`CardUpdatable`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | Description of the card.<br>**Constraints**: *Maximum Length*: `255` |
| `auto_reorder` | `bool` | Optional | Allows for auto reordering |
| `reorder_quantity` | `float` | Optional | The quantity of items to be reordered (only required when auto_reorder is true).<br>**Constraints**: `>= 10000`, `<= 10000000` |

## Example (as JSON)

```json
{
  "description": "description8",
  "auto_reorder": false,
  "reorder_quantity": 49.66
}
```

