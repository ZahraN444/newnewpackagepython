# URL Shortener

```python
url_shortener_controller = client.url_shortener
```

## Class Name

`URLShortenerController`

## Methods

* [Domain Get](../../doc/controllers/url-shortener.md#domain-get)
* [Domain Delete](../../doc/controllers/url-shortener.md#domain-delete)
* [Domain Create](../../doc/controllers/url-shortener.md#domain-create)
* [Domain List](../../doc/controllers/url-shortener.md#domain-list)
* [Domain Delete Links](../../doc/controllers/url-shortener.md#domain-delete-links)
* [Links List](../../doc/controllers/url-shortener.md#links-list)
* [Links Get](../../doc/controllers/url-shortener.md#links-get)
* [Link Update](../../doc/controllers/url-shortener.md#link-update)
* [Links Delete](../../doc/controllers/url-shortener.md#links-delete)
* [Link Create](../../doc/controllers/url-shortener.md#link-create)
* [Link Bulk Create](../../doc/controllers/url-shortener.md#link-bulk-create)


# Domain Get

Retrieve details for a single domain.

```python
def domain_get(self,
              domain_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `domain_id` | `str` | Template, Required | Unique identifier for a domain. |

## Response Type

[`DomainResponse`](../../doc/models/domain-response.md)

## Example Usage

```python
domain_id = 'domain_id2'

result = url_shortener_controller.domain_get(domain_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |


# Domain Delete

Delete a registered domain. This operation can only be performed if all associated links with the domain are deleted.

```python
def domain_delete(self,
                 domain_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `domain_id` | `str` | Template, Required | Unique identifier for a domain. |

## Response Type

[`DomainResponse`](../../doc/models/domain-response.md)

## Example Usage

```python
domain_id = 'domain_id2'

result = url_shortener_controller.domain_delete(domain_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |


# Domain Create

Add a new custom domain that can be used to create custom links.

```python
def domain_create(self,
                 content_type,
                 domain)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content_type` | [`ContentTypeEnum`](../../doc/models/content-type-enum.md) | Header, Required | - |
| `domain` | `str` | Form, Required | The registered domain/hostname. |

## Response Type

[`DomainResponse`](../../doc/models/domain-response.md)

## Example Usage

```python
content_type = ContentTypeEnum.ENUM_APPLICATIONXWWWFORMURLENCODED

domain = 'domain6'

result = url_shortener_controller.domain_create(
    content_type,
    domain
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |


# Domain List

Retrieve a list of all created domains.

```python
def domain_list(self)
```

## Response Type

[`DomainsResponse`](../../doc/models/domains-response.md)

## Example Usage

```python
result = url_shortener_controller.domain_list()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |


# Domain Delete Links

Delete all associated links for a domain

```python
def domain_delete_links(self,
                       domain_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `domain_id` | `str` | Template, Required | Unique identifier for a domain. |

## Response Type

[`DomainsResponse`](../../doc/models/domains-response.md)

## Example Usage

```python
domain_id = 'domain_id2'

result = url_shortener_controller.domain_delete_links(domain_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`DomainsLinks0Error1Exception`](../../doc/models/domains-links-0-error-1-exception.md) |


# Links List

Retrieves a list of shortened links. The list is sorted by  creation date, with the most recently created appearing first.

```python
def links_list(self,
              limit=10,
              offset=0,
              include=None,
              date_created=None,
              metadata=None,
              campaign_id=None,
              clicked=None,
              billing_group_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `int` | Query, Optional | How many results to return. |
| `offset` | `int` | Query, Optional | An integer that designates the offset at which to begin returning results. Defaults to 0. |
| `include` | `List[str]` | Query, Optional | Request that the response include the total count by specifying `include=["total_count"]`. |
| `date_created` | `Dict[str, str]` | Query, Optional | Filter by date created. Accepted formats are ISO-8601 date or datetime, e.g. `{ "gt": "2012-01-01", "lt": "2012-01-31T12:34:56Z" }` where `gt` is >, `lt` is <, `gte` is ≥, and `lte` is ≤. |
| `metadata` | `Dict[str, str]` | Query, Optional | Filter by metadata key-value pair`. |
| `campaign_id` | `str` | Query, Optional | Filter the links generated for a particular campaign using its campaign id. |
| `clicked` | `bool` | Query, Optional | Retrieve the list of links that have been opened. |
| `billing_group_id` | `str` | Query, Optional | Filter the links generated for a particular billing group id. |

## Response Type

[`LinksResponse`](../../doc/models/links-response.md)

## Example Usage

```python
limit = 10

offset = 0

result = url_shortener_controller.links_list(
    limit=limit,
    offset=offset
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Links0Error1Exception`](../../doc/models/links-0-error-1-exception.md) |


# Links Get

Retrievs a single shortened link.

```python
def links_get(self,
             link_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `link_id` | `str` | Template, Required | Unique identifier for a link. |

## Response Type

[`LinkResponse`](../../doc/models/link-response.md)

## Example Usage

```python
link_id = 'link_id0'

result = url_shortener_controller.links_get(link_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Links0Error1Exception`](../../doc/models/links-0-error-1-exception.md) |


# Link Update

Update any of the properties of a shortened link.

```python
def link_update(self,
               link_id,
               content_type,
               redirect_link,
               domain=None,
               slug=None,
               metadata_tag=None,
               billing_group_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `link_id` | `str` | Template, Required | Unique identifier for a link. |
| `content_type` | [`ContentTypeEnum`](../../doc/models/content-type-enum.md) | Header, Required | - |
| `redirect_link` | `str` | Form, Required | The original target URL. |
| `domain` | `str` | Form, Optional | The registered domain to be used for the short URL. |
| `slug` | `str` | Form, Optional | The unique path for the shortened URL, if empty a unique path will be used. |
| `metadata_tag` | `Dict[str, str]` | Form, Optional | Use metadata to store custom information for tagging and labeling back to your internal systems. Must be an object with up to 20 key-value pairs. Keys must be at most 40 characters and values must be at most 500 characters. Neither can contain the characters `"` and `\`. i.e. '{"customer_id" : "NEWYORK2015"}' Nested objects are not supported.  See [Metadata](#section/Metadata) for more information. |
| `billing_group_id` | `str` | Form, Optional | An optional string with the billing group ID to tag your usage with. Is used for billing purposes. Requires special activation to use. See <a href="#tag/Billing-Groups">Billing Group API</a> for more information. |

## Response Type

[`LinkResponse`](../../doc/models/link-response.md)

## Example Usage

```python
link_id = 'link_id0'

content_type = ContentTypeEnum.ENUM_APPLICATIONXWWWFORMURLENCODED

redirect_link = 'redirect_link0'

result = url_shortener_controller.link_update(
    link_id,
    content_type,
    redirect_link
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |


# Links Delete

Delete the shortened link.

```python
def links_delete(self,
                link_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `link_id` | `str` | Template, Required | Unique identifier for a link. |

## Response Type

[`LinkResponse`](../../doc/models/link-response.md)

## Example Usage

```python
link_id = 'link_id0'

result = url_shortener_controller.links_delete(link_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Links0Error1Exception`](../../doc/models/links-0-error-1-exception.md) |


# Link Create

Given a long URL, shorten your URL either by using a custom domain or Lob's own short domain.

```python
def link_create(self,
               content_type,
               redirect_link,
               domain=None,
               slug=None,
               metadata_tag=None,
               billing_group_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content_type` | [`ContentTypeEnum`](../../doc/models/content-type-enum.md) | Header, Required | - |
| `redirect_link` | `str` | Form, Required | The original target URL. |
| `domain` | `str` | Form, Optional | The registered domain to be used for the short URL. |
| `slug` | `str` | Form, Optional | The unique path for the shortened URL, if empty a unique path will be used. |
| `metadata_tag` | `Dict[str, str]` | Form, Optional | Use metadata to store custom information for tagging and labeling back to your internal systems. Must be an object with up to 20 key-value pairs. Keys must be at most 40 characters and values must be at most 500 characters. Neither can contain the characters `"` and `\`. i.e. '{"customer_id" : "NEWYORK2015"}' Nested objects are not supported.  See [Metadata](#section/Metadata) for more information. |
| `billing_group_id` | `str` | Form, Optional | An optional string with the billing group ID to tag your usage with. Is used for billing purposes. Requires special activation to use. See <a href="#tag/Billing-Groups">Billing Group API</a> for more information. |

## Response Type

[`LinkResponse`](../../doc/models/link-response.md)

## Example Usage

```python
content_type = ContentTypeEnum.ENUM_APPLICATIONXWWWFORMURLENCODED

redirect_link = 'redirect_link0'

result = url_shortener_controller.link_create(
    content_type,
    redirect_link
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |


# Link Bulk Create

Shortens a list of links in a single request.

```python
def link_bulk_create(self,
                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`List[LinkSingle]`](../../doc/models/link-single.md) | Body, Required | - |

## Response Type

[`LinksResponse`](../../doc/models/links-response.md)

## Example Usage

```python
body = [
    LinkSingle(
        redirect_link='redirect_link6'
    )
]

result = url_shortener_controller.link_bulk_create(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |

