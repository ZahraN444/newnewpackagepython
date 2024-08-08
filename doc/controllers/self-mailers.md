# Self Mailers

```python
self_mailers_controller = client.self_mailers
```

## Class Name

`SelfMailersController`

## Methods

* [Self Mailer Retrieve](../../doc/controllers/self-mailers.md#self-mailer-retrieve)
* [Self Mailer Delete](../../doc/controllers/self-mailers.md#self-mailer-delete)
* [Self Mailers List](../../doc/controllers/self-mailers.md#self-mailers-list)
* [Self Mailer Create](../../doc/controllers/self-mailers.md#self-mailer-create)


# Self Mailer Retrieve

Retrieves the details of an existing self_mailer. You need only supply the unique self_mailer identifier that was returned upon self_mailer creation.

```python
def self_mailer_retrieve(self,
                        sfm_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sfm_id` | `str` | Template, Required | id of the self_mailer |

## Response Type

[`SelfMailer`](../../doc/models/self-mailer.md)

## Example Usage

```python
sfm_id = 'sfm_id8'

result = self_mailers_controller.self_mailer_retrieve(sfm_id)
```

## Example Response *(as JSON)*

```json
{
  "id": "sfm_8ffbe811dea49dcf",
  "description": "April Campaign",
  "metadata": {},
  "to": {
    "id": "adr_bae820679f3f536b",
    "description": null,
    "name": "HARRY ZHANG",
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
    "date_created": "2017-09-05T17:47:53.767Z",
    "date_modified": "2017-09-05T17:47:53.767Z",
    "deleted": true,
    "object": "address"
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
    "date_created": "2017-09-05T17:47:53.767Z",
    "date_modified": "2017-09-05T17:47:53.767Z",
    "deleted": true,
    "object": "address"
  },
  "url": "https://lob-assets.com/self-mailers/sfm_8ffbe811dea49dcf.pdf?version=v1&expires=1618512040&signature=qvyCqXI1ndBvc4AjvG8FlirqLXEcfmYo4sDrRtabaXMOsX88to9G3K49uIk_aqevvZXe8HoRYD_nWydbQHqaCA",
  "outside_template_id": "tmpl_a3cb937f26d7eec",
  "inside_template_id": "tmpl_a3cb937f26d7eec",
  "inside_template_version_id": "vrsn_bfdf70893b00a85",
  "outside_template_version_id": "vrsn_bfdf70893b00a85",
  "carrier": "USPS",
  "tracking_events": [],
  "thumbnails": [
    {
      "small": "https://lob-assets.com/self-mailers/sfm_8ffbe811dea49dcf_thumb_small_1.png?version=v1&expires=1618512040&signature=-bipeUHP-hAMcCBSrWM0ZH1VwRdSPNVGGZN9hAZKr6Lh4ly6uxvratVd5LXJCK_zOEMYk_mTWASt0ge7OY6SDA",
      "medium": "https://lob-assets.com/self-mailers/sfm_8ffbe811dea49dcf_thumb_medium_1.png?version=v1&expires=1618512040&signature=ryxN7bsXGtw_GRFSP3Cs3A3IYjxZi3cW9BHDCNgMt6p3nobVmsc_iFHt2e-S7ndAXhhN7nP-MQVov3bt3r37BQ",
      "large": "https://lob-assets.com/self-mailers/sfm_8ffbe811dea49dcf_thumb_large_1.png?version=v1&expires=1618512040&signature=kBrm00xkyCkJNJRHxH8HshFaebtOxnzjVWOs1VVmGMuw8H6OBNcMAMxt9s49K0jlpHoh3Nr9uSncEZMQaaNjAg"
    },
    {
      "small": "https://lob-assets.com/self-mailers/sfm_8ffbe811dea49dcf_thumb_small_2.png?version=v1&expires=1618512040&signature=3gTgU7Fd3KoT_vNlQnTGptRps5ZgnkhSnPrAwk7L98higIzSwfKoLvuu_DIpMM48dHbxckKT9waR8euJ4KSDBQ",
      "medium": "https://lob-assets.com/self-mailers/sfm_8ffbe811dea49dcf_thumb_medium_2.png?version=v1&expires=1618512040&signature=Ue1lw5CMj7KRx6cMQL8xPeazaHCdJzWcACd1w3acuYPnWkVIpSt62OIO7hAtpAQK9xm1dhhlFj0rqRZMdRMMBA",
      "large": "https://lob-assets.com/self-mailers/sfm_8ffbe811dea49dcf_thumb_large_2.png?version=v1&expires=1618512040&signature=cICc7HEm1xG_eyM4a_wtvPk2FqoLRmtgGa29kJisWnMIYBL0OkyzG4ZCYGMhp-5cZpJlSpXfTgGKh_Qmeo1TDw"
    }
  ],
  "merge_variables": {
    "name": null
  },
  "size": "6x18_bifold",
  "mail_type": "usps_first_class",
  "expected_delivery_date": "2021-03-24",
  "date_created": "2021-03-16T18:40:40.504Z",
  "date_modified": "2021-03-16T18:40:40.504Z",
  "send_date": "2021-03-16T18:45:40.493Z",
  "use_type": "marketing",
  "fsc": false,
  "object": "self_mailer"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |


# Self Mailer Delete

Completely removes a self mailer from production. This can only be done if the self mailer's `send_date` has not yet passed. If the self mailer is successfully canceled, you will not be charged for it. This feature is exclusive to certain customers. Upgrade to the appropriate <a href="https://dashboard.lob.com/#/settings/editions" target="_blank">Print & Mail Edition</a> to gain access.

```python
def self_mailer_delete(self,
                      sfm_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sfm_id` | `str` | Template, Required | id of the self_mailer |

## Response Type

[`SelfMailersResponse1`](../../doc/models/self-mailers-response-1.md)

## Example Usage

```python
sfm_id = 'sfm_id8'

result = self_mailers_controller.self_mailer_delete(sfm_id)
```

## Example Response *(as JSON)*

```json
{
  "id": "sfm_123456789",
  "deleted": true
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |


# Self Mailers List

Returns a list of your self_mailers. The self_mailers are returned sorted by creation date, with the most recently created self_mailers appearing first.

```python
def self_mailers_list(self,
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
| `size` | [`List[SelfMailerSizeEnum]`](../../doc/models/self-mailer-size-enum.md) | Query, Optional | The self mailer sizes to be returned. |
| `scheduled` | `bool` | Query, Optional | * `true` - only return orders (past or future) where `send_date` is<br>  greater than `date_created`<br>* `false` - only return orders where `send_date` is equal to `date_created` |
| `send_date` | [`object`](../../doc/models/object-enum.md) | Query, Optional | Filter by ISO-8601 date or datetime, e.g. `{ "gt": "2012-01-01", "lt": "2012-01-31T12:34:56Z" }` where `gt` is >, `lt` is <, `gte` is ≥, and `lte` is ≤. |
| `mail_type` | [`MailTypeEnum`](../../doc/models/mail-type-enum.md) | Query, Optional | A string designating the mail postage type: * `usps_first_class` - (default) * `usps_standard` - a <a href="https://lob.com/pricing/print-mail#compare" target="_blank">cheaper option</a> which is less predictable and takes longer to deliver. `usps_standard` cannot be used with `4x6` postcards or for any postcards sent outside of the United States. |
| `sort_by` | [`SortBy1`](../../doc/models/sort-by-1.md) | Query, Optional | Sorts items by ascending or descending dates. Use either `date_created` or `send_date`, not both. |

## Response Type

[`AllSelfMailers`](../../doc/models/all-self-mailers.md)

## Example Usage

```python
limit = 10

result = self_mailers_controller.self_mailers_list(
    limit=limit
)
```

## Example Response *(as JSON)*

```json
{
  "data": [
    {
      "id": "sfm_7239rhwqkrfaskas",
      "description": "April Campaign",
      "metadata": {},
      "to": {
        "id": "adr_asdi2y3riuasasoi",
        "description": "Harry - Office",
        "name": "Harry Zhang",
        "company": "Lob",
        "phone": "5555555555",
        "email": "harry@lob.com",
        "metadata": {},
        "address_line1": "370 WATER ST",
        "address_line2": "",
        "address_city": "SUMMERSIDE",
        "address_state": "PRINCE EDWARD ISLAND",
        "address_zip": "C1N 1C4",
        "address_country": "CANADA",
        "recipient_moved": false,
        "date_created": "2019-09-20T00:14:00.361Z",
        "date_modified": "2019-09-20T00:14:00.361Z",
        "object": "address"
      },
      "from": {
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
      "url": "https://lob-assets.com/self-mailers/sfm_8ffbe811dea49dcf.pdf?version=v1&expires=1618781264&signature=YP_bCwrgVA2lz1Gr1YVCJN1f-WspUGsH0aJp2ihjfLXU7lDUV12_xRv4uPch0mfWeOOxEqpyP8hGpgvjmQKNAw",
      "outside_template_id": "tmpl_a3cb937f26d7eec",
      "inside_template_id": "tmpl_a3cb937f26d7eec",
      "inside_template_version_id": "vrsn_bfdf70893b00a85",
      "outside_template_version_id": "vrsn_bfdf70893b00a85",
      "carrier": "USPS",
      "tracking_events": [],
      "thumbnails": [
        {
          "small": "https://lob-assets.com/self-mailers/sfm_8ffbe811dea49dcf_thumb_small_1.png?version=v1&expires=1618781264&signature=A7q5HbRO53sUYYnwGlmP5mTS6ylLE7kS2mYhfcEOdexjyqG7UseK0MD26DppE4Q0aE4u2msDVMxd5ukjMerYCg",
          "medium": "https://lob-assets.com/self-mailers/sfm_8ffbe811dea49dcf_thumb_medium_1.png?version=v1&expires=1618781264&signature=b9pynuawVpU_vrhnT_mTpksdE-FLF_ZjdIBOFR_ltIzEGlx-VKD4VvZrqP98lG2D8V7UKQ7SdRr2nUAk4LxvCg",
          "large": "https://lob-assets.com/self-mailers/sfm_8ffbe811dea49dcf_thumb_large_1.png?version=v1&expires=1618781264&signature=g2jifhCselPqIj8au6lsbJMNFN8ZX3aM6GkLoAXiHBCS8X5mF9nhVbmO0odpnmwNlV1CWIp-MXVsZkC3NmxqBQ"
        },
        {
          "small": "https://lob-assets.com/self-mailers/sfm_8ffbe811dea49dcf_thumb_small_2.png?version=v1&expires=1618781264&signature=biJY4-ZbNNRydPYg3cZkq7wxjILbPBK_nIVyoyQsg5X5q4jlsa-2fzeMa48V9jprUetsC6WEuYvasHosRfG_DQ",
          "medium": "https://lob-assets.com/self-mailers/sfm_8ffbe811dea49dcf_thumb_medium_2.png?version=v1&expires=1618781264&signature=xEAX7bURyc8fSphacuo5yb7iVIpT8Xvq05KgMaNQS4r3aCpx0z1p42wbPmW758B5Ae0li1YDYvVyzS7qJIoWAw",
          "large": "https://lob-assets.com/self-mailers/sfm_8ffbe811dea49dcf_thumb_large_2.png?version=v1&expires=1618781264&signature=NieHDnoQ7STZUvofHrFt7S987CzIkUJWpaSgpVQPZw-C3_wwTPsIrvxYdXEuFrr6ciTUcxRBFPlE0lurmMkyCA"
        }
      ],
      "merge_variables": {
        "name": null
      },
      "size": "6x18_bifold",
      "mail_type": "usps_first_class",
      "expected_delivery_date": "2021-03-24",
      "date_created": "2021-03-16T18:40:40.504Z",
      "date_modified": "2021-03-16T18:41:06.691Z",
      "send_date": "2021-03-16T18:45:40.493Z",
      "deleted": true,
      "use_type": "marketing",
      "fsc": false,
      "object": "self_mailer"
    },
    {
      "id": "sfm_8ffbe811dea49dcf",
      "description": "April Campaign",
      "metadata": {},
      "to": {
        "id": "adr_f9228b743884ff98",
        "description": null,
        "name": "AYA",
        "company": null,
        "phone": null,
        "email": null,
        "address_line1": "2812 PARK RD",
        "address_line2": null,
        "address_city": "CHARLOTTE",
        "address_state": "NC",
        "address_zip": "28209-1314",
        "address_country": "UNITED STATES",
        "metadata": {},
        "date_created": "2021-03-16T18:40:40.410Z",
        "date_modified": "2021-03-16T18:40:40.410Z",
        "deleted": true,
        "object": "address"
      },
      "from": {
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
      "url": "https://lob-assets.com/self-mailers/sfm_8ffbe811dea49dcf.pdf?version=v1&expires=1618781264&signature=YP_bCwrgVA2lz1Gr1YVCJN1f-WspUGsH0aJp2ihjfLXU7lDUV12_xRv4uPch0mfWeOOxEqpyP8hGpgvjmQKNAw",
      "outside_template_id": "tmpl_a3cb937f26d7eec",
      "inside_template_id": "tmpl_a3cb937f26d7eec",
      "inside_template_version_id": "vrsn_bfdf70893b00a85",
      "outside_template_version_id": "vrsn_bfdf70893b00a85",
      "carrier": "USPS",
      "tracking_events": [],
      "thumbnails": [
        {
          "small": "https://lob-assets.com/self-mailers/sfm_8ffbe811dea49dcf_thumb_small_1.png?version=v1&expires=1618781264&signature=A7q5HbRO53sUYYnwGlmP5mTS6ylLE7kS2mYhfcEOdexjyqG7UseK0MD26DppE4Q0aE4u2msDVMxd5ukjMerYCg",
          "medium": "https://lob-assets.com/self-mailers/sfm_8ffbe811dea49dcf_thumb_medium_1.png?version=v1&expires=1618781264&signature=b9pynuawVpU_vrhnT_mTpksdE-FLF_ZjdIBOFR_ltIzEGlx-VKD4VvZrqP98lG2D8V7UKQ7SdRr2nUAk4LxvCg",
          "large": "https://lob-assets.com/self-mailers/sfm_8ffbe811dea49dcf_thumb_large_1.png?version=v1&expires=1618781264&signature=g2jifhCselPqIj8au6lsbJMNFN8ZX3aM6GkLoAXiHBCS8X5mF9nhVbmO0odpnmwNlV1CWIp-MXVsZkC3NmxqBQ"
        },
        {
          "small": "https://lob-assets.com/self-mailers/sfm_8ffbe811dea49dcf_thumb_small_2.png?version=v1&expires=1618781264&signature=biJY4-ZbNNRydPYg3cZkq7wxjILbPBK_nIVyoyQsg5X5q4jlsa-2fzeMa48V9jprUetsC6WEuYvasHosRfG_DQ",
          "medium": "https://lob-assets.com/self-mailers/sfm_8ffbe811dea49dcf_thumb_medium_2.png?version=v1&expires=1618781264&signature=xEAX7bURyc8fSphacuo5yb7iVIpT8Xvq05KgMaNQS4r3aCpx0z1p42wbPmW758B5Ae0li1YDYvVyzS7qJIoWAw",
          "large": "https://lob-assets.com/self-mailers/sfm_8ffbe811dea49dcf_thumb_large_2.png?version=v1&expires=1618781264&signature=NieHDnoQ7STZUvofHrFt7S987CzIkUJWpaSgpVQPZw-C3_wwTPsIrvxYdXEuFrr6ciTUcxRBFPlE0lurmMkyCA"
        }
      ],
      "merge_variables": {
        "name": null
      },
      "size": "6x18_bifold",
      "mail_type": "usps_first_class",
      "expected_delivery_date": "2021-03-24",
      "date_created": "2021-03-16T18:40:40.504Z",
      "date_modified": "2021-03-16T18:41:06.691Z",
      "send_date": "2021-03-16T18:45:40.493Z",
      "deleted": true,
      "use_type": "marketing",
      "fsc": true,
      "object": "self_mailer"
    }
  ],
  "object": "list",
  "next_url": null,
  "previous_url": null,
  "count": 2
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |


# Self Mailer Create

Creates a new self_mailer given information

```python
def self_mailer_create(self,
                      body,
                      idempotency_key=None,
                      idempotency_key_2=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SelfMailerEditable`](../../doc/models/self-mailer-editable.md) | Body, Required | - |
| `idempotency_key` | `str` | Header, Optional | A string of no longer than 256 characters that uniquely identifies this resource. For more help integrating idempotency keys, refer to our <a href="https://help.lob.com/print-and-mail/building-a-mail-strategy/managing-mail-settings#idempotent-requests-12" target="_blank">implementation guide</a>. |
| `idempotency_key_2` | `str` | Query, Optional | A string of no longer than 256 characters that uniquely identifies this resource. For more help integrating idempotency keys, refer to our <a href="https://help.lob.com/print-and-mail/building-a-mail-strategy/managing-mail-settings#idempotent-requests-12" target="_blank">implementation guide</a>. |

## Response Type

[`SelfMailer`](../../doc/models/self-mailer.md)

## Example Usage

```python
body = SelfMailerEditable(
    to='adr_bae820679f3f536b',
    inside='https://lob.com/selfmailerinside.pdf',
    outside='https://lob.com/selfmaileroutside.pdf',
    use_type=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    description='Demo Self Mailer job',
    metadata={
        'spiffy': 'true'
    },
    mail_type=MailTypeEnum.USPS_STANDARD,
    merge_variables={"name":"Harry"},
    send_date=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    size=SelfMailerSizeEnum.ENUM_12X9_BIFOLD,
    mfrom='adr_210a8d4b0b76d77b',
    qr_code=QrCode4(
        position='relative',
        redirect_url='https://www.lob.com',
        width='2.5',
        top='2.5',
        right='2.5',
        pages='inside,outside'
    ),
    fsc=True
)

idempotency_key = '026e7634-24d7-486c-a0bb-4a17fd0eebc5'

idempotency_key_2 = '026e7634-24d7-486c-a0bb-4a17fd0eebc5'

result = self_mailers_controller.self_mailer_create(
    body,
    idempotency_key=idempotency_key,
    idempotency_key_2=idempotency_key_2
)
```

## Example Response *(as JSON)*

```json
{
  "id": "sfm_8ffbe811dea49dcf",
  "description": "April Campaign",
  "metadata": {},
  "to": {
    "id": "adr_bae820679f3f536b",
    "description": null,
    "name": "HARRY ZHANG",
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
    "date_created": "2017-09-05T17:47:53.767Z",
    "date_modified": "2017-09-05T17:47:53.767Z",
    "deleted": true,
    "object": "address"
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
    "date_created": "2017-09-05T17:47:53.767Z",
    "date_modified": "2017-09-05T17:47:53.767Z",
    "deleted": true,
    "object": "address"
  },
  "url": "https://lob-assets.com/self-mailers/sfm_8ffbe811dea49dcf.pdf?version=v1&expires=1618512040&signature=qvyCqXI1ndBvc4AjvG8FlirqLXEcfmYo4sDrRtabaXMOsX88to9G3K49uIk_aqevvZXe8HoRYD_nWydbQHqaCA",
  "outside_template_id": "tmpl_a3cb937f26d7eec",
  "inside_template_id": "tmpl_a3cb937f26d7eec",
  "inside_template_version_id": "vrsn_bfdf70893b00a85",
  "outside_template_version_id": "vrsn_bfdf70893b00a85",
  "carrier": "USPS",
  "tracking_events": [],
  "thumbnails": [
    {
      "small": "https://lob-assets.com/self-mailers/sfm_8ffbe811dea49dcf_thumb_small_1.png?version=v1&expires=1618512040&signature=-bipeUHP-hAMcCBSrWM0ZH1VwRdSPNVGGZN9hAZKr6Lh4ly6uxvratVd5LXJCK_zOEMYk_mTWASt0ge7OY6SDA",
      "medium": "https://lob-assets.com/self-mailers/sfm_8ffbe811dea49dcf_thumb_medium_1.png?version=v1&expires=1618512040&signature=ryxN7bsXGtw_GRFSP3Cs3A3IYjxZi3cW9BHDCNgMt6p3nobVmsc_iFHt2e-S7ndAXhhN7nP-MQVov3bt3r37BQ",
      "large": "https://lob-assets.com/self-mailers/sfm_8ffbe811dea49dcf_thumb_large_1.png?version=v1&expires=1618512040&signature=kBrm00xkyCkJNJRHxH8HshFaebtOxnzjVWOs1VVmGMuw8H6OBNcMAMxt9s49K0jlpHoh3Nr9uSncEZMQaaNjAg"
    },
    {
      "small": "https://lob-assets.com/self-mailers/sfm_8ffbe811dea49dcf_thumb_small_2.png?version=v1&expires=1618512040&signature=3gTgU7Fd3KoT_vNlQnTGptRps5ZgnkhSnPrAwk7L98higIzSwfKoLvuu_DIpMM48dHbxckKT9waR8euJ4KSDBQ",
      "medium": "https://lob-assets.com/self-mailers/sfm_8ffbe811dea49dcf_thumb_medium_2.png?version=v1&expires=1618512040&signature=Ue1lw5CMj7KRx6cMQL8xPeazaHCdJzWcACd1w3acuYPnWkVIpSt62OIO7hAtpAQK9xm1dhhlFj0rqRZMdRMMBA",
      "large": "https://lob-assets.com/self-mailers/sfm_8ffbe811dea49dcf_thumb_large_2.png?version=v1&expires=1618512040&signature=cICc7HEm1xG_eyM4a_wtvPk2FqoLRmtgGa29kJisWnMIYBL0OkyzG4ZCYGMhp-5cZpJlSpXfTgGKh_Qmeo1TDw"
    }
  ],
  "merge_variables": {
    "name": null
  },
  "size": "6x18_bifold",
  "mail_type": "usps_first_class",
  "expected_delivery_date": "2021-03-24",
  "date_created": "2021-03-16T18:40:40.504Z",
  "date_modified": "2021-03-16T18:40:40.504Z",
  "send_date": "2021-03-16T18:45:40.493Z",
  "use_type": "marketing",
  "fsc": false,
  "object": "self_mailer"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |

