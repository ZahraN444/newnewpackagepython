
# Self Mailer

## Structure

`SelfMailer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | An internal description that identifies this resource. Must be no longer than 255 characters.<br>**Constraints**: *Maximum Length*: `255` |
| `metadata` | `Dict[str, str]` | Optional | Use metadata to store custom information for tagging and labeling back to your internal systems. Must be an object with up to 20 key-value pairs. Keys must be at most 40 characters and values must be at most 500 characters. Neither can contain the characters `"` and `\`. i.e. '{"customer_id" : "NEWYORK2015"}' Nested objects are not supported.  See [Metadata](#section/Metadata) for more information. |
| `mail_type` | [`MailTypeEnum`](../../doc/models/mail-type-enum.md) | Optional | - |
| `merge_variables` | [`object`](../../doc/models/object-enum.md) | Optional | You can input a merge variable payload object to your template to render dynamic content. For example, if you have a template like: `{{variable_name}}`, pass in `{"variable_name": "Harry"}` to render `Harry`. `merge_variables` must be an object. Any type of value is accepted as long as the object is valid JSON; you can use `strings`, `numbers`, `booleans`, `arrays`, `objects`, or `null`. The max length of the object is 25,000 characters. If you call `JSON.stringify` on your object, it can be no longer than 25,000 characters. Your variable names cannot contain any whitespace or any of the following special characters: `!`, `"`, `#`, `%`, `&`, `'`, `(`, `)`, `*`, `+`, `,`, `/`, `;`, `<`, `=`, `>`, `@`, `[`, `\`, `]`, `^`, `````, `{`, `\|`, `}`, `~`. More instructions can be found in <a href="https://help.lob.com/print-and-mail/designing-mail-creatives/dynamic-personalization#using-html-and-merge-variables-10" target="_blank">our guide to using html and merge variables</a>. Depending on your <a href="https://dashboard.lob.com/#/settings/account" target="_blank">Merge Variable strictness</a> setting, if you define variables in your HTML but do not pass them here, you will either receive an error or the variable will render as an empty string. |
| `send_date` | [`object`](../../doc/models/object-enum.md) | Optional | - |
| `size` | [`SelfMailerSizeEnum`](../../doc/models/self-mailer-size-enum.md) | Optional | - |
| `to` | [`object`](../../doc/models/object-enum.md) | Required | - |
| `carrier` | `str` | Required, Constant | **Default**: `'USPS'` |
| `thumbnails` | [`List[Thumbnail]`](../../doc/models/thumbnail.md) | Optional | - |
| `expected_delivery_date` | `date` | Optional | A date in YYYY-MM-DD format of the mailpiece's expected delivery date based on its `send_date`. |
| `date_created` | `datetime` | Optional | A timestamp in ISO 8601 format of the date the resource was created. |
| `date_modified` | `datetime` | Optional | A timestamp in ISO 8601 format of the date the resource was last modified. |
| `deleted` | `bool` | Optional | Only returned if the resource has been successfully deleted. |
| `mfrom` | [`AddressUs`](../../doc/models/address-us.md) | Optional | - |
| `id` | `str` | Required | Unique identifier prefixed with `sfm_`.<br>**Constraints**: *Pattern*: `^sfm_[a-zA-Z0-9]+$` |
| `outside_template_id` | `str` | Optional | The unique ID of the HTML template used for the outside of the self mailer.<br>**Constraints**: *Pattern*: `^tmpl_[a-zA-Z0-9]+$` |
| `inside_template_id` | `str` | Optional | The unique ID of the HTML template used for the inside of the self mailer.<br>**Constraints**: *Pattern*: `^tmpl_[a-zA-Z0-9]+$` |
| `outside_template_version_id` | `str` | Optional | The unique ID of the specific version of the HTML template used for the outside of the self mailer.<br>**Constraints**: *Pattern*: `^vrsn_[a-zA-Z0-9]+$` |
| `inside_template_version_id` | `str` | Optional | The unique ID of the specific version of the HTML template used for the inside of the self mailer.<br>**Constraints**: *Pattern*: `^vrsn_[a-zA-Z0-9]+$` |
| `object` | [`Object11Enum`](../../doc/models/object-11-enum.md) | Optional | - |
| `tracking_events` | [`List[TrackingEventCertified]`](../../doc/models/tracking-event-certified.md) | Optional | An array of certified tracking events ordered by ascending `time`. Not populated in test mode. |
| `use_type` | [`object`](../../doc/models/object-enum.md) | Required | - |
| `url` | `str` | Required | A [signed link](#section/Asset-URLs) served over HTTPS. The link returned will expire in 30 days to prevent mis-sharing. Each time a GET request is initiated, a new signed URL will be generated.<br>**Constraints**: *Pattern*: `^https://lob-assets\.com/(letters\|postcards\|bank-accounts\|checks\|self-mailers\|cards)/[a-z]{3,4}_[a-z0-9]{15,16}(\.pdf\|_thumb_[a-z]+_[0-9]+\.png)\?(version=[a-z0-9-]*&)?expires=[0-9]{10}&signature=[a-zA-Z0-9-_]+$` |
| `fsc` | `bool` | Optional | This is in beta. Contact support@lob.com or your account contact to learn more. Not available for `11x9_bifold` self-mailer size.<br>**Default**: `False` |
| `status` | [`ThestatusofthebuckslipEnum`](../../doc/models/thestatusofthebuckslip-enum.md) | Optional | - |
| `failure_reason` | `str` | Optional | A string describing the reason for failure if the self mailer failed to render. |

## Example (as JSON)

```json
{
  "to": {
    "key1": "val1",
    "key2": "val2"
  },
  "carrier": "USPS",
  "id": "id4",
  "use_type": {
    "key1": "val1",
    "key2": "val2"
  },
  "url": "url8",
  "fsc": false,
  "description": "description6",
  "metadata": {
    "key0": "metadata9",
    "key1": "metadata0",
    "key2": "metadata1"
  },
  "mail_type": "usps_first_class",
  "merge_variables": {
    "key1": "val1",
    "key2": "val2"
  },
  "send_date": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

