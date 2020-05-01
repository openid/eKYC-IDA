New tags to support more complex name and address formats. 

An array of middle names is required

Differentiation between current and previous addresses is required

An array of previous addresses is required

A UK address format is required.

NINO is required (for support for multiple user unique IDs)

Example request:

       "claims":{  
            "name"{ 
               "title":null,
               "given_name":{"essential": true},
               [ middle_name: null ],
               "family_name":{"essential": true}
               }
            "birthdate":{"essential": true},
            "current_address":{"essential": true},
            "NINO":null,
            "contact_details"';null',
            "previous_name”: null,
            [ "previous_address”:null ],
              }

Example response:

   "claims":{  
         "name"{ 
            "title":"Miss" ,
            "given_name":"Rita",
             [ middle_name:"Jane" ] ,
            },
          "birthdate":"1972-05-12", 
         "current_address":{ // complex UK address to be agreed //, 
        "NINO":"GH 78 67 34 C"
       }


