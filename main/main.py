from pages.write_file import WriteStatus
from pages.send_mail import SendReport


class DailyStatusReport:

    def main(self):
        """
        Main function to get the daily status from the user, read the status,
        write the status to file and mail the status of the report
        """

        # Calling write_file function to write user input to the file
        final_list = WriteStatus.write_file(self)

        # Call to send_mail function for sending Status Report
        SendReport.send_mail(self, final_list)


# Creating object 'dsr' to call main Function
dsr = DailyStatusReport()
dsr.main()





