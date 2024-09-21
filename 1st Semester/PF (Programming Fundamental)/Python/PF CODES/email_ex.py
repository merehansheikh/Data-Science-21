import smtplib
content="Hello World"
mail=smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
sender='pythonanytime@gmail.com'
recipient='mlathkar@gmail.com'
mail.login('pythonanytime@gmail.com','m15v5l61')
header='To:'+receipient+'\n'+'From:' \
+sender+'\n'+'subject:testmail\n'
content=header+content
mail.sendmail(sender, recipient, content)
mail.close()

#Before running above script, sender's gmail account must be configured to allow 'less secure apps'. Visit following link. 

#https://myaccount.google.com/lesssecureapps 