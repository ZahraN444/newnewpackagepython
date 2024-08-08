# US Verifications

```python
us_verifications_controller = client.us_verifications
```

## Class Name

`USVerificationsController`

## Methods

* [Bulk Us Verifications](../../doc/controllers/us-verifications.md#bulk-us-verifications)
* [Us Verification](../../doc/controllers/us-verifications.md#us-verification)


# Bulk Us Verifications

Verify a list of US or US territory addresses _with a live API key_. Requests to this endpoint with a test API key will return a dummy response based on the primary line you input.

```python
def bulk_us_verifications(self,
                         content_type,
                         addresses,
                         case=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content_type` | [`ContentTypeEnum`](../../doc/models/content-type-enum.md) | Header, Required | - |
| `addresses` | [`List[MultipleComponents]`](../../doc/models/multiple-components.md) | Form, Required | - |
| `case` | [`Case2Enum`](../../doc/models/case-2-enum.md) | Query, Optional | Casing of the verified address. Possible values are `upper` and `proper` for uppercased (e.g. "PO BOX") and proper-cased (e.g. "PO Box"), respectively. Only affects `recipient`, `primary_line`, `secondary_line`, `urbanization`, and `last_line`. Default casing is `upper`. |

## Response Type

[`UsVerifications`](../../doc/models/us-verifications.md)

## Example Usage

```python
content_type = ContentTypeEnum.ENUM_APPLICATIONXWWWFORMURLENCODED

addresses = [
    MultipleComponents(
        primary_line='210 King Street',
        city='San Francisco',
        state='CA',
        zip_code='94107'
    ),
    MultipleComponents(
        primary_line='Ave Wilson Churchill 123',
        city='RIO PIEDRAS',
        state='PR',
        zip_code='00926',
        recipient='Walgreens',
        secondary_line='',
        urbanization='URB FAIR OAKS'
    )
]

result = us_verifications_controller.bulk_us_verifications(
    content_type,
    addresses
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |


# Us Verification

Verify a US or US territory address _with a live API key_. The address can be in components (e.g. `primary_line` is "210 King Street", `zip_code` is "94107") or as a single string (e.g. "210 King Street 94107"), but not as both. Requests using a test API key validate required fields but return empty values unless specific `primary_line` values are provided. See the [US Verifications Test Environment](#section/US-Verifications-Test-Env) for details.

```python
def us_verification(self,
                   body,
                   case=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`object`](../../doc/models/object-enum.md) | Body, Required | - |
| `case` | [`Case2Enum`](../../doc/models/case-2-enum.md) | Query, Optional | Casing of the verified address. Possible values are `upper` and `proper` for uppercased (e.g. "PO BOX") and proper-cased (e.g. "PO Box"), respectively. Only affects `recipient`, `primary_line`, `secondary_line`, `urbanization`, and `last_line`. Default casing is `upper`. |

## Response Type

[`UsVerification`](../../doc/models/us-verification.md)

## Example Usage

```python
body = jsonpickle.decode('{"primary_line":"210 King Street","city":"San Francisco","state":"CA","zip_code":"94107"}')

result = us_verifications_controller.us_verification(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |

