
# Templates Response 2

## Structure

`TemplatesResponse2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Unique identifier prefixed with `tmpl_`. ID of a saved [HTML template](#section/HTML-Templates).<br>**Constraints**: *Pattern*: `^tmpl_[a-zA-Z0-9]+$` |
| `deleted` | `bool` | Optional | Only returned if the resource has been successfully deleted. |

## Example (as JSON)

```json
{
  "id": "id6",
  "deleted": false
}
```

