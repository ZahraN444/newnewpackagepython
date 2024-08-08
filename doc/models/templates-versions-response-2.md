
# Templates Versions Response 2

## Structure

`TemplatesVersionsResponse2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Unique identifier prefixed with `vrsn_`.<br>**Constraints**: *Pattern*: `^vrsn_[a-zA-Z0-9]+$` |
| `deleted` | `bool` | Optional | Only returned if the resource has been successfully deleted. |

## Example (as JSON)

```json
{
  "id": "id4",
  "deleted": false
}
```

