Feature: Log stalker

   searching keyword in a log file on real time

    Scenario Outline: Search for words <first> <second> <third>

        Given Robot runs <task> in <RPATool>
        When Robot do the <first> process 
        And Robot do the <second> process 
        And Robot do the <third> process 
        And Robot do the <fourth> process 
        And Robot do the <fifth> process 
        And Robot do the <sixth> process 

        Then All the process should be in <one> state 

        Examples:
        |   task                        | RPATool  | first              | second                     | third                         | fourth               | fifth                        | sixth                            | one   |
        |   giftList\\Flowchart1.xaml   | UIPath   | Ebay PROCESS: ps4  | Ebay PROCESS: xbox one x   | Ebay PROCESS: nintendo switch | Amazon PROCESS: ps4  | Amazon PROCESS: xbox one x   | Amazon PROCESS: nintendo switch  | ok    |