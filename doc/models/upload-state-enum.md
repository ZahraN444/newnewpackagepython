
# Upload State Enum

The `state` property on the `upload` object. As the file is processed, the `state` will change from `Ready for Validation` to `Validating` and then will be either `Scheduled` (successfully processed) or `Errored` (Unsuccessfully processed).

## Enumeration

`UploadStateEnum`

## Fields

| Name |
|  --- |
| `PREPROCESSING` |
| `DRAFT` |
| `ENUM_READY_FOR_VALIDATION` |
| `VALIDATING` |
| `SCHEDULED` |
| `CANCELLED` |
| `ERRORED` |

