Feature: Read the mails from mails.xlsx

    The Workshop bot should be capable of read the mails to send from a excel file and manage the inputs for the next task

    Background: There are no residual files of any previous execution of the Workshopbot
        Given All the residual files have been deleted


    Scenario Outline: Read <File> and create tempfiles with :<first> as data

        Given Robot runs <task> for <File>
        When Robot read the row until get the data: <last>
        Then Robot creates <n> files in tempData

        Examples:
        |   task                        | File        | last                                                             | n |
        |   2.excelReader.atmx          | Mails.xlsx  | Row 8 with data: mail02@test.com Test Workshop  TF00000018.xlsx  | 6 |