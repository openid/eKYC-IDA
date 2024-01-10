# README #

### What is this repository for? ###

* This is the repository for OpenID Foundation's [eKYC and Identity Assurance WG](https://openid.net/wg/ekyc-ida/).
* The document(s) are written in [markdown](https://bitbucket.org/tutorials/markdowndemo) and translated to html using [mmark](https://github.com/mmarkdown/mmark)

### What are each of the documents about? ###
openid-connect-4-identity-assurance.md
 - An extension of OpenID Connect to be explicit about (verified) claims that have been through an identity assurance process and to represent details fo the assurance processes used when assuring those claims
 - This document depends upon "openid-ida-verified-claims.md" for the schema definition of the verified_claims element

openid-ida-verified-claims.md
- A schema definition for the vereified _claims element, written in such a way tyat it can be used in the context of various application protocols including OpenID Connect.

openid-connect-4-ida-claims.md
- Registration of a number of new end-user claims that are used in some identity assurance use cases

openid-connect-4-ida-attachments.md

openid-authority.md
 - a draft that allows expression of "on behalf of" cases whether on behalf of a person or legal entity

openid-connect-advanced-syntax-for-claims.md
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

### Contribution guidelines ###

* There are two ways to contribute, creating issues and pull requests
* All proposals are discussed in the WG on the list and in our regular calls before being accepted and merged.

### Who do I talk to? ###

* The WG can be reached via the mailing list openid-specs-ekyc-ida@lists.openid.net
