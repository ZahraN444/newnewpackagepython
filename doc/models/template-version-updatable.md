
# Template Version Updatable

## Structure

`TemplateVersionUpdatable`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | An internal description that identifies this resource. Must be no longer than 255 characters.<br>**Constraints**: *Maximum Length*: `255` |
| `engine` | [`object`](../../doc/models/object-enum.md) | Optional | - |
| `required_vars` | `List[str]` | Optional | An array of required variables to be used in a template. Only available for `handlebars` templates. |

## Example (as JSON)

```json
{
  "description": "description0",
  "engine": {
    "key1": "val1",
    "key2": "val2"
  },
  "required_vars": [
    "required_vars1",
    "required_vars0",
    "required_vars9"
  ]
}
```

