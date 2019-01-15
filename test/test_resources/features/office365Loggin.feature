# Feature: Get logged in Office365

#     The Workshop bot should be capable of read a credentials in a excel file and get logged in office365 page

#     Background: There are no residual files of any previous execution of the Workshopbot
#         Given All the residual files have been deleted


#     Scenario Outline: Read <File> and runs:<first>,<second>,<third>,<fourth> Processes

#         Given Robot runs <task> for <File>

#         When Robot do the <first> process 
#         And Robot do the <second> process 
#         And Robot do the <third> process

#         Then Robot should <fourth>
#         And the excel column status should be <loggedStatus>



#         Examples:
#         |   task                        | File                       |   first                        | second                               | third                                 | fourth                           | loggedStatus |
#         |   1.Office365Loggin.atmx      | 1.Office365Loggin.xlsx     | Open the browser: Chrome       | Browse to office 365 login page      | Insert data in office365 login inputs | Succesful login in office365     | Logged |
