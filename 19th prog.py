#email scheduling using multiple users

# to multiple users 
# from your Gmail account 
import smtplib
 
# list of email_id to send the mail

s = smtplib.SMTP('smtp.gmail.com', 587)
l=("ganapathyshekar09@gmail.com","ganapathy.17ec@cmr.edu.in")
for i in l:
 s.starttls()
 s.login("ganapathy.17ec@cmr.edu.in","Houseno@786")
 message = "Hello World"
 s.sendmail("ganapathy.17ec@cmr.edu.in", "l[1]", message)
 print( "success")
 s.quit()
