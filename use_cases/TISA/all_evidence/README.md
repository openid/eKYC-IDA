# Request All Evidence

The use of the evidence tag with the value null should result in the IdP returning all evidence they have gathered in order to meet the required level of assurance. 

            "evidence":null  // All evidence sent back to RP to allow decisioning or record keeping" //

Level of assurance is determined using what? The trust_framework tag? Does this need breaking down into
trust_framework
trust_scheme
level_of_assurance

eIDAS is an example of these three tiers:

trust_framework = eIDAS
trust_scheme = UK Vefify
level_of_assurance = Substantial

Note that the verifier may be a separate role to all the above. It may be a (certified) ID services component provider that provides a particular piece of evidence. Examples would be: a CRA, a document verification provider, a government document verification service, etc. 

In the TISA example:

trust_framework = UK Gov
trust_scheme = TISA Financial Services
level_of_assurance = AML
