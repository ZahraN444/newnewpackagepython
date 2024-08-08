
# No Extra Service

## Structure

`NoExtraService`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tracking_events` | [`List[TrackingEventNormal]`](../../doc/models/tracking-event-normal.md) | Optional | An array of tracking events ordered by ascending `time`. |
| `cards` | [`List[Card]`](../../doc/models/card.md) | Optional | An array of cards associated with a specific letter |
| `buckslips` | [`List[Buckslip]`](../../doc/models/buckslip.md) | Optional | An array of buckslip(s) associated with a specific letter |
| `return_address` | [`object`](../../doc/models/object-enum.md) | Optional | - |
| `description` | `str` | Optional | An internal description that identifies this resource. Must be no longer than 255 characters.<br>**Constraints**: *Maximum Length*: `255` |
| `metadata` | `Dict[str, str]` | Optional | Use metadata to store custom information for tagging and labeling back to your internal systems. Must be an object with up to 20 key-value pairs. Keys must be at most 40 characters and values must be at most 500 characters. Neither can contain the characters `"` and `\`. i.e. '{"customer_id" : "NEWYORK2015"}' Nested objects are not supported.  See [Metadata](#section/Metadata) for more information. |
| `merge_variables` | [`object`](../../doc/models/object-enum.md) | Optional | You can input a merge variable payload object to your template to render dynamic content. For example, if you have a template like: `{{variable_name}}`, pass in `{"variable_name": "Harry"}` to render `Harry`. `merge_variables` must be an object. Any type of value is accepted as long as the object is valid JSON; you can use `strings`, `numbers`, `booleans`, `arrays`, `objects`, or `null`. The max length of the object is 25,000 characters. If you call `JSON.stringify` on your object, it can be no longer than 25,000 characters. Your variable names cannot contain any whitespace or any of the following special characters: `!`, `"`, `#`, `%`, `&`, `'`, `(`, `)`, `*`, `+`, `,`, `/`, `;`, `<`, `=`, `>`, `@`, `[`, `\`, `]`, `^`, `````, `{`, `\|`, `}`, `~`. More instructions can be found in <a href="https://help.lob.com/print-and-mail/designing-mail-creatives/dynamic-personalization#using-html-and-merge-variables-10" target="_blank">our guide to using html and merge variables</a>. Depending on your <a href="https://dashboard.lob.com/#/settings/account" target="_blank">Merge Variable strictness</a> setting, if you define variables in your HTML but do not pass them here, you will either receive an error or the variable will render as an empty string. |
| `send_date` | [`object`](../../doc/models/object-enum.md) | Optional | - |
| `mail_type` | [`MailTypeEnum`](../../doc/models/mail-type-enum.md) | Optional | - |
| `color` | `bool` | Required | Set this key to `true` if you would like to print in color. Set to `false` if you would like to print in black and white. |
| `double_sided` | `bool` | Optional | Set this attribute to `true` for double sided printing, or `false` for for single sided printing. Defaults to `true`.<br>**Default**: `True` |
| `address_placement` | [`AddressPlacementEnum`](../../doc/models/address-placement-enum.md) | Optional | - |
| `return_envelope` | [`object`](../../doc/models/object-enum.md) | Optional | - |
| `perforated_page` | `int` | Optional | Required if `return_envelope` is `true`. The number of the page that should be perforated for use with the return envelope. Must be greater than or equal to `1`. The blank page added by `address_placement=insert_blank_page` will be ignored when considering the perforated page number. To see how perforation will impact your letter design, view our <a href="https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/letter_perf_template.pdf" target="_blank">perforation guide</a>. |
| `custom_envelope` | [`object`](../../doc/models/object-enum.md) | Optional | - |
| `to` | [`object`](../../doc/models/object-enum.md) | Required | - |
| `carrier` | `str` | Required, Constant | **Default**: `'USPS'` |
| `thumbnails` | [`List[Thumbnail]`](../../doc/models/thumbnail.md) | Optional | - |
| `expected_delivery_date` | `date` | Optional | A date in YYYY-MM-DD format of the mailpiece's expected delivery date based on its `send_date`. |
| `date_created` | `datetime` | Optional | A timestamp in ISO 8601 format of the date the resource was created. |
| `date_modified` | `datetime` | Optional | A timestamp in ISO 8601 format of the date the resource was last modified. |
| `deleted` | `bool` | Optional | Only returned if the resource has been successfully deleted. |
| `mfrom` | [`object`](../../doc/models/object-enum.md) | Required | - |
| `url` | `str` | Optional | A [signed link](#section/Asset-URLs) served over HTTPS. The link returned will expire in 30 days to prevent mis-sharing. Each time a GET request is initiated, a new signed URL will be generated.<br>**Constraints**: *Pattern*: `^https://lob-assets\.com/(letters\|postcards\|bank-accounts\|checks\|self-mailers\|cards)/[a-z]{3,4}_[a-z0-9]{15,16}(\.pdf\|_thumb_[a-z]+_[0-9]+\.png)\?(version=[a-z0-9-]*&)?expires=[0-9]{10}&signature=[a-zA-Z0-9-_]+$` |
| `id` | `str` | Required | Unique identifier prefixed with `ltr_`.<br>**Constraints**: *Pattern*: `^ltr_[a-zA-Z0-9]+$` |
| `template_id` | `str` | Optional | **Constraints**: *Pattern*: `^tmpl_[a-zA-Z0-9]+$` |
| `template_version_id` | `str` | Optional | **Constraints**: *Pattern*: `^vrsn_[a-zA-Z0-9]+$` |
| `campaign_id` | `str` | Optional | The unique ID of the associated campaign if the resource was generated from a campaign. |
| `use_type` | [`object`](../../doc/models/object-enum.md) | Required | - |
| `fsc` | `bool` | Optional | This is in beta. Contact support@lob.com or your account contact to learn more. Not available for `A4` letter size.<br>**Default**: `False` |
| `status` | [`ThestatusofthebuckslipEnum`](../../doc/models/thestatusofthebuckslip-enum.md) | Optional | - |
| `failure_reason` | `str` | Optional | A string describing the reason for failure if the letter failed to render. |
| `object` | [`Object8Enum`](../../doc/models/object-8-enum.md) | Optional | - |

## Example (as JSON)

```json
{
  "color": false,
  "double_sided": true,
  "to": {
    "key1": "val1",
    "key2": "val2"
  },
  "carrier": "USPS",
  "from": {
    "key1": "val1",
    "key2": "val2"
  },
  "id": "id0",
  "use_type": {
    "key1": "val1",
    "key2": "val2"
  },
  "fsc": false,
  "tracking_events": [
    {
      "id": "id8",
      "time": "2016-03-13T12:52:32.123Z",
      "date_created": "2016-03-13T12:52:32.123Z",
      "date_modified": "2016-03-13T12:52:32.123Z",
      "object": "tracking_event",
      "type": "type2",
      "name": "Delivered",
      "details": {
        "key1": "val1",
        "key2": "val2"
      },
      "location": "location2"
    }
  ],
  "cards": [
    {
      "date_created": "2016-03-13T12:52:32.123Z",
      "date_modified": "2016-03-13T12:52:32.123Z",
      "deleted": false,
      "object": "object4",
      "description": "description8",
      "size": "3.375x2.125",
      "id": "id8",
      "url": "url2",
      "auto_reorder": false,
      "reorder_quantity": 78,
      "raw_url": "raw_url0",
      "front_original_url": "front_original_url8",
      "back_original_url": "back_original_url4",
      "thumbnails": [
        {
          "small": "small8",
          "medium": "medium8",
          "large": "large6"
        }
      ],
      "available_quantity": 98,
      "pending_quantity": 64,
      "status": "processed",
      "orientation": "horizontal",
      "threshold_amount": 200
    },
    {
      "date_created": "2016-03-13T12:52:32.123Z",
      "date_modified": "2016-03-13T12:52:32.123Z",
      "deleted": false,
      "object": "object4",
      "description": "description8",
      "size": "3.375x2.125",
      "id": "id8",
      "url": "url2",
      "auto_reorder": false,
      "reorder_quantity": 78,
      "raw_url": "raw_url0",
      "front_original_url": "front_original_url8",
      "back_original_url": "back_original_url4",
      "thumbnails": [
        {
          "small": "small8",
          "medium": "medium8",
          "large": "large6"
        }
      ],
      "available_quantity": 98,
      "pending_quantity": 64,
      "status": "processed",
      "orientation": "horizontal",
      "threshold_amount": 200
    }
  ],
  "buckslips": [
    {
      "date_created": "2016-03-13T12:52:32.123Z",
      "date_modified": "2016-03-13T12:52:32.123Z",
      "deleted": false,
      "object": "object4",
      "description": "description2",
      "size": "8.75x3.75",
      "id": "id8",
      "auto_reorder": false,
      "reorder_quantity": 40,
      "threshold_amount": 82,
      "url": "url2",
      "raw_url": "raw_url0",
      "front_original_url": "front_original_url8",
      "back_original_url": "back_original_url4",
      "thumbnails": [
        {
          "small": "small8",
          "medium": "medium8",
          "large": "large6"
        },
        {
          "small": "small8",
          "medium": "medium8",
          "large": "large6"
        },
        {
          "small": "small8",
          "medium": "medium8",
          "large": "large6"
        }
      ],
      "available_quantity": 245.56,
      "allocated_quantity": 159.6,
      "onhand_quantity": 114.48,
      "pending_quantity": 19.74,
      "projected_quantity": 56.66,
      "buckslip_orders": [
        {
          "date_created": "2016-03-13T12:52:32.123Z",
          "date_modified": "2016-03-13T12:52:32.123Z",
          "deleted": false,
          "object": "object0",
          "id": "id2",
          "buckslip_id": "buckslip_id8",
          "status": "printing",
          "quantity_ordered": 134.5
        },
        {
          "date_created": "2016-03-13T12:52:32.123Z",
          "date_modified": "2016-03-13T12:52:32.123Z",
          "deleted": false,
          "object": "object0",
          "id": "id2",
          "buckslip_id": "buckslip_id8",
          "status": "printing",
          "quantity_ordered": 134.5
        },
        {
          "date_created": "2016-03-13T12:52:32.123Z",
          "date_modified": "2016-03-13T12:52:32.123Z",
          "deleted": false,
          "object": "object0",
          "id": "id2",
          "buckslip_id": "buckslip_id8",
          "status": "printing",
          "quantity_ordered": 134.5
        }
      ],
      "stock": "text",
      "weight": "weight6",
      "finish": "gloss",
      "status": "processed"
    },
    {
      "date_created": "2016-03-13T12:52:32.123Z",
      "date_modified": "2016-03-13T12:52:32.123Z",
      "deleted": false,
      "object": "object4",
      "description": "description2",
      "size": "8.75x3.75",
      "id": "id8",
      "auto_reorder": false,
      "reorder_quantity": 40,
      "threshold_amount": 82,
      "url": "url2",
      "raw_url": "raw_url0",
      "front_original_url": "front_original_url8",
      "back_original_url": "back_original_url4",
      "thumbnails": [
        {
          "small": "small8",
          "medium": "medium8",
          "large": "large6"
        },
        {
          "small": "small8",
          "medium": "medium8",
          "large": "large6"
        },
        {
          "small": "small8",
          "medium": "medium8",
          "large": "large6"
        }
      ],
      "available_quantity": 245.56,
      "allocated_quantity": 159.6,
      "onhand_quantity": 114.48,
      "pending_quantity": 19.74,
      "projected_quantity": 56.66,
      "buckslip_orders": [
        {
          "date_created": "2016-03-13T12:52:32.123Z",
          "date_modified": "2016-03-13T12:52:32.123Z",
          "deleted": false,
          "object": "object0",
          "id": "id2",
          "buckslip_id": "buckslip_id8",
          "status": "printing",
          "quantity_ordered": 134.5
        },
        {
          "date_created": "2016-03-13T12:52:32.123Z",
          "date_modified": "2016-03-13T12:52:32.123Z",
          "deleted": false,
          "object": "object0",
          "id": "id2",
          "buckslip_id": "buckslip_id8",
          "status": "printing",
          "quantity_ordered": 134.5
        },
        {
          "date_created": "2016-03-13T12:52:32.123Z",
          "date_modified": "2016-03-13T12:52:32.123Z",
          "deleted": false,
          "object": "object0",
          "id": "id2",
          "buckslip_id": "buckslip_id8",
          "status": "printing",
          "quantity_ordered": 134.5
        }
      ],
      "stock": "text",
      "weight": "weight6",
      "finish": "gloss",
      "status": "processed"
    },
    {
      "date_created": "2016-03-13T12:52:32.123Z",
      "date_modified": "2016-03-13T12:52:32.123Z",
      "deleted": false,
      "object": "object4",
      "description": "description2",
      "size": "8.75x3.75",
      "id": "id8",
      "auto_reorder": false,
      "reorder_quantity": 40,
      "threshold_amount": 82,
      "url": "url2",
      "raw_url": "raw_url0",
      "front_original_url": "front_original_url8",
      "back_original_url": "back_original_url4",
      "thumbnails": [
        {
          "small": "small8",
          "medium": "medium8",
          "large": "large6"
        },
        {
          "small": "small8",
          "medium": "medium8",
          "large": "large6"
        },
        {
          "small": "small8",
          "medium": "medium8",
          "large": "large6"
        }
      ],
      "available_quantity": 245.56,
      "allocated_quantity": 159.6,
      "onhand_quantity": 114.48,
      "pending_quantity": 19.74,
      "projected_quantity": 56.66,
      "buckslip_orders": [
        {
          "date_created": "2016-03-13T12:52:32.123Z",
          "date_modified": "2016-03-13T12:52:32.123Z",
          "deleted": false,
          "object": "object0",
          "id": "id2",
          "buckslip_id": "buckslip_id8",
          "status": "printing",
          "quantity_ordered": 134.5
        },
        {
          "date_created": "2016-03-13T12:52:32.123Z",
          "date_modified": "2016-03-13T12:52:32.123Z",
          "deleted": false,
          "object": "object0",
          "id": "id2",
          "buckslip_id": "buckslip_id8",
          "status": "printing",
          "quantity_ordered": 134.5
        },
        {
          "date_created": "2016-03-13T12:52:32.123Z",
          "date_modified": "2016-03-13T12:52:32.123Z",
          "deleted": false,
          "object": "object0",
          "id": "id2",
          "buckslip_id": "buckslip_id8",
          "status": "printing",
          "quantity_ordered": 134.5
        }
      ],
      "stock": "text",
      "weight": "weight6",
      "finish": "gloss",
      "status": "processed"
    }
  ],
  "return_address": {
    "key1": "val1",
    "key2": "val2"
  },
  "description": "description0"
}
```

