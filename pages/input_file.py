from utility.validation import Validation  # imports Validation class to validate data
from configuration.config import Configuration  # imports Configuration file


class InputFile:

    @staticmethod
    def get_headers(self):
        """
        Function to get Header List
        """
        header_list = ["Topic", "Content", "Start Date", "End Date", "Progress", "Confidence Level",
                       "Team Member", "Comments"]
        return header_list

    @staticmethod
    def get_data(self):
        """
        Function to get Data List
        """
        data_list = []
        topic = Validation.topic_validator(self)
        data_list.append(topic)
        content = Validation.content_validator(self)
        data_list.append(content)
        start_date = Validation.start_date_validator(self)
        format_start_date = start_date.strftime(Configuration.date_format)
        data_list.append(format_start_date)
        end_date = Validation.end_date_validator(self, start_date)
        format_end_date = end_date.strftime(Configuration.date_format)
        data_list.append(format_end_date)
        progress = Validation.progress_validator(self)
        data_list.append(progress)
        confidence_level = Validation.confidence_level_validator(self)
        data_list.append(confidence_level)
        team_member = Validation.team_member_validator(self)
        data_list.append(team_member)
        comments = Validation.comments_validator(self)
        data_list.append(comments)

        return data_list


