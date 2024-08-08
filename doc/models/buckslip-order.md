
# Buckslip Order

## Structure

`BuckslipOrder`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date_created` | `datetime` | Required | A timestamp in ISO 8601 format of the date the resource was created. |
| `date_modified` | `datetime` | Required | A timestamp in ISO 8601 format of the date the resource was last modified. |
| `deleted` | `bool` | Optional | Only returned if the resource has been successfully deleted. |
| `object` | `str` | Required | Value is resource type. |
| `id` | `str` | Optional | Unique identifier prefixed with `bo_`.<br>**Constraints**: *Pattern*: `^bo_[a-zA-Z0-9]+$` |
| `buckslip_id` | `str` | Optional | Unique identifier prefixed with `bck_`.<br>**Constraints**: *Pattern*: `^bck_[a-zA-Z0-9]+$` |
| `status` | [`StatusEnum`](../../doc/models/status-enum.md) | Optional | - |
| `quantity_ordered` | `float` | Optional | The quantity of buckslips ordered.<br>**Default**: `0` |
| `unit_price` | `float` | Optional | The unit price for the buckslip order.<br>**Default**: `0` |
| `inventory` | `float` | Optional | The inventory of the buckslip order.<br>**Default**: `0` |
| `cancelled_reason` | `str` | Optional | The reason for cancellation. |
| `availability_date` | `datetime` | Optional | A timestamp in ISO 8601 format of the date the resource was created. |
| `expected_availability_date` | `datetime` | Optional | The fixed deadline for the buckslips to be printed. |

## Example (as JSON)

```json
{
  "date_created": "2016-03-13T12:52:32.123Z",
  "date_modified": "2016-03-13T12:52:32.123Z",
  "object": "object2",
  "quantity_ordered": 0.0,
  "unit_price": 0,
  "inventory": 0,
  "deleted": false,
  "id": "id0",
  "buckslip_id": "buckslip_id6",
  "status": "cancelled"
}
```

