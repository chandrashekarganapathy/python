
# Python code to illustrate Sending mail 
# to multiple users 
# from your Gmail account 
import smtplib
 
# list of email_id to send the mail

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("ganapathy.17ec@cmr.edu.in","Houseno@786")
message = "Hello World"
s.sendmail("ganapathy.17ec@cmr.edu.in", "ganapathyshekar09@gmail.com", message)
print( "success")
s.quit()
