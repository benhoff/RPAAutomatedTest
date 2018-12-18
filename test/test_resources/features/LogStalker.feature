Feature: Search for products in Ebay and Amazon page

   giftListBot search a list of products in ebay and amazon page, after that he writes information about the products in different CSV files

    Background: There are no residual files of any previous execution of the giftListbot
        Given All the residual files have been deleted


    Scenario Outline: giftListBot read <File> and runs: <first> <second> <third> <fourth> <fifth> <sixth>

        Given Robot runs <task> for <File> in <RPATool>

        When Robot do the <first> process 
        And Robot do the <second> process 
        And Robot do the <third> process 
        And Robot do the <fourth> process 
        And Robot do the <fifth> process 
        And Robot do the <sixth> process 

        Then All the process should be in <one> state
        And Robot should put the Amazon information in the CSV Files
        And Robot should put the Ebay information in the CSV Files



        Examples:
        |   task                        | File          | RPATool  | first                          | second                        | third                             | fourth                           | fifth                          | sixth                             | one         |
        |   giftList\\Flowchart1.xaml   | gifts.txt     | UIPath   | Ebay PROCESS: ps4              | Ebay PROCESS: xbox one x      | Ebay PROCESS: nintendo switch     | Amazon PROCESS: ps4              | Amazon PROCESS: xbox one x     | Amazon PROCESS: nintendo switch   | Finished OK |
        |   giftList\\Flowchart1.xaml   | gifts2.txt    | UIPath   | Ebay PROCESS: rocket launcher  | Ebay PROCESS: flamethrower    | Ebay PROCESS: elton john          | Amazon PROCESS: rocket launcher  | Amazon PROCESS: flamethrower   | Amazon PROCESS: elton john vinyl  | Finished OK |