
# Letters Response

## Structure

`LettersResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Unique identifier prefixed with `ltr_`.<br>**Constraints**: *Pattern*: `^ltr_[a-zA-Z0-9]+$` |
| `deleted` | `bool` | Optional | Only returned if the resource has been successfully deleted. |

## Example (as JSON)

```json
{
  "id": "id2",
  "deleted": false
}
```

