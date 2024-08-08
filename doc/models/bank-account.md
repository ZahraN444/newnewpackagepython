
# Bank Account

## Structure

`BankAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | An internal description that identifies this resource. Must be no longer than 255 characters.<br>**Constraints**: *Maximum Length*: `255` |
| `routing_number` | `str` | Required | Must be a <a href="https://www.frbservices.org/index.html" target="_blank">valid US routing number</a>.<br>**Constraints**: *Minimum Length*: `9`, *Maximum Length*: `9` |
| `account_number` | `str` | Required | **Constraints**: *Maximum Length*: `17` |
| `account_type` | [`AccountTypeEnum`](../../doc/models/account-type-enum.md) | Required | - |
| `signatory` | `str` | Required | The signatory associated with your account. This name will be printed on checks created with this bank account. If you prefer to use a custom signature image on your checks instead, please create your bank account from the <a href="https://dashboard.lob.com/#/login" target="_blank">Dashboard</a>.<br>**Constraints**: *Maximum Length*: `30` |
| `check_template` | [`CheckTemplateEnum`](../../doc/models/check-template-enum.md) | Optional | - |
| `fractional_routing_number` | `str` | Optional | The fractional routing number for your home bank account. Required for the `jpm` check template only. Please contact a bank representative if you do not know the fractional routing number associated with your home bank institution. |
| `city` | `str` | Optional | The city associated with your home bank account. Required for the `jpm` check template only. Please contact a bank representative if you do not know the city associated with your home bank institution. |
| `state` | `str` | Optional | The state associated with your home bank account. Required for the `jpm` check template only. Please contact a bank representative if you do not know the state associated with your home bank institution. |
| `zipcode` | `str` | Optional | The zipcode associated with your home bank account. Required for the `jpm` check template only. Please contact a bank representative if you do not know the zipcode associated with your home bank institution. |
| `metadata` | `Dict[str, str]` | Optional | Use metadata to store custom information for tagging and labeling back to your internal systems. Must be an object with up to 20 key-value pairs. Keys must be at most 40 characters and values must be at most 500 characters. Neither can contain the characters `"` and `\`. i.e. '{"customer_id" : "NEWYORK2015"}' Nested objects are not supported.  See [Metadata](#section/Metadata) for more information. |
| `date_created` | `datetime` | Required | A timestamp in ISO 8601 format of the date the resource was created. |
| `date_modified` | `datetime` | Required | A timestamp in ISO 8601 format of the date the resource was last modified. |
| `deleted` | `bool` | Optional | Only returned if the resource has been successfully deleted. |
| `object` | `str` | Required, Constant | Value is resource type.<br>**Default**: `'bank_account'` |
| `id` | `str` | Required | **Constraints**: *Pattern*: `^bank_[a-zA-Z0-9]+$` |
| `signature_url` | `str` | Optional | **Constraints**: *Pattern*: `^https://lob-assets\.com/(letters\|postcards\|bank-accounts\|checks\|self-mailers\|cards)/[a-z]{3,4}_[a-z0-9]{15,16}(\.pdf\|_thumb_[a-z]+_[0-9]+\.png)\?(version=[a-z0-9-]*&)?expires=[0-9]{10}&signature=[a-zA-Z0-9-_]+$` |
| `bank_name` | `str` | Optional | The name of the bank based on the provided routing number, e.g. `JPMORGAN CHASE BANK`. |
| `verified` | `bool` | Optional | A bank account must be verified before a check can be created. More info [here](#operation/bank_account_verify).<br>**Default**: `False` |

## Example (as JSON)

```json
{
  "id": "bank_a",
  "signature_url": "https://lob-assets.com/bank-accounts/asd_asdfghjkqwertyui.pdf?expires=1234567890&signature=aksdf",
  "bank_name": "JPMORGAN CHASE BANK",
  "verified": true,
  "object": "bank_account",
  "description": "Test Bank Account",
  "routing_number": "322271627",
  "account_number": "123456789",
  "signatory": "Jane Doe",
  "account_type": "individual",
  "metadat": {
    "spiffy": "true"
  },
  "date_created": "2019-08-08T19:34:47.571Z",
  "date_modified": "2019-08-08T19:34:47.571Z",
  "check_template": "common",
  "fractional_routing_number": "fractional_routing_number6",
  "city": "city4",
  "state": "state0"
}
```

