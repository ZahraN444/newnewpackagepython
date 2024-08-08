
# Components 4

## Structure

`Components4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `primary_number` | `str` | Required | The numeric or alphanumeric part of an address preceding the street name. Often the house, building, or PO Box number. |
| `street_predirection` | [`StreetPredirectionEnum`](../../doc/models/street-predirection-enum.md) | Required | - |
| `street_name` | `str` | Required | The name of the street. |
| `street_suffix` | `str` | Required | The standard USPS abbreviation for the street suffix (`ST`, `AVE`, `BLVD`, etc). |
| `street_postdirection` | [`StreetPostdirectionEnum`](../../doc/models/street-postdirection-enum.md) | Required | - |
| `secondary_designator` | `str` | Required | The standard USPS abbreviation describing the `components[secondary_number]` (`STE`, `APT`, `BLDG`, etc). |
| `secondary_number` | `str` | Required | Number of the apartment/unit/etc. |
| `pmb_designator` | `str` | Required | Designator of a <a href="https://en.wikipedia.org/wiki/Commercial_mail_receiving_agency" target="_blank">CMRA-authorized</a> private mailbox. |
| `pmb_number` | `str` | Required | Number of a <a href="https://en.wikipedia.org/wiki/Commercial_mail_receiving_agency" target="_blank">CMRA-authorized</a> private mailbox. |
| `extra_secondary_designator` | `str` | Required | An extra (often unnecessary) secondary designator provided with the input address. |
| `extra_secondary_number` | `str` | Required | An extra (often unnecessary) secondary number provided with the input address. |
| `city` | `str` | Required | **Constraints**: *Maximum Length*: `200` |
| `state` | `str` | Required | The <a href="https://en.wikipedia.org/wiki/ISO_3166-2" target="_blank">ISO 3166-2</a> two letter code for the state.<br>**Constraints**: *Maximum Length*: `2` |
| `zip_code` | `str` | Required | The 5-digit ZIP code<br>**Constraints**: *Pattern*: `^\d{5}$` |
| `zip_code_plus_4` | `str` | Required | **Constraints**: *Pattern*: `^\d{4}$` |
| `zip_code_type` | [`ZipCodeTypeEnum`](../../doc/models/zip-code-type-enum.md) | Required | - |
| `delivery_point_barcode` | `str` | Required | A 12-digit identifier that uniquely identifies a delivery point (location where mail can be sent and received). It consists of the 5-digit ZIP code (`zip_code`), 4-digit ZIP+4 add-on (`zip_code_plus_4`), 2-digit delivery point, and 1-digit delivery point check digit. |
| `address_type` | [`AddressTypeEnum`](../../doc/models/address-type-enum.md) | Required | - |
| `record_type` | [`RecordTypeEnum`](../../doc/models/record-type-enum.md) | Required | - |
| `default_building_address` | `bool` | Required | Designates whether or not the address is the default address for a building containing multiple delivery points. |
| `county` | `str` | Required | County name of the address city. |
| `county_fips` | `str` | Required | A 5-digit <a href="https://en.wikipedia.org/wiki/FIPS_county_code" target="_blank">FIPS county code</a> which uniquely identifies `components[county]`. It consists of a 2-digit state code and a 3-digit county code.<br>**Constraints**: *Pattern*: `\d{5}` |
| `carrier_route` | `str` | Required | A 4-character code assigned to a mail delivery route within a ZIP code. |
| `carrier_route_type` | [`CarrierRouteTypeEnum`](../../doc/models/carrier-route-type-enum.md) | Required | - |
| `latitude` | `float` | Optional | A positive or negative decimal indicating the geographic latitude of the address, specifying the north-to-south position of a location. This should be used with `longitude` to pinpoint locations on a map. Will not be returned for undeliverable addresses or military addresses (state is `AA`, `AE`, or `AP`). |
| `longitude` | `float` | Optional | A positive or negative decimal indicating the geographic longitude of the address, specifying the north-to-south position of a location. This should be used with `latitude` to pinpoint locations on a map. Will not be returned for undeliverable addresses or military addresses (state is `AA`, `AE`, or `AP`). |

## Example (as JSON)

```json
{
  "primary_number": "primary_number8",
  "street_predirection": "NE",
  "street_name": "street_name8",
  "street_suffix": "street_suffix8",
  "street_postdirection": "NE",
  "secondary_designator": "secondary_designator4",
  "secondary_number": "secondary_number0",
  "pmb_designator": "pmb_designator0",
  "pmb_number": "pmb_number4",
  "extra_secondary_designator": "extra_secondary_designator0",
  "extra_secondary_number": "extra_secondary_number2",
  "city": "city2",
  "state": "state6",
  "zip_code": "zip_code2",
  "zip_code_plus_4": "zip_code_plus_46",
  "zip_code_type": "unique",
  "delivery_point_barcode": "delivery_point_barcode4",
  "address_type": "residential",
  "record_type": "rural_route",
  "default_building_address": false,
  "county": "county8",
  "county_fips": "county_fips8",
  "carrier_route": "carrier_route6",
  "carrier_route_type": "general_delivery",
  "latitude": 171.38,
  "longitude": 82.42
}
```

