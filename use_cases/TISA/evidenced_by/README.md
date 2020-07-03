## TISA Evidenced by README.md 
by Nick Mothershaw

A way of indicating which pieces of evidence provided a particular user_info claim. 

This allows traceability of where each claim came from. 

For example I might get the given_name claim Nick from a credit card account and Nicholas from a passport. 

This allows the RP to determine the weight of evidence behind each claim. 

We need to determine how the claims that are associated with a particualar piece of evidence Vs the claims that the ID provider has decided are the "assured claims" are differentiated.

Example request:
```
        "evidenced_by": null"     // for each claim element returned show and arrany of which evidences the claim has come from. This could be requested at an individual claim element level, but that would be messy //
```

Example response:
```
         "name"{ 
            { "title":"Miss", "evidenced_by" [ "txn":"676q3636461467647q8498785747q487" , "txn":"676q3636461467647q8498785747q487" ] },
            { "given_name":"Rita", "evidenced_by" [ "txn":"676q3636461467647q8498785747q487" , "txn":"676q3636461467647q8498785747q487" ] },
            { [ middle_name:"Jane" ], "evidenced_by" [ "txn":"676q3636461467647q8498785747q487" ] },
            {"family_name":"Shandu�, "evidenced_by" [ "txn":"676q3636461467647q8498785747q487" , "txn":"676q3636461467647q8498785747q487" ] },
            },
         { "birthdate":"1972-05-12", "evidenced_by" [ "txn":"676q3636461467647q8498785747q487" , "txn":"676q3636461467647q8498785747q487" ] }, 
         { "current_address":{ // complex UK address to be agreed // }, "evidenced_by" [ "txn":"676q3636461467647q8498785747q487" , "txn":"676q3636461467647q8498785747q487" ] },
```

