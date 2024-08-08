
# Wordsatcheckbottom

## Structure

`Wordsatcheckbottom`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | An internal description that identifies this resource. Must be no longer than 255 characters.<br>**Constraints**: *Maximum Length*: `255` |
| `metadata` | `Dict[str, str]` | Optional | Use metadata to store custom information for tagging and labeling back to your internal systems. Must be an object with up to 20 key-value pairs. Keys must be at most 40 characters and values must be at most 500 characters. Neither can contain the characters `"` and `\`. i.e. '{"customer_id" : "NEWYORK2015"}' Nested objects are not supported.  See [Metadata](#section/Metadata) for more information. |
| `merge_variables` | [`object`](../../doc/models/object-enum.md) | Optional | You can input a merge variable payload object to your template to render dynamic content. For example, if you have a template like: `{{variable_name}}`, pass in `{"variable_name": "Harry"}` to render `Harry`. `merge_variables` must be an object. Any type of value is accepted as long as the object is valid JSON; you can use `strings`, `numbers`, `booleans`, `arrays`, `objects`, or `null`. The max length of the object is 25,000 characters. If you call `JSON.stringify` on your object, it can be no longer than 25,000 characters. Your variable names cannot contain any whitespace or any of the following special characters: `!`, `"`, `#`, `%`, `&`, `'`, `(`, `)`, `*`, `+`, `,`, `/`, `;`, `<`, `=`, `>`, `@`, `[`, `\`, `]`, `^`, `````, `{`, `\|`, `}`, `~`. More instructions can be found in <a href="https://help.lob.com/print-and-mail/designing-mail-creatives/dynamic-personalization#using-html-and-merge-variables-10" target="_blank">our guide to using html and merge variables</a>. Depending on your <a href="https://dashboard.lob.com/#/settings/account" target="_blank">Merge Variable strictness</a> setting, if you define variables in your HTML but do not pass them here, you will either receive an error or the variable will render as an empty string. |
| `send_date` | [`object`](../../doc/models/object-enum.md) | Optional | - |
| `mail_type` | [`MailType2Enum`](../../doc/models/mail-type-2-enum.md) | Optional | - |
| `memo` | `str` | Optional | Text to include on the memo line of the check.<br>**Constraints**: *Maximum Length*: `40` |
| `check_number` | `int` | Optional | An integer that designates the check number.<br>If `check_number` is not provided, checks created from a new `bank_account` will start at `10000` and increment with each check created with the `bank_account`.<br>A provided `check_number` overrides the defaults. Subsequent checks created with the same `bank_account` will increment from the provided check number.<br>**Constraints**: `>= 1`, `<= 500000000` |
| `message` | `str` | Required | Max of 400 characters to be included at the bottom of the check page.<br>**Constraints**: *Maximum Length*: `400` |
| `use_type` | [`object`](../../doc/models/object-enum.md) | Required | - |
| `to` | str \| [addressobjwithnamedefined](../../doc/models/addressobjwithnamedefined.md) \| [addressobjwithcompanydefined](../../doc/models/addressobjwithcompanydefined.md) | Required | This is a container for one-of cases. |
| `mfrom` | str \| [inline_address_us](../../doc/models/inline-address-us.md) | Required | This is a container for one-of cases. |
| `bank_account` | `str` | Required | **Constraints**: *Pattern*: `^bank_[a-zA-Z0-9]+$` |
| `amount` | `float` | Required | The payment amount to be sent in US dollars. Amounts will be rounded to two decimal places.<br>**Constraints**: `<= 999999.99` |
| `logo` | str \| None | Optional | This is a container for one-of cases. |
| `check_bottom` | [`object`](../../doc/models/object-enum.md) | Optional | - |
| `attachment` | str \| None | Optional | This is a container for one-of cases. |
| `billing_group_id` | `str` | Optional | An optional string with the billing group ID to tag your usage with. Is used for billing purposes. Requires special activation to use. See <a href="#tag/Billing-Groups">Billing Group API</a> for more information. |

## Example (as JSON)

```json
{
  "description": "description2",
  "metadata": {
    "key0": "metadata9",
    "key1": "metadata8"
  },
  "merge_variables": {
    "key1": "val1",
    "key2": "val2"
  },
  "send_date": {
    "key1": "val1",
    "key2": "val2"
  },
  "mail_type": "usps_first_class",
  "message": "message2",
  "use_type": {
    "key1": "val1",
    "key2": "val2"
  },
  "to": "String7",
  "from": "String1",
  "bank_account": "bank_account6",
  "amount": 83.14
}
```

