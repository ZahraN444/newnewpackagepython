
# Bank Accounts Response 1

## Structure

`BankAccountsResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | **Constraints**: *Pattern*: `^bank_[a-zA-Z0-9]+$` |
| `deleted` | `bool` | Optional | Only returned if the resource has been successfully deleted. |

## Example (as JSON)

```json
{
  "id": "id2",
  "deleted": false
}
```

