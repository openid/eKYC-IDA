# README #

### What is this repository for? ###

* This is the repository for OpenID Foundation's [eKYC and Identity Assurance WG](https://openid.net/wg/ekyc-ida/).
* The document(s) are written in [markdown](https://bitbucket.org/tutorials/markdowndemo) and translated to html using [mmark](https://github.com/mmarkdown/mmark)

### Current activity

* Finalisation of the "OpenId Attachments 1.0" draft
* Development of examples and further definition and clarification of the "OpenId Authority 1.0" spec
* Maintenance and guidance for the FINAL specs produced by this Working Group (see below)

### Contribution guidelines ###

* There are two ways to contribute, creating issues and pull requests
* All proposals are discussed in the WG on the list and in our regular calls before being accepted and merged.
* If you wish to actively participate then please review and sign the [OpenID Foundation Contribution Agreement](https://openid.net/intellectual-property/openid-foundation-contribution-agreements/)
* Also please review [The OpenID Foundation (OIDF) Antitrust Policy](https://openid.net/wp-content/uploads/2024/09/OIDF-Antitrust-Policy_Final_2024-09-12.docx)

### Who do I talk to? ###

* The WG can be reached via the mailing list openid-specs-ekyc-ida@lists.openid.net

### What are each of the documents about? ###

[**OpenID Connect for Identity Assurance 1.0**](https://openid.net/specs/openid-connect-4-identity-assurance-1_0-final.html) - **FINAL**

 - An extension of OpenID Connect to be explicit about (verified) claims that have been through an identity assurance process and to represent details fo the assurance processes used when assuring those claims
 - This document depends upon "openid-ida-verified-claims.md" for the schema definition of the verified_claims element

[**OpenID Identity Assurance Schema Definition 1.0**](https://openid.net/specs/openid-ida-verified-claims-1_0-final.html) - **FINAL**

- A schema definition for the vereified _claims element, written in such a way that it can be used in the context of various application protocols including OpenID Connect.
- There is a corresponding non-normative JSON schema defined by the WG and hosted on the bitbucket at https://bitbucket.org/openid/ekyc-ida/src/master/schema/

[**OpenID Connect for Identity Assurance Claims Registration 1.0**](https://openid.net/specs/openid-connect-4-ida-claims-1_0-final.html) - **FINAL**
- Registration of a number of new end-user claims that are used in some identity assurance use cases

[**OpenID Attachments 1.0 draft**](https://openid.bitbucket.io/ekyc/openid-connect-4-ida-attachments.html) - DRAFT

- a draft that defines a way of representing binary data in the context of a JSON payload
- It can be used as an extension of OpenID Connect that defines attachments relating to the identity of a natural person or in other JSON contexts that need to have binary data elements

[**OpenID Connect Authority claims extension**](https://openid.bitbucket.io/ekyc/openid-authority.html) - DRAFT

 - a draft that allows expression of "on behalf of" cases whether on behalf of a person or legal entity

[**OpenID Connect Advanced Syntax for Claims (ASC) 1.0**](https://openid.bitbucket.io/ekyc/openid-connect-advanced-syntax-for-claims.html) - DRAFT

- a draft that extends OpenID Connect to permit the relying party to be much more specific about their requirements for claims
- it adds two features "Transformed Claims" and "Selective Abort and Omit"

### Current version

The current SNAPSHOT versions is being built automatically from the master branch and can be accessed at:

* https://openid.bitbucket.io/ekyc/openid-ida-verified-claims.html
* https://openid.bitbucket.io/ekyc/openid-connect-4-identity-assurance.html
* https://openid.bitbucket.io/ekyc/openid-connect-4-ida-claims.html

* https://openid.bitbucket.io/ekyc/openid-connect-4-ida-attachments.html

* https://openid.bitbucket.io/ekyc/openid-authority.html

* https://openid.bitbucket.io/ekyc/openid-connect-advanced-syntax-for-claims.html

### How do I get set up? ###

* Clone the repository
* Edit the source using the markdown editor of your choice
* Build the HTML file as described at https://github.com/oauthstuff/markdown2rfc

### Running Tests ###
This repository contains examples from the specifications and the JSON
schema definitions extracted as separate files in the directories
`examples` and `schema`, respectively. The directory `tests` contains
tests (written in python) that check if the examples comply to the
schema files.

To run the tests, follow these instructions:

* Build the test command using docker:

```
docker build -t openid.net/tests-oidc4ida tests
```

* Run the tests:

```docker run -v `pwd`:/data openid.net/tests-oidc4ida```

### Build the HTML ###

```docker run -v `pwd`:/data danielfett/markdown2rfc openid-connect-4-identity-assurance.md```


