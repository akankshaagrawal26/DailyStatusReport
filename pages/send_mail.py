import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from configuration.config import Configuration


class SendReport:

    @staticmethod
    def send_mail(self, final_list):
        """
        Function to send mail to the configured email id
        """
        try:
            smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
            smtp_obj.ehlo()
            smtp_obj.starttls()
            smtp_obj.ehlo()
            smtp_obj.login(Configuration.server_login_email, Configuration.server_login_password)

            mail_from = Configuration.mail_from
            mail_to = Configuration.mail_to

            msg = MIMEMultipart()
            msg['From'] = mail_from
            msg['To'] = mail_to
            msg['Subject'] = "Daily Status Report"
            i = 0
            body = ""
            header = "<center><h1>Daily Status Report</h1><center><br><br><table style='width:100%'>" \
                     "<tr><th>Topic</th><th>Content</th><th>Start Date</th><th>End Date</th>" \
                     "<th>Progress</th><th>Confidence Level</th><th>Team Members</th><th>Comments</th></tr>"

            if len(final_list) > 1:
                while i < len(final_list):
                    body += "<tr><td>" + final_list[i][0] + "</td><td>" + final_list[i][1] + "</td><td>" + \
                            final_list[i][2] + "</td><td>" \
                            + final_list[i][3] + "</td><td>" + final_list[i][4] + "</td><td>" + final_list[i][5] \
                            + "</td><td>" + final_list[i][6] + "</td><td>" + final_list[i][7] + "</td></tr>"
                    i += 1
            else:
                body += "<tr><td>" + final_list[0][0] + "</td><td>" + final_list[0][1] + "</td><td>" + \
                        final_list[0][2] + "</td><td>" + final_list[0][3] + "</td><td>" + final_list[0][4] + \
                        "</td><td>" + final_list[0][5] + "</td><td>" + final_list[0][6] + "</td><td>" \
                        + final_list[0][7] + "</td></tr>"

            content = header + body
            print("content:", content)
            msg.attach(MIMEText(content, 'html'))
            text = msg.as_string()
            smtp_obj.sendmail(mail_from, mail_to, text)
            print("Status mail successfully sent")

        except smtplib.SMTPException as smtp:
            print("Unable to send mail", str(smtp))
        except Exception as e:
            print("Exception", e)
