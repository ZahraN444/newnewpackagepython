# Uploads

The uploads endpoint allows you to upload audience files that are then associated with a given campaign.
At this time, only CSV files are allowed. The API provides endpoints for creating uploads, uploading audience files,
and marking uploaded files as ready for processing. The API also provides endpoints for downloading files that
describe the results, both successful and not, of the processing.

```python
uploads_controller = client.uploads
```

## Class Name

`UploadsController`

## Methods

* [Uploads List](../../doc/controllers/uploads.md#uploads-list)
* [Upload Create](../../doc/controllers/uploads.md#upload-create)
* [Upload Retrieve](../../doc/controllers/uploads.md#upload-retrieve)
* [Upload Update](../../doc/controllers/uploads.md#upload-update)
* [Upload Delete](../../doc/controllers/uploads.md#upload-delete)
* [Upload File](../../doc/controllers/uploads.md#upload-file)
* [Upload Export Create](../../doc/controllers/uploads.md#upload-export-create)
* [Report Retrieve](../../doc/controllers/uploads.md#report-retrieve)
* [Export Retrieve](../../doc/controllers/uploads.md#export-retrieve)


# Uploads List

Returns a list of your uploads. Optionally, filter uploads by campaign.

```python
def uploads_list(self,
                campaign_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `campaign_id` | `str` | Query, Optional | id of the campaign |

## Response Type

[`List[Upload]`](../../doc/models/upload.md)

## Example Usage

```python
result = uploads_controller.uploads_list()
```

## Example Response *(as JSON)*

```json
[
  {
    "id": "upl_71be866e430b11e9",
    "accountId": "fa9ea650fc7b31a89f92",
    "campaignId": "cmp_1933ad629bae1408",
    "mode": "test",
    "failuresUrl": "https://www.example.com",
    "originalFilename": "my_audience.csv",
    "state": "Draft",
    "totalMailpieces": 100,
    "failedMailpieces": 5,
    "validatedMailpieces": 95,
    "bytesProcessed": 17268,
    "dateCreated": "2017-09-05T17:47:53.767Z",
    "dateModified": "2017-09-05T17:47:53.767Z",
    "requiredAddressColumnMapping": {
      "name": "recipient_name",
      "address_line1": "primary_line",
      "address_city": "city",
      "address_state": "state",
      "address_zip": "zip_code"
    },
    "optionalAddressColumnMapping": {
      "address_line2": "secondary_line",
      "company": "company",
      "address_country": "country"
    },
    "mergeVariableColumnMapping": {
      "gift_code": "code"
    },
    "metadata": {
      "columns": [
        "recipient_name",
        "zip_code"
      ]
    }
  }
]
```


# Upload Create

Creates a new upload with the provided properties.

```python
def upload_create(self,
                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`UploadWritable`](../../doc/models/upload-writable.md) | Body, Required | - |

## Response Type

[`Upload`](../../doc/models/upload.md)

## Example Usage

```python
body = UploadWritable(
    campaign_id='campaignId4',
    merge_variable_column_mapping={"name":"recipient_name","gift_code":"code"}
)

result = uploads_controller.upload_create(body)
```

## Example Response *(as JSON)*

```json
{
  "id": "upl_71be866e430b11e9",
  "accountId": "fa9ea650fc7b31a89f92",
  "campaignId": "cmp_1933ad629bae1408",
  "mode": "live",
  "failuresUrl": "http://www.example.com",
  "originalFilename": "my_audience.csv",
  "state": "Draft",
  "totalMailpieces": 100,
  "failedMailpieces": 5,
  "validatedMailpieces": 95,
  "bytesProcessed": 17628,
  "dateCreated": "2017-09-05T17:47:53.767Z",
  "dateModified": "2017-09-05T17:47:53.767Z",
  "requiredAddressColumnMapping": {
    "name": null,
    "address_line1": null,
    "address_city": null,
    "address_state": null,
    "address_zip": null
  },
  "optionalAddressColumnMapping": {
    "address_line2": null,
    "company": null,
    "address_country": null
  },
  "mergeVariableColumnMapping": null,
  "metadata": {
    "columns": []
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Validation Error | [`HTTPValidationError1Exception`](../../doc/models/http-validation-error-1-exception.md) |


# Upload Retrieve

Retrieves the details of an existing upload. You need only supply the unique upload identifier that was returned upon upload creation.

```python
def upload_retrieve(self,
                   upl_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `upl_id` | `str` | Template, Required | id of the upload |

## Response Type

[`Upload`](../../doc/models/upload.md)

## Example Usage

```python
upl_id = 'upl_id0'

result = uploads_controller.upload_retrieve(upl_id)
```

## Example Response *(as JSON)*

```json
{
  "id": "upl_71be866e430b11e9",
  "accountId": "fa9ea650fc7b31a89f92",
  "campaignId": "cmp_1933ad629bae1408",
  "mode": "live",
  "failuresUrl": "http://www.example.com",
  "originalFilename": "my_audience.csv",
  "state": "Draft",
  "totalMailpieces": 100,
  "failedMailpieces": 5,
  "validatedMailpieces": 95,
  "bytesProcessed": 17628,
  "dateCreated": "2017-09-05T17:47:53.767Z",
  "dateModified": "2017-09-05T17:47:53.767Z",
  "requiredAddressColumnMapping": {
    "name": null,
    "address_line1": null,
    "address_city": null,
    "address_state": null,
    "address_zip": null
  },
  "optionalAddressColumnMapping": {
    "address_line2": null,
    "company": null,
    "address_country": null
  },
  "mergeVariableColumnMapping": null,
  "metadata": {
    "columns": []
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |
| 422 | Validation Error | [`HTTPValidationError1Exception`](../../doc/models/http-validation-error-1-exception.md) |


# Upload Update

Update the details of an existing upload. You need only supply the unique identifier that was returned upon upload creation.

```python
def upload_update(self,
                 upl_id,
                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `upl_id` | `str` | Template, Required | id of the upload |
| `body` | [`UploadUpdatable`](../../doc/models/upload-updatable.md) | Body, Required | - |

## Response Type

[`Upload`](../../doc/models/upload.md)

## Example Usage

```python
upl_id = 'upl_id0'

body = UploadUpdatable(
    merge_variable_column_mapping={"name":"recipient_name","gift_code":"code"}
)

result = uploads_controller.upload_update(
    upl_id,
    body
)
```

## Example Response *(as JSON)*

```json
{
  "id": "upl_71be866e430b11e9",
  "accountId": "fa9ea650fc7b31a89f92",
  "campaignId": "cmp_1933ad629bae1408",
  "mode": "live",
  "failuresUrl": "http://www.example.com",
  "originalFilename": "my_audience.csv",
  "state": "Draft",
  "totalMailpieces": 100,
  "failedMailpieces": 5,
  "validatedMailpieces": 95,
  "bytesProcessed": 17628,
  "dateCreated": "2017-09-05T17:47:53.767Z",
  "dateModified": "2017-09-05T17:47:53.767Z",
  "requiredAddressColumnMapping": {
    "name": null,
    "address_line1": null,
    "address_city": null,
    "address_state": null,
    "address_zip": null
  },
  "optionalAddressColumnMapping": {
    "address_line2": null,
    "company": null,
    "address_country": null
  },
  "mergeVariableColumnMapping": null,
  "metadata": {
    "columns": []
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |
| 422 | Validation Error | [`HTTPValidationError1Exception`](../../doc/models/http-validation-error-1-exception.md) |


# Upload Delete

Delete an existing upload. You need only supply the unique identifier that was returned upon upload creation.

```python
def upload_delete(self,
                 upl_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `upl_id` | `str` | Template, Required | id of the upload |

## Response Type

`void`

## Example Usage

```python
upl_id = 'upl_id0'

result = uploads_controller.upload_delete(upl_id)
```


# Upload File

Upload an [audience file](https://help.lob.com/print-and-mail/building-a-mail-strategy/campaign-or-triggered-sends/campaign-audience-guide) and associate it with an upload.

```python
def upload_file(self,
               upl_id,
               file=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `upl_id` | `str` | Template, Required | ID of the upload |
| `file` | `typing.BinaryIO` | Form, Optional | - |

## Response Type

[`UploadFile`](../../doc/models/upload-file.md)

## Example Usage

```python
upl_id = 'upl_id0'

result = uploads_controller.upload_file(upl_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Validation Error | [`HTTPValidationError1Exception`](../../doc/models/http-validation-error-1-exception.md) |


# Upload Export Create

Campaign Exports can help you understand exactly which records in a campaign could not be created. By initiating and retrieving an export, you will get row-by-row errors for your campaign. For a step-by-step walkthrough of creating a campaign and exporting failures, see our [Campaigns Guide](https://help.lob.com/print-and-mail/building-a-mail-strategy/campaign-or-triggered-sends/launch-your-first-campaign).

Create an export file associated with an upload.

```python
def upload_export_create(self,
                        upl_id,
                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `upl_id` | `str` | Template, Required | ID of the upload |
| `body` | [`UploadsExportsRequest`](../../doc/models/uploads-exports-request.md) | Body, Required | - |

## Response Type

[`UploadCreateExport`](../../doc/models/upload-create-export.md)

## Example Usage

```python
upl_id = 'upl_id0'

body = UploadsExportsRequest()

result = uploads_controller.upload_export_create(
    upl_id,
    body
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 401 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 402 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 403 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 404 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 405 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 406 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 407 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 408 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 409 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 410 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 411 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 412 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 413 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 414 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 415 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 416 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 417 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 418 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 419 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 420 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 421 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 422 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 423 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 424 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 425 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 426 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 427 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 428 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 429 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 430 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 431 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 432 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 433 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 434 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 435 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 436 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 437 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 438 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 439 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 440 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 441 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 442 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 443 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 444 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 445 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 446 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 447 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 448 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 449 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 450 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 451 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 452 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 453 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 454 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 455 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 456 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 457 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 458 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 459 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 460 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 461 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 462 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 463 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 464 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 465 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 466 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 467 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 468 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 469 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 470 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 471 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 472 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 473 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 474 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 475 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 476 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 477 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 478 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 479 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 480 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 481 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 482 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 483 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 484 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 485 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 486 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 487 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 488 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 489 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 490 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 491 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 492 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 493 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 494 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 495 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 496 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 497 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 498 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |
| 499 | Create Export Error | [`UploadExportError1Exception`](../../doc/models/upload-export-error-1-exception.md) |


# Report Retrieve

Retrieves the line item data for each row from the csv file associated with the upload id record. NOTE: This endpoint is currently feature flagged. Please reach out to Lob's support team if you  would like access to this API endpoint.

```python
def report_retrieve(self,
                   upl_id,
                   status=None,
                   limit=100,
                   offset=0)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `upl_id` | `str` | Template, Required | ID of the upload |
| `status` | [`Status31Enum`](../../doc/models/status-31-enum.md) | Query, Optional | The status of line items to filter and retrieve. By default all line items are returned. |
| `limit` | `int` | Query, Optional | How many results to return. |
| `offset` | `int` | Query, Optional | An integer that designates the offset at which to begin returning results. Defaults to 0. |

## Response Type

[`UploadsReportResponse`](../../doc/models/uploads-report-response.md)

## Example Usage

```python
upl_id = 'upl_id0'

limit = 10

offset = 0

result = uploads_controller.report_retrieve(
    upl_id,
    limit=limit,
    offset=offset
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 403 | Forbidden Error | [`UploadsReport403ErrorException`](../../doc/models/uploads-report-403-error-exception.md) |
| 404 | Not Found Error | [`Domains0Error1Exception`](../../doc/models/domains-0-error-1-exception.md) |


# Export Retrieve

Retrieves the details of an existing export. You need only supply the unique export identifier that was returned upon export creation. If you try retrieving an export immediately after creating one (i.e., before we're done processing the export), you will get back an export object with `state = in_progress`.

```python
def export_retrieve(self,
                   upl_id,
                   ex_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `upl_id` | `str` | Template, Required | ID of the upload |
| `ex_id` | `str` | Template, Required | ID of the export |

## Response Type

[`UploadsExportsResponse`](../../doc/models/uploads-exports-response.md)

## Example Usage

```python
upl_id = 'upl_id0'

ex_id = 'ex_id4'

result = uploads_controller.export_retrieve(
    upl_id,
    ex_id
)
```

