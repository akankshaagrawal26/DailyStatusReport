from datetime import datetime
from configuration.config import Configuration  # imports Configuration file


class Validation:
    @staticmethod
    def topic_validator(self):
        while True:
            topic = input('Enter Topic :').strip()
            if len(topic) > 255:
                print("Please enter topic less than or equal to 255 characters")
                continue
            elif topic.find(Configuration.delimiter) != -1:
                print("Please enter topic without ';' as this would affect the data")
                continue
            else:
                return topic

    @staticmethod
    def content_validator(self):
        while True:
            content = input('Enter Content :').strip()
            if len(content) > 255:
                print("Please enter content less than or equal to 255 characters")
                continue
            elif content.find(Configuration.delimiter) != -1:
                print("Please enter content without ';' as this would affect the data")
                continue
            else:
                return content

    @staticmethod
    def start_date_validator(self):
        while True:
            start_date = input('Enter Start Date (DD/MM/YYYY):').strip()
            try:
                parsed_start_date = datetime.strptime(start_date, Configuration.date_format)
            except ValueError:
                print("Please enter date in DD/MM/YYYY format")
                continue
            if parsed_start_date > datetime.now():
                print("Future date is not allowed")
                continue
            else:
                return parsed_start_date

    @staticmethod
    def end_date_validator(self, start_date):
        while True:
            end_date = input('Enter End Date (DD/MM/YYYY):').strip()
            try:
                parsed_end_date = datetime.strptime(end_date, Configuration.date_format)
            except ValueError:
                print("Please enter date in DD/MM/YYYY format")
                continue
            if parsed_end_date > datetime.now():
                print("Future date is not allowed")
                continue
            elif parsed_end_date < start_date:
                print("End date cannot be less than the start date")
                continue
            else:
                return parsed_end_date

    @staticmethod
    def switch_progress(self, argument):
        switcher = {
            1: "Completed",
            2: "In-Progress",
        }
        return switcher.get(argument, "nothing")

    @staticmethod
    def progress_validator(self):
        while True:
            progress = int(input("Enter progress(1-2)\n1:Completed\n2:In-Progress\n").strip())
            result_progress = Validation.switch_progress(self,progress)
            if result_progress == "nothing":
                print("Please select either 1 or 2")
                continue
            else:
                return result_progress

    @staticmethod
    def switch_confidence(self, argument):
        switcher = {
            1: "High",
            2: "Medium",
            3: "Low",
        }
        return switcher.get(argument, "nothing")

    @staticmethod
    def confidence_level_validator(self):
        while True:
            confidence_level = int(input("Enter confidence level(1-3)\n1:High\n2:Medium\n3:Low\n").strip())
            result_confidence = Validation.switch_confidence(self,confidence_level)
            if result_confidence == "nothing":
                print("Please select options between 1-3")
                continue
            else:
                return result_confidence

    @staticmethod
    def team_member_validator(self):
        while True:
            team_member = input('Enter team member name :').strip()
            if len(team_member) > 100:
                print("Please enter Team member's name less than or equal to 100 characters")
                continue
            elif not team_member.isalnum():
                print("Please Enter only alphanumeric characters")
                continue
            else:
                return team_member

    @staticmethod
    def comments_validator(self):
        while True:
            comments = input('Enter Comments :').strip()
            if len(comments) > 1024:
                print("Please Enter comments less than or equal to 1024 Characters")
                continue
            elif comments.find(Configuration.delimiter) != -1:
                print("Please enter comments without ';' as this would affect the data")
                continue
            else:
                return comments


