# Feature: Write the new state of emails looking the temp files

#     The Workshop bot should be capable of read the temp file folder and for every file write Sent in the MailsToSend excel file
    
#     Background: There are no residual files of any previous execution of the Workshopbot
#         Given All the residual files have been deleted

#     Scenario Outline: Read temp files folder and write the output in <File>
#         Given is <testdatafile> in the input folder named as <File>
#         Given is <testdata> in the temp folder

#         Given Robot runs <task>

#         When Robot change row <Number1> and delete <theFile1>
#         And Robot change row <Number2> and delete <theFile2>
#         And Robot change row <Number3> and delete <theFile3>
#         And Robot change row <Number4> and delete <theFile4>
#         And Robot change row <Number5> and delete <theFile5>
#         And Robot change row <Number6> and delete <theFile6>

#         Then All the <Column> in excel <File> should be <inState>

#         Examples:
#         |   task                        | File        | testdatafile  | testdata  | Number1 | theFile1  | Number2 | theFile2  | Number3 | theFile3  | Number4 | theFile4  | Number5 | theFile5  | Number6 | theFile6  | Column            | inState |
#         |   4.excelWriter.atmx          | Mails.xlsx  | Mails1.xlsx   | testdata1 | row: 4  | row_4.txt | row: 5  | row_5.txt | row: 6  | row_6.txt | row: 7  | row_7.txt | row: 8  | row_8.txt | row: 9  | row_9.txt | State of the mail | Sent    |

    
#     Scenario Outline: Read temp files folder and write the output in <File>
#         Given is <testdatafile> in the input folder named as <File>
#         Given is <testdata> in the temp folder

#         Given Robot runs <task>
#         When Robot change row <Number1> and delete <theFile1>
#         Then All the <Column> in excel <File> should be <inState>

#         Examples:
#         |   task                        | File        | testdatafile  | testdata  | Number1 | theFile1  | Column            | inState |
#         |   4.excelWriter.atmx          | Mails.xlsx  | Mails2.xlsx   | testdata2 | row: 4  | row_4.txt | State of the mail | Sent    |