import smtplib
import ssl
from itertools import cycle
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.base import MIMEBase  # New line
from time import gmtime, strftime
from email.mime.image import MIMEImage
from email import encoders  # New line
import time,random



def get_senders(filename):
    #global sender_email
    sender_email = []
    #global password
    password = []
    with open(filename, mode='r', encoding='utf-8') as sender_file:
        for line in sender_file:
            sender_email.append(line.split()[0])
            password.append(line.split()[1])
    return sender_email, password

def get_targets(filename):
    #global target_email
    target_email = []

    with open(filename, mode='r', encoding='utf-8') as target_file:
        for line in target_file:
            target_email.append(line.split()[0])



    return target_email



def main():


    sender_email, password = get_senders('from.txt')
    target_email = get_targets('to.txt')
    LastElement.append(target_email[-1])
    print(target_email)
    print("Total mails ",len(target_email))
    len_m=len(target_email)
    starting_mail=1

    file=open('body.txt', 'r')   #define email body
    body=file.read()

    zip_list = zip(target_email, cycle(sender_email),cycle(password)) if len(target_email) > len(sender_email) else zip(target_email, sender_email,password)
    # email_html = open('email.html')
    # email_body = email_html.read()
    attachment = 'abc.jpg'
    for email_t, email_s,passwd in zip_list:
        print("Email {} of {}".format(starting_mail,len_m))
        starting_mail=starting_mail+1
        print("Sending the email...")
        msg = MIMEMultipart()       #create a message

        # setup the parameters of the message
        sender = 'Your Name+'<'+email_s+'>'
        msg['From']=sender
        print('sending from', email_s)
        msg['To']=email_t
        print('sending to', email_t)

        msg['Subject']="Email Subject"
        # add in the message body
        # msg.attach(MIMEText(email_body, 'html'))
        msgText = MIMEText('<centre><b>%s</b><br><br><img src="cid:%s"><br><br><p> Random Text Of your wish </p><p>Thank you</p></centre>' % (body, attachment), 'html')
        msg.attach(msgText)   # Added, and edited the previous line
        fp = open(attachment, 'rb')
        img = MIMEImage(fp.read())
        fp.close()
        img.add_header('Content-ID', '<{}>'.format(attachment))
        msg.attach(img)
        # print(msg.as_string())


        try:
                # Creating a SMTP session | use 587 with TLS, 465 SSL and 25
                server = smtplib.SMTP('smtp.gmail.com', 587)
                # Encrypts the email
                context = ssl.create_default_context()
                server.starttls(context=context)
                # We log in into our Google account
                print ("loging in",email_s)
                server.login(email_s, passwd)
                # Sending email from sender, to receiver with the email body
                server.sendmail(email_s, email_t, msg.as_string())
                print('Email sent!')
        except Exception as e:
                print(f'Oh no! Something bad happened!n{e}')
                break
        finally:
                print('Closing the server...')
                server.quit()
                t=random.randint(5,12)
                time.sleep(t)


if __name__ == '__main__':
    # exec(open('range.py').read())
    LastElement=[]
    main()
    target_email = get_targets('to.txt')
    if(len(target_email)==0):
        print("All Emails are done! give next task")
    # print("Done Successfully!!")
    from datetime import datetime
    import pytz
    UTC = pytz.utc
    IST = pytz.timezone('Asia/Kolkata')
    with open("in.txt",'a') as f:
        datetime_ist = datetime.now(IST)
        s1="Done Successfully at "+str(datetime_ist.strftime('%Y:%m:%d %H:%M:%S %Z %z'))+", Total Mails Sent: "+str(len(target_email))+" And the last mail sent was: "+LastElement[0]
        f.write("%s\n" %s1)
