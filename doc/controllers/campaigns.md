# Campaigns

The campaigns endpoint allows you to create and view campaigns that can be used to send multiple letters or postcards.
The API provides endpoints for creating campaigns, updating campaigns, retrieving individual campaigns, listing campaigns, and deleting
campaigns.

```python
campaigns_controller = client.campaigns
```

## Class Name

`CampaignsController`

## Methods

* [Campaigns List](../../doc/controllers/campaigns.md#campaigns-list)
* [Campaign Create](../../doc/controllers/campaigns.md#campaign-create)
* [Campaign Retrieve](../../doc/controllers/campaigns.md#campaign-retrieve)
* [Campaign Update](../../doc/controllers/campaigns.md#campaign-update)
* [Campaign Delete](../../doc/controllers/campaigns.md#campaign-delete)
* [Campaign Send](../../doc/controllers/campaigns.md#campaign-send)


# Campaigns List

Returns a list of your campaigns. The campaigns are returned sorted by creation date, with the most recently created campaigns appearing first.

```python
def campaigns_list(self,
                  limit=10,
                  include=None,
                  before_after=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `int` | Query, Optional | How many results to return. |
| `include` | `List[str]` | Query, Optional | Request that the response include the total count by specifying `include=["total_count"]`. |
| `before_after` | [`Beforeafter`](../../doc/models/beforeafter.md) | Query, Optional | `before` and `after` are both optional but only one of them can be in the query at a time. |

## Response Type

[`AllCampaigns`](../../doc/models/all-campaigns.md)

## Example Usage

```python
limit = 10

result = campaigns_controller.campaigns_list(
    limit=limit
)
```

## Example Response *(as JSON)*

```json
{
  "data": [
    {
      "id": "cmp_e05ee61ff80764b",
      "billing_group_id": "bg_fe3079dcdd80e5ae",
      "name": "My Campaign",
      "description": "My Campaign's description",
      "schedule_type": "immediate",
      "send_date": null,
      "target_delivery_date": null,
      "cancel_window_campaign_minutes": 60,
      "metadata": {},
      "use_type": "marketing",
      "is_draft": true,
      "deleted": false,
      "creatives": [],
      "uploads": [],
      "auto_cancel_if_ncoa": false,
      "date_created": "2017-09-05T17:47:53.767Z",
      "date_modified": "2017-09-05T17:47:53.767Z",
      "object": "campaign"
    }
  ],
  "object": "list",
  "previous_url": null,
  "next_url": null,
  "count": 1
}
```


# Campaign Create

Creates a new campaign with the provided properties. See how to launch your first campaign [here](https://help.lob.com/print-and-mail/building-a-mail-strategy/campaign-or-triggered-sends/launch-your-first-campaign).

```python
def campaign_create(self,
                   content_type,
                   name,
                   schedule_type,
                   use_type,
                   x_lang_output=None,
                   billing_group_id=None,
                   description=None,
                   target_delivery_date=None,
                   send_date=None,
                   cancel_window_campaign_minutes=None,
                   metadata=None,
                   auto_cancel_if_ncoa=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content_type` | [`ContentTypeEnum`](../../doc/models/content-type-enum.md) | Header, Required | - |
| `name` | `str` | Form, Required | Name of the campaign. |
| `schedule_type` | [`CmpScheduleTypeEnum`](../../doc/models/cmp-schedule-type-enum.md) | Form, Required | - |
| `use_type` | `typing.BinaryIO` | Form, Required | - |
| `x_lang_output` | [`XLangOutput1Enum`](../../doc/models/x-lang-output-1-enum.md) | Header, Optional | * `native` - Translate response to the native language of the country in the request<br>* `match` - match the response to the language in the request<br><br>Default response is in English. |
| `billing_group_id` | `str` | Form, Optional | Unique identifier prefixed with `bg_`. |
| `description` | `str` | Form, Optional | An internal description that identifies this resource. Must be no longer than 255 characters. |
| `target_delivery_date` | `datetime` | Form, Optional | If `schedule_type` is `target_delivery_date`, provide a targeted delivery date for mail pieces in this campaign. |
| `send_date` | `datetime` | Form, Optional | If `schedule_type` is `scheduled_send_date`, provide a date to send this campaign. |
| `cancel_window_campaign_minutes` | `int` | Form, Optional | A window, in minutes, within which the campaign can be canceled. |
| `metadata` | `Dict[str, str]` | Form, Optional | Use metadata to store custom information for tagging and labeling back to your internal systems. Must be an object with up to 20 key-value pairs. Keys must be at most 40 characters and values must be at most 500 characters. Neither can contain the characters `"` and `\`. i.e. '{"customer_id" : "NEWYORK2015"}' Nested objects are not supported.  See [Metadata](#section/Metadata) for more information. |
| `auto_cancel_if_ncoa` | `bool` | Form, Optional | Whether or not a mail piece should be automatically canceled and not sent if the address is updated via NCOA. |

## Response Type

[`Campaign`](../../doc/models/campaign.md)

## Example Usage

```python
content_type = ContentTypeEnum.ENUM_APPLICATIONXWWWFORMURLENCODED

name = 'My Demo Campaign'

schedule_type = CmpScheduleTypeEnum.IMMEDIATE

use_type = FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type')

description = 'My Campaign\'s description'

result = campaigns_controller.campaign_create(
    content_type,
    name,
    schedule_type,
    use_type,
    description=description
)
```

## Example Response *(as JSON)*

```json
{
  "id": "cmp_e05ee61ff80764b",
  "billing_group_id": "bg_fe3079dcdd80e5ae",
  "name": "My Campaign",
  "description": "My Campaign's description",
  "schedule_type": "immediate",
  "cancel_window_campaign_minutes": 60,
  "metadata": {},
  "use_type": "marketing",
  "is_draft": true,
  "deleted": false,
  "creatives": [],
  "uploads": [],
  "auto_cancel_if_ncoa": false,
  "date_created": "2017-09-05T17:47:53.767Z",
  "date_modified": "2017-09-05T17:47:53.767Z",
  "object": "campaign"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |


# Campaign Retrieve

Retrieves the details of an existing campaign. You need only supply the unique campaign identifier that was returned upon campaign creation.

```python
def campaign_retrieve(self,
                     cmp_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cmp_id` | `str` | Template, Required | id of the campaign |

## Response Type

[`Campaign`](../../doc/models/campaign.md)

## Example Usage

```python
cmp_id = 'cmp_id0'

result = campaigns_controller.campaign_retrieve(cmp_id)
```

## Example Response *(as JSON)*

```json
{
  "id": "cmp_e05ee61ff80764b",
  "billing_group_id": "bg_fe3079dcdd80e5ae",
  "name": "My Campaign",
  "description": "My Campaign's description",
  "schedule_type": "immediate",
  "cancel_window_campaign_minutes": 60,
  "metadata": {},
  "use_type": "marketing",
  "is_draft": true,
  "deleted": false,
  "creatives": [],
  "uploads": [],
  "auto_cancel_if_ncoa": false,
  "date_created": "2017-09-05T17:47:53.767Z",
  "date_modified": "2017-09-05T17:47:53.767Z",
  "object": "campaign"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |


# Campaign Update

Update the details of an existing campaign. You need only supply the unique identifier that was returned upon campaign creation.

```python
def campaign_update(self,
                   cmp_id,
                   content_type,
                   name=None,
                   description=None,
                   schedule_type=None,
                   target_delivery_date=None,
                   send_date=None,
                   cancel_window_campaign_minutes=None,
                   metadata=None,
                   is_draft=None,
                   use_type=None,
                   auto_cancel_if_ncoa=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cmp_id` | `str` | Template, Required | id of the campaign |
| `content_type` | [`ContentTypeEnum`](../../doc/models/content-type-enum.md) | Header, Required | - |
| `name` | `str` | Form, Optional | - |
| `description` | `str` | Form, Optional | An internal description that identifies this resource. Must be no longer than 255 characters. |
| `schedule_type` | [`CmpScheduleTypeEnum`](../../doc/models/cmp-schedule-type-enum.md) | Form, Optional | - |
| `target_delivery_date` | `datetime` | Form, Optional | If `schedule_type` is `target_delivery_date`, provide a targeted delivery date for mail pieces in this campaign. |
| `send_date` | `datetime` | Form, Optional | If `schedule_type` is `scheduled_send_date`, provide a date to send this campaign. |
| `cancel_window_campaign_minutes` | `int` | Form, Optional | A window, in minutes, within which the campaign can be canceled. |
| `metadata` | `Dict[str, str]` | Form, Optional | Use metadata to store custom information for tagging and labeling back to your internal systems. Must be an object with up to 20 key-value pairs. Keys must be at most 40 characters and values must be at most 500 characters. Neither can contain the characters `"` and `\`. i.e. '{"customer_id" : "NEWYORK2015"}' Nested objects are not supported.  See [Metadata](#section/Metadata) for more information. |
| `is_draft` | `bool` | Form, Optional | Whether or not the campaign is still a draft. Can either be excluded or `false`. |
| `use_type` | `typing.BinaryIO` | Form, Optional | - |
| `auto_cancel_if_ncoa` | `bool` | Form, Optional | Whether or not a mail piece should be automatically canceled and not sent if the address is updated via NCOA. |

## Response Type

[`Campaign`](../../doc/models/campaign.md)

## Example Usage

```python
cmp_id = 'cmp_id0'

content_type = ContentTypeEnum.ENUM_APPLICATIONXWWWFORMURLENCODED

description = 'Test campaign'

result = campaigns_controller.campaign_update(
    cmp_id,
    content_type,
    description=description
)
```

## Example Response *(as JSON)*

```json
{
  "id": "cmp_e05ee61ff80764b",
  "billing_group_id": "bg_fe3079dcdd80e5ae",
  "name": "My Campaign",
  "description": "My Campaign's description",
  "schedule_type": "immediate",
  "cancel_window_campaign_minutes": 60,
  "metadata": {},
  "use_type": "marketing",
  "is_draft": true,
  "deleted": false,
  "creatives": [],
  "uploads": [],
  "auto_cancel_if_ncoa": false,
  "date_created": "2017-09-05T17:47:53.767Z",
  "date_modified": "2017-09-05T17:47:53.767Z",
  "object": "campaign"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |


# Campaign Delete

Delete an existing campaign. You need only supply the unique identifier that was returned upon campaign creation. Deleting a campaign also deletes any associated mail pieces that have been created but not sent. A campaign's `send_date` matches its associated mail pieces' `send_date`s.

```python
def campaign_delete(self,
                   cmp_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cmp_id` | `str` | Template, Required | id of the campaign |

## Response Type

[`CampaignsResponse4`](../../doc/models/campaigns-response-4.md)

## Example Usage

```python
cmp_id = 'cmp_id0'

result = campaigns_controller.campaign_delete(cmp_id)
```

## Example Response *(as JSON)*

```json
{
  "id": "cmp_e05ee61ff80764b",
  "deleted": true
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |


# Campaign Send

Sends a campaign. You need only supply the unique campaign identifier that was returned upon campaign creation.

```python
def campaign_send(self,
                 cmp_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cmp_id` | `str` | Template, Required | id of the campaign |

## Response Type

[`Campaign`](../../doc/models/campaign.md)

## Example Usage

```python
cmp_id = 'cmp_id0'

result = campaigns_controller.campaign_send(cmp_id)
```

## Example Response *(as JSON)*

```json
{
  "id": "cmp_e05ee61ff80764b",
  "billing_group_id": "bg_fe3079dcdd80e5ae",
  "name": "My Campaign",
  "description": "My Campaign's description",
  "schedule_type": "immediate",
  "cancel_window_campaign_minutes": 60,
  "metadata": {},
  "use_type": "marketing",
  "is_draft": true,
  "deleted": false,
  "creatives": [],
  "uploads": [],
  "auto_cancel_if_ncoa": false,
  "date_created": "2017-09-05T17:47:53.767Z",
  "date_modified": "2017-09-05T17:47:53.767Z",
  "object": "campaign"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |

