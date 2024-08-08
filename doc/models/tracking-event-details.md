
# Tracking Event Details

## Structure

`TrackingEventDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `event` | [`EventEnum`](../../doc/models/event-enum.md) | Required | - |
| `description` | `str` | Required | The description as listed in the description for event. |
| `notes` | `str` | Optional | Event-specific notes from USPS about the tracking event. |
| `action_required` | `bool` | Required | `true` if action is required by the end recipient, `false` otherwise. |

## Example (as JSON)

```json
{
  "event": "contact_carrier",
  "description": "description4",
  "notes": "notes4",
  "action_required": false
}
```

