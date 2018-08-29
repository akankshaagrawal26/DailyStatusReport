import os
from configuration.config import Configuration
from pages.input_file import InputFile


class WriteStatus:

    @staticmethod
    def write_file(self):
        """
        Function to write status to the Daily Status Report file
        """

        final_list = []       # Appends Header and Data to the list
        try:
            with open(Configuration.file_name, 'a') as out:
                if os.path.getsize(Configuration.file_name) > 0:    # checks the size of the file is greater than 0
                    final_list.append(InputFile.get_data(self))     # Appends data to the final list
                    print(final_list)
                    for word in final_list:
                        out.write(Configuration.delimiter.join(word)+"\n")
                    out.close()
                    return final_list
                else:
                    final_list.append(InputFile.get_headers(self))       # Appends headers to the final list
                    final_list.append(InputFile.get_data(self))          # Appends data to the final list
                    print(final_list)
                    for word in final_list:
                        out.write(Configuration.delimiter.join(word) + "\n")
                    out.close()
                    return final_list
        except IOError as io:
            print("IO Exception occurred", io)
        except Exception as e:
            print("Exception", e)
        finally:
            out.close()