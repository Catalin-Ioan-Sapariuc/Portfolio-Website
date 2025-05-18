## Here is the email app password set up for sapariuc@gmail.com: luue pfjc ittr bgnm 
import smtplib, ssl

def send_email(message):

    password = "vnmi sdiq kuil lubz"
    #password = input("Type your password and press enter:")
    sender_email = "sapariuc@gmail.com" 

    #from email.mime.text import MIMEText
    #from email.mime.multipart import MIMEMultipart

    host = "smtp.gmail.com"
    port = 465

    receiver_email = "catalinsapariuc8020@gmail.com"
    #receiver = sender
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context = context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        #server.sendmail(sender_email, receiver_email, message.as_string())

