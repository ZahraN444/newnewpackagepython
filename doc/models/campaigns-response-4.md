
# Campaigns Response 4

## Structure

`CampaignsResponse4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Unique identifier prefixed with `cmp_`.<br>**Constraints**: *Pattern*: `^cmp_[a-zA-Z0-9]+$` |
| `deleted` | `bool` | Optional | True if the resource has been successfully deleted. |

## Example (as JSON)

```json
{
  "id": "id2",
  "deleted": false
}
```

