import imaplib as imap #package to connect smpt server of gmail
import email           #package to parse email to check the string
#import re               #regular expression for ch
import os              #package to run the command above operating system
from sys import argv   #to get arguments from cmd
import hashlib         #to hash the required data for validating purpose
import base64
import json
import smtplib
import time
import socket


#utility functions
def remove(str,char):
    s=""
    for i in str.split(char):
        s=s+i
    return s
class RemoteSide:
    def __init__(self,email,password): #email=gmail address of email from which is controlled 
                                       #password=google app password [Note:THIS IS NOT PASSWORD WHICH IS USED BY TRADITIONAL LOGIN, THIS IS GENERATE IN https://myaccount.google.com/apppasswords]
       self.email=email
       self.password=password
       self.commandCounter=0
       #self.OUT=open("./OUTPUT","wb")


    def Connect(self):   #function to connect the smtp server of gmail
        try:
            mail=imap.IMAP4_SSL("smtp.gmail.com")
            mail.login(self.email,self.password)
            global mail_replicata
            mail_replicata=mail
        except (imap.IMAP4_SSL.abort,imap.IMAP4_SSL.error):
            
            
            print("-->Please make sure the parametered email and password are coorect and in string format")
            time.sleep(2)
            os.system("clear")
            exit(0)
        except(socket.gaierror):
            print(">>Please check Internet Connection")
            time.sleep(2)
            exit(0)
        
        
        return mail
   
   # def NumberOfTotalMails(self,mail):
    #   return  {'inbox':int(mail.select("INBOX")[1][0]),'spam':int(mail.select("[Gmail]/Spam")[1][0])}
     #  #check the number of emails currently exists in email in INBOX and SPAM section

    def __LatestCommandMail__(self,mail):
        #search latest mail from command email
        #SearchString="FROM "+"\""+self.email+"\""
        SearchString="UNSEEN"
        try:
            print("select")
            mail.select("INBOX")
            mail.check()  
            index=((mail.search(None,SearchString)[1][0]).split()).pop()
        except(IndexError):
            index=-1
        
        return index
        
    def __ExtractMessage__(self,mail,index):
       # print(index)
        type,msg=mail.fetch(index,"(RFC822)")
        #print(msg)
        raw_content=msg[0][1]
        #print(raw_content)
        #extracting content from email
        raw_content_string=raw_content.decode('utf-8') #decoding binary bits data too utf-8 encoded string
        msg=email.message_from_string(raw_content_string)
        #print(raw_content_string)

        if(hashlib.sha256(((self.email+self.password+"CONTROLLER").encode('utf-8'))).hexdigest() in raw_content_string):
           for part in msg.walk():
              code=part.get_payload()
            #  print(code)  
           return (base64.b64decode(code)).decode("utf-8")
        else:
            return False


    def __ExtractData__(self,data):
        #Extract the command id and command cl

        
        d=json.loads(data)
        return [int(d["CommandID"]),d["Command"]] 
        

    def __updateCommadId__(self,id):
        self.commandCounter=id
        
        
    
  
    

    def __RunCommand__(self,com):
        os.system(com+">OUTPUT")

    

    def __FormatContent__(self):
        file=open("OUTPUT","r")
        output=file.read()
        print(json.dumps({"commandID":self.commandCounter,"command":output}))


    def ConnectSMTP(self):
        smptmail=smtplib.SMTP_SSL("smtp.gmail.com")
        smptmail.login(self.email,self.password)
        global smpt
        smpt=smptmail
        return smptmail
    




if __name__=="__main__":
    print("************************************************************************************************\n")
    print("********************************REMOTE CLIENT***************************************************\n")
    print("************************************************************************************************\n")
    if(len(argv)!=3):
        print(">>INVALID ARGUMENT")
        time.sleep(2)
        os.system("clear")
        exit(0)
    while(True):
         Remote=RemoteSide(argv[1],argv[2])
         mail=Remote.Connect()
         ind=Remote.__LatestCommandMail__(mail)
         print(ind)
         if(ind!=-1):
            datas=Remote.__ExtractMessage__(mail,ind)
            if(datas!=False):
               comm=Remote.__ExtractData__(datas.replace("\n","").replace("'",""))
               print(comm)
               Remote.__RunCommand__(comm[1])
               Remote.__updateCommadId__(comm[0])
               Remote.__FormatContent__()





               
            else:
                continue
         else:
             continue
               


        







        
            
        




            


 
    
    

    
    

    


    

    

    

    


    
    
    
    

        


    



 



   
        

        
        

        



    
    def CheckInInbox(self,mail):
        #Assuming that command mail may be among latest 5 emails 
        latestID=NumberOfTotalMails(mail)['inbox']
        i=latestID
        while(i>latestID-5):
            msg=mail.fetch(str(i),"(RFC822)")


            





    
         


   