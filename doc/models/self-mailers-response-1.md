
# Self Mailers Response 1

## Structure

`SelfMailersResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Unique identifier prefixed with `sfm_`.<br>**Constraints**: *Pattern*: `^sfm_[a-zA-Z0-9]+$` |
| `deleted` | `bool` | Optional | Only returned if the resource has been successfully deleted. |

## Example (as JSON)

```json
{
  "id": "id8",
  "deleted": false
}
```

