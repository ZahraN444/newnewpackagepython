
# Tracking Event Certified

## Structure

`TrackingEventCertified`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | Unique identifier prefixed with `evnt_`.<br>**Constraints**: *Pattern*: `^evnt_[a-zA-Z0-9]+$` |
| `time` | `datetime` | Optional | A timestamp in ISO 8601 format of the date USPS registered the event. |
| `date_created` | `datetime` | Required | A timestamp in ISO 8601 format of the date the resource was created. |
| `date_modified` | `datetime` | Required | A timestamp in ISO 8601 format of the date the resource was last modified. |
| `object` | [`Object3Enum`](../../doc/models/object-3-enum.md) | Required | - |
| `mtype` | `str` | Required, Constant | a Certified letter tracking event<br>**Default**: `'certified'` |
| `name` | [`Name1Enum`](../../doc/models/name-1-enum.md) | Required | - |
| `details` | [`TrackingEventDetails`](../../doc/models/tracking-event-details.md) | Optional | - |
| `location` | `str` | Optional | The zip code in which the event occurred if it exists, otherwise will be the name of a Regional Distribution Center if it exists, otherwise will be null. |

## Example (as JSON)

```json
{
  "id": "id2",
  "date_created": "2016-03-13T12:52:32.123Z",
  "date_modified": "2016-03-13T12:52:32.123Z",
  "object": "tracking_event",
  "type": "certified",
  "name": "Re-Routed",
  "time": "2016-03-13T12:52:32.123Z",
  "details": {
    "event": "pickup_available",
    "description": "description0",
    "notes": "notes0",
    "action_required": false
  },
  "location": "location6"
}
```

