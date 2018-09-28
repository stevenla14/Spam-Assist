spam_assist
------------------
About:
It takes in a file containing a list of emails, and sends 
the contents of another "spam" message file to each email. This project was completed 
in the span of 2 days. It is compatible only with Python versions 3 and above.

How To Use:
1.) Place all emails that you want to 'spam' in a file within the same directory as 'spam.py'. 
Make sure to place each email on their own line, which means that each pair of emails has a '\n' 
char in between.
2.) Place the entire spam message in a file within the same directory as 'spam.py'.
3.) Run 'spam.py' using Python 3 or above.
Note: You may need to enable 'Allow less secure apps' on Gmail, to allow a connection from the
command line. Also, the uploaded files include 'emails.txt' and 'message.txt' which are supposed 
to be the respective files in Steps 1 and 2, but you can make your own/rename them if you wish. 
(Just make sure to put in the right file names when prompted.)

Documented Limitations:
1.) Only supports email providers: Gmail, Outlook, Hotmail, Yahoo, AT&T, Comcast, Verizon
2.) Fairly slow if a lot of emails are within the file...
