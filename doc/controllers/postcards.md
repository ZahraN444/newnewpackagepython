# Postcards

The postcards endpoint allows you to easily print and mail postcards. The API provides endpoints for creating postcards,
retrieving individual postcards, canceling postcards, and retrieving a list of postcards.

<div class="back-to-top" ><a href="#" onclick="toTopLink()">back to top</a></div>


```python
postcards_controller = client.postcards
```

## Class Name

`PostcardsController`

## Methods

* [Postcard Retrieve](../../doc/controllers/postcards.md#postcard-retrieve)
* [Postcard Delete](../../doc/controllers/postcards.md#postcard-delete)
* [Postcards List](../../doc/controllers/postcards.md#postcards-list)
* [Postcard Create](../../doc/controllers/postcards.md#postcard-create)


# Postcard Retrieve

Retrieves the details of an existing postcard. You need only supply the unique customer identifier that was returned upon postcard creation.

```python
def postcard_retrieve(self,
                     psc_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `psc_id` | `str` | Template, Required | id of the postcard |

## Response Type

[`Postcard`](../../doc/models/postcard.md)

## Example Usage

```python
psc_id = 'psc_id2'

result = postcards_controller.postcard_retrieve(psc_id)
```

## Example Response *(as JSON)*

```json
{
  "id": "psc_208e45e48d271294",
  "description": null,
  "metadata": {},
  "to": {
    "id": "adr_210a8d4b0b76d77b",
    "description": null,
    "name": null,
    "company": "LOB",
    "phone": null,
    "email": null,
    "address_line1": "210 KING ST STE 6100",
    "address_line2": null,
    "address_city": "SAN FRANCISCO",
    "address_state": "CA",
    "address_zip": "94107-1741",
    "address_country": "UNITED STATES",
    "metadata": {},
    "date_created": "2018-12-08T03:01:07.651Z",
    "date_modified": "2018-12-08T03:01:07.651Z",
    "object": "address"
  },
  "url": "https://lob-assets.com/postcards/psc_208e45e48d271294.pdf?version=v1&expires=1619218302&signature=NfHHLBSr5tOHA_Z4kij4dKqZG8f3vMDtwvuFVeeF9pV_lylcjLsVVODhNCE5hR6-2slUr6t9WMNsi429Pj7_DA",
  "carrier": "USPS",
  "front_template_id": null,
  "back_template_id": null,
  "date_created": "2021-03-24T22:51:42.838Z",
  "date_modified": "2021-03-24T22:51:42.838Z",
  "send_date": "2021-03-24T22:51:42.838Z",
  "use_type": "marketing",
  "object": "postcard"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |


# Postcard Delete

Completely removes a postcard from production. This can only be done if the postcard has a `send_date` and the `send_date` has not yet passed. If the postcard is successfully canceled, you will not be charged for it. Read more on [cancellation windows](#section/Cancellation-Windows) and [scheduling](#section/Scheduled-Mailings). Scheduling and cancellation is a premium feature. Upgrade to the appropriate <a href="https://dashboard.lob.com/#/settings/editions" target="_blank">Print & Mail Edition</a> to gain access.

```python
def postcard_delete(self,
                   psc_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `psc_id` | `str` | Template, Required | id of the postcard |

## Response Type

[`PostcardsResponse1`](../../doc/models/postcards-response-1.md)

## Example Usage

```python
psc_id = 'psc_id2'

result = postcards_controller.postcard_delete(psc_id)
```

## Example Response *(as JSON)*

```json
{
  "id": "psc_123456789",
  "deleted": true
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |


# Postcards List

Returns a list of your postcards. The addresses are returned sorted by creation date, with the most recently created addresses appearing first.

```python
def postcards_list(self,
                  limit=10,
                  before_after=None,
                  include=None,
                  date_created=None,
                  metadata=None,
                  size=None,
                  scheduled=None,
                  send_date=None,
                  mail_type=None,
                  sort_by=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `int` | Query, Optional | How many results to return. |
| `before_after` | [`Beforeafter`](../../doc/models/beforeafter.md) | Query, Optional | `before` and `after` are both optional but only one of them can be in the query at a time. |
| `include` | `List[str]` | Query, Optional | Request that the response include the total count by specifying `include=["total_count"]`. |
| `date_created` | `Dict[str, str]` | Query, Optional | Filter by date created. Accepted formats are ISO-8601 date or datetime, e.g. `{ "gt": "2012-01-01", "lt": "2012-01-31T12:34:56Z" }` where `gt` is >, `lt` is <, `gte` is ≥, and `lte` is ≤. |
| `metadata` | `Dict[str, str]` | Query, Optional | Filter by metadata key-value pair`. |
| `size` | [`List[PostcardSizeEnum]`](../../doc/models/postcard-size-enum.md) | Query, Optional | Specifies the size of the postcard. Only `4x6` postcards can be sent to international destinations. |
| `scheduled` | `bool` | Query, Optional | * `true` - only return orders (past or future) where `send_date` is<br>  greater than `date_created`<br>* `false` - only return orders where `send_date` is equal to `date_created` |
| `send_date` | [`object`](../../doc/models/object-enum.md) | Query, Optional | Filter by ISO-8601 date or datetime, e.g. `{ "gt": "2012-01-01", "lt": "2012-01-31T12:34:56Z" }` where `gt` is >, `lt` is <, `gte` is ≥, and `lte` is ≤. |
| `mail_type` | [`MailTypeEnum`](../../doc/models/mail-type-enum.md) | Query, Optional | A string designating the mail postage type: * `usps_first_class` - (default) * `usps_standard` - a <a href="https://lob.com/pricing/print-mail#compare" target="_blank">cheaper option</a> which is less predictable and takes longer to deliver. `usps_standard` cannot be used with `4x6` postcards or for any postcards sent outside of the United States. |
| `sort_by` | [`SortBy1`](../../doc/models/sort-by-1.md) | Query, Optional | Sorts items by ascending or descending dates. Use either `date_created` or `send_date`, not both. |

## Response Type

[`AllPostcards`](../../doc/models/all-postcards.md)

## Example Usage

```python
limit = 10

result = postcards_controller.postcards_list(
    limit=limit
)
```

## Example Response *(as JSON)*

```json
{
  "data": [
    {
      "id": "psc_208e45e48d271294",
      "description": null,
      "metadata": {},
      "to": {
        "id": "adr_210a8d4b0b76d77b",
        "description": null,
        "name": "LEORE AVIDAR",
        "company": null,
        "phone": null,
        "email": null,
        "address_line1": "210 KING ST STE 6100",
        "address_line2": null,
        "address_city": "SAN FRANCISCO",
        "address_state": "CA",
        "address_zip": "94107-1741",
        "address_country": "UNITED STATES",
        "metadata": {},
        "date_created": "2018-12-08T03:01:07.651Z",
        "date_modified": "2018-12-08T03:01:07.651Z",
        "object": "address"
      },
      "url": "https://lob-assets.com/postcards/psc_208e45e48d271294.pdf?version=v1&expires=1619218302&signature=NfHHLBSr5tOHA_Z4kij4dKqZG8f3vMDtwvuFVeeF9pV_lylcjLsVVODhNCE5hR6-2slUr6t9WMNsi429Pj7_DA",
      "carrier": "USPS",
      "front_template_id": null,
      "back_template_id": null,
      "front_template_version_id": null,
      "back_template_version_id": null,
      "date_created": "2021-03-24T22:51:42.838Z",
      "date_modified": "2021-03-24T22:51:42.838Z",
      "send_date": "2021-03-24T22:51:42.838Z",
      "use_type": "marketing",
      "object": "postcard"
    },
    {
      "id": "psc_0e03d1ad7d31f151",
      "description": null,
      "metadata": {},
      "to": {
        "id": "adr_c7cb63d68f8d6",
        "description": null,
        "name": "JANE DOE",
        "company": "LOB",
        "phone": "5555555555",
        "email": "jane.doe@lob.com",
        "address_line1": "370 WATER ST",
        "address_line2": "",
        "address_city": "SUMMERSIDE",
        "address_state": "PE",
        "address_zip": "C1N 1C4",
        "address_country": "CANADA",
        "metadata": {},
        "date_created": "2018-12-08T03:01:07.651Z",
        "date_modified": "2018-12-08T03:01:07.651Z",
        "object": "address",
        "recipient_moved": false
      },
      "from": {
        "id": "adr_210a8d4b0b76d77b",
        "description": null,
        "name": "LEORE AVIDAR",
        "company": null,
        "phone": null,
        "email": null,
        "address_line1": "210 KING ST STE 6100",
        "address_line2": null,
        "address_city": "SAN FRANCISCO",
        "address_state": "CA",
        "address_zip": "94107-1741",
        "address_country": "UNITED STATES",
        "metadata": {},
        "date_created": "2018-12-08T03:01:07.651Z",
        "date_modified": "2018-12-08T03:01:07.651Z",
        "object": "address"
      },
      "url": "https://lob-assets.com/postcards/psc_208e45e48d271294.pdf?version=v1&expires=1619218302&signature=NfHHLBSr5tOHA_Z4kij4dKqZG8f3vMDtwvuFVeeF9pV_lylcjLsVVODhNCE5hR6-2slUr6t9WMNsi429Pj7_DA",
      "carrier": "USPS",
      "front_template_id": null,
      "back_template_id": null,
      "front_template_version_id": null,
      "back_template_version_id": null,
      "tracking_events": [],
      "size": "6x11",
      "mail_type": "usps_first_class",
      "merge_variables": {},
      "thumbnails": [
        {
          "small": "https://lob-assets.com/letters/ltr_4868c3b754655f90_thumb_small_1.png?expires=1540372221&signature=a5fRBJ22ZA78Vgpg34M9UfmHWTS3eha",
          "medium": "https://lob-assets.com/letters/ltr_4868c3b754655f90_thumb_medium_1.png?expires=1540372221&signature=bAzL8sv935PY09FWSkpDpWKkyvGSWYF",
          "large": "https://lob-assets.com/letters/ltr_4868c3b754655f90_thumb_large_1.png?expires=1540372221&signature=gsKvxXgrm4v4iZD3bOibK7jApNkEMdW"
        }
      ],
      "expected_delivery_date": "2021-03-30",
      "date_created": "2021-03-24T22:51:42.838Z",
      "date_modified": "2021-03-24T22:51:42.838Z",
      "send_date": "2021-03-24T22:51:42.838Z",
      "use_type": "marketing",
      "object": "postcard"
    }
  ],
  "object": "list",
  "previous_url": null,
  "next_url": null,
  "count": 2
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |


# Postcard Create

Creates a new postcard given information

```python
def postcard_create(self,
                   body,
                   idempotency_key=None,
                   idempotency_key_2=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PostcardEditable`](../../doc/models/postcard-editable.md) | Body, Required | - |
| `idempotency_key` | `str` | Header, Optional | A string of no longer than 256 characters that uniquely identifies this resource. For more help integrating idempotency keys, refer to our <a href="https://help.lob.com/print-and-mail/building-a-mail-strategy/managing-mail-settings#idempotent-requests-12" target="_blank">implementation guide</a>. |
| `idempotency_key_2` | `str` | Query, Optional | A string of no longer than 256 characters that uniquely identifies this resource. For more help integrating idempotency keys, refer to our <a href="https://help.lob.com/print-and-mail/building-a-mail-strategy/managing-mail-settings#idempotent-requests-12" target="_blank">implementation guide</a>. |

## Response Type

[`Postcard`](../../doc/models/postcard.md)

## Example Usage

```python
body = PostcardEditable(
    to=InlineAddressUs(
        address_line_1='210 King St',
        address_city='San Francisco',
        address_state='CA',
        address_zip='94107',
        name='Harry Zhang',
        company='Lob',
        address_line_2='# 6100',
        description='Harry - Office',
        phone='5555555555',
        email='harry@lob.com',
        address_country=AddressCountry2Enum.US
    ),
    front=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    back=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    use_type=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    description='demo',
    metadata={
        'spiffy': 'true'
    },
    mail_type=MailTypeEnum.USPS_FIRST_CLASS,
    merge_variables={"name":"Harry"},
    send_date=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    size=PostcardSizeEnum.ENUM_6X9,
    mfrom=InlineAddressUs(
        address_line_1='210 King St',
        address_city='San Francisco',
        address_state='CA',
        address_zip='94107',
        name='Harry Zhang',
        company='Lob',
        address_line_2='# 6100',
        description='Harry - Office',
        phone='5555555555',
        email='harry@lob.com',
        address_country=AddressCountry2Enum.US
    ),
    qr_code=QrCode4(
        position='relative',
        redirect_url='https://www.lob.com',
        width='2.5',
        top='2.5',
        right='2.5',
        pages='front,back'
    )
)

idempotency_key = '026e7634-24d7-486c-a0bb-4a17fd0eebc5'

idempotency_key_2 = '026e7634-24d7-486c-a0bb-4a17fd0eebc5'

result = postcards_controller.postcard_create(
    body,
    idempotency_key=idempotency_key,
    idempotency_key_2=idempotency_key_2
)
```

## Example Response *(as JSON)*

```json
{
  "id": "psc_208e45e48d271294",
  "description": null,
  "metadata": {},
  "to": {
    "id": "adr_210a8d4b0b76d77b",
    "description": null,
    "name": null,
    "company": "LOB",
    "phone": null,
    "email": null,
    "address_line1": "210 KING ST STE 6100",
    "address_line2": null,
    "address_city": "SAN FRANCISCO",
    "address_state": "CA",
    "address_zip": "94107-1741",
    "address_country": "UNITED STATES",
    "metadata": {},
    "date_created": "2018-12-08T03:01:07.651Z",
    "date_modified": "2018-12-08T03:01:07.651Z",
    "object": "address"
  },
  "url": "https://lob-assets.com/postcards/psc_208e45e48d271294.pdf?version=v1&expires=1619218302&signature=NfHHLBSr5tOHA_Z4kij4dKqZG8f3vMDtwvuFVeeF9pV_lylcjLsVVODhNCE5hR6-2slUr6t9WMNsi429Pj7_DA",
  "carrier": "USPS",
  "front_template_id": null,
  "back_template_id": null,
  "date_created": "2021-03-24T22:51:42.838Z",
  "date_modified": "2021-03-24T22:51:42.838Z",
  "send_date": "2021-03-24T22:51:42.838Z",
  "use_type": "marketing",
  "object": "postcard"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |

