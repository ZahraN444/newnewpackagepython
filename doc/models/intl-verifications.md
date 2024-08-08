
# Intl Verifications

## Structure

`IntlVerifications`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `addresses` | List[[intl_verification](../../doc/models/intl-verification.md) \| [error](../../doc/models/error.md)] | Required | This is List of a container for one-of cases. |
| `errors` | `bool` | Required | Indicates whether any errors occurred during the verification process. |

## Example (as JSON)

```json
{
  "addresses": [
    {
      "recipient": "recipient0",
      "primary_line": "primary_line8",
      "secondary_line": "secondary_line4",
      "id": "id8",
      "last_line": "last_line8"
    },
    {
      "recipient": "recipient0",
      "primary_line": "primary_line8",
      "secondary_line": "secondary_line4",
      "id": "id8",
      "last_line": "last_line8"
    }
  ],
  "errors": false
}
```

