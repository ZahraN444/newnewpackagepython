
# Zip Lookup City

## Structure

`ZipLookupCity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `city` | `str` | Required | **Constraints**: *Maximum Length*: `200` |
| `state` | `str` | Required | The <a href="https://en.wikipedia.org/wiki/ISO_3166-2" target="_blank">ISO 3166-2</a> two letter code for the state.<br>**Constraints**: *Maximum Length*: `2` |
| `county` | `str` | Required | County name of the address city. |
| `county_fips` | `str` | Required | A 5-digit <a href="https://en.wikipedia.org/wiki/FIPS_county_code" target="_blank">FIPS county code</a> which uniquely identifies `components[county]`. It consists of a 2-digit state code and a 3-digit county code.<br>**Constraints**: *Pattern*: `\d{5}` |
| `preferred` | `bool` | Required | Indicates whether or not the city is the <a href="https://en.wikipedia.org/wiki/ZIP_Code#ZIP_Codes_and_previous_zoning_lines" target="_blank">USPS default city</a> (preferred city) of a ZIP code. There is only one preferred city per ZIP code, which will always be in position 0 in the array of cities. |

## Example (as JSON)

```json
{
  "city": "city2",
  "state": "state8",
  "county": "county6",
  "county_fips": "county_fips2",
  "preferred": true
}
```

