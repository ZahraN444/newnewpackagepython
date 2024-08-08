
# Error 1

## Structure

`Error1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message` | `str` | Required | A human-readable message with more details about the error |
| `status_code` | [`FailureStatusCodeEnum`](../../doc/models/failure-status-code-enum.md) | Required | - |
| `code` | [`CodeEnum`](../../doc/models/code-enum.md) | Required | - |

## Example (as JSON)

```json
{
  "message": "Rate limit exceeded. Please wait 5 seconds and try your request again.",
  "status_code": 500,
  "code": "feature_limit_reached"
}
```

