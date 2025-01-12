
# Code Enum

A pre-defined string identifying an error. Error codes fall into three categories:

**GENERIC**

* `bad_request` - 422: an invalid request was made. See error message for details.
* `conflict` - 409/422: this operation would leave data in a conflicted state.
* `feature_limit_reached` - 403: the account has reached its resource limit and requires upgrading to add more.
* `internal_server_error` - 500: an error has occured on Lob's servers. Please try request again.
* `invalid` - 422: an invalid request was made. See error message for details.
* `not_deletable` - 422: an attempt was made to delete a resource, but the resource cannot be deleted.
* `not_found` - 404: the requested resource was not found.
* `request_timeout` - 408: the request took too long. Please try again.
* `service_unavailable` - 503: the Lob servers are temporarily unavailable. Please try agian.
* `unrecognized_endpoint` - 404: the requested endpoint doesn't exist.
* `unsupported_lob_version` - 422: an unsupported Lob API version was requested.

**ADVANCED**

* `address_length_exceeds_limit` - 422: the sum of to.address_line1 and to.address_line2 cannot surpass 50 characters.
* `bank_account_already_verified` - 422: the bank account has already been verified.
* `bank_error` - 422: there's an issue with the bank account.
* `billing_address_required` - 403: in order to create a live mail piece, your account needs to set up a billing address.
* `custom_envelope_inventory_depleted` - 422: custom envelope inventory is depleted, and more will need to be ordered.
* `deleted_bank_account` - 404: checks cannot be created with a deleted bank account.
* `failed_deliverability_strictness` - 422: the `to` address doesn't meet strictness requirements. See <a href="https://dashboard.lob.com/#/settings/account" target="_blank">Account Settings</a> to configure strictness.
* `file_pages_below_min` - 422: not enough pages.
* `file_pages_exceed_max` - 422: too many pages.
* `file_size_exceeds_limit` - 422: the file size is too large. See description for details.
* `foreign_return_address` - 422: the `from` address must be a US address.
* `inconsistent_page_dimensions` - 422: all pages of the input file must have the same dimensions.
* `invalid_bank_account` - 422: the provided bank routing number is invalid.
* `invalid_bank_account_verification` - 422: verification amounts do not match.
* `invalid_check_international` - 422: checks cannot be sent internationally.
* `invalid_country_covid` - 422: the postal service in the specified country is currently unable to process the request due to COVID-19 restrictions.
* `invalid_file` - 422: the file is invalid.
* `invalid_file_dimensions` - 422: file dimensions are incorrect for the selected mail type.
* `invalid_file_download_time` - 422: file download from remote server took too long.
* `invalid_file_url` - 422: the file URL when creating a resource is invalid.
* `invalid_image_dpi` - 422: DPI must be at least 300.
* `invalid_international_feature` - 422: the specified product cannot be sent to the destination.
* `invalid_perforation_return_envelope` - 422: both `return_envelope` and `perforation` must be used together.
* `invalid_template_html` - 422: the provided HTML is invalid.
* `mail_use_type_can_not_be_null` - 422: use_type must be one of "marketing" or "operational". Alternatively, an admin can set the account default use type in Account Settings.
* `merge_variable_required` - 422: a required merge variable is missing.
* `merge_variable_whitespace` - 422: merge variable names cannot contain whitespace.
* `payment_method_unverified` - 401: you must have a verified bank account or credit card to submit live requests.
* `pdf_encrypted` - 422: an encrypted PDF was provided.
* `special_characters_restricted` - 422: cannot use special characters for merge variable names.
* `unembedded_fonts` - 422: the provided PDF contains non-standard unembedded fonts. See description for details.

**AUTHENTICATION**

* `email_required` - 401: account must have a verified email address before creating live resources.
* `invalid_api_key` - 401/403: the API key is invalid.
* `publishable_key_not_allowed` - 403: the requested operation needs a secret key, not a publishable key. See [API Keys](#section/API-Keys) for more information.
* `rate_limit_exceeded` - 429: requests were sent too quickly and must be slowed down.
* `unauthorized` - 401: the request isn't authorized.
* `unauthorized_token` - 401: token isn't authorized.

## Enumeration

`CodeEnum`

## Fields

| Name |
|  --- |
| `BAD_REQUEST` |
| `CONFLICT` |
| `FEATURE_LIMIT_REACHED` |
| `INTERNAL_SERVER_ERROR` |
| `INVALID` |
| `NOT_DELETABLE` |
| `NOT_FOUND` |
| `REQUEST_TIMEOUT` |
| `SERVICE_UNAVAILABLE` |
| `UNRECOGNIZED_ENDPOINT` |
| `UNSUPPORTED_LOB_VERSION` |
| `ADDRESS_LENGTH_EXCEEDS_LIMIT` |
| `BANK_ACCOUNT_ALREADY_VERIFIED` |
| `BANK_ERROR` |
| `BILLING_ADDRESS_REQUIRED` |
| `CUSTOM_ENVELOPE_INVENTORY_DEPLETED` |
| `DELETED_BANK_ACCOUNT` |
| `FAILED_DELIVERABILITY_STRICTNESS` |
| `FILE_PAGES_BELOW_MIN` |
| `FILE_PAGES_EXCEED_MAX` |
| `FILE_SIZE_EXCEEDS_LIMIT` |
| `FOREIGN_RETURN_ADDRESS` |
| `INCONSISTENT_PAGE_DIMENSIONS` |
| `INVALID_BANK_ACCOUNT` |
| `INVALID_BANK_ACCOUNT_VERIFICATION` |
| `INVALID_CHECK_INTERNATIONAL` |
| `INVALID_COUNTRY_COVID` |
| `INVALID_FILE` |
| `INVALID_FILE_DIMENSIONS` |
| `INVALID_FILE_DOWNLOAD_TIME` |
| `INVALID_FILE_URL` |
| `INVALID_IMAGE_DPI` |
| `INVALID_INTERNATIONAL_FEATURE` |
| `INVALID_PERFORATION_RETURN_ENVELOPE` |
| `INVALID_TEMPLATE_HTML` |
| `MAIL_USE_TYPE_CAN_NOT_BE_NULL` |
| `MERGE_VARIABLE_REQUIRED` |
| `MERGE_VARIABLE_WHITESPACE` |
| `PAYMENT_METHOD_UNVERIFIED` |
| `PDF_ENCRYPTED` |
| `SPECIAL_CHARACTERS_RESTRICTED` |
| `UNEMBEDDED_FONTS` |
| `EMAIL_REQUIRED` |
| `INVALID_API_KEY` |
| `PUBLISHABLE_KEY_NOT_ALLOWED` |
| `RATE_LIMIT_EXCEEDED` |
| `UNAUTHORIZED` |
| `UNAUTHORIZED_TOKEN` |

