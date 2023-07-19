%%%
title = "OpenID Connect for Identity Assurance Claims Registration 1.0 draft"
abbrev = "openid-connect-4-ida-attachments-1_0"
ipr = "none"
workgroup = "eKYC-IDA"
keyword = ["security", "openid", "identity assurance", "ekyc", "claims"]

[seriesInfo]
name = "Internet-Draft"

value = "openid-connect-4-ida-attachments-1_0-00"

status = "standard"

[[author]]
initials="T."
surname="Lodderstedt"
fullname="Torsten Lodderstedt"
organization="yes.com"
    [author.address]
    email = "torsten@lodderstedt.net"

[[author]]
initials="D."
surname="Fett"
fullname="Daniel Fett"
organization="yes.com"
    [author.address]
    email = "mail@danielfett.de"

[[author]]
initials="M."
surname="Haine"
fullname="Mark Haine"
organization="Considrd.Consulting Ltd"
    [author.address]
    email = "mark@considrd.consulting"

[[author]]
initials="A."
surname="Pulido"
fullname="Alberto Pulido"
organization="Santander"
    [author.address]
    email = "alberto.pulido@santander.co.uk"

[[author]]
initials="K."
surname="Lehmann"
fullname="Kai Lehmann"
organization="1&1 Mail & Media Development & Technology GmbH"
    [author.address]
    email = "kai.lehmann@1und1.de"

[[author]]
initials="K."
surname="Koiwai"
fullname="Kosuke Koiwai"
organization="KDDI Corporation"
    [author.address]
    email = "ko-koiwai@kddi.com"

%%%

.# Abstract

This specification defines an extension of OpenID Connect that registers new JWT claims about End-Users. This extension defines new evidences and attachments relating to the identity of a natural person that were originally defined within earlier drafts of OpenID Connect for Identity Assurance. The work and the preceding drafts are the work of the eKYC and Identity Assurance working group of the OpenID Foundation.

{mainmatter}

# Introduction {#Introduction}

This specification defines additional JWT claims about the natural person.  The attachments defined MAY be used in various contexts. 

# Scope

This specification only defines evidences and attachments to be maintained in the IANA "JSON Web Token Claims Registry" established by [@!RFC7519].  These evidences and attachments SHOULD be used in any context that needs to describe these characteristics of the end-user in a JWT as per [@RFC7519].

## verification Element {#verification}

Additional attributes defined under `assurance_process`:

    * `evidence_ref`: OPTIONAL. JSON array of the evidence being referred to. When present this array MUST have at least one member.
    * `evidence_metadata`: OPTIONAL. Object indicating any meta data about the `evidence` that is required by the `assurance_process` in order to demonstrate compliance with the `trust_framework`. It has the following sub-elements:
    * `evidence_classification`: OPTIONAL. String indicating how the process demonstrated by the `check_details` for the `evidence` is classified by the `assurance_process` in order to demonstrate compliance with the `trust_framework`.

Additional attributes defined in the verification element.

`evidence`: OPTIONAL. JSON array containing information about the evidence the OP used to verify the End-User's identity as separate JSON objects. Every object contains the property `type` which determines the type of the evidence. The RP uses this information to process the `evidence` property appropriately.

Important: Implementations MUST ignore any sub-element not defined in this specification or extensions of this specification.

### evidence Element {#evidence_element}

The `evidence` element is structured with the following elements:

`attachments`: OPTIONAL. Array of JSON objects representing attachments like photocopies of documents or certificates. See (#attachments) on how an attachment is structured.

`type`: REQUIRED. The value defines the type of the evidence.

The following types of evidence are defined:

* `document`: Verification based on the content of a physical or electronic document provided by the End-User, e.g. a passport, ID card, PDF signed by a recognized authority, etc.
* `electronic_record`: Verification based on data or information obtained electronically from an approved, recognized, regulated or certified source, e.g. a Government organization, bank, utility provider, credit reference agency, etc.
* `vouch`: Verification based on an attestation given by an approved or recognized natural person declaring they believe that the Claim(s) presented by the End-User are, to the best of their knowledge, genuine and true.
* `electronic_signature`: Verification based on the use of an electronic signature that can be uniquely linked to the End-User and is capable of identifying the signatory, e.g. an eIDAS Advanced Electronic Signature (AES) or Qualified Electronic Signature (QES).

Depending on the evidence type additional elements are defined, as described in the following.

#### Evidence Type document

The following elements are contained in an evidence sub-element where type is `document`.

`type`: REQUIRED. Value MUST be set to `document`.

`check_details`: OPTIONAL. JSON array representing the checks done in relation to the `evidence`. When present this array MUST have at least one member.

  * `check_method`: REQUIRED. String representing the check done, this includes processes such as checking the authenticity of the document, or verifying the user's biometric against an identity document. For information on predefined `check_details` values see [@!predefined_values].
  * `organization`: OPTIONAL. String denoting the legal entity that performed the check. This  SHOULD be included if the OP did not perform the check itself.
  * `txn`: OPTIONAL. Identifier referring to the identity verification transaction. The OP MUST ensure that this is present when `evidence_ref` element is used. The OP MUST ensure that the transaction identifier can be resolved into transaction details during an audit.
  * `time`: OPTIONAL. Time stamp in ISO 8601 [@!ISO8601] `YYYY-MM-DDThh:mm[:ss]TZD` format representing the date when the check was completed.

`verifier`: OPTIONAL. JSON object denoting the legal entity that performed the identity verification. This object SHOULD be included if the OP did not perform the identity verification itself. This object is retained for backward compatibility, implementers are recommended to use `check_details` & `organization` instead. This object consists of the following properties:

* `organization`: REQUIRED. String denoting the organization which performed the verification on behalf of the OP.
* `txn`: OPTIONAL. Identifier referring to the identity verification transaction. The OP MUST ensure that the transaction identifier can be resolved into transaction details during an audit.

`time`: OPTIONAL. Time stamp in ISO 8601 [@!ISO8601] `YYYY-MM-DDThh:mm[:ss]TZD` format representing the date when this document was verified.

`document_details`: OPTIONAL. JSON object representing the document used to perform the identity verification. It consists of the following properties:

* `type`: REQUIRED. String denoting the type of the document. For information on predefined document values see [@!predefined_values]. The OP MAY use other than the predefined values in which case the RPs will either be unable to process the assertion, just store this value for audit purposes, or apply bespoken business logic to it.
* `document_number`: OPTIONAL. String representing an identifier/number that uniquely identifies a document that was issued to the End-User. This is used on one document and will change if it is reissued, e.g., a passport number, certificate number, etc.
* `serial_number`: OPTIONAL. String representing an identifier/number that identifies the document irrespective of any personalization information (this usually only applies to physical artifacts and is present before personalization).
* `date_of_issuance`: OPTIONAL. The date the document was issued as ISO 8601 [@!ISO8601] `YYYY-MM-DD` format.
* `date_of_expiry`: OPTIONAL. The date the document will expire as ISO 8601 [@!ISO8601] `YYYY-MM-DD` format.
* `issuer`: OPTIONAL. JSON object containing information about the issuer of this document. This object consists of the following properties:
    * `name`: OPTIONAL. Designation of the issuer of the document.
    * All elements of the OpenID Connect `address` Claim (see [@!OpenID])
    * `country_code`: OPTIONAL. String denoting the country or supranational organization that issued the document as ISO 3166/ICAO 3-letter codes [@!ICAO-Doc9303], e.g., "USA" or "JPN". 2-letter ICAO codes MAY be used in some circumstances for compatibility reasons.
    * `jurisdiction`: OPTIONAL. String containing the name of the region(s)/state(s)/province(s)/municipality(ies) that issuer has jurisdiction over (if this information is not common knowledge or derivable from the address).

* `derived_claims`: OPTIONAL. JSON object containing Claims about the End-User which were derived from the document described in the evidence array member it is part of. When used the `derived_claims` element has the following conditions:
    * The `derived_claims` element MAY contain any of the Claims defined in Section 5.1 of the OpenID Connect specification [@!OpenID] and the Claims defined in (#userclaims).
    * The `derived_claims` element MAY also contain other End-User Claims (not defined in the OpenID Connect specification [@!OpenID] nor in (#userclaims)) derived from the document described in the evidence array member it is part of.
    * End-User Claims contained in a `derived_claims` element MUST have corresponding Claims in the `claims` element of `verified_claims`.
    * When the `derived_claims` element is used it SHOULD be present in all members of the `evidence` array and all Claims under the `claims` element of `verified_claims` SHOULD have a corresponding Claim in at least one `derived_claims` element.
    * Claim names MAY be annotated with language tags as specified in Section 5.2 of the OpenID Connect specification [@!OpenID].
    * When it is present the `derived_claims` element MUST NOT be empty.

#### Evidence Type electronic_record

The following elements are contained in an evidence sub-element where type is `electronic_record`.

`type`: REQUIRED. Value MUST be set to `electronic_record`.

`check_details`: OPTIONAL. JSON array representing the checks done in relation to the `evidence`.

  * `check_method`: REQUIRED. String representing the check done. For information on predefined `check_method` values see [@!predefined_values].
  * `organization`: OPTIONAL. String denoting the legal entity that performed the check. This  SHOULD be included if the OP did not perform the check itself.
  * `txn`: OPTIONAL. Identifier referring to the identity verification transaction. The OP MUST ensure that this is present when `evidence_ref` element is used. The OP MUST ensure that the transaction identifier can be resolved into transaction details during an audit.
  * `time`: OPTIONAL. Time stamp in ISO 8601 [@!ISO8601] `YYYY-MM-DDThh:mm[:ss]TZD` format representing the date when the check was completed.  

`time`: OPTIONAL. Time stamp in ISO 8601 [@!ISO8601] `YYYY-MM-DDThh:mm[:ss]TZD` format representing the date when this record was verified.

`record`: OPTIONAL. JSON object representing the record used to perform the identity verification. It consists of the following properties:

* `type`: REQUIRED. String denoting the type of electronic record. For information on predefined identity evidence values see [@!predefined_values]. The OP MAY use other than the predefined values in which case the RPs will either be unable to process the assertion, just store this value for audit purposes, or apply bespoken business logic to it.
* `created_at`: OPTIONAL. The time the record was created as ISO 8601 [@!ISO8601] `YYYY-MM-DDThh:mm[:ss]TZD` format.
* `date_of_expiry`: OPTIONAL. The date the evidence will expire as ISO 8601 [@!ISO8601] `YYYY-MM-DD` format.
* `source`: OPTIONAL. JSON object containing information about the source of this record. This object consists of the following properties:
    * `name`: OPTIONAL. Designation of the source of the electronic_record.
    * All elements of the OpenID Connect `address` Claim (see [@!OpenID]): OPTIONAL.
    * `country_code`: OPTIONAL. String denoting the country or supranational organization that issued the evidence as ISO 3166/ICAO 3-letter codes [@!ICAO-Doc9303], e.g., "USA" or "JPN". 2-letter ICAO codes MAY be used in some circumstances for compatibility reasons.
    * `jurisdiction`: OPTIONAL. String containing the name of the region(s) / state(s) / province(s) / municipality(ies) that source has jurisdiction over (if it’s not common knowledge or derivable from the address).
* `derived_claims`: OPTIONAL. JSON object containing Claims about the End-User which were derived from the electronic record described in the evidence array member it is part of.
    * The `derived_claims` element MAY contain any of the Claims defined in Section 5.1 of the OpenID Connect specification [@!OpenID] and the Claims defined in (#userclaims).
    * The `derived_claims` element MAY also contain other End-User Claims (not defined in the OpenID Connect specification [@!OpenID] nor in (#userclaims)) derived from the electronic record described in the evidence array member it is part of.
    * Claim names MAY be annotated with language tags as specified in Section 5.2 of the OpenID Connect specification [@!OpenID].
    * When it is present the `derived_claims` element MUST NOT be empty.

#### Evidence Type vouch

The following elements are contained in an evidence sub-element where type is `vouch`.

`type`: REQUIRED. Value MUST be set to `vouch`.

`check_details`: OPTIONAL. JSON array representing the checks done in relation to the `vouch`.

  * `check_method`: REQUIRED. String representing the check done, this includes processes such as checking the authenticity of the vouch, or verifing the user as the person referenced in the vouch. For information on predefined `check_method` values see [@!predefined_values].
  * `organization`: OPTIONAL. String denoting the legal entity that performed the check. This  SHOULD be included if the OP did not perform the check itself.
  * `txn`: OPTIONAL. Identifier referring to the identity verification transaction. The OP MUST ensure that this is present when `evidence_ref` element is used. The OP MUST ensure that the transaction identifier can be resolved into transaction details during an audit.
  * `time`: OPTIONAL. Time stamp in ISO 8601 [@!ISO8601] `YYYY-MM-DDThh:mm[:ss]TZD` format representing the date when the check was completed.  

`time`: OPTIONAL. Time stamp in ISO 8601 [@!ISO8601] `YYYY-MM-DDThh:mm[:ss]TZD` format representing the date when this vouch was verified.

`attestation`: OPTIONAL. JSON object representing the attestation that is the basis of the vouch. It consists of the following properties:

* `type`: REQUIRED. String denoting the type of vouch. For information on predefined vouch values see [@!predefined_values]. The OP MAY use other than the predefined values in which case the RPs will either be unable to process the assertion, just store this value for audit purposes, or apply bespoken business logic to it.
* `reference_number`: OPTIONAL. String representing an identifier/number that uniquely identifies a vouch given about the End-User.
* `date_of_issuance`: OPTIONAL. The date the vouch was made as ISO 8601 [@!ISO8601] `YYYY-MM-DD` format.
* `date_of_expiry`: OPTIONAL. The date the evidence will expire as ISO 8601 [@!ISO8601] `YYYY-MM-DD` format.
* `voucher`: OPTIONAL. JSON object containing information about the entity giving the vouch. This object consists of the following properties:
    * `name`: OPTIONAL. String containing the name of the person giving the vouch/reference in the same format as defined in Section 5.1 (Standard Claims) of the OpenID Connect Core specification.
    * `birthdate`: OPTIONAL. String containing the birthdate of the person giving the vouch/reference in the same format as defined in Section 5.1 (Standard Claims) of the OpenID Connect Core specification.
    * All elements of the OpenID Connect `address` Claim (see [@!OpenID]): OPTIONAL.
    * `country_code`: OPTIONAL. String denoting the country or supranational organization that issued the evidence as ISO 3166/ICAO 3-letter codes [@!ICAO-Doc9303], e.g., "USA" or "JPN". 2-letter ICAO codes MAY be used in some circumstances for compatibility reasons.
    * `occupation`: OPTIONAL. String containing the occupation or other authority of the person giving the vouch/reference.
    * `organization`: OPTIONAL. String containing the name of the organization the voucher is representing.
* `derived_claims`: OPTIONAL. JSON object containing Claims about the End-User which were derived from the vouch described in the evidence array member it is part of.
    * The `derived_claims` element MAY contain any of the Claims defined in Section 5.1 of the OpenID Connect specification [@!OpenID] and the Claims defined in (#userclaims).
    * The `derived_claims` element MAY also contain other End-User Claims (not defined in the OpenID Connect specification [@!OpenID] nor in (#userclaims)) derived from the vouch described in the evidence array member it is part of.
    * Claim names MAY be annotated with language tags as specified in Section 5.2 of the   OpenID Connect specification [@!OpenID].
    * When it is present the `derived_claims` element MUST NOT be empty.

#### Evidence Type electronic_signature

The following elements are contained in a `electronic_signature` evidence sub-element.

* `type`: REQUIRED. Value MUST be set to `electronic_signature`.
* `signature_type`: REQUIRED. String denoting the type of signature used as evidence. The value range might be restricted by the respective trust framework.
* `issuer`: REQUIRED. String denoting the certification authority that issued the signer's certificate.
* `serial_number`: REQUIRED. String containing the serial number of the certificate used to sign.
* `created_at`: OPTIONAL. The time the signature was created as ISO 8601 [@!ISO8601] `YYYY-MM-DDThh:mm[:ss]TZD` format.
* `derived_claims`: OPTIONAL. JSON object containing Claims about the End-User which were derived from the electronic signature described in the evidence array member it is part of.
    * The `derived_claims` element MAY contain any of the Claims defined in Section 5.1 of the OpenID Connect specification [@!OpenID] and the Claims defined in (#userclaims).
    * The `derived_claims` element MAY also contain other End-User Claims derived from the electronically signed object described in the evidence array member it is part of, such as elements of an advanced electronic signature described under eIDAS used to uniquely link the signed object to the signatory.
    * Claim names MAY be annotated with language tags as specified in Section 5.2 of the OpenID Connect specification [@!OpenID].
    * When it is present the `derived_claims` element MUST NOT be empty.

## Attachments {#attachments}

During the identity verification process, specific document artifacts will be created and depending on the trust framework, will be required to be stored for a specific duration. These artifacts can later be reviewed during audits or quality control for example. These artifacts include, but are not limited to:

* scans of filled and signed forms documenting/certifying the verification process itself,
* scans or photocopies of the documents used to verify the identity of End-Users,
* video recordings of the verification process,
* certificates of electronic signatures.

When requested by the RP, these artifacts can be attached to the Verified Claims response allowing the RP to store these artifacts along with the Verified Claims information.

An attachment is represented by a JSON object. This specification allows two types of representations:

### Embedded Attachments

All the information of the document (including the content itself) is provided within a JSON object having the following elements:

`desc`: OPTIONAL. Description of the document. This can be the filename or just an explanation of the content. The used language is not specified, but is usually bound to the jurisdiction of the underlying trust framework of the OP.

`content_type`: REQUIRED. Content (MIME) type of the document. See [@!RFC6838]. Multipart or message media types are not allowed. Example: "image/png"

`content`: REQUIRED. Base64 encoded representation of the document content.

`txn`: OPTIONAL. Identifier referring to the transaction. The OP SHOULD ensure this matches a `txn` contained within `check_method` when `check_method` needs to reference the embedded attachment.

The following example shows embedded attachments. The actual contents of the documents are truncated:

<{{examples/response/embedded_attachments.json}}

Note: Due to their size, embedded attachments may not be appropriate when embedding Verified Claims in Access Tokens or ID Tokens.

### External Attachments

External attachments are similar to distributed Claims. The reference to the external document is provided in a JSON object with the following elements:

`desc`: OPTIONAL. Description of the document. This can be the filename or just an explanation of the content. The used language is not specified, but is usually bound to the jurisdiction of the underlying trust framework or the OP.

`url`: REQUIRED. OAuth 2.0 resource endpoint from which the attachment can be retrieved. Providers MUST protect this endpoint, ensuring that the attachment cannot be retrieved by unauthorized parties (typically by requiring an access token as described below). The endpoint URL MUST return the attachment whose cryptographic hash matches the value given in the `digest` element. The content MIME type of the attachment MUST be indicated in a content-type HTTP response header, as per [@!RFC6838]. Multipart or message media types SHALL NOT be used.

`access_token`: OPTIONAL. Access Token as type `string` enabling retrieval of the attachment from the given `url`. The attachment MUST be requested using the OAuth 2.0 Bearer Token Usage [@!RFC6750] protocol and the OP MUST support this method, unless another Token Type or method has been negotiated with the Client. Use of other Token Types is outside the scope of this specification. If the `access_token` element is not available, RPs MUST use the Access Token issued by the OP in the Token response and when requesting the attachment the RP MUST use the same method as when accessing the UserInfo endpoint. If the value of this element is `null`, no Access Token is used to request the attachment and the RP MUST NOT use the Access Token issued by the Token response. In this case the OP MUST incorporate other effective methods to protect the attachment and inform/instruct the RP accordingly.

`exp`: OPTIONAL. The "exp" (expiration time) claim identifies the expiration time on or after which the External Attachment will not be available from the resource endpoint defined in the `url` element (e.g. the `access_token` may expire or the document may be removed at that time). Implementers MAY provide for some small leeway, usually no more than a few minutes, to account for clock skew.  Its value MUST be a number containing a NumericDate value as per as per [@!RFC7519].

`digest`: REQUIRED. JSON object containing details of a cryptographic hash of the document content taken over the bytes of the payload (and not, e.g., the representation in the HTTP response). The JSON object has the following elements:

* `alg`: REQUIRED. Specifies the algorithm used for the calculation of the cryptographic hash. The algorithm has been negotiated previously between RP and OP during Client Registration or Management.
* `value`: REQUIRED. Base64-encoded [@RFC4648] bytes of the cryptographic hash.

`txn`: OPTIONAL. Identifier referring to the transaction. The OP SHOULD ensure this matches a `txn` contained within `check_method` when `check_method` needs to reference the embedded attachment.

External attachments are suitable when embedding Verified Claims in Tokens. However, the `verified_claims` element is not self-contained. The documents need to be retrieved separately, and the digest values MUST be calculated and validated to ensure integrity.

It is RECOMMENDED that access tokens for external attachments have a binding to the specific resource being requested so that the access token may not be used to retrieve additional external attachments or resources. For example, the value of `url` could be tied to the access token as audience. This enhances security by enabling the resource server to check whether the audience of a presented access token matches the accessed URL and reject the access when they do not match. The same idea is described in Resource Indicators for OAuth 2.0 [@RFC8707], which defines the `resource` request parameter whereby to specify one or more resources which should be tied to an access token being issued.

The following example shows external attachments:

<{{examples/response/external_attachments.json}}

### External Attachment Validation

Clients MUST validate any member of the attachments array that is an external attachment they wish to rely on in the following manner:

1. Ensure that the object includes the required elements: `url`, `digest`.
2. Ensure that at the time of the request the time is before the time represented by the `exp` element. 
3. Ensure that the URL defined in the `url` element uses the `https` scheme.
4. Retrieve the attachment from the `url` element in the object.
5. Ensure that the content MIME type of the attachment is indicated in a content-type HTTP response header
6. Ensure that the MIME type is not Multipart (see Section 5.1 of [@RFC2046])
7. Ensure that the MIME type is not a "message" media type (see [@RFC5322])
8. Ensure the returned attachment has a cryptographic hash digest that matches the value given in the `digest` object's `value` key.

If any of these requirements are not met the content of the attachment SHOULD NOT be used, SHOULD be discarded and MUST NOT be relied upon.

### Privacy Considerations

As attachments will most likely contain more personal information than was requested by the RP with specific Claim names, an OP MUST ensure that the End-User is well aware of when and what kind of attachments are about to be transferred to the RP. If possible or applicable, the OP SHOULD allow the End-User to review the content of these attachments before giving consent to the transaction.

# OP Metadata {#opmetadata}

The OP advertises its capabilities with respect to Verified Claims in its openid-configuration (see [@!OpenID-Discovery]) using the following new elements:

`evidence_supported`: REQUIRED when one or more type of evidence is supported. JSON array containing all types of identity evidence the OP uses. This array MUST have at least one member. Members of this array SHOULD only be the types of evidence supported by the OP in the evidence element (see [@!evidence_element]).

`documents_supported`: REQUIRED when `evidence_supported` contains "document". JSON array containing all identity document types utilized by the OP for identity verification. This array MUST have at least one member.

`documents_methods_supported`: OPTIONAL. JSON array containing the methods the OP supports for evidences of type "document" (see @!predefined_values). When present this array MUST have at least one member.

`documents_check_methods_supported`: OPTIONAL. JSON array containing the check methods the OP supports for evidences of type "document" (see @!predefined_values). When present this array MUST have at least one member.

`electronic_records_supported`: REQUIRED when `evidence_supported` contains "electronic\_record". JSON array containing all electronic record types the OP supports (see [@!predefined_values]). When present this array MUST have at least one member.

`attachments_supported`: REQUIRED when OP supports attachments. JSON array containing all attachment types supported by the OP. Possible values are `external` and `embedded`. When present this array MUST have at least one member. If omitted, the OP does not support attachments.

This is an example openid-configuration snippet:

```json
{
...
   "evidence_supported": [
      "document",
      "electronic_record",
      "vouch",
      "electronic_signature"
   ],
   "documents_supported": [
       "idcard",
       "passport",
       "driving_permit"
   ],
   "documents_methods_supported": [
       "pipp",
       "sripp",
       "eid"
   ],
   "electronic_records_supported": [
       "secure_mail"
   ],   
  "attachments_supported": [
    "external",
    "embedded"
  ],
...
}
```

## Examples

This section contains JSON snippets showing examples of evidences and attachments described in this document.

# Example Requests
This section shows examples of requests for `verified_claims`.

## Verification of Claims by trust framework and evidence types

<{{examples/request/verification_claims_trust_frameworks_evidence.json}}

## Verification of Claims by trust framework with a document and attachments

<{{examples/request/verification_aml_with_attachments.json}}

## Verification of Claims by electronic signature

<{{examples/request/verification_electronic_signature.json}}

### Attachments

RPs can explicitly request to receive attachments along with the Verified Claims:

<{{examples/request/verification_with_attachments.json}}

As with other Claims, the attachment Claim can be marked as `essential` in the request as well.

# Example Responses

This section shows examples of responses containing `verified_claims`.

## Document

<{{examples/response/document_800_63A.json}}

Same document under a different `trust_framework`

<{{examples/response/document_UK_DIATF.json}}

## Document and verifier details

<{{examples/response/document_verifier.json}}

## Document with external attachments

<{{examples/response/document_with_attachments.json}}

## Evidence with all assurance details

<{{examples/response/evidence_with_assurance_details.json}}

## Utility statement with attachments

<{{examples/response/utility_statement_with_attachments.json}}

## Document + utility statement

<{{examples/response/document_and_utility_statement.json}}

## Electronic_record

<{{examples/response/electronic_record.json}}

## Vouch with embedded attachments

<{{examples/response/vouch_with_attachments.json}}


# Example Requests and Responses

This section shows examples of pairs of requests and responses containing `verified_claims`.

{backmatter}

<reference anchor="OpenID" target="http://openid.net/specs/openid-connect-core-1_0.html">
  <front>
    <title>OpenID Connect Core 1.0 incorporating errata set 1</title>
    <author initials="N." surname="Sakimura" fullname="Nat Sakimura">
      <organization>NRI</organization>
    </author>
    <author initials="J." surname="Bradley" fullname="John Bradley">
      <organization>Ping Identity</organization>
    </author>
    <author initials="M." surname="Jones" fullname="Mike Jones">
      <organization>Microsoft</organization>
    </author>
    <author initials="B." surname="de Medeiros" fullname="Breno de Medeiros">
      <organization>Google</organization>
    </author>
    <author initials="C." surname="Mortimore" fullname="Chuck Mortimore">
      <organization>Salesforce</organization>
    </author>
   <date day="8" month="Nov" year="2014"/>
  </front>
</reference>

<reference anchor="OpenID4IDA" target="http://openid.net/specs/openid-connect-4-identity-assurance-1_0.html">
  <front>
    <title>OpenID Connect for Identity Assurance 1.0</title>
    <author initials="T." surname="Lodderstedt" fullname="Torsten Lodderstedt">
      <organization>yes.com</organization>
    </author>
    <author initials="D." surname="Fett" fullname="Daniel Fett">
      <organization>Authlete</organization>
    </author>
    <author initials="M." surname="Haine" fullname="Mark Haine">
      <organization>Considrd.Consulting Ltd</organization>
    </author>
    <author initials="A." surname="Pulido" fullname="Alberto Pulido">
      <organization>Santander</organization>
    </author>
    <author initials="K." surname="Lehmann" fullname="Kai Lehmann">
      <organization>1&amp;1 Mail &amp; Media Development &amp; Technology GmbH</organization>
    </author>
        <author initials="K." surname="Koiwai" fullname="Kosuke Koiwai">
      <organization>KDDI Corporation</organization>
    </author>
   <date day="16" month="Jun" year="2023"/>
  </front>
</reference>

<reference anchor="ISO3166-1" target="https://www.iso.org/standard/72482.html">
    <front>
      <title>ISO 3166-1:2020. Codes for the representation of names of
      countries and their subdivisions -- Part 1: Country codes</title>
      <author surname="International Organization for Standardization">
        <organization abbrev="ISO">International Organization for Standardization</organization>
      </author>
      <date year="2020" />
    </front>
</reference>

<reference anchor="ISO3166-3" target="https://www.iso.org/standard/72482.html">
    <front>
      <title>ISO 3166-3:2020. Codes for the representation of names of countries and their subdivisions -- Part 3: Code for formerly used names of countries</title>
      <author surname="International Organization for Standardization">
        <organization abbrev="ISO">International Organization for
        Standardization</organization>
      </author>
      <date year="2020" />
    </front>
</reference>

<reference anchor="ICAO-Doc9303" target="https://www.icao.int/publications/Documents/9303_p3_cons_en.pdf">
  <front>
    <title>Machine Readable Travel Documents, Seventh Edition, 2015, Part 3: Specifications Common to all MRTDs</title>
      <author surname="INTERNATIONAL CIVIL AVIATION ORGANIZATION">
        <organization>INTERNATIONAL CIVIL AVIATION ORGANIZATION</organization>
      </author>
   <date year="2015"/>
  </front>
</reference>

<reference anchor="E.164" target="https://www.itu.int/rec/T-REC-E.164/en">
  <front>
    <title>Recommendation ITU-T E.164</title>
    <author>
      <organization>ITU-T</organization>
    </author>
    <date year="2010" month="11"/>
  </front>
</reference>

# Acknowledgements {#Acknowledgements}

The following people at yes.com and partner companies contributed to the concept described in the initial contribution to this specification: Karsten Buch, Lukas Stiebig, Sven Manz, Waldemar Zimpfer, Willi Wiedergold, Fabian Hoffmann, Daniel Keijsers, Ralf Wagner, Sebastian Ebling, Peter Eisenhofer.

We would like to thank Julian White, Bjorn Hjelm, Stephane Mouy, Alberto Pulido, Joseph Heenan, Vladimir Dzhuvinov, Azusa Kikuchi, Naohiro Fujie, Takahiko Kawasaki, Sebastian Ebling, Marcos Sanz, Tom Jones, Mike Pegman, Michael B. Jones, Jeff Lombardo, Taylor Ongaro, Peter Bainbridge-Clayton, Adrian Field, George Fletcher, Tim Cappalli, Michael Palage, Sascha Preibisch, Giuseppe De Marco, Nick Mothershaw, Hodari McClain, and Nat Sakimura for their valuable feedback and contributions that helped to evolve this specification.

# Notices

Copyright (c) 2023 The OpenID Foundation.

The OpenID Foundation (OIDF) grants to any Contributor, developer, implementer, or other interested party a non-exclusive, royalty free, worldwide copyright license to reproduce, prepare derivative works from, distribute, perform and display, this Implementers Draft or Final Specification solely for the purposes of (i) developing specifications, and (ii) implementing Implementers Drafts and Final Specifications based on such documents, provided that attribution be made to the OIDF as the source of the material, but that such attribution does not indicate an endorsement by the OIDF.

The technology described in this specification was made available from contributions from various sources, including members of the OpenID Foundation and others. Although the OpenID Foundation has taken steps to help ensure that the technology is available for distribution, it takes no position regarding the validity or scope of any intellectual property or other rights that might be claimed to pertain to the implementation or use of the technology described in this specification or the extent to which any license under such rights might or might not be available; neither does it represent that it has made any independent effort to identify any such rights. The OpenID Foundation and the contributors to this specification make no (and hereby expressly disclaim any) warranties (express, implied, or otherwise), including implied warranties of merchantability, non-infringement, fitness for a particular purpose, or title, related to this specification, and the entire risk as to implementing this specification is assumed by the implementer. The OpenID Intellectual Property Rights policy requires contributors to offer a patent promise not to assert certain patent claims against other contributors and against implementers. The OpenID Foundation invites any interested party to bring to its attention any copyrights, patents, patent applications, or other proprietary rights that may cover technology that may be required to practice this specification.

# Document History

   [[ To be removed from the final specification ]]


   -00 (WG document)

   *  Split this content from openid-connect-4-identity-assurance-1_0-13 WG document

