
# Event Type

## Structure

`EventType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | [postcard_types](../../doc/models/postcard-types-enum.md) \| [self_mailer_types](../../doc/models/self-mailer-types-enum.md) \| [letter_types](../../doc/models/letter-types-enum.md) \| [check_types](../../doc/models/check-types-enum.md) \| [address_types](../../doc/models/address-types-enum.md) \| [bank_account_types](../../doc/models/bank-account-types-enum.md) | Required | This is a container for one-of cases. |
| `enabled_for_test` | `bool` | Required | Value is `true` if the event type is enabled in both the test and live environments and `false` if it is only enabled in the live environment. |
| `resource` | [`ResourceEnum`](../../doc/models/resource-enum.md) | Required | - |
| `object` | `str` | Required, Constant | Value is resource type.<br>**Default**: `'event_type'` |

## Example (as JSON)

```json
{
  "id": "postcard.international_exit",
  "enabled_for_test": false,
  "resource": "addresses",
  "object": "event_type"
}
```

