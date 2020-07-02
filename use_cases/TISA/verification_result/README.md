New tag to request and communicate the status of the verification request from the IdP to the RP.

Some the status indicate an interim state: pending, part verified.
Some the the status indidate a currently final state: verified
Other status indicate a result of a user decision: not_consented.

Request format:
"verification_result":null,   // return the verification result from the IdP //

Response format:
         "verification_result": "pending",  // Values of "verified", "pending", “part_verified”, ”not-verified", "fraud”,”not-consented” //


Need to determine whereabout in the response this tag fits. Should it go in the user_info section? Maybe not as some responses may not include any user info, such as “not-consented” or “pending”. 

Each result type will require the RP to take a different action:

"verified": The RP can accept the ID and move to the next part of thier process.
"part_verified": The RP can determine how much evidence has been gathered (from the returned verified evidence) and what gaps they need to fill. 
"pending": The IdP tells the user to wait until some part of the proofing process is completed. THe RP is also informed to wait by the return of this pending status. The RP informs the user they are pending an IDP action.
"not-verified": The RP will decide whether to terminate the transaction or try to verify the user locally. 
"fraud": a message is put to the user that will not tip them off that fraud is suspected. 
"non-consented": The RP will decide whether to terminate the transaction or try to verify the user locally. 



