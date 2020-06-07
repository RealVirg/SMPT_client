import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def send_email(subject, to_addr, from_addr, body_text, files_to_attach):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = ', '.join(to_addr)
    text = MIMEText(body_text)
    msg.attach(text)
    for image in files_to_attach:
        attachment = MIMEBase('application', "octet-stream")
        header = 'Content-Disposition', 'attachment; filename="%s"' % image
        with open("attach/" + image, 'rb') as f:
            img_data = f.read()
        attachment.set_payload(img_data)
        encoders.encode_base64(attachment)
        attachment.add_header(*header)
        msg.attach(attachment)

        # image = MIMEImage(img_data, name=os.path.basename("attach/attached.png"))
        # msg.attach(image)

    BODY = "\r\n".join((
        "From: %s" % from_addr,
        "To: %s" % to_addr,
        "Subject: %s" % subject,
        "",
        body_text
    ))

    server = smtplib.SMTP_SSL('smtp.gmail.com:465')
    server.login('server.smtp.to.ex', 'Server_Server_123')
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()


if __name__ == "__main__":
    to_addr = "server.smtp.to.ex@gmail.com"
    from_addr = "server.smtp.to.ex@gmail.com"
    files_to_attach = ""
    subject = "Just check server"
    with open('config.txt') as f:
        try:
            to_addr = f.readline()
            subject = f.readline()
        except EOFError:
            print("error config")
            quit()
        try:
            files_to_attach = f.readline()
        except EOFError:
            files_to_attach = []
    body_text = "..."
    with open('text.txt') as f:
        try:
            body_text = f.read()
        except EOFError:
            print("error text")
            quit()
    if files_to_attach:
        files_to_attach = files_to_attach.split(" ")
    to_addr = to_addr.split(" ")
    send_email(subject, to_addr, from_addr, body_text, files_to_attach)
