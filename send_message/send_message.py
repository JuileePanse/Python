#################### SEND ALERT EMAIL AT FINISH WITH GMAIL #####################
# To send email from Python from your google account, MUST 
# 1) Enable less secure app
# https://myaccount.google.com/lesssecureapps
# 2) Disable Unlock Capcha
# https://accounts.google.com/b/0/DisplayUnlockCaptcha

import smtplib

def SendEmail(msg):
    # store gmail password in my google drive (not the most secure way)
    # but it is much safer than storing it directly in this notebook, 
    # and upload it to github for everyone to see
    #with open('/content/gdrive/My Drive/Colab Notebooks/pw.txt') as file:
    #    data = file.readlines()
        
    gmail_user = 'juieeyoga0506@gmail.com'  
    gmail_password = 'juieeyoga@123'

    sent_from = gmail_user  
    to = ['juileepanse123@gmail.com']  
    subject = msg  
    body = '%s\n\n How are you?' % msg

    email_text = \
"""From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.quit()

    print('Email: \n{email_text}')
def main():
    msg= "CS531 Test Message from <Juilee Panse>, <19535>"
    SendEmail(msg)
if __name__ == '__main__':
    main()