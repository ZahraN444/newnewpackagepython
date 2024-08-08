
# Datum

## Structure

`Datum`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `row_number` | `float` | Optional | The row number of the csv file containing this data. |
| `status` | [`Status4Enum`](../../doc/models/status-4-enum.md) | Optional | - |
| `error_message` | `str` | Optional | The error message detailing the reason why processing the line item failed. |
| `mailpiece_id` | `str` | Optional | The mailpiece id created from the line item when it was validated. |
| `original_data` | [`object`](../../doc/models/object-enum.md) | Optional | Key-value pairs where each key is the column header and each value is the value of the column for the row. |

## Example (as JSON)

```json
{
  "rowNumber": 28.48,
  "status": "Processing",
  "errorMessage": "errorMessage0",
  "mailpieceId": "mailpieceId8",
  "originalData": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

