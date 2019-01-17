Feature: Send Emails from temp txt files

    The Workshop bot should be capable of read the files in the temp folder and send one email for txt file, after that the bot should change the temp txt file name

    Background: There are no residual files of any previous execution of the Workshopbot
        Given All the residual files have been deleted


    Scenario Outline: Read temp folder files and send 1 emails
        Given is <testdata> in the temp folder

        Given Robot runs <task>
        When Robot send email with: <first>
        Then the robot should have marked all temporary files as <state>

        Examples:
        |   task                        | testdata   | first                                                                       | state |
        |   3.sendEmails.atmx           | testdata2  | mail03@test.com Test Workshop numer 4 TF00000017.xlsx Sheet: invoices main  | sent  |


    Scenario Outline: Read temp folder files and send 6 emails
        Given is <testdata> in the temp folder

        Given Robot runs <task>

        When Robot send email with: <first> 
        And Robot send email with: <second>
        And Robot send email with: <third>
        And Robot send email with: <fourth>
        And Robot send email with: <fifth>
        And Robot send email with: <sixth>

        Then the robot should have marked all temporary files as <state>

        Examples:
        |   task                        | testdata   | first                                                                       | second                                                                      | third                                                                                                | fourth                                                                              | fifth                                                                  | sixth                                                                       | state |
        |   3.sendEmails.atmx           | testdata1  | mail03@test.com Test Workshop numer 4 TF00000017.xlsx Sheet: invoices main  | mail02@test.com Test Workshop numer 5 TF00000018.xlsx Sheet: invoice detail | yenylopez@digitalamericas.ai Test Workshop numer 6 TF00000006.xlsx Sheet: About This Invoice Tracker | jose.garcia@digitalamericas.ai Test Workshop numer 7 TF00000014.xlsx Sheet: invoice | mail03@test.com Test Workshop numer 8 TF00000017.xlsx Sheet: customers | mail02@test.com Test Workshop numer 9 TF00000018.xlsx Sheet: invoice detail | sent  |
