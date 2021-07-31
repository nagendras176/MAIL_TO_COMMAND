import imaplib as imap #package to connect smpt server of gmail
#import email           #package to parse email body
import os              #package to run the command above operating system
from sys import argv   #to get arguments from cmd

class RemoteSide:
    def __init__(self,email,password): #email=gmail address of email from which is controlled 
                                       #password=google app password [Note:THIS IS NOT PASSWORD WHICH IS USED BY TRADITIONAL LOGIN, THIS IS GENERATE IN https://myaccount.google.com/apppasswords]
       self.email=email
       self.password=password

    def Connect(self):   #function to connect the smtp server of gmail
        try:
            mail=imap.IMAP4_SSL("smtp.gmail.com")
            mail.login(self.email,self.password)
        except (imap.IMAP4_SSL.abort,imap.IMAP4_SSL.error):
            print("-->Please Check the internet connection")
            print("-->Please make sure the parametered email and password are coorect and in string format")
        return mail
    
    def NumberOfTotalMails(self,mail):
       return  {'inbox':int(mail.select("INBOX")[1][0]),'spam':int(mail.select("[Gmail]/Spam")[1][0])}
       #check the number of emails currently exists in email in INBOX and SPAM section

    def CheckInInbox(self,mail):
        #Assuming that command mail may be among latest 5 messeges and return the file 
        latestID=NumberOfTotalMails(mail)['inbox']
        i=latestID
        while(i>latestID-5):
            msg=mail.fetch(str(i),"(RFC822)")
            




    
         


   