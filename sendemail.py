import smtplib,email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
email_from_addr = "rrabshette@gmail.com"
email_to_addr = "rohit.rabshette777@gmail.com"
email_smtp_server = "smtp.gmail.com"
email_smtp_port = "587"
# email_user = "rrabshette@gmail.com"
# email_password = "Agnes@50"

#Email Subject
email_subject = "Welcome to Python Email Test"
email_body = None

email_body_header = ' '
email_body_header = email_body_header + '<html><head></head><body>'
email_body_header = email_body_header + '<style type="text/css"></style>'
email_body_header = email_body_header + '<br><p>Hello Dholu,,<br><br>This is a test email.<br>'

email_body_content = ' '
email_body_content = email_body_content + '<H1>Dholu yeda aahe Pagal ahe</h1>'

email_body_footer = ' '
email_body_footer = email_body_footer + '<br>Thank you'
email_body_footer = email_body_footer + '<br>Dholu<br>'

email_body = str(email_body_header) + str(email_body_content) + str(email_body_footer)
message = MIMEMultipart('alternative')
message['From'] = email_from_addr
message['To'] = email_to_addr
message['Subject'] = email_subject
body = email_body
message.attach(MIMEText(body, 'html'))

# print (email_body)
s = smtplib.SMTP(email_smtp_server,int(email_smtp_port))
text = message.as_string()

s.starttls()
s.login("rrabshette@gmail.com","Agnes@50")
s.sendmail(email_from_addr,email_to_addr,text)
s.quit()