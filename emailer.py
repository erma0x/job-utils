import smtp
from email.message import EmailMessage

def allerter(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] =  subject
    msg['to'] = to
    
    user = "user@gmail.com" # sender
    password = "password"
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    
    server.quit()
    
if __name__ == '__main__':
    # SEND EMAIL TEXT MESSAGE
    email_alert("subject", "full text", "user@gmail.com")

    # SEND SMS TEXT MESSAGE
    # email_alert("subject", "full text", "+111111111111@sms.vodafone.en")

# https://www.liquisearch.com/list_of_sms_gateways
