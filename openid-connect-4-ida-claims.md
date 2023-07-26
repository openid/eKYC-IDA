%%%
title = "OpenID Connect for Identity Assurance Claims Registration 1.0 draft"
abbrev = "openid-connect-4-ida-claims-1_0"
ipr = "none"
workgroup = "eKYC-IDA"
keyword = ["security", "openid", "identity assurance", "ekyc", "claims"]

[seriesInfo]
name = "Internet-Draft"

value = "openid-connect-4-ida-claims-1_0-00"

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

This specification defines an extension of OpenID Connect that registers new JWT claims about End-Users. This extension defines new claims relating to the identity of a natural person that were originally defined within earlier drafts of OpenID Connect for Identity Assurance. The work and the preceding drafts are the work of the eKYC and Identity Assurance working group of the OpenID Foundation.

{mainmatter}

# Introduction {#Introduction}

This specification defines additional JWT claims about the natural person.  The claims defined MAY be used in various contexts including an id_token. 

# Scope

This specification only defines claims to be maintained in the IANA "JSON Web Token Claims Registry" established by [@!RFC7519].  These claims SHOULD be used in any context that needs to describe these characteristics of the end-user in a JWT as per [@RFC7519].

# Claims {#claims}

## Additional Claims about End-Users {#userclaims}

This specification defines the following Claims for conveying End-User data in addition to the Claims defined in the OpenID Connect specification [@!OpenID] and the OpenID Connect for Identity Assurance specification [@!OpenID4IDA] and in any other context that a JWT (as per [@RFC7519]) may be used:

| Claim | Type | Description |
|:------|:-----|:------------|
|`place_of_birth`| JSON object | End-User’s place of birth. The value of this member is a JSON structure containing some or all of the following members:|
| | |`country`: String representing country in [@!ISO3166-1] Alpha-2  or [@!ISO3166-3] syntax.|
| | |`region`: String representing state, province, prefecture, or region component. This field might be required in some jurisdictions.|
| | |`locality`: String representing city or locality component.|
|`nationalities`| array | End-User’s nationalities using ICAO 3-letter codes [@!ICAO-Doc9303], 2-letter ICAO codes MAY be used in some circumstances for compatibility reasons.|
|`birth_family_name`| string | End-User’s family name(s) when they were born, or at least from the time they were a child. This term can be used by a person who changes the family name later in life for any reason. Note that in some cultures, people can have multiple family names or no family name; all can be present, with the names being separated by space characters.|
|`birth_given_name`| string | End-User’s given name(s) when they were born, or at least from the time they were a child. This term can be used by a person who changes the given name later in life for any reason. Note that in some cultures, people can have multiple given names; all can be present, with the names being separated by space characters.|
|`birth_middle_name`| string | End-User’s middle name(s) when they were born, or at least from the time they were a child. This term can be used by a person who changes the middle name later in life for any reason. Note that in some cultures, people can have multiple middle names; all can be present, with the names being separated by space characters. Also note that in some cultures, middle names are not used.|
|`salutation`| string | End-User’s salutation|
|`title`| string | End-User’s title|
|`msisdn`| string | End-User’s mobile phone number formatted according to ITU-T recommendation [@!E.164]|
|`also_known_as`| string | Stage name, religious name or any other type of alias/pseudonym with which a person is known in a specific context besides their legal name.|

## Extended address Claim

This specification extends the `address` Claim as defined in [@!OpenID] by another sub field containing the country as ISO code.

`country_code`: OPTIONAL. country part of an address represented using an ISO 3-letter code [@!ISO3166-3], e.g., "USA" or "JPN". 2-letter ISO codes [@!ISO3166-1] MAY be used for compatibility reasons. `country_code` MAY be used as alternative to the existing `country` field.

## Examples

This section contains JSON snippets showing examples of end-user claims described in this document.

```
{
"place_of_birth": {
  "country": "GB",
  "locality": "London"
  }  
}
```

```
{
"nationalities": ["GB", "SL"]
}
```

```
{
"birth_family_name": "Elba"
}
```

```
{
"birth_given_name": "Idrissa"
}
```

```
{
"birth_middle_name": "Akuna"
}
```

```
{
"salutation": "Mr"
}
```

```
{
"salutation": "Dr"
}
```

```
{
"msisdn": "1999550123"
}
```

```
{
"also_known_as": "DJ Big Driis"
}
```

```
"address": {
  "locality": "Leavesden",
  "postal_code": "WD25 7LR",
  "country": "United Kingdom",
  "street_address": "4 Privet Drive",
  "country_code": "GBR"
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

# IANA Considerations

## JSON Web Token Claims Registration

This specification requests registration of the following value in the IANA "JSON Web Token Claims Registry" established by [@!RFC7519].

### Registry Contents

Claim Name:
: `place_of_birth`

Claim Description:
: A structured Claim representing the End-User’s place of birth.

Change Controller:
: eKYC and Identity Assurance Working Group - openid-specs-ekyc-ida@lists.openid.net

Specification Document(s):
: Section [Claims](#claims) of this document

Claim Name:
: `nationalities`

Claim Description:
: String array representing the End-User’s nationalities.

Change Controller:
: eKYC and Identity Assurance Working Group - openid-specs-ekyc-ida@lists.openid.net

Specification Document(s):
: Section [Claims](#claims) of this document

Claim Name:
: `birth_family_name`

Claim Description:
: Family name(s) someone has when they were born, or at least from the time they were a child. This term can be used by a person who changes the family name(s) later in life for any reason. Note that in some cultures, people can have multiple family names or no family name; all can be present, with the names being separated by space characters.

Change Controller:
: eKYC and Identity Assurance Working Group - openid-specs-ekyc-ida@lists.openid.net

Specification Document(s):
: Section [Claims](#claims) of this document

Claim Name:
: `birth_given_name`

Claim Description:
: Given name(s) someone has when they were born, or at least from the time they were a child. This term can be used by a person who changes the given name later in life for any reason. Note that in some cultures, people can have multiple given names; all can be present, with the names being separated by space characters.

Change Controller:
: eKYC and Identity Assurance Working Group - openid-specs-ekyc-ida@lists.openid.net

Specification Document(s):
: Section [Claims](#claims) of this document

Claim Name:
: `birth_middle_name`

Claim Description:
: Middle name(s) someone has when they were born, or at least from the time they were a child. This term can be used by a person who changes the middle name later in life for any reason. Note that in some cultures, people can have multiple middle names; all can be present, with the names being separated by space characters. Also note that in some cultures, middle names are not used.

Change Controller:
: eKYC and Identity Assurance Working Group - openid-specs-ekyc-ida@lists.openid.net

Specification Document(s):
: Section [Claims](#claims) of this document

Claim Name:
: `salutation`

Claim Description:
: End-User’s salutation, e.g., “Mr.”

Change Controller:
: eKYC and Identity Assurance Working Group - openid-specs-ekyc-ida@lists.openid.net

Specification Document(s):
: Section [Claims](#claims) of this document

Claim Name:
: `title`

Claim Description:
: End-User’s title, e.g., “Dr.”

Change Controller:
: eKYC and Identity Assurance Working Group - openid-specs-ekyc-ida@lists.openid.net

Specification Document(s):
: Section [Claims](#claims) of this document

Claim Name:
: `msisdn`

Claim Description:
: End-User’s mobile phone number formatted according to ITU-T recommendation [@!E.164]

Change Controller:
: eKYC and Identity Assurance Working Group - openid-specs-ekyc-ida@lists.openid.net

Specification Document(s):
: Section [Claims](#claims) of this document

Claim Name:
: `also_known_as`

Claim Description:
: Stage name, religious name or any other type of alias/pseudonym with which a person is known in a specific context besides its legal name.

Change Controller:
: eKYC and Identity Assurance Working Group - openid-specs-ekyc-ida@lists.openid.net

Specification Document(s):
: Section [Claims](#claims) of this document

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

