
# Link Single

## Structure

`LinkSingle`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `redirect_link` | `str` | Required | The original target URL. |
| `domain` | `str` | Optional | The registered domain to be used for the short URL. |
| `slug` | `str` | Optional | The unique path for the shortened URL, if empty a unique path will be used. |
| `metadata_tag` | `Dict[str, str]` | Optional | Use metadata to store custom information for tagging and labeling back to your internal systems. Must be an object with up to 20 key-value pairs. Keys must be at most 40 characters and values must be at most 500 characters. Neither can contain the characters `"` and `\`. i.e. '{"customer_id" : "NEWYORK2015"}' Nested objects are not supported.  See [Metadata](#section/Metadata) for more information. |
| `billing_group_id` | `str` | Optional | An optional string with the billing group ID to tag your usage with. Is used for billing purposes. Requires special activation to use. See <a href="#tag/Billing-Groups">Billing Group API</a> for more information. |

## Example (as JSON)

```json
{
  "redirect_link": "redirect_link4",
  "domain": "domain0",
  "slug": "slug8",
  "metadata_tag": {
    "key0": "metadata_tag0",
    "key1": "metadata_tag9"
  },
  "billing_group_id": "billing_group_id6"
}
```

