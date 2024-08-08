
# Template

## Structure

`Template`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | An internal description that identifies this resource. Must be no longer than 255 characters.<br>**Constraints**: *Maximum Length*: `255` |
| `id` | `str` | Required | Unique identifier prefixed with `tmpl_`. ID of a saved [HTML template](#section/HTML-Templates).<br>**Constraints**: *Pattern*: `^tmpl_[a-zA-Z0-9]+$` |
| `versions` | [`List[TemplateVersion]`](../../doc/models/template-version.md) | Required | An array of all non-deleted [version objects](#tag/Template-Versions) associated with the template. |
| `published_version` | [`TemplateVersion`](../../doc/models/template-version.md) | Required | - |
| `object` | [`Object12Enum`](../../doc/models/object-12-enum.md) | Optional | - |
| `metadata` | `Dict[str, str]` | Optional | Use metadata to store custom information for tagging and labeling back to your internal systems. Must be an object with up to 20 key-value pairs. Keys must be at most 40 characters and values must be at most 500 characters. Neither can contain the characters `"` and `\`. i.e. '{"customer_id" : "NEWYORK2015"}' Nested objects are not supported.  See [Metadata](#section/Metadata) for more information. |
| `date_created` | `datetime` | Optional | A timestamp in ISO 8601 format of the date the resource was created. |
| `date_modified` | `datetime` | Optional | A timestamp in ISO 8601 format of the date the resource was last modified. |
| `deleted` | `bool` | Optional | Only returned if the resource has been successfully deleted. |

## Example (as JSON)

```json
{
  "id": "id6",
  "versions": [
    {
      "html": "html0",
      "date_created": "2016-03-13T12:52:32.123Z",
      "date_modified": "2016-03-13T12:52:32.123Z",
      "object": "version",
      "id": "id0",
      "description": "description0",
      "engine": {
        "key1": "val1",
        "key2": "val2"
      },
      "required_vars": [
        "required_vars3"
      ],
      "deleted": false,
      "suggest_json_editor": false
    }
  ],
  "published_version": {
    "html": "html4",
    "date_created": "2016-03-13T12:52:32.123Z",
    "date_modified": "2016-03-13T12:52:32.123Z",
    "object": "version",
    "id": "id4",
    "description": "description4",
    "engine": {
      "key1": "val1",
      "key2": "val2"
    },
    "required_vars": [
      "required_vars7"
    ],
    "deleted": false,
    "suggest_json_editor": false
  },
  "description": "description4",
  "object": "template",
  "metadata": {
    "key0": "metadata7"
  },
  "date_created": "2016-03-13T12:52:32.123Z",
  "date_modified": "2016-03-13T12:52:32.123Z"
}
```

