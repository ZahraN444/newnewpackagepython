
# Name 1 Enum

Name of tracking event for Certified letters. Letters sent with USPS Certified Mail are fully tracked by USPS, therefore their tracking events have an additional details object with more detailed information about the tracking event. Some certified tracking event names have multiple meanings, noted in the list here. See the description of the details object for the full set of combined certified tracking event name meanings.

* `Mailed` - Package has been accepted into the carrier network for delivery.

* `In Transit` - Maps to four distinct stages of transit.

* `In Local Area` - Package is at a location near the end destination.

* `Processed for Delivery` - Maps to two distinct stages of delivery.

* `Pickup Available` - Package is available for pickup at carrier location.

* `Delivered` - Package has been delivered.

* `Re-Routed` - Package has been forwarded.

* `Returned to Sender` - Package is to be returned to sender.

* `Issue` - Maps to (at least) 15 possible issues, some of which are actionable.

## Enumeration

`Name1Enum`

## Fields

| Name |
|  --- |
| `MAILED` |
| `ENUM_IN_TRANSIT` |
| `ENUM_IN_LOCAL_AREA` |
| `ENUM_PROCESSED_FOR_DELIVERY` |
| `ENUM_PICKUP_AVAILABLE` |
| `DELIVERED` |
| `REROUTED` |
| `ENUM_RETURNED_TO_SENDER` |
| `ISSUE` |

