# README #

### What is this repository for? ###

* This is the repository for OpenID Foundation's [eKYC and Identity Assurance WG](https://openid.net/wg/ekyc-ida/).
* The document(s) are written in [markdown](https://bitbucket.org/tutorials/markdowndemo) and translated to html using [mmark](https://github.com/mmarkdown/mmark)

### Current version

The current SNAPSHOT versions is being built automatically from the master branch and can be accessed at:

* https://openid.bitbucket.io/ekyc/openid-connect-4-identity-assurance.html
* https://openid.bitbucket.io/ekyc/openid-authority.html
 
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

docker run -v `pwd`:/data danielfett/markdown2rfc openid-connect-4-identity-assurance.md

### Contribution guidelines ###

* There are two ways to contribute, creating issues and pull requests
* All proposals are discussed in the WG on the list and in our regular calls before being accepted and merged.

### Who do I talk to? ###

* The WG can be reached via the mailing list openid-specs-ekyc-ida@lists.openid.net
