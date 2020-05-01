New tag to communicate the score a piece of evidence achieved within the ID proofing and verification model being used. 

For example a passport that is scanned, chip read and selfie cross checked would achieve the following in the UK GPG45 framework:
Evidence - Strength: 3
Evidence - Validity: 3
Activity: 0
Identity Fraud: 0
Verification: 2

In the TISA AML standard it would score:
Validation: 3
Verification: 2

Suggest a new tag called “trust_framework_model_element_scores” that contains sub-tags to convey this information. 

Response Example: 

       "trust_framework_model_element_scores”: 
                  [ 
                     { "trust_framework_model_element":"validation", "score":"2"},
                     { "trust_framework_model_element":"verification", "score":"2"}
                  ], // Allows combination for sripp and online banking logon //