# Buckslips

The Buckslips endpoint allows you to easily create buckslips that can later be used as add-ons for Letters Campaigns. Note that a Letter Campaign with Buckslip add-on requires a minimum send quantity of 5,000 letters.
The API provides endpoints for creating buckslips, retrieving individual buckslips, creating buckslip orders, and retrieving a list of buckslips.

<div class="back-to-top" ><a href="#" onclick="toTopLink()">back to top</a></div>


```python
buckslips_controller = client.buckslips
```

## Class Name

`BuckslipsController`

## Methods

* [Buckslips List](../../doc/controllers/buckslips.md#buckslips-list)
* [Buckslip Create](../../doc/controllers/buckslips.md#buckslip-create)
* [Buckslip Retrieve](../../doc/controllers/buckslips.md#buckslip-retrieve)
* [Buckslip Update](../../doc/controllers/buckslips.md#buckslip-update)
* [Buckslip Delete](../../doc/controllers/buckslips.md#buckslip-delete)


# Buckslips List

Returns a list of your buckslips. The buckslips are returned sorted by creation date, with the most recently created buckslips appearing first.

```python
def buckslips_list(self,
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

[`BuckslipsResponse`](../../doc/models/buckslips-response.md)

## Example Usage

```python
limit = 10

result = buckslips_controller.buckslips_list(
    limit=limit
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |


# Buckslip Create

Creates a new buckslip given information

```python
def buckslip_create(self,
                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`BuckslipEditable`](../../doc/models/buckslip-editable.md) | Body, Required | - |

## Response Type

[`Buckslip`](../../doc/models/buckslip.md)

## Example Usage

```python
body = BuckslipEditable(
    front='https://s3-us-west-2.amazonaws.com/public.lob.com/assets/buckslip.pdf',
    description='Test buckslip',
    back='https://s3-us-west-2.amazonaws.com/public.lob.com/assets/buckslip.pdf'
)

result = buckslips_controller.buckslip_create(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |


# Buckslip Retrieve

Retrieves the details of an existing buckslip. You need only supply the unique customer identifier that was returned upon buckslip creation.

```python
def buckslip_retrieve(self,
                     buckslip_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `buckslip_id` | `str` | Template, Required | id of the buckslip |

## Response Type

[`Buckslip`](../../doc/models/buckslip.md)

## Example Usage

```python
buckslip_id = 'buckslip_id6'

result = buckslips_controller.buckslip_retrieve(buckslip_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |


# Buckslip Update

Update the details of an existing buckslip. You need only supply the unique identifier that was returned upon buckslip creation.

```python
def buckslip_update(self,
                   buckslip_id,
                   content_type,
                   description=None,
                   auto_reorder=None,
                   reorder_quantity=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `buckslip_id` | `str` | Template, Required | id of the buckslip |
| `content_type` | [`ContentTypeEnum`](../../doc/models/content-type-enum.md) | Header, Required | - |
| `description` | `str` | Form, Optional | Description of the buckslip. |
| `auto_reorder` | `bool` | Form, Optional | Allows for auto reordering |
| `reorder_quantity` | `float` | Form, Optional | The quantity of items to be reordered (only required when auto_reorder is true). |

## Response Type

[`Buckslip`](../../doc/models/buckslip.md)

## Example Usage

```python
buckslip_id = 'buckslip_id6'

content_type = ContentTypeEnum.ENUM_APPLICATIONXWWWFORMURLENCODED

description = 'Test buckslip'

auto_reorder = True

result = buckslips_controller.buckslip_update(
    buckslip_id,
    content_type,
    description=description,
    auto_reorder=auto_reorder
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |


# Buckslip Delete

Delete an existing buckslip. You need only supply the unique identifier that was returned upon buckslip creation.

```python
def buckslip_delete(self,
                   buckslip_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `buckslip_id` | `str` | Template, Required | id of the buckslip |

## Response Type

[`BuckslipsResponse1`](../../doc/models/buckslips-response-1.md)

## Example Usage

```python
buckslip_id = 'buckslip_id6'

result = buckslips_controller.buckslip_delete(buckslip_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |

