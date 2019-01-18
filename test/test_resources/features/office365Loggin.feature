# Feature: Get logged in Office365

#     The Workshop bot should be capable of read a credentials in a excel file and get logged in office365 page

#     Background: There are no residual files of any previous execution of the Workshopbot
#         Given All the residual files have been deleted


#     Scenario Outline: the robot should the read credentials in configuration file and get logged to Office365 outlook
#         Given is <testdata> in the temp folder

#         Given Robot runs <task>

#         When Robot do the: <first> process 
#         And Robot do the: <second> process 
#         And Robot do the: <third> process

#         Then Robot should: <fourth>


#         Examples:
#         |   task                        |  File       | testdata     | first                          | second                               | third                                 | fourth                           |
#         |   2.Office365Loggin.atmx      |  Mails.xlsx | testdata1    | Open the browser: Chrome       | Browse to office 365 login page      | Insert data in office365 login inputs | Succesful login in office365     |
