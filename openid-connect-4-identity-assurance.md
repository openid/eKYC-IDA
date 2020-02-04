%%%
title = "OpenID Connect for Identity Assurance 1.0"
abbrev = "openid-connect-4-identity-assurance-1_0"
ipr = "trust200902"
workgroup = "connect"
keyword = ["security", "openid", "identity assurance"]

[seriesInfo]
name = "Internet-Draft"
value = "openid-connect-4-identity-assurance-1_0-09"
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


%%%

.# Abstract

This specification defines an extension of OpenID Connect for providing Relying Parties with verified Claims about End-Users. This extension is intended to be used to verify the identity of a natural person in compliance with a certain law.

{mainmatter}

# Introduction {#Introduction}

This specification defines an extension to OpenID Connect [@!OpenID] to address the use case of strong identity verification of a natural person in accordance with certain laws. Examples include Anti Money Laundering Laws, Telecommunication Acts, Anti Terror Laws, and regulations on trust services, such as eIDAS [@?eIDAS].

In such use cases, the Relying Parties (RPs) need to know the assurance level of the Claims about the End-User attested by the OpenID Connect Providers (OPs) or any other trusted source along with evidence related to the identity verification process.

The `acr` Claim, as defined in Section 2 of the OpenID Connect specification [@!OpenID], is suited to attest information about the authentication performed in an OpenID Connect transaction. But identity assurance requires a different representation for the following reason: authentication is an aspect of an OpenID Connect transaction while identity assurance is a property of a certain Claim or a group of Claims and several of them will typically be conveyed to the RP as the result of an OpenID Connect transaction.

For example, the assurance an OP typically will be able to attest for an e-mail address will be “self-asserted” or “verified by opt-in or similar mechanism”. The family name of a user, in contrast, might have been verified in accordance with the respective Anti Money Laundering Law by showing an ID Card to a trained employee of the OP operator.

Identity assurance therefore requires a way to convey assurance data along with and coupled to the respective Claims about the End-User. This specification proposes a suitable representation and mechanisms the RP will utilize to request verified claims about an End-User along with identity assurance data and for the OP to represent these verified Claims and accompanying identity assurance data.

## Terminology

This section defines some terms relevant to the topic covered in this document, heavily inspired by NIST SP 800-63A [@?NIST-SP-800-63a].

* Identity Proofing - process in which a user provides evidence to an OP or claim provider reliably identifying themselves, thereby allowing the OP to assert that identification at a useful identity assurance level.

* Identify Verification - process conducted by the OP or a claim provider to verify the user's identity.

* Identity Assurance - process in which the OP or a claim provider attests identity data of a certain user with a certain assurance towards an RP, typically expressed by way of an assurance level. Depending on legal requirements, the OP may also be required to provide evidence of the identity verification process to the RP.

* Verified Claims - Claims about an End-User, typically a natural person, whose binding to a particular user account was verified in the course of an identity verification process.

[1]: https://pages.nist.gov/800-63-3/sp800-63a.html "NIST Special Publication 800-63A, Digital Identity Guidelines, Enrollment and Identity Proofing Requirements"

# Scope and Requirements

The scope of the extension is to define a mechanism to assert verified Claims, in general, and to introduce new Claims about the End-User required in the identity assurance space; one example would be the place of birth.

The RP will be able to request the minimal data set it needs (data minimization) and to express requirements regarding this data and the evidence and the identity verification processes employed by the OP.

This extension will be usable by OPs operating under a certain regulation related to identity assurance, such as eIDAS notified eID systems, as well as other OPs. Strictly regulated OPs can attest identity data without the need to provide further evidence since they are approved to operate according to well-defined rules with clearly defined liability.

For example in the case of eIDAS, the peer review ensures eIDAS compliance and the respective member state takes the liability for the identities asserted by its notified eID systems. Every other OP not operating under such well-defined conditions is typically required to provide the RP data about the identity verification process along with identity evidence to allow the RP to conduct their own risk assessment and to map the data obtained from the OP to other laws. For example, it shall be possible to use identity data maintained in accordance with the Anti Money Laundering Law to fulfill requirements defined by eIDAS.

From a technical perspective, this means this specification allows the OP to attest verified Claims along with information about the respective trust framework (and assurance level) but also supports the externalization of information about the identity verification process.

The representation defined in this specification can be used to provide RPs with verified Claims about the End-User via any appropriate channel. In the context of OpenID Connnect, verified Claims can be attested in ID Tokens or as part of the UserInfo response. It is also possible to utilize the format described here in OAuth Token Introspection responses (see [@?RFC7662] and [@?I-D.ietf-oauth-jwt-introspection-response]) to provide resource servers with verified Claims.

This extension is intended to be truly international and support identity assurance for different and across jurisdictions. The extension is therefore extensible to support additional trust frameworks, verification methods, and identity evidence.

In order to give implementors as much flexibility as possible, this extension can be used in conjunction with existing OpenID Connect Claims and other extensions within the same OpenID Connect assertion (e.g., ID Token or UserInfo response) utilized to convey Claims about End-Users.

For example, OpenID Connect [@!OpenID] defines Claims for representing family name and given name of a user without a verification status. Those Claims can be used in the same OpenID Connect assertion beside verified Claims represented according to this extension.

In the same way, existing Claims to inform the RP of the verification status of the `phone_number` and `email` Claims can be used together with this extension.

Even for asserting verified Claims, this extension utilizes existing OpenID Connect Claims if possible and reasonable. The extension will, however, ensure RPs cannot (accidentally) interpret unverified Claims as verified Claims.

# Claims {#claims}

## Additional Claims about End-Users {#userclaims}

In order to fulfill the requirements of some jurisdictions on identity assurance, this specification defines the following Claims for conveying user data in addition to the Claims defined in the OpenID Connect specification [@!OpenID]:

| Claim | Type | Description |
|:------|:-----|:------------|
|`place_of_birth`| JSON object | End-User’s place of birth. The value of this member is a JSON structure containing some or all of the following members: `country`: REQUIRED. String representing country in [@!ISO3166-1] Alpha-2 (e.g., DE) or [@!ISO3166-3] syntax. `region`: String representing state, province, prefecture, or region component. This field might be required in some jurisdictions. `locality`: REQUIRED. String representing city or locality component.|
|`nationalities`| array | End-User’s nationalities in ICAO 2-letter codes [@!ICAO-Doc9303], e.g. "US" or "DE". 3-letter codes MAY be used when there is no corresponding ISO 2-letter code, such as "EUE".|
|`birth_family_name`| string | End-User’s family name when he or she is born, or at least from the time he or she is a child. This term can be used by a person who changes the family name later in life for any reason.|
|`birth_given_name`| string | End-User’s given name when he or she is born, or at least from the time he or she is a child. This term can be used by a person who changes the given name later in life for any reason.|
|`birth_middle_name`| string | End-User’s middle name when he or she is born, or at least from the time he or she is a child. This term can be used by a person who changes the middle name later in life for any reason.|
|`salutation`| string | End-User’s salutation, e.g. “Mr.”|
|`title`| string | End-User’s title, e.g. “Dr.”|

## txn Claim

Strong identity verification typically requires the participants to keep an audit trail of the whole process.

The `txn` Claim as defined in [@!RFC8417] is used in the context of this extension to build audit trails across the parties involved in an OpenID Connect transaction.

If the OP issues a `txn`, it MUST maintain a corresponding audit trail, which at least consists of the following details:

* the transaction ID,
* the authentication method employed, and
* the transaction type (e.g. scope values).

This transaction data MUST be stored as long as it is required to store transaction data for auditing purposes by the respective regulation.

The RP requests this Claim like any other Claim via the `claims` parameter or as part of a default Claim set identified by a scope value.

The `txn` value MUST allow an RP to obtain these transaction details if needed.

Note: The mechanism to obtain the transaction details from the OP and their format is out of scope of this specification.

# Verified Data Representation

This extension to OpenID Connect wants to ensure that RPs cannot mix up verified and unverified Claims and incidentally process unverified Claims as verified Claims.

The representation proposed therefore provides the RP with the verified Claims within a container element `verified_claims`. This container is composed of the verification evidence related to a certain verification process and the corresponding Claims about the End-User which were verified in this process.

This section explains the structure and meaning of `verified_claims` in detail. A machine-readable syntax definition is given as JSON schema in (#json_schema). It can be used to automatically validate JSON documents containing a `verified_claims` element.

`verified_claims` consists of the following sub-elements:

* `verification`: REQUIRED. Object that contains all data about the verification process.
* `claims`: REQUIRED. Object that is the container for the verified Claims about the End-User.

Note: Implementations MUST ignore any sub-element not defined in this specification or extensions of this specification.

## verification Element {#verification}

This element contains the information about the process conducted to verify a person's identity and bind the respective person data to a user account.

The `verification` element consists of the following elements:

`trust_framework`: REQUIRED. String determining the trust framework governing the identity verification process and the identity assurance level of the OP.

An example value is `eidas_ial_high`, which denotes a notified eID system under eIDAS [@?eIDAS] providing identity assurance at level of assurance "High".

An initial list of standardized values is defined in [Trust Frameworks](#predefined_values_tf). Additional trust framework identifiers can be introduced [how?]. RPs SHOULD ignore `verified_claims` claims containing a trust framework ID they don't understand.

The `trust_framework` value determines what further data is provided to the RP in the `verification` element. A notified eID system under eIDAS, for example, would not need to provide any further data whereas an OP not governed by eIDAS would need to provide verification evidence in order to allow the RP to fulfill its legal obligations. An example of the latter is an OP acting under the German Anti-Money Laundering Law (`de_aml`).

`time`: Time stamp in ISO 8601:2004 [ISO8601-2004] `YYYY-MM-DDThh:mm:ss±hh:mm` format representing the date and time when identity verification took place. Presence of this element might be required for certain trust frameworks.

`verification_process`: Unique reference to the identity verification process as performed by the OP. Used for backtracing in case of disputes or audits. Presence of this element might be required for certain trust frameworks.

Note: While `verification_process` refers to the identity verification process at the OP, the `txn` claim refers to a particular OpenID Connect transaction in which the OP attested the user's verified identity data towards an RP.

`evidence`: JSON array containing information about the evidence the OP used to verify the user's identity as separate JSON objects. Every object contains the property `type` which determines the type of the evidence. The RP uses this information to process the `evidence` property appropriately.

Important: Implementations MUST ignore any sub-element not defined in this specification or extensions of this specification.

### Evidence

The following types of evidence are defined:

* `id_document`: Verification based on any kind of government issued identity document.
* `utility_bill`: Verification based on a utility bill.
* `qes`: Verification based on an eIDAS Qualified Electronic Signature.

#### id_document

The following elements are contained in an `id_document` evidence sub-element.

`type`: REQUIRED. Value MUST be set to "id_document".

`method`: REQUIRED. The method used to verify the ID document. Predefined values are given in  [Verification Methods](#predefined_values_vm).

`verifier`: OPTIONAL. JSON object denoting the legal entity that performed the identity verification on behalf of the OP. This object SHOULD only be included if the OP did not perform the identity verification itself. This object consists of the following properties:

* `organization`: String denoting the organization which performed the verification on behalf of the OP.
* `txn`: Identifier refering to the identity verification transaction. This transaction identifier can be resolved into transaction details during an audit.

`time`: Time stamp in ISO 8601:2004 [ISO8601-2004] `YYYY-MM-DDThh:mm:ss±hh:mm` format representing the date when this ID document was verified.

`document`: JSON object representing the ID document used to perform the identity verification. It consists of the following properties:

* `type`: REQUIRED. String denoting the type of the ID document. Standardized values are defined in [Identity Documents](#predefined_values_idd). The OP MAY use other than the predefined values in which case the RPs will either be unable to process the assertion, just store this value for audit purposes, or apply bespoken business logic to it.
* `number`: String representing the number of the identity document.
* `issuer`: JSON object containing information about the issuer of this identity document. This object consists of the following properties:
	*  `name`: REQUIRED. Designation of the issuer of the identity document.
	*  `country`: String denoting the country or organization that issued the document as ICAO 2-letter code [@!ICAO-Doc9303], e.g. "JP". ICAO 3-letter codes MAY be used when there is no corresponding ISO 2-letter code, such as "UNO".
* `date_of_issuance`: REQUIRED if this attribute exists for the particular type of document. The date the document was issued as ISO 8601:2004 `YYYY-MM-DD` format.
* `date_of_expiry`: REQUIRED if this attribute exists for the particular type of document. The date the document will expire as ISO 8601:2004 `YYYY-MM-DD` format.

#### utility_bill

The following elements are contained in a `utility_bill` evidence sub-element.

`type`: REQUIRED. Value MUST be set to "utility_bill".

`provider`: REQUIRED. JSON object identifying the respective provider that issued the bill. The object consists of the following properties:

* `name`: String designating the provider.
* All elements of the OpenID Connect `address` Claim ([@!OpenID])

`date`: String in ISO 8601:2004 `YYYY-MM-DD` format containing the date when this bill was issued.

#### qes

The following elements are contained in a `qes` evidence sub-element.

`type`: REQUIRED. Value MUST be set to "qes".

`issuer`: REQUIRED. String denoting the certification authority that issued the signer's certificate.

`serial_number`: REQUIRED. String containing the serial number of the certificate used to sign.

`created_at`: REQUIRED. The time the signature was created as ISO 8601:2004 `YYYY-MM-DDThh:mm:ss±hh:mm` format.

## claims Element {#claimselement}

The `claims` element contains the claims about the End-User which were verified by the process and according to the policies determined by the corresponding `verification` element.

The `claims` element MAY contain one or more of the following Claims as defined in Section 5.1 of the OpenID Connect specification [@!OpenID]

* `name`
* `given_name`
* `middle_name`
* `family_name`
* `birthdate`
* `address`

and the claims defined in (#userclaims).

The `claims` element MAY also contain other claims given the value of the respective claim was verified in the verification process represented by the sibling `verification` element.

Claim names MAY be annotated with language tags as specified in Section 5.2 of the OpenID Connect specification [@!OpenID].

# Requesting Verified Claims

## Requesting End-User Claims {#req_claims}

Verified Claims can be requested on the level of individual Claims about the End-User by utilizing the `claims` parameter as defined in Section 5.5 of the OpenID Connect specification [@!OpenID].

To request verified claims, the `verified_claims` element is added to the `userinfo` or the `id_token` element of the `claims` parameter.

Since `verified_claims` contains the effective Claims about the End-User in a nested `claims` element, the syntax is extended to include expressions on nested elements as follows. The `verified_claims` element includes a `claims` element, which in turn includes the desired Claims as keys with a `null` value. An example is shown in the following:

```json
{
   "userinfo":{
      "verified_claims":{
         "claims":{
            "given_name":null,
            "family_name":null,
            "birthdate":null
         }
      }
   }
}
```

Use of the `claims` parameter allows the RP to exactly select the Claims about the End-User needed for its use case. This extension therefore allows RPs to fulfill the requirement for data minimization.

RPs MAY indicate that a certain Claim is essential to the successful completion of the user journey by utilizing the `essential` field as defined in Section 5.5.1 of the OpenID Connect specification [@!OpenID]. The following example designates both given name as well as family name as being essential.

```json
{
   "userinfo":{
      "verified_claims":{
         "claims":{
            "given_name":{"essential": true},
            "family_name":{"essential": true},
            "birthdate":null
         }
      }
   }
}
```

This specification introduces the additional field `purpose` to allow an RP
to state the purpose for the transfer of a certain End-User Claim it is asking for.
The field `purpose` can be a member value of each individually requested
Claim, but a Claim cannot have more than one associated purpose.

`purpose`: OPTIONAL. String describing the purpose for obtaining a certain End-User Claim from the OP. The purpose MUST NOT be shorter than 3 characters or
longer than 300 characters. If this rule is violated, the authentication
request MUST fail and the OP returns an error `invalid_request` to the RP.
The OP MUST display this purpose in the respective user consent screen(s)
in order to inform the user about the designated use of the data to be
transferred or the authorization to be approved. If the parameter `purpose`
is not present in the request, the OP MAY display a
value that was pre-configured for the respective RP. For details on UI
localization, see (#purpose).

Example:

```json
{
   "userinfo":{
      "verified_claims":{
         "claims":{
            "given_name":{
               "essential":true,
               "purpose":"To make communication look more personal"
            },
            "family_name":{
               "essential":true
            },
            "birthdate":{
               "purpose":"To send you best wishes on your birthday"
            }
         }
      }
   }
}
```

Note: A `claims` sub-element with value `null` is interpreted as a request for all possible Claims. An example is shown in the following:

```json
{
   "userinfo":{
      "verified_claims":{
         "claims":null
      }
   }
}
```

Note: The `claims` sub-element can be omitted, which is equivalent to a `claims` element whose value is `null`.

Note: If the `claims` sub-element is empty or contains a Claim not fulfilling the requirements defined in (#claimselement), the OP will abort the transaction with an `invalid_request` error.

## Requesting Verification Data {#req_verification}

The content of the `verification` element is basically determined by the respective `trust_framework` and the Claim source's policy.

This specification also defines a way for the RP to explicitly request certain data to be present in the `verification` element. The syntax is based on the rules given in (#req_claims) and extends them for navigation into the structure of the `verification` element.

Elements within `verification` can be requested in the same way as defined in (#req_claims) by adding the respective element as shown in the following example:

```json
{
   "verified_claims":{
      "verification":{
         "time":null,
         "evidence":null
      },
      "claims":null
   }
}
```

It requests the date of the verification and the available evidence to be present in the issued assertion.

Note: The RP does not need to explicitly request the `trust_framework` field as it is a mandatory element of the `verified_claims` Claim.

The RP may also dig one step deeper into the structure and request certain data to be present within every `evidence`. A single entry is used as prototype for all entries in the result array:

```json
{
   "verified_claims":{
      "verification":{
         "time":null,
         "evidence":[
            {
               "method":null,
               "document":null
            }
         ]
      },
      "claims":null
   }
}
```

This example requests the `method` element and the `document` element for every evidence available for a certain user account.

Note: The RP does not need to explicitly request the `type` field as it is a mandatory element of any `evidence` entry.

The RP may also request certain data within the `document` element to be present. This again follows the syntax rules used above.

```json
{
   "verified_claims":{
      "verification":{
         "time":null,
         "evidence":[
            {
               "method":null,
               "document":{
                  "issuer":null,
                  "number":null,
                  "date_of_issuance":null
               }
            }
         ]
      },
      "claims":null
   }
}
```

Note: The RP does not need to explicitly request the `type` field as it is a mandatory element of any `document` entry.

It is at the discretion of the OP to decide whether the requested verification data is provided to the RP. It is also at the discretion of the OP to provide more verification data than has been requested by the RP.

## Defining constraints on Verification Data {#constraintedclaims}

The RP MAY express requirements regarding the elements in the `verification` sub-element.

This, again, requires an extension to the syntax as defined in Section 5.5 of the OpenID Connect specification [@!OpenID] due to the nested nature of the `verified_claims` claim.

Section 5.5.1 of the OpenID Connect specification [@!OpenID] defines a query syntax that allows for the member value of the Claim being requested to be a JSON object with additional information/constraints on the Claim. For doing so it defines three members (`essential`, `value` and `values`) with special query
meanings and allows for other special members to be defined (while stating that any members that are not understood must be ignored).

This specification re-uses that mechanism and introduces a new such member `max_age` (see below).

To start with, the RP MAY limit the possible values of the elements `trust_framework`, `evidence/type`, `evidence/method`, and `evidence/document/type` by utilizing the `value` or `values` fields.

The following example shows that the RP wants to obtain an attestation based on AML and limited to users who were identified in a bank branch in person using government issued ID documents.

```json
{
   "userinfo":{
      "verified_claims":{
         "verification":{
            "trust_framework":{
               "value":"de_aml"
            },
            "evidence":[
               {
                  "type":{
                     "value":"id_document"
                  },
                  "method":{
                     "value":"pipp"
                  },
                  "document":{
                     "type":{
                        "values":[
                           "idcard",
                           "passport"
                        ]
                     }
                  }
               }
            ]
         },
         "claims":null
      }
   }
}
```

The RP MAY also express a requirement regarding the age of the verification data, i.e., the time elapsed since the verification process asserted in the `verification` element has taken place.

This specification therefore defines a new member `max_age`.

`max_age`: OPTIONAL. JSON number value only applicable to Claims that contain dates or timestamps. It defines the maximum time (in seconds) to be allowed to elapse since the value of the date/timestamp up to the point in time of the request. The OP should make the calculation of elapsed time starting from the last valid second of the date value. The following is an example of a request for Claims where the verification process of the data is not allowed to be older than 63113852 seconds.

The following is an example:

```json
{
   "userinfo":{
      "verified_claims":{
         "verification":{
            "time":{
               "max_age":63113852
            }
         },
         "claims":null
      }
   }
}
```

The OP SHOULD try to fulfill this requirement. If the verification data of the user is older than the requested `max_age`, the OP MAY attempt to refresh the user’s verification by sending her through an online identity verification process, e.g. by utilizing an electronic ID card or a video identification approach.

If the OP is unable to fulfill any of the requirements stated in this section (even in case it is marked as being `essential`), it will provide the RP with the data available and the RP may decide how to use the data. The OP MUST NOT return an error in case it cannot return all Claims requested as essential Claims.

# Examples

The following sections show examples of `verified_claims`.

The first and second sections show JSON snippets of the general identity assurance case, where the RP is provided with verification evidence for different verification methods along with the actual Claims about the End-User.

The third section illustrates how the contents of this object could look like in case of a notified eID system under eIDAS, where the OP does not need to provide evidence of the identity verification process to the RP.

Subsequent sections contain examples for using the `verified_claims` Claim on different channels and in combination with other (unverified) Claims.

## id_document

```JSON
{
   "verified_claims":{
      "verification":{
         "trust_framework":"de_aml",
         "time":"2012-04-23T18:25:43.511+01",
         "verification_process":"676q3636461467647q8498785747q487",
         "evidence":[
            {
               "type":"id_document",
               "method":"pipp",
               "document":{
                  "type":"idcard",
                  "issuer":{
                     "name":"Stadt Augsburg",
                     "country":"DE"
                  },
                  "number":"53554554",
                  "date_of_issuance":"2012-04-23",
                  "date_of_expiry":"2022-04-22"
               }
            }
         ]
      },
      "claims":{
         "given_name":"Max",
         "family_name":"Meier",
         "birthdate":"1956-01-28",
         "place_of_birth":{
            "country":"DE",
            "locality":"Musterstadt"
         },
         "nationalities":[
            "DE"
         ],
         "address":{
            "locality":"Maxstadt",
            "postal_code":"12344",
            "country":"DE",
            "street_address":"An der Sanddüne 22"
         }
      }
   }
}
```

## id_document + utility bill

```JSON
{
   "verified_claims":{
      "verification":{
         "trust_framework":"de_aml",
         "time":"2012-04-23T18:25:43.511+01",
         "verification_process":"676q3636461467647q8498785747q487",
         "evidence":[
            {
               "type":"id_document",
               "method":"pipp",
               "document":{
                  "type":"de_erp_replacement_idcard",
                  "issuer":{
                     "name":"Stadt Augsburg",
                     "country":"DE"
                  },
                  "number":"53554554",
                  "date_of_issuance":"2012-04-23",
                  "date_of_expiry":"2022-04-22"
               }
            },
            {
               "type":"utility_bill",
               "provider":{
                  "name":"Stadtwerke Musterstadt",
                  "country":"DE",
                  "region":"Thüringen",
                  "street_address":"Energiestrasse 33"
               },
               "date":"2013-01-31"
            }
         ]
      },
      "claims":{
         "given_name":"Max",
         "family_name":"Meier",
         "birthdate":"1956-01-28",
         "place_of_birth":{
            "country":"DE",
            "locality":"Musterstadt"
         },
         "nationalities":[
            "DE"
         ],
         "address":{
            "locality":"Maxstadt",
            "postal_code":"12344",
            "country":"DE",
            "street_address":"An der Sanddüne 22"
         }
      }
   }
}
```

## Notified eID system (eIDAS)

```JSON
{
   "verified_claims":{
      "verification":{
         "trust_framework":"eidas_ial_substantial"
      },
      "claims":{
         "given_name":"Max",
         "family_name":"Meier",
         "birthdate":"1956-01-28",
         "place_of_birth":{
            "country":"DE",
            "locality":"Musterstadt"
         },
         "nationalities":[
            "DE"
         ],
         "address":{
            "locality":"Maxstadt",
            "postal_code":"12344",
            "country":"DE",
            "street_address":"An der Sanddüne 22"
         }
      }
   }
}
```

## Verified Claims in UserInfo Response

### Request

In this example we assume the RP uses the `scope` parameter to request the email address and, additionally, the `claims` parameter, to request verified Claims.

The scope value is: `scope=openid email`

The value of the `claims` parameter is:

```json
{
   "userinfo":{
       "verified_claims":{
         "claims":{
            "given_name":null,
            "family_name":null,
            "birthdate":null
         }
      }
   }
}
```

### UserInfo Response

The respective UserInfo response would be

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
   "sub":"248289761001",
   "email":"janedoe@example.com",
   "email_verified":true,
   "verified_claims":{
      "verification":{
         "trust_framework":"de_aml",
         "time":"2012-04-23T18:25:43.511+01",
         "verification_process":"676q3636461467647q8498785747q487",
         "evidence":[
            {
               "type":"id_document",
               "method":"pipp",
               "document":{
                  "type":"idcard",
                  "issuer":{
                     "name":"Stadt Augsburg",
                     "country":"DE"
                  },
                  "number":"53554554",
                  "date_of_issuance":"2012-04-23",
                  "date_of_expiry":"2022-04-22"
               }
            }
         ]
      },
      "claims":{
         "given_name":"Max",
         "family_name":"Meier",
         "birthdate":"1956-01-28"
      }
   }
}
```

## Verified Claims in ID Tokens

### Request

In this case, the RP requests verified Claims along with other Claims about the End-User in the `claims` parameter and allocates the response to the ID Token (delivered from the token endpoint in case of grant type `authorization_code`).

The `claims` parameter value is

```json
{
   "id_token":{
      "email":null,
      "preferred_username":null,
      "picture":null,
      "verified_claims":{
         "claims":{
            "given_name":null,
            "family_name":null,
            "birthdate":null
         }
      }
   }
}
```

### ID Token

The respective ID Token could be

```json
{
   "iss":"https://server.example.com",
   "sub":"24400320",
   "aud":"s6BhdRkqt3",
   "nonce":"n-0S6_WzA2Mj",
   "exp":1311281970,
   "iat":1311280970,
   "auth_time":1311280969,
   "acr":"urn:mace:incommon:iap:silver",
   "email":"janedoe@example.com",
   "preferred_username":"j.doe",
   "picture":"http://example.com/janedoe/me.jpg",
   "verified_claims":{
      "verification":{
         "trust_framework":"de_aml",
         "time":"2012-04-23T18:25:43.511+01",
         "verification_process":"676q3636461467647q8498785747q487",
         "evidence":[
            {
               "type":"id_document",
               "method":"pipp",
               "document":{
                  "type":"idcard",
                  "issuer":{
                     "name":"Stadt Augsburg",
                     "country":"DE"
                  },
                  "number":"53554554",
                  "date_of_issuance":"2012-04-23",
                  "date_of_expiry":"2022-04-22"
               }
            }
         ]
      },
      "claims":{
         "given_name":"Max",
         "family_name":"Meier",
         "birthdate":"1956-01-28"
      }
   }
}
```

## Aggregated Claims

Note: Line breaks for display purposes only.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
   "iss":"https://server.example.com",
   "sub":"248289761001",
   "email":"janedoe@example.com",
   "email_verified":true,
   "_claim_names":{
      "verified_claims":"src1"
   },
   "_claim_sources":{
      "src1":{
      "JWT":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL3NlcnZlci5vdGh
      lcm9wLmNvbSIsInZlcmlmaWVkX2NsYWltcyI6eyJ2ZXJpZmljYXRpb24iOnsidHJ1c3RfZnJhbWV3b3
      JrIjoiZWlkYXNfaWFsX3N1YnN0YW50aWFsIn0sImNsYWltcyI6eyJnaXZlbl9uYW1lIjoiTWF4IiwiZ
      mFtaWx5X25hbWUiOiJNZWllciIsImJpcnRoZGF0ZSI6IjE5NTYtMDEtMjgifX19.M8tTKxzj5LBgqGj
      UAzFooEiCPJ4wcZVQDrnW5_ooAG4"
      }
   }
}
```

## Distributed Claims

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
   "iss":"https://server.example.com",
   "sub":"248289761001",
   "email":"janedoe@example.com",
   "email_verified":true,
   "_claim_names":{
      "verified_claims":"src1"
   },
   "_claim_sources":{
      "src1":{
         "endpoint":"https://server.yetanotherop.com/claim_source",
         "access_token":"ksj3n283dkeafb76cdef"
      }
   }
}
```

# OP Metadata {#opmetadata}

The OP advertises its capabilities with respect to verified Claims in its openid-configuration (see [@!OpenID-Discovery]) using the following new elements:

`verified_claims_supported`: Boolean value indicating support for `verified_claims`, i.e. the OpenID Connect for Identity Assurance extension.

`trust_frameworks_supported`: JSON array containing all supported trust frameworks.

`evidence_supported`: JSON array containing all types of identity evidence the OP uses.

`id_documents_supported`: JSON array containing all identity documents utilized by the OP for identity verification.

`id_documents_verification_methods_supported`: JSON array containing the ID document verification methods the OP supports as defined in (#verification).

`claims_in_verified_claims_supported`: JSON array containing all claims supported within `verified_claims`.

This is an example openid-configuration snippet:

```json
{
...
   "verified_claims_supported":true,
   "trust_frameworks_supported":[
     "nist_800_63A_ial_2",
     "nist_800_63A_ial_3"
   ],
   "evidence_supported":[
      "id_document",
      "utility_bill",
      "qes"
   ],
   "id_documents_supported":[
       "idcard",
       "passport",
       "driving_permit"
   ],
   "id_documents_verification_methods_supported":[
       "pipp",
       "sripp",
       "eid"
   ],
   "claims_in_verified_claims_supported":[
      "given_name",
      "family_name",
      "birthdate",
      "place_of_birth",
      "nationalities",
      "address"
   ],
...
}
```

The OP MUST support the `claims` parameter and needs to publish this in its openid-configuration using the `claims_parameter_supported` element.

# Transaction-specific Purpose {#purpose}

This specification introduces the request parameter `purpose` to allow an RP
to state the purpose for the transfer of user data it is asking for.

`purpose`: OPTIONAL. String describing the purpose for obtaining certain user data from the OP. The purpose MUST NOT be shorter than 3 characters and MUST NOT be longer than 300 characters. If these rules are violated, the authentication request MUST fail and the OP returns an error `invalid_request` to the RP.

The OP MUST display this purpose in the respective user consent screen(s) in order to inform the user about the designated use of the data to be transferred or the authorization to be approved.

In order to ensure a consistent UX, the RP MAY send the `purpose` in a certain language and request the OP to use the same language using the `ui_locales` parameter.

If the parameter `purpose` is not present in the request, the OP MAY utilize a description that was pre-configured for the respective RP.

Note: In order to prevent injection attacks, the OP MUST escape the text appropriately before it will be shown in a user interface. The OP MUST expect special characters in the URL decoded purpose text provided by the RP. The OP MUST ensure that any special characters in the purpose text cannot be used to inject code into the web interface of the OP (e.g., cross-site scripting, defacing). Proper escaping MUST be applied by the OP. The OP SHALL NOT remove characters from the purpose text to this end.

# Privacy Consideration {#Privacy}

OP and RP MUST establish a legal basis before exchanging any personally identifiable information. It can be established upfront or in the course of the OpenID process.

# Security Considerations {#Security}

The integrity and authenticity of the issued assertions MUST be ensured in order to prevent identity spoofing. The Claims source MUST therefore cryptographically sign all assertions.

The confidentiality of all user data exchanged between the protocol parties MUST be ensured using suitable methods at transport or application layer.

# Predefined Values {#predefined_values}

## Trust Frameworks {#predefined_values_tf}

This section defines trust framework identifiers for use with this specification.

| Identifier | Definition|
|:------------|:-----------|
|`de_aml`    |The OP verifies and maintains user identities in conformance with the German Anti-Money Laundering Law.|
|`eidas_ial_substantial`| The OP is able to attest user identities in accordance with the EU regulation No 910/2014 (eIDAS) at the identitfication assurance level "Substantial".|
|`eidas_ial_high`|The OP is able to attest user identities in accordance with the EU regulation No 910/2014 (eIDAS) at the identitfication assurance level "High".|
|`nist_800_63A_ial_2`|The OP is able to attest user identities in accordance with the NIST Special Publication 800-63A at the Identity Assurance Level 2.|
|`nist_800_63A_ial_3`|The OP is able to attest user identities in accordance with the NIST Special Publication 800-63A at the Identity Assurance Level 3.|
|`jp_aml`|The OP verifies and maintains user identities in conformance with the Japanese Act on Prevention of Transfer of Criminal Proceeds.|
|`jp_mpiupa`|The OP verifies and maintains user identities in conformance with the Japanese Act for Identification, etc. by Mobile Voice Communications Carriers of Their Subscribers, etc. and for Prevention of Improper Use of Mobile Voice Communications Services.|

## Identity Documents {#predefined_values_idd}

This section defines identity document identifiers for use with this specification.

| Identifier | Definition|
|:------------|:-----------|
|`idcard`|An identity document issued by a country's government for the purpose of identifying a citizen.|
|`passport`|A passport is a travel document, usually issued by a country's government, that certifies the identity and nationality of its holder primarily for the purpose of international travel.[@?OxfordPassport]|
|`driving_permit`|Official document permitting an individual to operate motorized vehicles. In the absence of a formal identity document, a driver's license may be accepted in many countries for identity verification.|
|`de_idcard_foreigners`|ID Card issued by the German government to foreign nationals.|
|`de_emergency_idcard`|ID Card issued by the German government to foreign nationals as passports replacement.|
|`de_erp`|Electronic Resident Permit issued by the German government to foreign nationals.|
|`de_erp_replacement_idcard`|Electronic Resident Permit issued by the German government to foreign nationals as replacement for another identity document.|
|`de_idcard_refugees`|ID Card issued by the German government to refugees as passports replacement.|
|`de_idcard_apatrids`|ID Card issued by the German government to apatrids as passports replacement.|
|`de_certificate_of_suspension_of_deportation`|An identity document issued to refugees in case of suspension of deportation that are marked as "ID card replacement".|
|`de_permission_to_reside`|Permission to reside issued by the German government to foreign nationals appliying for asylum.|
|`de_replacement_idcard`|ID Card replacement document issued by the German government to foreign nationals. (see Act on the Residence, Economic Activity and Integration of Foreigners in the Federal Territory, Residence Act, Appendix D1 ID Card replacement according to § 48 Abs. 2 i.V.m. § 78a Abs. 4)|
|`jp_drivers_license`| Japanese driver's license.|
|`jp_residency_card_for_foreigner`| Japanese residence card for foreigners.|
|`jp_individual_number_card`| Japanese national ID card.|
|`jp_permanent_residency_card_for_foreigner`| Japanese special residency card for foreigners to permit permanently resident.|
|`jp_health_insurance_card`| Japanese health and insurance card.|
|`jp_residency_card`| Japanese residency card.|

## Verification Methods {#predefined_values_vm}

This section defines verification method identifiers for use with this specification.

| Identifier | Definition          |
|:------------|---------------------|
|`pipp`|Physical In-Person Proofing.|
|`sripp`|Supervised remote In-Person Proofing.|
|`eid`|Online verification of an electronic ID card.|
|`uripp`|Unsupervised remote in-person proofing with video capture of the ID document, user self-portrait video and liveness checks.|

# JSON Schema {#json_schema}

This section contains the JSON Schema of assertions containing the `verified_claims` claim.

```JSON
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "definitions":{
    "qes":{
      "type":"object",
      "properties":{
        "type":{
          "type":"string",
          "enum":[
            "qes"
          ]
        },
        "issuer":{
          "type":"string"
        },
        "serial_number":{
          "type":"string"
        },
        "created_at":{
          "type":"string",
          "format":"date-time"
        }
      },
      "required": ["type","issuer","serial_number","issued_at"]
    },
    "utility_bill":{
      "type":"object",
      "properties":{
        "type":{
          "type":"string",
          "enum":[
            "utility_bill"
          ]
        },
        "provider":{
          "type":"object",
          "properties":{
            "name":{
              "type":"string"
            },
            "formatted":{
              "type":"string"
            },
            "street_address":{
              "type":"string"
            },
            "locality":{
              "type":"string"
            },
            "region":{
              "type":"string"
            },
            "postal_code":{
              "type":"string"
            },
            "country":{
              "type":"string"
            }
          }
        },
        "date":{
          "type":"string",
          "format":"date"
        }
      },
      "required": ["type","provider","date"]
    },
    "id_document":{
      "type":"object",
      "properties":{
        "type":{
          "type":"string",
          "enum":[
            "id_document"
          ]
        },
        "method":{
          "type":"string",
          "enum":["pipp","sripp","eid","uripp"]
        },
        "verifier":{
          "type":"object",
          "properties":{
            "organization":{
              "type":"string"
            },
            "txn":{
              "type":"string"
            }
          }
        },
        "time":{
          "type":"string",
          "format":"date-time"
        },
        "document":{
          "type":"object",
          "properties":{
            "type":{
              "type":"string",
              "enum":[
                "idcard",
                "passport",
                "driving_permit",
                "de_idcard_foreigners",
                "de_emergency_idcard",
                "de_erp",
                "de_erp_replacement_idcard",
                "de_idcard_refugees",
                "de_idcard_apatrids",
                "de_certificate_of_suspension_of_deportation",
                "de_permission_to_reside",
                "de_replacement_idcard",
                "jp_drivers_license",
                "jp_residency_card_for_foreigner",
                "jp_individual_number_card",
                "jp_permanent_residency_card_for_foreigner",
                "jp_health_insurance_card",
                "jp_residency_card"
              ]
            },
            "number":{
              "type":"string"
            },
            "issuer":{
              "type":"object",
              "properties":{
                "name":{
                  "type":"string"
                },
                "country":{
                  "type":"string"
                }
              }
            },
            "date_of_issuance":{
              "type":"string",
              "format":"date"
            },
            "date_of_expiry":{
              "type":"string",
              "format":"date"
            }
          }
        }
      },
      "required":[
        "type",
        "method",
        "document"
      ]
    }
  },
  "type":"object",
  "properties":{
    "verified_claims":{
      "type":"object",
      "properties":{
        "verification":{
          "type":"object",
          "properties":{
            "trust_framework":{
              "type":"string",
              "enum":[
                "de_aml",
                "eidas_ial_substantial",
                "eidas_ial_hig",
                "nist_800_63A_ial_2",
                "nist_800_63A_ial_3",
                "jp_aml",
                "jp_mpiupa"
              ]
            },
            "time":{
              "type":"string",
              "format":"time"
            },
            "verification_process":{
              "type":"string"
            },
            "evidence":{
              "type":"array",
              "minItems": 1,
              "items":{
                "oneOf":[
                  {
                    "$ref":"#/definitions/id_document"
                  },
                  {
                    "$ref":"#/definitions/utility_bill"
                  },
                  {
                    "$ref":"#/definitions/qes"
                  }
                ]
              }
            }
          },
          "required":["trust_framework"],
          "additionalProperties": false
        },
        "claims":{
          "type":"object",
          "minProperties": 1
        }
      },
      "required":["verification","claims"],
      "additionalProperties": false
    },
    "txn": {"type": "string"}
  },
  "required":["verified_claims"]
}
```
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
    <author initials="B." surname="de Medeiros" fullname="Breno de Medeiros">
      <organization>Google</organization>
    </author>
    <author initials="E." surname="Jay" fullname="Edmund Jay">
      <organization> Illumila </organization>
    </author>
   <date day="8" month="Nov" year="2014"/>
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

<reference anchor="ISO8601-2004" target="http://www.iso.org/iso/catalogue_detail?csnumber=40874">
	<front>
	  <title>ISO 8601:2004. Data elements and interchange formats - Information interchange -
	  Representation of dates and times</title>
	  <author surname="International Organization for Standardization">
	    <organization abbrev="ISO">International Organization for
	    Standardization</organization>
	  </author>
	  <date year="2004" />
	</front>
</reference>

<reference anchor="ISO3166-1" target="https://www.iso.org/standard/63545.html">
	<front>
	  <title>ISO 3166-1:1997. Codes for the representation of names of
	  countries and their subdivisions -- Part 1: Country codes</title>
	  <author surname="International Organization for Standardization">
	    <organization abbrev="ISO">International Organization for
	    Standardization</organization>
	  </author>
	  <date year="2013" />
	</front>
</reference>

<reference anchor="ISO3166-3" target="https://www.iso.org/standard/63547.html">
	<front>
	  <title>ISO 3166-1:2013. Codes for the representation of names of countries and their subdivisions -- Part 3: Code for formerly used names of countries</title>
	  <author surname="International Organization for Standardization">
	    <organization abbrev="ISO">International Organization for
	    Standardization</organization>
	  </author>
	  <date year="2013" />
	</front>
</reference>

<reference anchor="OxfordPassport" target="http://www.oxfordreference.com/view/10.1093/acref/9780199290543.001.0001/acref-9780199290543-e-1616">
  <front>
    <title>The New Oxford Companion to Law. ISBN 9780199290543.</title>
    <author initials="P" surname="Cane" fullname="P. Cane">
    </author>
    <author initials="Mary F." surname="Conaghan" fullname="J. Conaghan">
    </author>
   <date year="2008"/>
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

# Acknowledgements {#Acknowledgements}

The following people at yes.com and partner companies contributed to the concept described in the initial contribution to this specification: Karsten Buch, Lukas Stiebig, Sven Manz, Waldemar Zimpfer, Willi Wiedergold, Fabian Hoffmann, Daniel Keijsers, Ralf Wagner, Sebastian Ebling, Peter Eisenhofer.

We would like to thank Takahiko Kawasaki, Sebastian Ebling, Marcos Sanz, Tom Jones, Mike Pegman,
Michael B. Jones, and Jeff Lombardo for their valuable feedback that helped to evolve this specification.

# Notices

Copyright (c) 2019 The OpenID Foundation.

The OpenID Foundation (OIDF) grants to any Contributor, developer, implementer, or other interested party a non-exclusive, royalty free, worldwide copyright license to reproduce, prepare derivative works from, distribute, perform and display, this Implementers Draft or Final Specification solely for the purposes of (i) developing specifications, and (ii) implementing Implementers Drafts and Final Specifications based on such documents, provided that attribution be made to the OIDF as the source of the material, but that such attribution does not indicate an endorsement by the OIDF.

The technology described in this specification was made available from contributions from various sources, including members of the OpenID Foundation and others. Although the OpenID Foundation has taken steps to help ensure that the technology is available for distribution, it takes no position regarding the validity or scope of any intellectual property or other rights that might be claimed to pertain to the implementation or use of the technology described in this specification or the extent to which any license under such rights might or might not be available; neither does it represent that it has made any independent effort to identify any such rights. The OpenID Foundation and the contributors to this specification make no (and hereby expressly disclaim any) warranties (express, implied, or otherwise), including implied warranties of merchantability, non-infringement, fitness for a particular purpose, or title, related to this specification, and the entire risk as to implementing this specification is assumed by the implementer. The OpenID Intellectual Property Rights policy requires contributors to offer a patent promise not to assert certain patent claims against other contributors and against implementers. The OpenID Foundation invites any interested party to bring to its attention any copyrights, patents, patent applications, or other proprietary rights that may cover technology that may be required to practice this specification.

# Document History

   [[ To be removed from the final specification ]]
   
   -09
   
   * integrated source into single md file
   * fixed typos


   -08
   
   * added `uripp` verification method
   * small fixes to examples
   
   -07
   
   * fixed typos
   * changed `nationality` String claim to `nationalities` String array claim
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
   *  added several examples (ID Token vs UserInfo, unverified & verified claims, aggregated & distributed claims)
   *  incorporated text proposal of Marcos Sanz regarding max_age
   *  added IANA registration for new error code `unable_to_meet_requirement`

