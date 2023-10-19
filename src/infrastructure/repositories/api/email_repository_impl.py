import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate



class EmailRepositoryImpl(EmailRepository):
    def __init__(self, smtp_server, smtp_port, email, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email = email
        self.password = password

    def send_email(self, to_emails: list, cc_emails: list, subject, body, attachments=()) -> None:
        message = MIMEMultipart()
        message['From'] = self.email
        message['To'] = ', '.join(to_emails)
        message["Cc"] = ', '.join(cc_emails)
        message["Date"] = formatdate(localtime=True)
        message['Subject'] = subject
        message.attach(MIMEText(body, "html", "utf-8"))

        if attachments is not None:
            for file_name, file_content, mime_application_type in attachments:
                attachment = MIMEApplication(file_content, mime_application_type)
                attachment[
                    "Content-Disposition"
                ] = f'attachment; filename="{file_name}"'
                message.attach(attachment)

        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.starttls()
        server.login(self.email, self.password)
        text = message.as_string()
        server.sendmail(self.email, to_emails, text)
        server.quit()
