# Feature: Read the mails from mails.xlsx

#     The Workshop bot should be capable of read the mails to send from a excel file and manage the inputs for the next task

#     Background: There are no residual files of any previous execution of the Workshopbot
#         Given All the residual files have been deleted


#     Scenario Outline: Read <File> and create tempfiles with :<first> as data
#         Given is <testdatafile> in the input folder named as <File>

#         Given Robot runs <task>
#         When Robot read the row until get the data: <last>
#         Then Robot creates <n> files in tempData

#         Examples:
#         |   task                        | File        | testdatafile | last                                                                    | n |
#         |   1.excelReader.atmx          | Mails.xlsx  | Mails1.xlsx  | Row 8 with data: mail02@test.com Test Workshop numer 9 TF00000018.xlsx  | 6 |