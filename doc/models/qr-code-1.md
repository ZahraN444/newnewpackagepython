
# Qr Code 1

## Structure

`QrCode1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `position` | `str` | Required, Constant | Sets how a QR code is being positioned in the document. Together with this, you should provide one of 'top' or 'bottom', and one of 'left' or 'right'.<br>**Default**: `'relative'` |
| `top` | `str` | Optional | Vertical distance (in inches) to place QR code from the top. Only allowed if "bottom" isn't provided. |
| `right` | `str` | Optional | Horizonal distance (in inches) to place QR code from the right. Only allowed if "left" isn't provided. |
| `left` | `str` | Optional | Horizonal distance (in inches) to place QR code from the left. Only allowed if "right" isn't provided. |
| `bottom` | `str` | Optional | Vertical distance (in inches) to place QR code from the bottom. Only allowed if "top" isn't provided. |
| `redirect_url` | str \| None | Optional | This is a container for one-of cases. |
| `width` | `str` | Required | The size (in inches) of the QR code with a minimum of 1 inch. All QR codes are generated as a square. |
| `pages` | `str` | Optional | Specify the pages where the QR code should be stamped in a comma separated format. Your QR code can be printed in the same position on multiple pages. For postcards, the values should either be "front", "back" (for either front or back) or "front,back" (for the QR code to be printed on both sides). For self-mailers, the values should either be "inside", "outside" (for either inside or outside) or "inside,outside" (for the QR code to be printed on both sides). For letters, the values can be specific page numbers ("1", "3"), page number ranges such as "1-3", or a comma separated combination of both ("1,3,5-7"). |

## Example (as JSON)

```json
{
  "position": "relative",
  "width": "width6",
  "top": "top4",
  "right": "right6",
  "left": "left6",
  "bottom": "bottom8",
  "redirect_url": "String3"
}
```

