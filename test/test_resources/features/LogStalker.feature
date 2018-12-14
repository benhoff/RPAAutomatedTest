Feature: Log stalker

   searching keyword in a log file on real time

    Scenario Outline: Search for words <first> <second> <third>

        Given Robot runs <task> in <RPATool> and logs in <file>
        When Robot do the <first> process 
        And Robot do the <second> process 
        And Robot do the <third> process 
        Then All the process should be in <one> state 

        Examples:
        |   task            |    RPATool     |  thefile       | first  | second   | third  |    one     |
        |   tasknamexx      |    UIPath      |  Overwatch.log | hello  | fucking  | world  |    ok      |