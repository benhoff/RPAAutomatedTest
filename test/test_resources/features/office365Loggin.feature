Feature: Get logged in Office365

    The Workshop bot should be capable of read a credentials in a excel file and get logged in office365 page

    Background: There are no residual files of any previous execution of the Workshopbot
        Given All the residual files have been deleted


    Scenario Outline: the robot should read <File> and runs this steps:<first>,<second>,<third>,<fourth>

        Given Robot runs <task>

        When Robot do the: <first> process 
        And Robot do the: <second> process 
        And Robot do the: <third> process

        Then Robot should: <fourth>


        Examples:
        |   task                        | File                       | first                          | second                               | third                                 | fourth                           |
        |   2.Office365Loggin.atmx      | 2.Office365Loggin.xlsx     | Open the browser: Chrome       | Browse to office 365 login page      | Insert data in office365 login inputs | Succesful login in office365     |
