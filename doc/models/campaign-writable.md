
# Campaign Writable

## Structure

`CampaignWritable`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `billing_group_id` | `str` | Optional | Unique identifier prefixed with `bg_`.<br>**Constraints**: *Pattern*: `^bg_[a-zA-Z0-9]+$` |
| `name` | `str` | Required | Name of the campaign. |
| `description` | `str` | Optional | An internal description that identifies this resource. Must be no longer than 255 characters.<br>**Constraints**: *Maximum Length*: `255` |
| `schedule_type` | `str` | Required, Constant | How the campaign should be scheduled. Only value available today is `immediate`.<br>**Default**: `'immediate'` |
| `target_delivery_date` | `datetime` | Optional | If `schedule_type` is `target_delivery_date`, provide a targeted delivery date for mail pieces in this campaign. |
| `send_date` | `datetime` | Optional | If `schedule_type` is `scheduled_send_date`, provide a date to send this campaign. |
| `cancel_window_campaign_minutes` | `int` | Optional | A window, in minutes, within which the campaign can be canceled. |
| `metadata` | `Dict[str, str]` | Optional | Use metadata to store custom information for tagging and labeling back to your internal systems. Must be an object with up to 20 key-value pairs. Keys must be at most 40 characters and values must be at most 500 characters. Neither can contain the characters `"` and `\`. i.e. '{"customer_id" : "NEWYORK2015"}' Nested objects are not supported.  See [Metadata](#section/Metadata) for more information. |
| `use_type` | [`object`](../../doc/models/object-enum.md) | Required | - |
| `auto_cancel_if_ncoa` | `bool` | Optional | Whether or not a mail piece should be automatically canceled and not sent if the address is updated via NCOA. |

## Example (as JSON)

```json
{
  "name": "name8",
  "schedule_type": "immediate",
  "use_type": {
    "key1": "val1",
    "key2": "val2"
  },
  "billing_group_id": "billing_group_id0",
  "description": "description8",
  "target_delivery_date": "2016-03-13T12:52:32.123Z",
  "send_date": "2016-03-13T12:52:32.123Z",
  "cancel_window_campaign_minutes": 58
}
```

