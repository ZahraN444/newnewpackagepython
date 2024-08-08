# Identity Validation

```python
identity_validation_controller = client.identity_validation
```

## Class Name

`IdentityValidationController`


# Identity Validation

Validates whether a given name is associated with an address.

```python
def identity_validation(self,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`object`](../../doc/models/object-enum.md) | Body, Required | - |

## Response Type

[recipient_validation](../../doc/models/recipient-validation.md) | [company_validation](../../doc/models/company-validation.md)

## Example Usage

```python
body = jsonpickle.decode('{"recipient":"Larry Lobster","primary_line":"210 King St.","secondary_line":"","city":"San Francisco","state":"CA","zip_code":"94107"}')

result = identity_validation_controller.identity_validation(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |

