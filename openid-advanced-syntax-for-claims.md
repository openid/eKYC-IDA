%%%
title = "OpenID Connect Advanced Syntax for Claims (ASC) 1.0"
abbrev = "openid-connect-4-identity-assurance-1_0"
ipr = "none"
workgroup = "eKYC-IDA"
keyword = ["openid", "identity assurance", "ekyc"]

[seriesInfo]
name = "Internet-Draft"

value = "openid-connect-advanced-syntax-for-claims-1_0-00"

status = "standard"

[[author]]
initials="D."
surname="Fett"
fullname="Daniel Fett"
organization="yes.com"
    [author.address]
    email = "mail@danielfett.de"

%%%

.# Abstract

This specification defines an extension of OpenID Connect to enable new features for requesting and receiving Claims and meta information about Claims.

{mainmatter}

# Introduction {#Introduction}
TBD
## Terminology
TBD
# Scope
TBD

# Transformed Claims

# Selective Abort/Omit

Using Selective Abort/Omit (SAO), an RP can define the expected behavior of an OP when certain data is not available, when a user does not consent to the release of the data, or when restrictions defined on claims using `value`, `values`, or `max_age` cannot be fulfilled. 

Note: SAO is in particular useful when some of the claims (e.g., verified claims) are priced and the RP is only interested to pay for the respective claims if certain conditions are met.

This feature is fully independent from the use of `essential` as defined in Section 5.5 of [@!OpenID].

## Syntax

The RP can use the following two "case keys" on all standard OpenID Connect claims, verified claims, and verification elements:

 * `if_unavailable` describes the case that the OP does not have data about this
   claim or does not support this claim, or that the user did not consent to the release of the data. Note that the latter can only apply if the user interface of the OP allows the user to deselect single claims. If the user does not consent to the whole transaction, standard OpenID Connect logic applies. 

 * `if_different` describes the case that the restrictions on claim data expressed using
   `value`, `values`, or `max_age` cannot be fulfilled with the available data.
   Will be ignored if no restriction was defined.


For each of these two keys, one of the following expected "actions" can be defined:

 * `omit`: Omit this particular claim from the response. If an element is to be
   omitted that is required for a valid response, its parent elements MUST be
   omitted as well, recursively until the response is valid.

 * `omit_set`: Omit this particular claim and all claims for which the same
   action is set. This can be used by the RP to define a set of claims that is
   only useful when delivered in full.

 * `omit_verified_claims`: (Only applicable when used with [@ekyc].) Omit this
   particular claim and the whole `verified_claims` section. Only valid within
   the `verified_claims` section.

 * `abort`: Abort the whole transaction by returning an Authentication Error
   Response (as in Section 3.1.2.6 of [@!OpenID]) using the error code
   `access_denied` to the RP. The `error_description` SHOULD indicate which rule
   led to the abort of the transaction if and only if the action is
   `if_unavailable` or the user has consented to the release of the data (see
   (#privacy_if_no) below).

If both conditions apply (e.g., the user did not consent to the release of data
and this data does not fulfill a `value` restriction), the case `if_unavailable`
takes precedence.  Whenever an `abort` action is met, it takes precedence over
any of the other actions, i.e., the transaction is aborted in this case.

Omitting Claims can be recursive: If a Claim is omitted through `omit` or `omit_set`, or it is a Claim within `verified_claims` and `omit_verified_claims` was applied, the Claim's `if_unavailable` action is triggered as well.

The following table shows the default actions when case keys are omitted:

|                  | default | within `verified_claims/verification` of [@ekyc] |
| ---------------- | ------- | ------------------------------------------------ |
| `if_unavailable` | `omit`  | `omit`                                           |
| `if_different`   | `omit`  | `omit_verified_claims`                           |


Example:

<{{examples/request/omit_abort.json}}

This example would yield the following results (among other outcomes, always assuming that other data is available and matches the requirements):


| Condition                                                             | Result                                                                  |
| --------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `phone_number` not available                                          | Transaction is aborted.                                                 |
| `email_verified` not available                                        | `email_verified` is omitted.                                            |
| `email_verified` is not `test@example.com`                            | Transaction is aborted.                                                 |
| `trust_framework` is not `de_aml` or is unavailable                   | Transaction is aborted.                                                 |
| `verification_process` is unavailable                                 | `verified_claims` is omitted → `custom_paid_claim` is omitted as well   |
| verified `address` is unavailable                                     | `verified_claims` is omitted → `custom_paid_claim` is omitted as well   |
| verified `nationalities` or verified `place_of_birth` are unavailable | `nationalities`, `place_of_birth`, and `custom_paid_claim` are omitted. |


## Error Handling

If the `claims` sub-element is empty or if an action is used that is unknown to the OP, the OP MUST abort the transaction with an `invalid_request` error. If a case key is used that is unknown to the OP, it MUST be ignored.


## Privacy {#privacy_if_no}


In the interest of data minimization, RPs SHOULD use the mechanisms shown above to limit cases in which incomplete data sets are provided by the OP that are not useful to the RP.


An RP might be able to derive information from a response even if the response is an error response or claims are omitted. For example, the following request can be used to derive whether or not the user is named `Max`:

```json
{
  "given_name": {
    "value": "Max",
    "if_different": "abort",
    "if_unavailable": "omit"
  }
}
```

When the request is aborted, the user is not called Max. In a naive implementation, the abort of the request might happen before the user has consented to the release of the data. In this case, using a series of carefully crafted requests, an RP might be able to derive substantial information about a user even if the user's name is never transferred from the OP to the RP directly. A malicious RP can use this to derive user information without the user's consent or without paying for the data.

To avoid leakage of user information through this mechanism without the user's consent, implementations MUST in general avoid evaluating `if_not_match` before a user has consented to the release of the data if privacy is a concern in the respective application. In the example above, the user would be asked to confirm the release of the given name data field before the OP aborts the transaction or omits the claim. OPs MAY make exceptions for RPs when a contractual or trust relationship with this RP was established beforehand or there are other mechanisms in place such that this kind of misuse is prevented.

OPs MUST also consider whether the (un)availability of data (`if_unavailable`) can leak data in a similar way in the respective application and, if so, apply the same restrictions. 

To the same end, and to avoid relying parties not paying for data, OPs SHOULD additionally consider rate-limiting requests and monitoring requests for anomalies (frequent dynamic changes in request structure, frequent aborts).

## Selective Abort/Omit Metadata

An OP supporting SAO shall publish the key `selective_abort_omit_supported` in its OP Metadata as follows:


```json
...
  "selective_abort_omit_supported": true,
...
```

## Compatibility Considerations

An OP not supporting SAO will ignore the additional keys as defined in Section 5.5.1 of [@!OpenID]. The RP may therefore receive data from such an OP when aborting the transaction was requested instead. RPs can avoid this by checking for SAO support at the OP before sending the request.

# Data Availability Feedback



# Privacy Consideration {#Privacy}

TBD
# Security Considerations {#Security}
TBD

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
# IANA Considerations

TBD

# Acknowledgements {#Acknowledgements}

TBD
# Notices

Copyright (c) 2020 The OpenID Foundation.

The OpenID Foundation (OIDF) grants to any Contributor, developer, implementer, or other interested party a non-exclusive, royalty free, worldwide copyright license to reproduce, prepare derivative works from, distribute, perform and display, this Implementers Draft or Final Specification solely for the purposes of (i) developing specifications, and (ii) implementing Implementers Drafts and Final Specifications based on such documents, provided that attribution be made to the OIDF as the source of the material, but that such attribution does not indicate an endorsement by the OIDF.

The technology described in this specification was made available from contributions from various sources, including members of the OpenID Foundation and others. Although the OpenID Foundation has taken steps to help ensure that the technology is available for distribution, it takes no position regarding the validity or scope of any intellectual property or other rights that might be claimed to pertain to the implementation or use of the technology described in this specification or the extent to which any license under such rights might or might not be available; neither does it represent that it has made any independent effort to identify any such rights. The OpenID Foundation and the contributors to this specification make no (and hereby expressly disclaim any) warranties (express, implied, or otherwise), including implied warranties of merchantability, non-infringement, fitness for a particular purpose, or title, related to this specification, and the entire risk as to implementing this specification is assumed by the implementer. The OpenID Intellectual Property Rights policy requires contributors to offer a patent promise not to assert certain patent claims against other contributors and against implementers. The OpenID Foundation invites any interested party to bring to its attention any copyrights, patents, patent applications, or other proprietary rights that may cover technology that may be required to practice this specification.

# Document History

   [[ To be removed from the final specification ]]

   -00

   *  first version

