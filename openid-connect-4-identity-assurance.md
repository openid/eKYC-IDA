%%%
title = "OpenID Connect for Identity Assurance 1.0"
abbrev = "openid-connect-4-identity-assurance-1_0"
ipr = "none"
workgroup = "eKYC-IDA"
keyword = ["security", "openid", "identity assurance", "ekyc"]

[seriesInfo]
name = "Internet-Draft"

value = "openid-connect-4-identity-assurance-1_0-13"

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

This specification defines an extension of OpenID Connect for providing Relying Parties with Verified Claims about End-Users. This extension facilitates the verification of the identity of a natural person.

{mainmatter}

# Introduction {#Introduction}

This specification defines an extension to OpenID Connect [@!OpenID] for providing Relying Parties with identity information, i.e., Verified Claims, along with an explicit statement about the verification status of these Claims (what, how, when, according to what rules, using what evidence). This specification is aimed at enabling use cases requiring strong assurance, for example, to comply with regulatory requirements such as Anti-Money Laundering laws or access to health data, risk mitigation, or fraud prevention.

In such use cases, the Relying Party (RP) needs to understand the trustworthiness or assurance level of the Claims about the End-User that the OpenID Connect Provider (OP) is willing to communicate, along with process-related information and evidence used to verify the End-User Claims.

The `acr` Claim, as defined in Section 2 of the OpenID Connect specification [@!OpenID], is suited to assure information about the authentication performed in an OpenID Connect transaction. Identity assurance, however, requires a different representation: While authentication is an aspect of an OpenID Connect transaction, assurance is a property of a certain Claim or a group of Claims. Several of them will typically be conveyed to the RP as the result of an OpenID Connect transaction.

For example, the assurance an OP typically will be able to give for an e-mail address will be “self-asserted” or “verified by opt-in or similar mechanism”. The family name of an End-User, in contrast, might have been verified in accordance with the respective Anti Money Laundering Law by showing an ID Card to a trained employee of the OP operator.

Identity assurance therefore requires a way to convey assurance data along with and coupled to the respective Claims about the End-User. This specification defines a suitable representation and mechanisms the RP will utilize to request Verified Claims about an End-User along with assurance data and for the OP to represent these Verified Claims and accompanying assurance data.

Note: This specifications fulfills the criteria for portability and interoperability mechanisms of Digital ID systems as defined in [@FATF-Digital-Identity].

## Terminology

This section defines some terms relevant to the topic covered in this document, inspired by NIST SP 800-63A [@NIST-SP-800-63a].

* Claim - as per definition in Section 1.2 of [@!OpenID]

* Identity Proofing - process in which an End-User provides evidence to an OP or Claim provider reliably identifying themselves, thereby allowing the OP or Claim provider to assert that identification at a useful assurance level.

* Identity Verification - process conducted by the OP or a Claim provider to verify the End-User's identity.

* Identity Assurance - process in which the OP or a Claim provider asserts identity data of a certain End-User with a certain assurance towards an RP, typically expressed by way of an assurance level. Depending on legal requirements, the OP may also need to provide evidence of the identity verification process to the RP.

* Verified Claims - Claims about an End-User, typically a natural person, whose binding to a particular End-User account was verified in the course of an identity verification process.

# Scope

This specification defines the technical mechanisms to allow Relying Parties to request Verified Claims and to enable OpenID Providers to provide Relying Parties with Verified Claims ("the tools").

Additional facets needed to deploy a complete solution for identity assurance, such as legal aspects (including liability), trust frameworks, or commercial agreements are out of scope. It is up to the particular deployment to complement the technical solution based on this specification with the respective definitions ("the rules").

Note: Although such aspects are out of scope, the aim of the specification is to enable implementations of the technical mechanism to be flexible enough to fulfill different legal and commercial requirements in jurisdictions around the world. Consequently, such requirements will be discussed in this specification as examples.

# Requirements

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119 [RFC2119].

The RP will be able to request the minimal data set it needs (data minimization) and to express requirements regarding this data, the evidence and the identity verification processes employed by the OP.

This extension will be usable by OPs operating under a certain regulation related to identity assurance, such as eIDAS, as well as other OPs operating without such a regulation.

It is assumed that OPs operating under a suitable regulation can assure identity data without the need to provide further evidence since they are approved to operate according to well-defined rules with clearly defined liability. For example in the case of eIDAS, the peer review ensures eIDAS compliance and the respective member state assumes the liability for the identities asserted by its notified eID systems.

Every other OP not operating under such well-defined conditions may have the need to provide the RP data about the identity verification process along with identity evidence to allow the RP to conduct their own risk assessment and to map the data obtained from the OP to other laws. For example, if an OP verifies and maintains identity data in accordance with an Anti Money Laundering Law, it shall be possible for an RP to use the respective identity in a different regulatory context, such as eHealth or the previously mentioned eIDAS.

The concept of this specification is that the OP can provide all identity data along with metadata about the identity assurance process. It is the responsibility of the RP to assess this data and map it into its own legal context.

From a technical perspective, this means this specification allows the OP to provide Verified Claims along with information about the respective trust framework, but also supports the externalization of information about the identity verification process.

The representation defined in this specification can be used to provide RPs with Verified Claims about the End-User via any appropriate channel. In the context of OpenID Connnect, Verified Claims can be provided in ID Tokens or as part of the UserInfo response. It is also possible to utilize the format described here in OAuth Access Tokens or Token Introspection responses to provide resource servers with Verified Claims.

This extension is intended to be truly international and support identity assurance across different jurisdictions. The extension is therefore extensible to support various trust frameworks, identity evidence and assurance processes.

In order to give implementors as much flexibility as possible, this extension can be used in conjunction with existing OpenID Connect Claims and other extensions within the same OpenID Connect assertion (e.g., ID Token or UserInfo response) utilized to convey Claims about End-Users.

For example, OpenID Connect [@!OpenID] defines Claims for representing family name and given name of an End-User without a verification status. These Claims can be used in the same OpenID Connect assertion beside Verified Claims represented according to this extension.

In the same way, existing Claims to inform the RP of the verification status of the `phone_number` and `email` Claims can be used together with this extension.

Even for representing Verified Claims, this extension utilizes existing OpenID Connect Claims if possible and reasonable. The extension will, however, ensure RPs cannot (accidentally) interpret unverified Claims as Verified Claims.

# Claims {#claims}

## Additional Claims about End-Users {#userclaims}

In order to fulfill the requirements of some jurisdictions on identity assurance, the OpenID Connect for IDA claims [@OpenID4IDAClaims] specification defines the a number of Claims for conveying End-User data in addition to the Claims defined in the OpenID Connect specification [@!OpenID].

# Verified Claims {#verified_claims}

This specification uses the [!@IDA-verified-claims] document as the definition of the schema for representation of assured digital identity attributes and identity assurance metadata. The basic idea is to use a container element, called `verified_claims`, to provide the RP with a set of Claims along with the respective metadata and verification evidence related to the verification of these Claims. This way, it is explicit which Claims are verified and which are not, reducing the risk of RPs accidentally processing unverified Claims as Verified Claims.

The following example would assert to the RP that the OP has verified the Claims provided (`given_name` and `family_name`) according to an example trust framework `trust_framework_example`:

<{{examples/response/verified_claims_simple.json}}

This specification requires that the schema defined in [!@IDA-verified-claims] MUST be used.  There are places in the JSON structure where that schema can be extended by implementers but deviation from the schema as defined would not be correct use of this specification.

## verified_claims Delivery {#verified_claims_delivery}

OPs can deliver `verified_claims` in various ways.

A `verified_claims` element can be added to an OpenID Connect UserInfo response or an ID Token.

OAuth Authorization Servers can add `verified_claims` to Access Tokens in JWT format or Token Introspection responses, either in plain JSON or JWT-protected format.

Here is an example of the payload of an Access Token in JWT format including Verified Claims:

```json
{
  "iss": "https://server.example.com",
  "sub": "248289761",
  "aud": "https://rs.example.com/",
  "exp": 1544645174,
  "client_id": "s6BhdRkqt3_",
  "verified_claims": {
    "verification": {
      "trust_framework": "example"
    },
    "claims": {
      "given_name": "Max",
      "family_name": "Mustermann"
    }
  }
}
```

An OP or AS MAY also include `verified_claims` in the above assertions, whether they are Access Tokens or in Token Introspection responses, as aggregated or distributed claims (see Section 5.6.2 of the OpenID Connect specification [@!OpenID]).

## Requesting End-User Claims {#req_claims}

Verified Claims can be requested on the level of individual Claims about the End-User by utilizing the `claims` parameter as defined in Section 5.5 of the OpenID Connect specification [@!OpenID].

Note: A machine-readable definition of the syntax to be used to request `verified_claims` is given as JSON schema in [@verified_claims_request.json], it can be used to automatically validate `claims` request parameters. The provided JSON schema files are a non-normative implementation of this specification and any discrepancies that exist are either implementation bugs or interpretations.

To request Verified Claims, the `verified_claims` element is added to the `userinfo` or the `id_token` element of the `claims` parameter.

Since `verified_claims` contains the effective Claims about the End-User in a nested `claims` element, the syntax is extended to include expressions on nested elements as follows. The `verified_claims` element includes a `claims` element, which in turn includes the desired Claims as keys. For each claim, the value is either `null` (default), or an object. The object may contain restrictions using `value` or `values` as defined in [@!OpenID] and/or the `essential` or `purpose` keys as described below. An example is shown in the following:

<{{examples/request/claims.json}}

Use of the `claims` parameter allows the RP to request specified Claims about the End-User needed for its use case. This allows RPs to fulfill the requirements for data minimization by requesting only Claims needed for its use case. Note: it is not possible to request sub-claims (for example the ‘country’ subclaim of the ‘address’ claim) using mechanisms from OpenID Connect Core or this draft.

RPs MAY use the `essential` field as defined in Section 5.5.1 of the OpenID Connect specification [@!OpenID]. The following example shows this for the family and given names.

<{{examples/request/essential.json}}

This specification introduces the additional field `purpose` to allow an RP
to state the purpose for the transfer of a certain End-User Claim it is asking for.
The field `purpose` can be a member value of each individually requested
Claim, but a Claim cannot have more than one associated purpose.

`purpose`: OPTIONAL. String describing the purpose for obtaining a certain End-User Claim from the OP. The purpose MUST NOT be shorter than 3 characters or
longer than 300 characters. If this rule is violated, the authentication
request MUST fail and the OP return an error `invalid_request` to the RP.
The OP MUST display this purpose in the respective End-User consent screen(s)
in order to inform the End-User about the designated use of the data to be
transferred or the authorization to be approved. If the parameter `purpose`
is not present in the request, the OP MAY display a
value that was pre-configured for the respective RP. For details on UI
localization, see (#purpose).

Example:

<{{examples/request/purpose.json}}

## Requesting Verification Data {#req_verification}

RPs request verification data in the same way they request Claims about the End-User. When the claims request parameter is being used, the syntax is based on the rules given in (#req_claims) and extends them for navigation into the structure of the `verification` element.

Elements within `verification` are requested by adding the respective element as shown in the following example:

<{{examples/request/verification.json}}

It requests the trust framework the OP complies with and the date of the verification of the End-User Claims.

The RP MUST explicitly request any data it wants the OP to add to the `verification` element.

Therefore, the RP MUST set fields one step deeper into the structure if it wants to obtain evidence. One or more entries in the `evidence` array are used as filter criteria and templates for all entries in the result array. The following example shows a request asking for evidence of type `document` only.

<{{examples/request/verification_deeper.json}}

The example also requests the OP to add the respective `method` and the `document` elements (including data about the document type), for every evidence array member, to the resulting `verified_claims` Claim.

A single entry in the `evidence` array represents a filter over elements of a certain evidence type. The RP therefore MUST specify this type by including the `type` field including a suitable `value` sub-element value. The `values` sub-element MUST NOT be used for the `evidence/type` field.

If multiple entries are present in `evidence`, these filters are linked by a logical OR.

`check_details` is an array of the processes that have been applied to the `evidence`. An RP MAY filter `check_details` by requesting a particular value for one or more of its sub-elements. If multiple entries for the same sub-element are present this acts as a logical OR between them.

`assurance_details` is an array representing how the `evidence` and `check_details` meets the requirements of the `trust_framework`. RP SHOULD only request this where they need to know this information. Where `assurance_details` have been requested by an RP the OP MUST return the `assurance_details` element along with all sub-elements that it has. If an RP wants to filter what types of `evidence` and `check_methods` they MUST use those methods to do so, e.g. requesting an `assurance_type` SHOULD have no filtering effect.

The RP MAY also request certain data within the `document` element to be present. This again follows the syntax rules used above:

<{{examples/request/verification_document.json}}

## Defining further constraints on Verification Data {#constraintedclaims}

### value/values

The RP MAY limit the possible values of the elements `trust_framework`, `evidence/method`, `evidence/check_details`, and `evidence/document/type` by utilizing the `value` or `values` fields and the element `evidence/type` by utilizing the `value` field.

Note: Examples on the usage of a restriction on `evidence/type` were given in the previous section.

The following example shows how an RP may request Claims either complying with trust framework `gold` or `silver`.

<{{examples/request/verification_claims_different_trust_frameworks.json}}

The following example shows that the RP wants to obtain an attestation based on the German Anti Money Laundering Law (trust framework `de_aml`) and limited to End-Users who were identified in a bank branch in person (physical in person proofing - method `pipp`) using either an `idcard` or a `passport`.

<{{examples/request/verification_aml.json}}

The OP MUST NOT ignore some or all of the query restrictions on possible values and MUST NOT deliver available verified/verification data that does not match these constraints.

### max_age

The RP MAY also express a requirement regarding the age of certain data, like the time elapsed since the issuance/expiry of certain evidence types or since the verification process asserted in the `verification` element took place. Section 5.5.1 of the OpenID Connect specification [@!OpenID] defines a query syntax that allows for new special query members to be defined. This specification introduces a new such member `max_age`, which is applicable to the possible values of any elements containing dates or timestamps (e.g., `time`, `date_of_issuance` and `date_of_expiry` elements of evidence of type `document`).

`max_age`: OPTIONAL. JSON number value only applicable to Claims that contain dates or timestamps. It defines the maximum time (in seconds) to be allowed to elapse since the value of the date/timestamp up to the point in time of the request. The OP SHOULD make the calculation of elapsed time starting from the last valid second of the date value.

The following is an example of a request for Claims where the verification process of the data is not allowed to be older than 63113852 seconds:

<{{examples/request/verification_max_age.json}}

The OP SHOULD try to fulfill this requirement. If the verification data of the End-User is older than the requested `max_age`, the OP MAY attempt to refresh the End-User’s verification by sending them through an online identity verification process, e.g., by utilizing an electronic ID card or a video identification approach.

## Requesting Claims sets with different verification requirements

It is also possible to request different trust frameworks, assurance levels, and methods for different Claim sets. This requires the RP to send an array of `verified_claims` objects instead of passing a single object.

The following example illustrates this functionality.

<{{examples/request/verification_claims_by_trust_frameworks.json}}

When the RP requests multiple verifications as described above, the OP will process each element in the array independently. The OP will provide `verified_claims` response elements for every `verified_claims` request element whose requirements it is able to fulfill. This also means if multiple `verified_claims` elements contain the same End-User Claim(s), the OP delivers the Claim in as many Verified Claims response objects it can fulfil. For example, if the trust framework the OP uses is compatible with multiple of the requested trust frameworks, it provides a `verified_claims` element for each of them.

The RP MAY combine multiple `verified_claims` Claims in the request with multiple `trust_framework` and/or `assurance_level` values using the `values` element. In that case, the rules given above for processing `values` are applied for the particular `verified_claims` request object.

<{{examples/request/verification_claims_by_trust_frameworks_same_claims.json}}

In the above example, the RP asks for family and given name either under trust framework `gold` with an evidence of type `document` or under trust framework `silver` or `bronze` but with an evidence `electronic_record`.

## Returning less data than requested
As stated in Section 3.3.6 of [@!OpenID], "the OP MAY choose to return fewer Claims about the End-User from the Authorization Endpoint".  This document makes no change to that provision.  The OP MAY also choose to return a subset of the `verification` element of any `verified_claims` providing it remains complaint with the `verified_claims` JSON schema defined in [@!OpenID4IDAClaims].

In some cases, OPs cannot deliver the requested data to an RP, for example, because the data is not available or does not match the RP's requirements. The rules for handling these cases are described in the following.

Extensions of this specification MAY define additional rules or override these rules, for example

* to allow or disallow the use of Claims depending on scheme-specific checks,
* to enable a finer-grained control of the RP over the behavior of the OP when data is unavailable or does not match the criteria, or
* to abort transactions (return error codes) in cases where requests cannot be fulfilled.

Important: The behavior described below is independent from the use of `essential` (as defined in Section 5.5 of [@!OpenID]).

### Unavailable or Non-consented Data
If the OP does not have data about a certain Claim, does not understand/support the respective Claim, or the End-User does not consent to the release of the specific data, the respective Claim MUST be omitted from the response. The OP MUST NOT return an error to the RP. 

### Data not Matching Requirements
When the available data does not fulfill the requirements of the RP expressed through `value`, `values`, or `max_age`, the following logic applies:

 * If the respective requirement was expressed for a Claim within `verified_claims/verification`, the whole `verified_claims` element MUST be omitted.
 * Otherwise, the respective Claim MUST be omitted from the response.

In both cases, the OP MUST NOT return an error to the RP.

### Omitting Elements

If an element is to be omitted according to the rules above, but is a requirement for a valid response, its parent element MUST be omitted as well. This process MUST be repeated until the response is valid.

### Error Handling

If the OP encounters an error, or the End-User does not consent to the whole transaction, standard OpenID Connect authentication error response logic applies, as defined in Section 3.1.2.6 of [@!OpenID].

## Requesting sets of Claims by scope {#req_scope}

Verified Claims about the End-User can be requested as part of a pre-defined set by utilizing the `scope` parameter as defined in Section 5.4 of the OpenID Connect specification [@!OpenID].

When using this approach the Claims associated with a `scope` are administratively defined at the OP.  The OP configuration and RP request parameters will determine whether the Claims are returned via the ID Token or UserInfo endpoint as defined in Section 5.3.2 of the OpenID Connect specification [@!OpenID].

# Aggregated and Distributed claims
## Aggregated and Distributed claims assertions

When distributed claims are used the URL that is the value of the `endpoint` element in any distributed `_claim_source` sub-element MUST use the https URI scheme and the JWT returned SHOULD NOT be accessible via any other URI scheme.

For aggregated or distributed claims, every assertion provided by the external Claims source MUST contain:

* a `typ` header parameter with the value `provided-claims+jwt`,
* an `iss` Claim identifying the claims source,
* a `sub` Claim identifying the End-User in the context of the claim source, and
* a `verified_claims` element containing one or more `verified_claims` objects.

To ensure that assertions cannot be confused with OpenID Connect ID Tokens, assertions MUST NOT contain:

 * an `exp` claim, or
 * an `aud` claim.

The `verified_claims` element in an aggregated or distributed claims object MUST have one of the following forms:

* a JSON string referring to a certain claim source (as defined in [@!OpenID])
* a JSON array of strings referring to the different claim sources
* a JSON object composed of sub-elements formatted with the syntax as defined for requesting `verified_claims` where the name of each object is a name for the respective claim source. Every such named object contains sub-objects called  `claims` and `verification` expressing data provided by the respective claims source. This allows the RP to look ahead before it actually requests distributed Claims in order to prevent extra time, cost, data collisions, etc. caused by these requests.

Note: The two later forms extend the syntax as defined in Section 5.6.2 of the OpenID Connect specification [@!OpenID]) in order to accommodate the specific use cases for `verified_claims`.

The following are examples of assertions including Verified Claims as aggregated Claims

<{{examples/response/aggregated_claims_simple.json}}

and distributed Claims.

<{{examples/response/distributed_claims.json}}

The following example shows an ID Token containing `verified_claims` from two different external claim sources, one as aggregated and the other as distributed Claims.

<{{examples/response/multiple_external_claims_sources.json}}

The next example shows an ID Token containing `verified_claims` from two different external claim sources along with additional data about the content of the Verified Claims (look ahead).

<{{examples/response/multiple_external_claims_sources_with_lookahead.json}}

Claim sources SHOULD sign the assertions containing `verified_claims` in order to demonstrate authenticity and provide for non-repudiation.
The RECOMMENDED way for an RP to determine the key material used for validation of the signed assertions is via the claim source's public keys. These keys SHOULD be available in the JSON Web Key Set available in the `jwks_uri` metadata value in the `openid-configuration` metadata document. This document can be discovered using the `iss` Claim of the particular JWT.

The OP MAY combine aggregated and distributed Claims with `verified_claims` provided by itself (see (#op_attested_and_external_claims)).

If `verified_claims` elements are contained in multiple places of a response, e.g., in the ID Token and an embedded aggregated Claim, the RP MUST preserve the claims source as context of the particular `verified_claims` element.

Note: Any assertion provided by an OP or AS including aggregated or distributed Claims MAY contain multiple instances of the same End-User Claim. It is up to the RP to decide how to process these different instances.

## Aggregated and Distributed claims validation

Clients MUST validate any Aggregated and Distributed `verified_claims` they wish to rely on in the following manner:

1. Ensure that both the `_claim_names` and `_claim_sources` are present in the response
2. Ensure that there is a `verified_claims` element present in the `_claim_names` member of the response
3. Ensure that the `verified_claims` element contains a value that is one of the following:
    a. a string that exists as a key name in the `_claim_sources` element of the response.
    b. a JSON array containing members that all exist as key names in the `_claim_sources` element of the response.
    c. a JSON object containing elements that all exist as key names in the `_claim_sources` element of the response and each element is formatted with the syntax as defined for requesting `verified_claims`.
4. Ensure that the `_claim_sources` element is a JSON structured object that has one or more sub-elements
5. Ensure that the sub-elements of the `_claim_sources` element have matching values in the `_claim_names` element of the response

When `verified_claims` are delivered as distributed claims, i.e., when a sub-element of the `_claim_sources` contains the `endpoint` claim, clients MUST also:

1. Ensure that the `endpoint` element defined in any distributed `_claim_sources` uses the https URI scheme.
2. Retrieve the distributed claims object from the `endpoint` element defined in any distributed `_claim_sources`.
3. Ensure that the object returned from the `endpoint` is a JWT as per [@RFC7519].

When `verified_claims` are delivered as aggregated claims, i.e., when a sub-element of the `_claim_sources` contains the `JWT` claim, clients MUST also:

1. Ensure that the value in the `JWT` claim is a valid JWT as per [@RFC7519].

Once the JWT has been delivered either via distributed or aggregated mechanism the client MUST:

1. Verify the signature of the returned JWT.
2. Ensure that the JWT includes the `typ`, `iss`, `sub`, and `verified_claims` elements; and that their values are not null or empty.
3. Ensure that the JWT does not contain either an `exp` claim or an `aud` claim.
4. Ensure that the value of the `typ` header parameter in the JWT is `provided-claims+jwt`.

# Requesting Verified Claims

Making a request for Verified Claims and related verification data can be explicitly requested on the level of individual data elements by utilizing the `claims` parameter as defined in Section 5.5 of the OpenID Connect specification [@!OpenID].

It is also possible to use the `scope` parameter to request one or more specific pre-defined Claim sets as defined in Section 5.4 of the OpenID Connect specification [@!OpenID].

Note: The OP MUST NOT provide the RP with any data it did not request. However, the OP MAY at its discretion omit Claims from the response.

The example authorize call in this section will use the following unencoded example claims request parameter:

<{{examples/request/simple_id_token.json}}

The following is the non-normative example request that would be sent by the User Agent to the Authorization Server in response to the HTTP 302 redirect from the Client initiating the authorization code flow (with line wraps within values for display purposes only):

```
  GET /authorize?
     response_type=code
     &scope=openid%20email
     &client_id=s6BhdRkqt3
     &state=af0ifjsldkj
     &redirect_uri=https%3A%2F%2Fclient.example.org%2Fcb
     &claims=%7B%22id_token%22%3A%20%7B%22
     given_name%22%3A%20null%2C%22
     verified_claims%22%3A%20%7B%22
     verification%22%3A%20%7B%22
     trust_framework%22%3A%20null%7D%2C%22
     claims%22%3A%20%7B%22
     family_name%22%3A%20null%7D%7D%7D%7D HTTP/1.1
  Host: server.example.com
```

# OP Metadata {#opmetadata}

The OP advertises its capabilities with respect to Verified Claims in its openid-configuration (see [@!OpenID-Discovery]) using the following new elements:

`verified_claims_supported`: REQUIRED. Boolean value indicating support for `verified_claims`, i.e., the OpenID Connect for Identity Assurance extension.

`trust_frameworks_supported`: REQUIRED. JSON array containing all supported trust frameworks. This array MUST have at least one member.

`claims_in_verified_claims_supported`: REQUIRED. JSON array containing all Claims supported within `verified_claims`. Claims that are not present in this array MUST NOT be returned within the `verified_claims` object. This array MUST have at least one member.

`evidence_supported`: REQUIRED when one or more type of evidence is supported. JSON array containing all types of identity evidence the OP uses. This array MUST have at least one member. Members of this array SHOULD only be the types of evidence supported by the OP in the evidence element (see section 4.2.2 of [@!IDA-verified-claims]).

`documents_supported`: REQUIRED when `evidence_supported` contains "document". JSON array containing all identity document types utilized by the OP for identity verification. This array MUST have at least one member.

`documents_methods_supported`: OPTIONAL. JSON array containing the verification methods the OP supports for evidences of type "document" (see @!predefined_values). When present this array MUST have at least one member.

`documents_check_methods_supported`: OPTIONAL. JSON array containing the check methods the OP supports for evidences of type "document" (see [@!predefined_values]). When present this array MUST have at least one member.

`electronic_records_supported`: REQUIRED when `evidence_supported` contains "electronic\_record". JSON array containing all electronic record types the OP supports (see [@!predefined_values]). When present this array MUST have at least one member.

`digest_algorithms_supported`: REQUIRED when OP supports external attachments. JSON array containing all supported digest algorithms which can be used as `alg` property within the digest object of external attachments. If the OP supports external attachments, at least the algorithm `sha-256` MUST be supported by the OP as well. The list of possible digest/hash algorithm names is maintained by IANA in [@!hash_name_registry] (established by [@RFC6920]).

This is an example openid-configuration snippet:

```json
{
...
   "verified_claims_supported":true,
   "trust_frameworks_supported":[
     "nist_800_63A"
   ],
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
   "claims_in_verified_claims_supported": [
      "given_name",
      "family_name",
      "birthdate",
      "place_of_birth",
      "nationalities",
      "address"
   ],
  "digest_algorithms_supported": [
    "sha-256"
  ],
...
}
```

If the OP supports the `claims` parameter as defined in Section 5.5 of the OpenID Connect specification [@!OpenID], the OP MUST advertise this in its OP metadata using the `claims_parameter_supported` element.

If the OP supports distributed and/or aggregated Claim types, as defined in Section 5.6.2 of the OpenID Connect specification [@!OpenID], in `verified_claims`, the OP MUST advertise this in its metadata using the `claim_types_supported` element.

# Client Registration and Management

During Client Registration (see [@!OpenID-Registration]) as well as during Client Management [@RFC7592] the following additional properties are available:

`digest_algorithm`: String value representing the chosen digest algorithm (for external attachments). The value MUST be one of the digest algorithms supported by the OP as advertised in the [OP metadata](#opmetadata). If this property is not set, `sha-256` will be used by default.

# Transaction-specific Purpose {#purpose}

This specification introduces the request parameter `purpose` to allow an RP
to state the purpose for the transfer of End-User data it is asking for.

`purpose`: OPTIONAL. String describing the purpose for obtaining certain End-User data from the OP. The purpose MUST NOT be shorter than 3 characters and MUST NOT be longer than 300 characters. If these rules are violated, the authentication request MUST fail and the OP returns an error `invalid_request` to the RP.

The OP SHOULD use the purpose provided by the RP to inform the respective End-User about the designated use of the data to be transferred or the authorization to be approved.

In order to ensure a consistent UX, the RP MAY send the `purpose` in a certain language and request the OP to use the same language using the `ui_locales` parameter.

If the parameter `purpose` is not present in the request, the OP MAY utilize a description that was pre-configured for the respective RP.

Note: In order to prevent injection attacks, the OP MUST escape the text appropriately before it will be shown in a user interface. The OP MUST expect special characters in the URL decoded purpose text provided by the RP. The OP MUST ensure that any special characters in the purpose text cannot be used to inject code into the web interface of the OP (e.g., cross-site scripting, defacing). Proper escaping MUST be applied by the OP. The OP SHALL NOT remove characters from the purpose text to this end.

# Privacy Consideration {#Privacy}

The use of scopes is a potential shortcut to request a pre-defined set of Claims, however, the use of scopes might result in more data being returned to the RP than is strictly necessary and not achieving the goal of data minimization. The RP SHOULD only request End-User Claims and metadata it requires.

Timestamps with a time zone component can potentially reveal the person’s location. To preserve the person’s privacy, timestamps within the verification element and Verified Claims that represent times SHOULD be represented in Coordinated Universal Time (UTC), unless there is a specific reason to include the time zone, such as the time zone being an essential part of a consented time related Claim in verified data.

# Security Considerations {#Security}

This specification focuses on mechanisms to carry End-User Claims and accompanying metadata in JSON objects and JSON web tokens, typically as part of an OpenID Connect protocol exchange. Since such an exchange is supposed to take place in security sensitive use cases, implementers MUST:

* ensure End-Users are authenticated using appropriately strong authentication methods, and
* combine this specification with an appropriate security profile for OpenID Connect.

To achieve the full security and interoperability benefits, it is important the implementation of this specification, and the underlying OpenID Connect and OAuth specifications, and selected security profile, are complete and correct. The OpenID Foundation provides tools that SHOULD be used to confirm that deployments behave as described in the specifications, with information available at: https://openid.net/certification/.

## End-User Authentication

Secure identification of End-Users not only depends on the identity verification at the OP but also on the strength of the user authentication at the OP. Combining a strong identification with weak authentication creates a false impression of security while being open to attacks. For example if an OP uses a simple PIN login, an attacker could guess the PIN of another user and identify himself as the other user at an RP with a high identity assurance level. To prevent this kind of attack, RPs SHOULD request the OP to authenticate the user at a reasonable level, typically using multi-factor authentication, when requesting verified End-User Claims. OpenID Connect supports this by way of the `acr_values` request parameter.

## Security Profile

This specification does not define or require a particular security profile since there are several security 
profiles and new security profiles under development.  Implementers have the flexibility to select the security profile that best suits 
their needs. Implementers might consider [@FAPI-1-RW] or [@FAPI-2-BL].

Implementers are RECOMMENDED to select a security profile that has a certification program or other resources that allow both OpenID Providers and Relying Parties to ensure they have complied with the profile’s security and interoperability requirements, such as the OpenID Foundation Certification Program, https://openid.net/certification/.

The integrity and authenticity of the issued assertions MUST be ensured in order to prevent identity spoofing.

The confidentiality of all End-User data exchanged between the protocol parties MUST be ensured using suitable methods at transport or application layer.

# Predefined Values {#predefined_values}

This specification focuses on the technical mechanisms to convey Verified Claims and thus does not define any identifiers for trust frameworks, documents, methods, check methods. This is left to adopters of the technical specification, e.g., implementers, identity schemes, or jurisdictions.

Each party defining such identifiers MUST ensure the collision resistance of these identifiers. This is achieved by including a domain name under the control of this party into the identifier name, e.g., `https://mycompany.com/identifiers/cool_check_method`.

The eKYC and Identity Assurance Working Group maintains a wiki page [@!predefined_values_page] that can be utilized to share predefined values with other parties.

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

<reference anchor="OpenID-Discovery" target="https://openid.net/specs/openid-connect-discovery-1_0.html">
  <front>
    <title>OpenID Connect Discovery 1.0 incorporating errata set 1</title>
    <author initials="N." surname="Sakimura" fullname="Nat Sakimura">
      <organization>NRI</organization>
    </author>
    <author initials="J." surname="Bradley" fullname="John Bradley">
      <organization>Ping Identity</organization>
    </author>
    <author initials="M." surname="Jones" fullname="Mike Jones">
      <organization>Microsoft</organization>
    </author>
    <author initials="E." surname="Jay" fullname="Edmund Jay">
      <organization>Illumila</organization>
    </author>
   <date day="8" month="Nov" year="2014"/>
  </front>
</reference>

<reference anchor="OpenID-Registration" target="https://openid.net/specs/openid-connect-registration-1_0.html">
  <front>
    <title>OpenID Connect Dynamic Client Registration 1.0 incorporating errata set 1</title>
    <author initials="N." surname="Sakimura" fullname="Nat Sakimura">
      <organization>NRI</organization>
    </author>
    <author initials="J." surname="Bradley" fullname="John Bradley">
      <organization>Ping Identity</organization>
    </author>
    <author initials="M." surname="Jones" fullname="Mike Jones">
      <organization>Microsoft</organization>
    </author>
   <date day="8" month="Nov" year="2014"/>
  </front>
</reference>

<reference anchor="FAPI-1-RW" target="https://bitbucket.org/openid/fapi/src/master/Financial_API_WD_002.md">
  <front>
    <title>Financial-grade API - Part 2: Read and Write API Security Profile</title>
    <author initials="" surname="OpenID Foundation's Financial API (FAPI) Working Group">
      <organization>OpenID Foundation's Financial API (FAPI) Working Group</organization>
    </author>
   <date day="9" month="Sep" year="2020"/>
  </front>
</reference>

<reference anchor="FAPI-2-BL" target="https://bitbucket.org/openid/fapi/src/master/FAPI_2_0_Baseline_Profile.md">
  <front>
    <title>FAPI 2.0 Baseline Profile </title>
    <author initials="" surname="OpenID Foundation's Financial API (FAPI) Working Group">
      <organization>OpenID Foundation's Financial API (FAPI) Working Group</organization>
    </author>
   <date day="9" month="Sep" year="2020"/>
  </front>
</reference>

<reference anchor="OpenID4IDAClaims" target="http://openid.net/specs/openid-connect-4-ida-claims-1_0.html">
  <front>
    <title>OpenID Connect for Identity Assurance Claims Registration 1.0</title>
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

<reference anchor="IDA-verified-claims" target="https://openid.net/specs/openid-ida-verified-claims-1_0.html">
  <front>
    <title>OpenID Identity Assurance schema definition</title>
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
   <date day="9" month="Aug" year="2023"/>
  </front>
</reference>

<reference anchor="NIST-SP-800-63a" target="https://doi.org/10.6028/NIST.SP.800-63a">
  <front>
    <title>NIST Special Publication 800-63A, Digital Identity Guidelines, Enrollment and Identity Proofing Requirements</title>
    <author initials="Paul. A." surname="Grassi" fullname="Paul A. Grassi">
      <organization>NIST</organization>
    </author>
    <author initials="James L." surname="Fentony" fullname="James L. Fentony">
      <organization>Altmode Networks</organization>
    </author>
    <author initials="Naomi B." surname="Lefkovitz" fullname="Naomi B. Lefkovitz">
      <organization>NIST</organization>
    </author>
    <author initials="Jamie M." surname="Danker" fullname="Jamie M. Danker">
      <organization>Department of Homeland Security</organization>
    </author>
    <author initials="Yee-Yin" surname="Choong" fullname="Yee-Yin Choong">
      <organization>NIST</organization>
    </author>
    <author initials="Kristen K." surname="Greene" fullname="Kristen K. Greene">
      <organization>NIST</organization>
    </author>
    <author initials="Mary F." surname="Theofanos" fullname="Mary F. Theofanos">
      <organization>NIST</organization>
    </author>
   <date month="June" year="2017"/>
  </front>
</reference>

<reference anchor="eIDAS" target="https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32014R0910">
  <front>
    <title>REGULATION (EU) No 910/2014 OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL on electronic identification and trust services for electronic transactions in the internal market and repealing Directive 1999/93/EC</title>
    <author initials="" surname="European Parliament">
      <organization>European Parliament</organization>
    </author>
   <date day="23" month="July" year="2014"/>
  </front>
</reference>

<reference anchor="FATF-Digital-Identity" target="https://www.fatf-gafi.org/media/fatf/documents/recommendations/Guidance-on-Digital-Identity.pdf">
  <front>
    <title>Guidance on Digital Identity</title>
    <author initials="" surname="FATF">
      <organization>Financial Action Task Force (FATF)</organization>
    </author>
   <date month="March" year="2020"/>
  </front>
</reference>

<reference anchor="verified_claims.json" target="https://openid.net/wg/ekyc-ida/references/">
  <front>
    <title>JSON Schema for assertions using verified_claims</title>
    <author>
        <organization>OpenID Foundation</organization>
      </author>
   <date year="2020"/>
  </front>
</reference>

<reference anchor="verified_claims_request.json" target="https://openid.net/wg/ekyc-ida/references/">
  <front>
    <title>JSON Schema for requesting verified_claims</title>
    <author>
        <organization>OpenID Foundation</organization>
      </author>
   <date year="2020"/>
  </front>
</reference>

<reference anchor="predefined_values_page" target="https://openid.net/wg/ekyc-ida/identifiers/">
  <front>
    <title>Overview page for predefined values</title>
    <author>
      <organization>OpenID Foundation</organization>
    </author>
    <date year="2021"/>
  </front>
</reference>

<reference anchor="hash_name_registry" target="https://www.iana.org/assignments/named-information/">
  <front>
    <title>Named Information Hash Algorithm Registry</title>
    <author>
      <organization>IANA</organization>
    </author>
    <date year="2016" month="09"/>
  </front>
</reference>

<reference anchor="IANA.MediaTypes" target="https://www.iana.org/assignments/media-types">
 <front>
   <title>Media Types</title>
   <author><organization>IANA</organization></author>
 </front>
</reference>

# IANA Considerations

## JSON Web Token Claims Registration

This specification requests registration of the following value in the IANA "JSON Web Token Claims Registry" established by [@!RFC7519].

### Registry Contents

Claim Name:
: `verified_claims`

Claim Description:
: This container Claim is composed of the verification evidence related to a certain verification process and the corresponding Claims about the End-User which were verified in this process.

Change Controller:
: eKYC and Identity Assurance Working Group - openid-specs-ekyc-ida@lists.openid.net

Specification Document(s):
: Section [Verified Claims](#verified_claims) of this document

## Media Type Registration

This section registers the `application/provided-claims+jwt` media type [@RFC2046]
in the IANA "Media Types" registry [@IANA.MediaTypes] in the manner described in [@RFC6838],
which is used to indicate that the content is a JWT describing aggregated claims.

  * Type name: application
  * Subtype name: provided-claims+jwt
  * Required parameters: n/a
  * Optional parameters: n/a
  * Encoding considerations: binary; An external claims JWT is a JWT; JWT values are encoded as a series of base64url-encoded values (some of which may be the empty string) separated by period ('.') characters.
  * Security considerations: See https://openid.net/specs/openid-connect-4-identity-assurance-1_0.html#name-representing-verified-claim
  * Interoperability considerations: n/a
  * Published specification: (#verified_claims_delivery) of [[ this specification ]]
  * Applications that use this media type: When using [[ this specification ]], this media type is used in the `typ` header of assertions provided as aggregated or distributed claims (see Section 5.6.2 of the OpenID Connect specification [@!OpenID]).
  * Fragment identifier considerations: n/a
  * Additional information:
    * File extension(s): n/a
    * Macintosh file type code(s): n/a
  * Person &amp; email address to contact for further information: Daniel Fett, mail@danielfett.de
  * Intended usage: COMMON
  * Restrictions on usage: none
  * Author: Daniel Fett, mail@danielfett.de
  * Change controller: IETF
  * Provisional registration? No


# Example Requests
This section shows examples of requests for `verified_claims`.

## Verification of Claims by a document

<{{examples/request/verification_deeper.json}}

Note that, as shown in the above example, this specification requires that implementations receiving requests are able to distinguish between JSON objects where a key is not present versus where a key is present with a null value.

Support for these null value requests is mandatory for identity providers, so implementors are encouraged to test this behaviour early in their development process. In some programming languages many JSON libraries or HTTP frameworks will, at least by default, ignore null values and omit the relevant key when parsing the JSON.

## Verification of Claims by trust framework and evidence types

<{{examples/request/verification_claims_trust_frameworks_evidence.json}}

## Verification of Claims by trust framework and check method

<{{examples/request/verification_spid_document_biometric.json}}

## Verification of Claims by electronic signature

<{{examples/request/verification_electronic_signature.json}}

# Example Responses

This section shows examples of responses containing `verified_claims`.

The first and second subsections show JSON snippets of the general identity assurance case, where the RP is provided with verification evidence for different methods along with the actual Claims about the End-User.

The third subsection illustrates the possible contents of this object in case of a notified eID system under eIDAS, where the OP does not need to provide evidence of the identity verification process to the RP.

Subsequent subsections contain examples for using the `verified_claims` Claim on different channels and in combination with other (unverified) Claims.

## Document

<{{examples/response/document_800_63A.json}}

Same document under a different `trust_framework`

<{{examples/response/document_UK_DIATF.json}}

## Document and verifier details

<{{examples/response/document_verifier.json}}

## Evidence with all assurance details

<{{examples/response/evidence_with_assurance_details.json}}

## Notified eID system (eIDAS)

<{{examples/response/eidas.json}}

## Electronic_record

<{{examples/response/electronic_record.json}}

## Vouch

<{{examples/response/vouch.json}}

## Multiple Verified Claims

<{{examples/response/multiple_verified_claims.json}}

## Claims provided by the OP and external sources {#op_attested_and_external_claims}

This example shows how an OP can mix own Claims and Claims provided by  
external sources in a single ID Token.

<{{examples/response/all_in_one.json}}

## Self-Issued OpenID Connect Provider and External Claims

This example shows how a Self-Issued OpenID Connect Provider (SIOP)
may include Verified Claims obtained from different external Claim
sources into a ID Token.

<{{examples/response/siop_aggregated_and_distributed_claims.json}}

# Example Requests and Responses

This section shows examples of pairs of requests and responses containing `verified_claims`.

## Verified Claims in UserInfo Response

### Request

In this example we assume the RP uses the `scope` parameter to request the email address and, additionally, the `claims` parameter, to request Verified Claims.

The scope value is: `scope=openid email`

The value of the `claims` parameter is:

<{{examples/request/userinfo.json}}

### Response

The respective UserInfo response would be

<{{examples/response/userinfo.json}}

## Verified Claims in ID Tokens

### Request

In this case, the RP requests Verified Claims along with other Claims about the End-User in the `claims` parameter and allocates the response to the ID Token (delivered from the token endpoint in case of grant type `authorization_code`).

The `claims` parameter value is

<{{examples/request/id_token.json}}

### Response

The decoded body of the respective ID Token could be

<{{examples/response/userinfo.id_token.json}}

# Acknowledgements {#Acknowledgements}

The following people at yes.com and partner companies contributed to the concept described in the initial contribution to this specification: Karsten Buch, Lukas Stiebig, Sven Manz, Waldemar Zimpfer, Willi Wiedergold, Fabian Hoffmann, Daniel Keijsers, Ralf Wagner, Sebastian Ebling, Peter Eisenhofer.

We would like to thank Julian White, Bjorn Hjelm, Stephane Mouy, Alberto Pulido, Joseph Heenan, Vladimir Dzhuvinov, Azusa Kikuchi, Naohiro Fujie, Takahiko Kawasaki, Sebastian Ebling, Marcos Sanz, Tom Jones, Mike Pegman, Michael B. Jones, Jeff Lombardo, Taylor Ongaro, Peter Bainbridge-Clayton, Adrian Field, George Fletcher, Tim Cappalli, Michael Palage, Sascha Preibisch, Giuseppe De Marco, Nick Mothershaw, Dima Postnikov and Nat Sakimura for their valuable feedback and contributions that helped to evolve this specification.

# Notices

Copyright (c) 2022 The OpenID Foundation.

The OpenID Foundation (OIDF) grants to any Contributor, developer, implementer, or other interested party a non-exclusive, royalty free, worldwide copyright license to reproduce, prepare derivative works from, distribute, perform and display, this Implementers Draft or Final Specification solely for the purposes of (i) developing specifications, and (ii) implementing Implementers Drafts and Final Specifications based on such documents, provided that attribution be made to the OIDF as the source of the material, but that such attribution does not indicate an endorsement by the OIDF.

The technology described in this specification was made available from contributions from various sources, including members of the OpenID Foundation and others. Although the OpenID Foundation has taken steps to help ensure that the technology is available for distribution, it takes no position regarding the validity or scope of any intellectual property or other rights that might be claimed to pertain to the implementation or use of the technology described in this specification or the extent to which any license under such rights might or might not be available; neither does it represent that it has made any independent effort to identify any such rights. The OpenID Foundation and the contributors to this specification make no (and hereby expressly disclaim any) warranties (express, implied, or otherwise), including implied warranties of merchantability, non-infringement, fitness for a particular purpose, or title, related to this specification, and the entire risk as to implementing this specification is assumed by the implementer. The OpenID Intellectual Property Rights policy requires contributors to offer a patent promise not to assert certain patent claims against other contributors and against implementers. The OpenID Foundation invites any interested party to bring to its attention any copyrights, patents, patent applications, or other proprietary rights that may cover technology that may be required to practice this specification.

# Document History

   [[ To be removed from the final specification ]]

   -14
   * Added requirements on aggregated and distributed claims to reduce risk of confusion with other JWTs (incl. IANA media type registration)
   * Removed deprecated elements `utility_bill` and `document`
   * split out IANA claims registration into separate document "openid-connect-4-ida-claims"
   * split out schema definition of `verified_claims` into separate documemnt 

   -13
   * Preparation for Implementers Draft 4
   * Checked and fixed referencing
   * Added note about issues with JSON null
   * Defined clearly that JSON schema is not normative
   * Various editorial clarifications
   * Added checking of defined end-user claims to JSON schema
   * Clarified OP Metadata wording

   -12

   * introduced `document` evidence type, which is more universal than `id_document`
   * deprecated `id_document`
   * introduced `electronic_record` and `vouch` evidence types
   * introduced `check_details` & `assurance_details` to provide more detail than `method`
   * added lookahead capabilities for distributed Claims
   * added support to attach document artifacts
   * added txn for attachments
   * changed evidence type `qes` to `electronic_signature`
   * added Claim `also_known_as`
   * added text regarding security profiles
   * editorial improvements
   * added further co-authors
   * added `assurance_level` field
   * added `assurance_process` type
   * added text about dependency between identity assurance and authentication assurance
   * added new field `country_code` to `address` Claim
   * relaxed requirements for showing purpose

   -11

   * Added support for requesting different sets of Claims with different requirements regarding trust_framework and other verification elements (e.g., evidence)
   * added `msisdn` Claim
   * clarified scope of this specification

   -10

   * Editorial improvements
   * Improved JSON schema (alignment with spec and bug fix)

   -09

   * `verified_claims` element may contain one or more Verified Claims objects
   * an individual assertion may contain `verified_claims` elements in the assertion itself and any aggregated or distributed Claims sets it includes or refers to, respectively
   * moved all definitions of pre-defined values for trust frameworks, id documents and verification methods to a wiki page as non-normative overview
   * clarified and simplified request syntax
   * reduced mandatory requirement `verified_claims` to bare minimum
   * removed JSON schema from draft and added reference to JSON schema file instead
   * added request JSON schema
   * added IANA section with JSON Web Token Claims Registration
   * integrated source into single md file
   * added privacy considerations regarding time zone data, enhanced syntax definition of time and date-time fields in spec and response schema
   * fixed typos

   -08

   * added `uripp` verification method
   * small fixes to examples

   -07

   * fixed typos
   * changed `nationality` String Claim to `nationalities` String array Claim
   * replaced `agent` in id_document verifier element by `txn` element
   * qes method: fixed error in description of `issuer`
   * qes method: changed `issued_at` to `created_at` since this field applies to the signature (that is created and not issued)
   * Changed format of `nationalities` and issuing `country` to ICAO codes
   * Changed `date` in verification element to `time`
   * Added Japanese trust frameworks to pre-defined values
   * Added Japanese id documents to pre-defined values
   * adapted JSON schema and examples

   -06

   * Incorporated review feedback by Marcos Sanz and Adam Cooper
   * Added text on integrity, authenticity, and confidentiality for data passed between OP and RP to Security Considerations section
   * added `purpose` field to `claims` parameter
   * added feature to let the RP explicitly requested certain `verification` data

   -05

   * incorporated review feedback by Mike Jones
   * Added OIDF Copyright Notices
   * Moved Acknowledgements to Appendix A
   * Removed RFC 2119 keywords from scope & requirements section and rephrased section
   * rephrased introduction
   * replaced `birth_name` with `birth_family_name`, `birth_given_name`, and `birth_middle_name`
   * replaced `transaction_id` with `txn` from RFC 8417
   * added references to eIDAS, ISO 3166-1, ISO 3166-3, and ISO 8601-2004
   * added note on `purpose` and locales
   * changed file name and document title to include 1.0 version id
   * corrected evidence plural
   * lots of editorial fixes
   * Alignment with OpenID Connect Core wording
   * Renamed `id` to `verification_process`
   * Renamed `verified_person_data` to `verified_claims`

   -04
   
   * incorporated review feedback by Marcos Sanz
   
   -03

   * enhanced draft to support multiple evidence
   * added a JSON Schema for assertions containing the `verified_person_data` Claim
   * added more identity document definitions
   * added `region` field to `place_of_birth` Claim
   * changed `eidas_loa_substantial/high` to `eidas_ial_substantial/high`
   * fixed typos in examples
   * uppercased all editorial occurences of the term `claims` to align with OpenID Connect Core

   -02

   * added new request parameter `purpose`
   * simplified/reduced number of verification methods
   * simplfied identifiers
   * added `identity_documents_supported` to metadata section
   * improved examples

   -01

   *  fixed some typos
   *  remove organization element (redundant) (issue 1080)
   *  allow other Claims about the End-User in the `claims` sub element (issue 1079)
   *  changed `legal_context` to `trust_framework`
   *  added explanation how the content of the verification element is determined by the trust framework
   *  added URI-based identifiers for `trust_framework`, `identity_document` and (verification) `method`
   *  added example attestation for notified/regulated eID system
   *  adopted OP metadata section accordingly
   *  changed error behavior for `max_age` member to alig with OpenID Core
   *  Added feature to let the RP express requirements for verification data (trust framework, identity documents, verification method)
   *  Added privacy consideration section and added text on legal basis for data exchange
   *  Added explanation about regulated and un-regulated eID systems

   -00 (WG document)

   *  turned the proposal into a WG document
   *  changed name
   *  added terminology section and reworked introduction
   *  added several examples (ID Token vs UserInfo, unverified & Verified Claims, aggregated & distributed Claims)
   *  incorporated text proposal of Marcos Sanz regarding max_age
   *  added IANA registration for new error code `unable_to_meet_requirement`
