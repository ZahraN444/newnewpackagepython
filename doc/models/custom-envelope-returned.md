
# Custom Envelope Returned

A nested custom envelope object containing more information about the custom envelope used or `null` if a custom envelope was not used.

## Structure

`CustomEnvelopeReturned`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | The unique identifier of the custom envelope used.<br>**Constraints**: *Maximum Length*: `40` |
| `url` | `str` | Required | The url of the envelope asset used. |
| `object` | `str` | Required, Constant | **Default**: `'envelope'` |

## Example (as JSON)

```json
{
  "id": "id6",
  "url": "url0",
  "object": "envelope"
}
```

