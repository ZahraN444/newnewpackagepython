# Zip Lookups

```python
zip_lookups_controller = client.zip_lookups
```

## Class Name

`ZipLookupsController`


# Zip Lookup

Returns information about a ZIP code

```python
def zip_lookup(self,
              content_type,
              zip_code)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content_type` | [`ContentTypeEnum`](../../doc/models/content-type-enum.md) | Header, Required | - |
| `zip_code` | `str` | Form, Required | A 5-digit ZIP code. |

## Response Type

[`Zip`](../../doc/models/zip.md)

## Example Usage

```python
content_type = ContentTypeEnum.ENUM_APPLICATIONXWWWFORMURLENCODED

zip_code = '94107'

result = zip_lookups_controller.zip_lookup(
    content_type,
    zip_code
)
```

## Example Response *(as JSON)*

```json
{
  "id": "us_zip_c7cb63d68f8d6",
  "cities": [
    {
      "city": "SAN FRANCISCO",
      "state": "CA",
      "county": "SAN FRANCISCO",
      "county_fips": "06075",
      "preferred": true
    }
  ],
  "zip_code_type": "standard",
  "object": "us_zip_lookup",
  "zip_code": "94107"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |

