
# Tracking Event Base

As mail pieces travel through the mail stream, USPS scans their unique barcodes, and Lob processes these mail scans to generate tracking events.

## Structure

`TrackingEventBase`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | Unique identifier prefixed with `evnt_`.<br>**Constraints**: *Pattern*: `^evnt_[a-zA-Z0-9]+$` |
| `time` | `datetime` | Optional | A timestamp in ISO 8601 format of the date USPS registered the event. |
| `date_created` | `datetime` | Required | A timestamp in ISO 8601 format of the date the resource was created. |
| `date_modified` | `datetime` | Required | A timestamp in ISO 8601 format of the date the resource was last modified. |
| `object` | [`Object3Enum`](../../doc/models/object-3-enum.md) | Required | - |

## Example (as JSON)

```json
{
  "id": "id2",
  "time": "2016-03-13T12:52:32.123Z",
  "date_created": "2016-03-13T12:52:32.123Z",
  "date_modified": "2016-03-13T12:52:32.123Z",
  "object": "tracking_event"
}
```

