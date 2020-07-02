New tag to request and communicate the status of the verification request from the IdP to the RP.

Some the status indicate an interim state: pending, part verified.
Some the the status indidate a currently final state: verified
Other status indicate a result of a user decision: not_consented.

Request format:
"verification_result":null,   // return the verification result from the IdP //

Response format:
         "verification_result": "pending",  // Values of "verified", "pending", “part_verified”, ”not-verified", "fraud”,”not-consented” //


Need to determine whereabout in the response this tag fits. It should not go in the user_info section as some responses may not include any user info, such as “not-consented” or “pending”. 

