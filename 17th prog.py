# scheduled email
import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("ganapathy.17ec@cmr.edu.in", "587")
 
msg = "hello world!"
server.sendmail("ganapathy.17ec@cmr.edu.in", "ganapathyshekar09@gmail.com", msg)
server.quit()
