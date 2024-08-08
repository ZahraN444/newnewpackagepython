# Buckslip Orders

```python
buckslip_orders_controller = client.buckslip_orders
```

## Class Name

`BuckslipOrdersController`

## Methods

* [Buckslip Orders Retrieve](../../doc/controllers/buckslip-orders.md#buckslip-orders-retrieve)
* [Buckslip Order Create](../../doc/controllers/buckslip-orders.md#buckslip-order-create)


# Buckslip Orders Retrieve

Retrieves the buckslip orders associated with the given buckslip id.

```python
def buckslip_orders_retrieve(self,
                            buckslip_id,
                            limit=10,
                            offset=0)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `buckslip_id` | `str` | Template, Required | The ID of the buckslip to which the buckslip orders belong. |
| `limit` | `int` | Query, Optional | How many results to return. |
| `offset` | `int` | Query, Optional | An integer that designates the offset at which to begin returning results. Defaults to 0. |

## Response Type

[`BuckslipsOrdersResponse`](../../doc/models/buckslips-orders-response.md)

## Example Usage

```python
buckslip_id = 'buckslip_id6'

limit = 10

offset = 0

result = buckslip_orders_controller.buckslip_orders_retrieve(
    buckslip_id,
    limit=limit,
    offset=offset
)
```

## Example Response *(as JSON)*

```json
{
  "data": [
    {
      "id": "bo_e0f8a0562a06bea7f",
      "buckslip_id": "bck_6afffd19045076c",
      "status": "available",
      "quantity_ordered": 5000,
      "unit_price": 0.75,
      "cancelled_reason": "No longer needed",
      "availability_date": "2021-10-12T21:41:48.326Z",
      "expected_availability_date": "2021-11-04T21:03:18.871Z",
      "date_created": "2021-10-07T21:03:18.871Z",
      "date_modified": "2021-10-16T01:00:30.144Z",
      "object": "buckslip_order"
    }
  ],
  "object": "list",
  "next_url": null,
  "previous_url": null,
  "count": 1
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |


# Buckslip Order Create

Creates a new buckslip order given information

```python
def buckslip_order_create(self,
                         buckslip_id,
                         content_type,
                         quantity)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `buckslip_id` | `str` | Template, Required | The ID of the buckslip to which the buckslip orders belong. |
| `content_type` | [`ContentTypeEnum`](../../doc/models/content-type-enum.md) | Header, Required | - |
| `quantity` | `int` | Form, Required | The quantity of buckslips in the order (minimum 5,000). |

## Response Type

[`BuckslipOrder`](../../doc/models/buckslip-order.md)

## Example Usage

```python
buckslip_id = 'buckslip_id6'

content_type = ContentTypeEnum.ENUM_APPLICATIONXWWWFORMURLENCODED

quantity = 10000

result = buckslip_orders_controller.buckslip_order_create(
    buckslip_id,
    content_type,
    quantity
)
```

## Example Response *(as JSON)*

```json
{
  "id": "bo_e0f8a0562a06bea7f",
  "buckslip_id": "bck_6afffd19045076c",
  "status": "available",
  "quantity_ordered": 10000,
  "unit_price": 0.75,
  "cancelled_reason": "No longer needed",
  "availability_date": "2021-10-12T21:41:48.326Z",
  "expected_availability_date": "2021-11-04T21:03:18.871Z",
  "date_created": "2021-10-07T21:03:18.871Z",
  "date_modified": "2021-10-16T01:00:30.144Z",
  "object": "buckslip_order"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |

