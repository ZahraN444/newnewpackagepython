
# Uploads Exports Response

## Structure

`UploadsExportsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | Unique identifier prefixed with `ex_`.<br>**Constraints**: *Pattern*: `^ex_[a-zA-Z0-9]+$` |
| `date_created` | `datetime` | Required | A timestamp in ISO 8601 format of the date the export was created |
| `date_modified` | `datetime` | Required | A timestamp in ISO 8601 format of the date the export was last modified |
| `deleted` | `bool` | Required | Returns as `true` if the resource has been successfully deleted. |
| `s_3_url` | `str` | Required | The URL for the generated export file. |
| `state` | [`StateEnum`](../../doc/models/state-enum.md) | Required | - |
| `mtype` | [`Type1Enum`](../../doc/models/type-1-enum.md) | Required | - |
| `upload_id` | `str` | Required | Unique identifier prefixed with `upl_`.<br>**Constraints**: *Pattern*: `^upl_[a-zA-Z0-9]+$` |

## Example (as JSON)

```json
{
  "id": "id8",
  "dateCreated": "2016-03-13T12:52:32.123Z",
  "dateModified": "2016-03-13T12:52:32.123Z",
  "deleted": false,
  "s3Url": "s3Url8",
  "state": "succeeded",
  "type": "failures",
  "uploadId": "uploadId8"
}
```

