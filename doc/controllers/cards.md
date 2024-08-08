# Cards

The cards endpoint allows you to easily create cards that can later be affixed to Letters.
The API provides endpoints for creating cards, retrieving individual cards, creating card orders, and retrieving a list of cards.

<div class="back-to-top" ><a href="#" onclick="toTopLink()">back to top</a></div>


```python
cards_controller = client.cards
```

## Class Name

`CardsController`

## Methods

* [Cards List](../../doc/controllers/cards.md#cards-list)
* [Card Create](../../doc/controllers/cards.md#card-create)
* [Card Retrieve](../../doc/controllers/cards.md#card-retrieve)
* [Card Update](../../doc/controllers/cards.md#card-update)
* [Card Delete](../../doc/controllers/cards.md#card-delete)


# Cards List

Returns a list of your cards. The cards are returned sorted by creation date, with the most recently created addresses appearing first.

```python
def cards_list(self,
              limit=10,
              before_after=None,
              include=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `int` | Query, Optional | How many results to return. |
| `before_after` | [`Beforeafter`](../../doc/models/beforeafter.md) | Query, Optional | `before` and `after` are both optional but only one of them can be in the query at a time. |
| `include` | `List[str]` | Query, Optional | Request that the response include the total count by specifying `include=["total_count"]`. |

## Response Type

[`CardsResponse`](../../doc/models/cards-response.md)

## Example Usage

```python
limit = 10

result = cards_controller.cards_list(
    limit=limit
)
```

## Example Response *(as JSON)*

```json
{
  "data": [
    {
      "id": "card_7a6d73c5c8457fc",
      "account_id": "fa9ea650fc7b31a89f92",
      "description": null,
      "url": "https://lob-assets.com/cards/card_c51ae96f5cebf3e.pdf?version=v1&expires=1636910992&signature=mnsDH2DAxdkN9VibdlLMxJC86sME5WYDqkNtmvGwdNsAaUWfbnv0rJhJ1mR8Ol4uxQq61j5wYZ0r3s-lBkQfDA",
      "size": "2.125x3.375",
      "auto_reorder": false,
      "reorder_quantity": null,
      "raw_url": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_raw.pdf?version=v1&expires=1636910992&signature=-bZo31FMAp2vmNaZKyXn_Qa4APqwtNinw76FrQ7uyQejFZw6VBQQYfoiQ642iXh0H2K5i2aOo8_BAkt3UJdVDw",
      "front_original_url": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_raw.pdf?version=v1&expires=1636910992&signature=-bZo31FMAp2vmNaZKyXn_Qa4APqwtNinw76FrQ7uyQejFZw6VBQQYfoiQ642iXh0H2K5i2aOo8_BAkt3UJdVDw",
      "back_original_url": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_raw.pdf?version=v1&expires=1636910992&signature=-bZo31FMAp2vmNaZKyXn_Qa4APqwtNinw76FrQ7uyQejFZw6VBQQYfoiQ642iXh0H2K5i2aOo8_BAkt3UJdVDw",
      "thumbnails": [
        {
          "small": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_thumb_small_1.png?version=v1&expires=1636910992&signature=mrv8JDvpZK4I8WUGH0tPdtK-My5oes0Ltj_gL7BDw96SpCTTeZFHkz81SzclyFP9dQRtlsvAsjcuGcTBvCvOCg",
          "medium": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_thumb_medium_1.png?version=v1&expires=1636910992&signature=VgL_2Ckm_kxKiWGgWtdNoy9HHOn8dGYSVOn7UqyCbwdbVlUtx28TRN4Bo8Iru3n0keKp9He0YhKT1ILotznMDA",
          "large": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_thumb_large_1.png?version=v1&expires=1636910992&signature=FKSzymA13j-CQ0uk20cGHZTzT3vimzNBYrgp-xifLFg4mMdo1BZALR5O0aF_jVhsX614hKP35ONdYl47TQxXAw"
        }
      ],
      "available_quantity": 10000,
      "pending_quantity": 0,
      "countries": null,
      "status": "rendered",
      "mode": "test",
      "orientation": "horizontal",
      "threshold_amount": 0,
      "date_created": "2021-03-24T22:51:42.838Z",
      "date_modified": "2021-03-24T22:51:42.838Z",
      "send_date": "2021-03-24T22:51:42.838Z",
      "object": "card"
    }
  ],
  "object": "list",
  "previous_url": null,
  "next_url": null,
  "count": 1
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |


# Card Create

Creates a new card given information

```python
def card_create(self,
               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CardEditable`](../../doc/models/card-editable.md) | Body, Required | - |

## Response Type

[`Card`](../../doc/models/card.md)

## Example Usage

```python
body = CardEditable(
    front='https://s3-us-west-2.amazonaws.com/public.lob.com/assets/card_horizontal.pdf',
    description='Test card',
    size=Size1Enum.ENUM_2125X3375,
    back='https://s3-us-west-2.amazonaws.com/public.lob.com/assets/card_horizontal.pdf'
)

result = cards_controller.card_create(body)
```

## Example Response *(as JSON)*

```json
{
  "id": "card_7a6d73c5c8457fc",
  "account_id": "fa9ea650fc7b31a89f92",
  "description": "Test card",
  "url": "https://lob-assets.com/cards/card_c51ae96f5cebf3e.pdf?version=v1&expires=1636910992&signature=mnsDH2DAxdkN9VibdlLMxJC86sME5WYDqkNtmvGwdNsAaUWfbnv0rJhJ1mR8Ol4uxQq61j5wYZ0r3s-lBkQfDA",
  "size": "2.125x3.375",
  "auto_reorder": false,
  "reorder_quantity": null,
  "raw_url": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_raw.pdf?version=v1&expires=1636910992&signature=-bZo31FMAp2vmNaZKyXn_Qa4APqwtNinw76FrQ7uyQejFZw6VBQQYfoiQ642iXh0H2K5i2aOo8_BAkt3UJdVDw",
  "front_original_url": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_raw.pdf?version=v1&expires=1636910992&signature=-bZo31FMAp2vmNaZKyXn_Qa4APqwtNinw76FrQ7uyQejFZw6VBQQYfoiQ642iXh0H2K5i2aOo8_BAkt3UJdVDw",
  "back_original_url": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_raw.pdf?version=v1&expires=1636910992&signature=-bZo31FMAp2vmNaZKyXn_Qa4APqwtNinw76FrQ7uyQejFZw6VBQQYfoiQ642iXh0H2K5i2aOo8_BAkt3UJdVDw",
  "thumbnails": [
    {
      "small": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_thumb_small_1.png?version=v1&expires=1636910992&signature=mrv8JDvpZK4I8WUGH0tPdtK-My5oes0Ltj_gL7BDw96SpCTTeZFHkz81SzclyFP9dQRtlsvAsjcuGcTBvCvOCg",
      "medium": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_thumb_medium_1.png?version=v1&expires=1636910992&signature=VgL_2Ckm_kxKiWGgWtdNoy9HHOn8dGYSVOn7UqyCbwdbVlUtx28TRN4Bo8Iru3n0keKp9He0YhKT1ILotznMDA",
      "large": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_thumb_large_1.png?version=v1&expires=1636910992&signature=FKSzymA13j-CQ0uk20cGHZTzT3vimzNBYrgp-xifLFg4mMdo1BZALR5O0aF_jVhsX614hKP35ONdYl47TQxXAw"
    },
    {
      "small": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_thumb_small_2.png?version=v1&expires=1636910992&signature=IWsmPa_ULlv2yyqjX564d_YfHHY_M7i9YxDnw-WXDr2jtOFcArmRZQbnHeE9g_rYxnddJbgosuv8-c2utiu7Cg",
      "medium": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_thumb_medium_2.png?version=v1&expires=1636910992&signature=zxK7VKGiTvz5Ywrkaydd0v3GcYf58R7A08J4tNfI7-aiNODDcTF3l0MqY13n9Pyc8RXSdD0XVBY-OpbA1VM-Ag",
      "large": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_thumb_large_2.png?version=v1&expires=1636910992&signature=r0OFUhh315ZwN0raMZdIwJd2oCIEYsz0BABaMxIuO1PKTD0ckGWrhcGdzk2dlWQ6vSvp0CUQ5k1RXGqkIIqkDw"
    }
  ],
  "available_quantity": 10000,
  "pending_quantity": 0,
  "countries": null,
  "status": "rendered",
  "mode": "test",
  "orientation": "horizontal",
  "threshold_amount": 0,
  "date_created": "2021-03-24T22:51:42.838Z",
  "date_modified": "2021-03-24T22:51:42.838Z",
  "send_date": "2021-03-24T22:51:42.838Z",
  "object": "card"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |


# Card Retrieve

Retrieves the details of an existing card. You need only supply the unique customer identifier that was returned upon card creation.

```python
def card_retrieve(self,
                 card_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_id` | `str` | Template, Required | id of the card |

## Response Type

[`Card`](../../doc/models/card.md)

## Example Usage

```python
card_id = 'card_id4'

result = cards_controller.card_retrieve(card_id)
```

## Example Response *(as JSON)*

```json
{
  "id": "card_7a6d73c5c8457fc",
  "account_id": "fa9ea650fc7b31a89f92",
  "description": "Test card",
  "url": "https://lob-assets.com/cards/card_c51ae96f5cebf3e.pdf?version=v1&expires=1636910992&signature=mnsDH2DAxdkN9VibdlLMxJC86sME5WYDqkNtmvGwdNsAaUWfbnv0rJhJ1mR8Ol4uxQq61j5wYZ0r3s-lBkQfDA",
  "size": "2.125x3.375",
  "auto_reorder": false,
  "reorder_quantity": null,
  "raw_url": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_raw.pdf?version=v1&expires=1636910992&signature=-bZo31FMAp2vmNaZKyXn_Qa4APqwtNinw76FrQ7uyQejFZw6VBQQYfoiQ642iXh0H2K5i2aOo8_BAkt3UJdVDw",
  "front_original_url": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_raw.pdf?version=v1&expires=1636910992&signature=-bZo31FMAp2vmNaZKyXn_Qa4APqwtNinw76FrQ7uyQejFZw6VBQQYfoiQ642iXh0H2K5i2aOo8_BAkt3UJdVDw",
  "back_original_url": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_raw.pdf?version=v1&expires=1636910992&signature=-bZo31FMAp2vmNaZKyXn_Qa4APqwtNinw76FrQ7uyQejFZw6VBQQYfoiQ642iXh0H2K5i2aOo8_BAkt3UJdVDw",
  "thumbnails": [
    {
      "small": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_thumb_small_1.png?version=v1&expires=1636910992&signature=mrv8JDvpZK4I8WUGH0tPdtK-My5oes0Ltj_gL7BDw96SpCTTeZFHkz81SzclyFP9dQRtlsvAsjcuGcTBvCvOCg",
      "medium": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_thumb_medium_1.png?version=v1&expires=1636910992&signature=VgL_2Ckm_kxKiWGgWtdNoy9HHOn8dGYSVOn7UqyCbwdbVlUtx28TRN4Bo8Iru3n0keKp9He0YhKT1ILotznMDA",
      "large": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_thumb_large_1.png?version=v1&expires=1636910992&signature=FKSzymA13j-CQ0uk20cGHZTzT3vimzNBYrgp-xifLFg4mMdo1BZALR5O0aF_jVhsX614hKP35ONdYl47TQxXAw"
    },
    {
      "small": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_thumb_small_2.png?version=v1&expires=1636910992&signature=IWsmPa_ULlv2yyqjX564d_YfHHY_M7i9YxDnw-WXDr2jtOFcArmRZQbnHeE9g_rYxnddJbgosuv8-c2utiu7Cg",
      "medium": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_thumb_medium_2.png?version=v1&expires=1636910992&signature=zxK7VKGiTvz5Ywrkaydd0v3GcYf58R7A08J4tNfI7-aiNODDcTF3l0MqY13n9Pyc8RXSdD0XVBY-OpbA1VM-Ag",
      "large": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_thumb_large_2.png?version=v1&expires=1636910992&signature=r0OFUhh315ZwN0raMZdIwJd2oCIEYsz0BABaMxIuO1PKTD0ckGWrhcGdzk2dlWQ6vSvp0CUQ5k1RXGqkIIqkDw"
    }
  ],
  "available_quantity": 10000,
  "pending_quantity": 0,
  "countries": null,
  "status": "rendered",
  "mode": "test",
  "orientation": "horizontal",
  "threshold_amount": 0,
  "date_created": "2021-03-24T22:51:42.838Z",
  "date_modified": "2021-03-24T22:51:42.838Z",
  "send_date": "2021-03-24T22:51:42.838Z",
  "object": "card"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |


# Card Update

Update the details of an existing card. You need only supply the unique identifier that was returned upon card creation.

```python
def card_update(self,
               card_id,
               content_type,
               description=None,
               auto_reorder=None,
               reorder_quantity=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_id` | `str` | Template, Required | id of the card |
| `content_type` | [`ContentTypeEnum`](../../doc/models/content-type-enum.md) | Header, Required | - |
| `description` | `str` | Form, Optional | Description of the card. |
| `auto_reorder` | `bool` | Form, Optional | Allows for auto reordering |
| `reorder_quantity` | `float` | Form, Optional | The quantity of items to be reordered (only required when auto_reorder is true). |

## Response Type

[`Card`](../../doc/models/card.md)

## Example Usage

```python
card_id = 'card_id4'

content_type = ContentTypeEnum.ENUM_APPLICATIONXWWWFORMURLENCODED

description = 'Test card'

auto_reorder = True

result = cards_controller.card_update(
    card_id,
    content_type,
    description=description,
    auto_reorder=auto_reorder
)
```

## Example Response *(as JSON)*

```json
{
  "id": "card_7a6d73c5c8457fc",
  "account_id": "fa9ea650fc7b31a89f92",
  "description": "Test card",
  "url": "https://lob-assets.com/cards/card_c51ae96f5cebf3e.pdf?version=v1&expires=1636910992&signature=mnsDH2DAxdkN9VibdlLMxJC86sME5WYDqkNtmvGwdNsAaUWfbnv0rJhJ1mR8Ol4uxQq61j5wYZ0r3s-lBkQfDA",
  "size": "2.125x3.375",
  "auto_reorder": false,
  "reorder_quantity": null,
  "raw_url": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_raw.pdf?version=v1&expires=1636910992&signature=-bZo31FMAp2vmNaZKyXn_Qa4APqwtNinw76FrQ7uyQejFZw6VBQQYfoiQ642iXh0H2K5i2aOo8_BAkt3UJdVDw",
  "front_original_url": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_raw.pdf?version=v1&expires=1636910992&signature=-bZo31FMAp2vmNaZKyXn_Qa4APqwtNinw76FrQ7uyQejFZw6VBQQYfoiQ642iXh0H2K5i2aOo8_BAkt3UJdVDw",
  "back_original_url": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_raw.pdf?version=v1&expires=1636910992&signature=-bZo31FMAp2vmNaZKyXn_Qa4APqwtNinw76FrQ7uyQejFZw6VBQQYfoiQ642iXh0H2K5i2aOo8_BAkt3UJdVDw",
  "thumbnails": [
    {
      "small": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_thumb_small_1.png?version=v1&expires=1636910992&signature=mrv8JDvpZK4I8WUGH0tPdtK-My5oes0Ltj_gL7BDw96SpCTTeZFHkz81SzclyFP9dQRtlsvAsjcuGcTBvCvOCg",
      "medium": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_thumb_medium_1.png?version=v1&expires=1636910992&signature=VgL_2Ckm_kxKiWGgWtdNoy9HHOn8dGYSVOn7UqyCbwdbVlUtx28TRN4Bo8Iru3n0keKp9He0YhKT1ILotznMDA",
      "large": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_thumb_large_1.png?version=v1&expires=1636910992&signature=FKSzymA13j-CQ0uk20cGHZTzT3vimzNBYrgp-xifLFg4mMdo1BZALR5O0aF_jVhsX614hKP35ONdYl47TQxXAw"
    },
    {
      "small": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_thumb_small_2.png?version=v1&expires=1636910992&signature=IWsmPa_ULlv2yyqjX564d_YfHHY_M7i9YxDnw-WXDr2jtOFcArmRZQbnHeE9g_rYxnddJbgosuv8-c2utiu7Cg",
      "medium": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_thumb_medium_2.png?version=v1&expires=1636910992&signature=zxK7VKGiTvz5Ywrkaydd0v3GcYf58R7A08J4tNfI7-aiNODDcTF3l0MqY13n9Pyc8RXSdD0XVBY-OpbA1VM-Ag",
      "large": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_thumb_large_2.png?version=v1&expires=1636910992&signature=r0OFUhh315ZwN0raMZdIwJd2oCIEYsz0BABaMxIuO1PKTD0ckGWrhcGdzk2dlWQ6vSvp0CUQ5k1RXGqkIIqkDw"
    }
  ],
  "available_quantity": 10000,
  "pending_quantity": 0,
  "countries": null,
  "status": "rendered",
  "mode": "test",
  "orientation": "horizontal",
  "threshold_amount": 0,
  "date_created": "2021-03-24T22:51:42.838Z",
  "date_modified": "2021-03-24T22:51:42.838Z",
  "send_date": "2021-03-24T22:51:42.838Z",
  "object": "card"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |


# Card Delete

Delete an existing card. You need only supply the unique identifier that was returned upon card creation.

```python
def card_delete(self,
               card_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_id` | `str` | Template, Required | id of the card |

## Response Type

[`CardsResponse5`](../../doc/models/cards-response-5.md)

## Example Usage

```python
card_id = 'card_id4'

result = cards_controller.card_delete(card_id)
```

## Example Response *(as JSON)*

```json
{
  "id": "card_123456789",
  "deleted": true
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |

