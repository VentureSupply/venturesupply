import os
import io

class Curlm:
    """class to manipulate our curl html search"""
    def __init__(self):
        if not os.path.isfile("curl.txt"):
            print("curl.txt does not exist!")
            sys.exit(1)

        self.company_Search = ""

    def ask(self):
       """asks for search var"""
       return input("What company do you want to search for? ")
       #print(self.company_Search) 

    def search(self, target):
        """searchs for target string in file"""
        curl = open("curl.txt", "r")
        curl_command = curl.readline() # file should be one line
        curl.close()
        return  curl_command.find(target)

    def insert(self, company, start, end):
        """inserts company after start but before end"""
        start_index = self.search(start)
        if start_index == -1:
            print(start, "not found")

        end_index = self.search(end)
        if end_index == -1:
            print(end, "not found")
        curl = open("curl.txt", "r")
        curlline = curl.readline()
        curl.close()
        curl_first_half = curlline[ :(start_index + len(start))] # returns string includling the start string 
        # print(curl_first_half)
        curl_second_half = curlline[end_index: ]  # returns rest of the file starting at our end
        # print(curl_second_half)
        new_command = curl_first_half + company + curl_second_half  # smashs our target between them
        # print(new_command)
        curl = open("curl.txt", "w")
        curl.write(new_command)
        curl.close()


test_class = Curlm()
current_search = test_class.ask()

test_class.insert(current_search,"TextBox_NameSearch=", "&ctl00%24content_placeholder_body%24BusinessSearch1%24Button_Search=Search")

