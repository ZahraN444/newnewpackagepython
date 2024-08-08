
# Self Mailer Details Returned

Properties that the self mailers in your Creative should have. Check within in order to add a QR code to your creative.

## Structure

`SelfMailerDetailsReturned`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mail_type` | [`MailTypeEnum`](../../doc/models/mail-type-enum.md) | Optional | - |
| `size` | [`SelfMailerSizeEnum`](../../doc/models/self-mailer-size-enum.md) | Optional | - |
| `inside_original_url` | `str` | Optional | The original URL of the `inside` template.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `2083` |
| `outside_original_url` | `str` | Optional | The original URL of the `outside` template.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `2083` |

## Example (as JSON)

```json
{
  "mail_type": "usps_first_class",
  "size": "12x9_bifold",
  "inside_original_url": "inside_original_url8",
  "outside_original_url": "outside_original_url0"
}
```

