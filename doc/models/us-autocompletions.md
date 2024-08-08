
# Us Autocompletions

## Structure

`UsAutocompletions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Unique identifier prefixed with `us_auto_`.<br>**Constraints**: *Pattern*: `^us_auto_[a-zA-Z0-9]+$` |
| `suggestions` | [`List[Suggestions]`](../../doc/models/suggestions.md) | Optional | An array of objects representing suggested addresses.<br>**Constraints**: *Minimum Items*: `0`, *Maximum Items*: `10` |
| `object` | [`Object13Enum`](../../doc/models/object-13-enum.md) | Optional | - |

## Example (as JSON)

```json
{
  "id": "id2",
  "suggestions": [
    {
      "primary_line": "primary_line6",
      "city": "city4",
      "state": "state8",
      "zip_code": "zip_code0",
      "object": "us_autocompletion"
    },
    {
      "primary_line": "primary_line6",
      "city": "city4",
      "state": "state8",
      "zip_code": "zip_code0",
      "object": "us_autocompletion"
    }
  ],
  "object": "us_autocompletion"
}
```

