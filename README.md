# README #

### What is this repository for? ###

* This is the repository for OpenID Foundation's [eKYC and Identity Assurance WG](https://openid.net/wg/ekyc-ida/).
* The document(s) are written in [markdown](https://bitbucket.org/tutorials/markdowndemo) and translated to html using [mmark](https://github.com/mmarkdown/mmark)

### How do I get set up? ###

* Clone the repository
* Edit the source using the markdown editor of your choice
* Build the build command using docker: 

```
docker build -t openid.net/xml2rfc .
```

* Build the HTML/TXT versions of the specification: 

```
docker run -v `pwd`:/data openid.net/xml2rfc openid-connect-4-identity-assurance.md
```

NOTE: If you are experiencing problems with the build process, you might try this build command

```
docker build -t openid.net/xml2rfc . --no-cache
```


### Running Tests ###
This repository contains examples from the specifications and the JSON
schema definitions extracted as separate files in the directories
`examples` and `schema`, respectively. The directory `tests` contains
tests (written in python) that check if the examples comply to the
schema files.

To run the tests, follow these instructions:

* Build the test command using docker: 

```
docker build -t openid.net/tests-oidc4ia tests
```

* Run the tests: 

```docker run -v `pwd`:/data openid.net/tests-oidc4ia```

### Contribution guidelines ###

* There are two ways to contribute, creating issues and pull requests
* All proposals are discussed in the WG on the list and in our regular calls before being accepted and merged.

### Who do I talk to? ###

* The WG can be reached via the mailing list openid-specs-ekyc-ida@lists.openid.net
