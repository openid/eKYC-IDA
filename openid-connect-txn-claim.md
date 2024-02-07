%%%
title = "OpenID Connect txn claim 1.0 draft"
abbrev = "openid-connect-txn-claim-1_0"
ipr = "none"
workgroup = "eKYC-IDA"
keyword = ["security", "openid", "identity assurance", "claims"]

[seriesInfo]
name = "Internet-Draft"

value = "openid-connect-txn-claim-1_0-00"

status = "standard"

[[author]]
initials="D."
surname="Postnikov"
fullname="Dima Postnikov"
organization="ConnectID"
    [author.address]
    email = "dima@postnikov.net"

%%%

.# Abstract

This specification defines an extension of OpenID Connect that defines a use of txn claim.

.# Foreword

The OpenID Foundation (OIDF) promotes, protects and nurtures the OpenID community and technologies. As a non-profit international standardizing body, it is comprised by over 160 participating entities (workgroup participant). The work of preparing implementer drafts and final international standards is carried out through OIDF workgroups in accordance with the OpenID Process. Participants interested in a subject for which a workgroup has been established have the right to be represented in that workgroup. International organizations, governmental and non-governmental, in liaison with OIDF, also take part in the work. OIDF collaborates closely with other standardizing bodies in the related fields.

Final drafts adopted by the Workgroup through consensus are circulated publicly for the public review for 60 days and for the OIDF members for voting. Publication as an OIDF Standard requires approval by at least 50% of the members casting a vote. There is a possibility that some of the elements of this document may be subject to patent rights. OIDF shall not be held responsible for identifying any or all such patent rights.

# Introduction {#Introduction}

Strong identity verification typically requires the participants to keep an audit trail of the whole process.
The `txn` claim as defined in [@!RFC8417] is used in the context of this extension to build audit trails across the parties involved in an OpenID Connect transaction.

.# Warning

This document is not an OIDF International Standard. It is distributed for
review and comment. It is subject to change without notice and may not be
referred to as an International Standard.

Recipients of this draft are invited to submit, with their comments,
notification of any relevant patent rights of which they are aware and to
provide supporting documentation.

.# Notational conventions

The keywords "shall", "shall not", "should", "should not", "may", and "can" in
this document are to be interpreted as described in ISO Directive Part 2
[@!ISODIR2]. These keywords are not used as dictionary terms such that any
occurrence of them shall be interpreted as keywords and are not to be
interpreted with their natural language meanings.

{mainmatter}

# Scope

Add specification scope

# Normative references

See section 6 for normative references.

# Terms and definitions
No terms and definitions are listed in this document.

# txn request

The RP requests this claim like any other claim via the `claims` parameter or as part of a default claim set identified by a scope value, for example:

```
"txn": null
```

# txn issuance, response and processing

The OP generates txn claim as a unique identifier, for example:

```
{
  "txn": "2c6fb585-d51b-465a-9dca-b8cd22a11451"
}
```

If the OP issues a `txn`, it shall maintain a corresponding audit trail, which at least consists of the following details:

* the transaction ID,
* the transaction date and time,
* the transaction parties,
* the authentication method employed, and
* the transaction details (e.g., the set of claims returned).

This transaction data MUST be stored as long as it is required to store transaction data for auditing purposes by the respective regulation or ecoysystem governance rules and procedures.

The `txn` value MUST allow an RP to obtain these transaction details if needed.

Note: The mechanism to obtain the transaction details from the OP and their format is out of scope of this specification.


{backmatter}

<reference anchor="ISODIR2" target="https://www.iso.org/sites/directives/current/part2/index.xhtml">
<front>
<title>ISO/IEC Directives Part 2 - </title>
    <author fullname="International Organization for Standardization">
      <organization></organization>
    </author>
</front>
</reference>

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

# Acknowledgements {#Acknowledgements}

We would like to thank Mark Haine, Andres Uribe for their valuable feedback and contributions that helped to evolve this specification.

# Notices

Copyright (c) 2023 The OpenID Foundation.

The OpenID Foundation (OIDF) grants to any Contributor, developer, implementer, or other interested party a non-exclusive, royalty free, worldwide copyright license to reproduce, prepare derivative works from, distribute, perform and display, this Implementers Draft or Final Specification solely for the purposes of (i) developing specifications, and (ii) implementing Implementers Drafts and Final Specifications based on such documents, provided that attribution be made to the OIDF as the source of the material, but that such attribution does not indicate an endorsement by the OIDF.

The technology described in this specification was made available from contributions from various sources, including members of the OpenID Foundation and others. Although the OpenID Foundation has taken steps to help ensure that the technology is available for distribution, it takes no position regarding the validity or scope of any intellectual property or other rights that might be claimed to pertain to the implementation or use of the technology described in this specification or the extent to which any license under such rights might or might not be available; neither does it represent that it has made any independent effort to identify any such rights. The OpenID Foundation and the contributors to this specification make no (and hereby expressly disclaim any) warranties (express, implied, or otherwise), including implied warranties of merchantability, non-infringement, fitness for a particular purpose, or title, related to this specification, and the entire risk as to implementing this specification is assumed by the implementer. The OpenID Intellectual Property Rights policy requires contributors to offer a patent promise not to assert certain patent claims against other contributors and against implementers. The OpenID Foundation invites any interested party to bring to its attention any copyrights, patents, patent applications, or other proprietary rights that may cover technology that may be required to practice this specification.

# Document history

   [[ To be removed from the final specification ]]


   -00 (WG document)

   *  New spec

