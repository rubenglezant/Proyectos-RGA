__author__ = 'ruben'

import smtplib

fromaddr = 'ruben_gonzalez@iecisa.com'
toaddrs  = 'rubenglezant@gmail.com'
msg = "\r\n".join([
  "From: user_me@gmail.com",
  "To: user_you@gmail.com",
  "Subject: Just a message",
  "",
  "Why, oh why"
  ])
username = 'ruben_gonzalez@iecisa.com'
password = 'XXXXXXXX'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
