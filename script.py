# Copyright 2020 Hamza Arain. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================


"""
For Numbers
------------
0. -r 92xxxxxxxxxx
1. -r 92xxxxxxxxxx -m "Hi from bot"
2. -r "92xxxxxxxxxx, 92xxxxxxxxxx" -m "Hi from bot"
3. -r 92xxxxxxxxxx -m "Hi from bot" -mmode none
4. -r 92xxxxxxxxxx -m "Hi from bot" -mmode cli
5. -r 92xxxxxxxxxx -mmode cli
6. -r 92xxxxxxxxxx -mmode both'
7. -r 92xxxxxxxxxx -m Hi -mmode both
8. -r 92xxxxxxxxxx -af ./1.png
9. -r 92xxxxxxxxxx,92xxxxxxxxxx -m Hi -mmode cli -af ./2.png  -amode cli


python3 script.py -r "./leads2.xlsx,
        ./leads2.xlsx,Twilio,Twilio,
        92xxxxxxxxxx,92xxxxxxxxxx"
        -m "Hi from cli" -af ./3.svg
        -mmode cli  -amode file
"""


# Modules
from selenium import webdriver
import time
import pandas as pd
import numpy as np
import sys

from args import CLIArguments 


"""
Whatsapp Bot
============

Whatsapp bot that can send files and messags to recipients.
----------------------------------------------------------------

Sends (messages + files) to recipients (files + names + numbers)

Recipients       -r      [ name/group | file.xlsx/file.csv | number(92xxxxxxxxxx) ]
Message          -m      [ String(from CLI) ]
Attachments      -at     [ List(from CLI attachments) ]
Attachment mode  -amode  [ both(cli + file) | file | cli | none ]
Message mode     -mmode  [ both(cli + file) | file | cli | none ]
"""

class WhatsappBot():
    
    def __init__(self, modes, recipients, message, attchments, web_driver_path):
        # Modes
        self.MSG_MODE    = modes[0] # "both" -> ("both", "cli", "file", "none")
        self.ATTACH_MODE = modes[1] # "both" -> ("both", "cli", "file", "none")

        # Recipients ->  already striped
        self.NUMBER_RECIPIENTS = recipients[0]          # [923370392561, 923342843869] 
        self.NAME_OR_GROUP_RECIPIENTS = recipients[1]   # ['hamza', 'Linear aljebra']
        self.FILE_RECIPIENTS = recipients[2]            # ['file.csv', 'o.xlsx']

        # Message form CLI
        self.CLI_MESSAGE = message                      # Hi

        # Attachments from CLI
        self.CLI_ATTACHMENTS = attchments               # ["1.png", "2.png"]

        self.WEB_DRIVER_PATH = web_driver_path

        self.precheck()
        


    # ##############################################
    # ################## Methods ###################
    # ##############################################

    def precheck(self):
        """Handle the modes of CLI & Attachment flags.
        This runs from constructor"""
        # No files + both msg mode
        if ((not self.FILE_RECIPIENTS) and (self.MSG_MODE == "both")):
            print("'both': message CLI mode is not valid for given argument or file is missing")
            print("Exiting.....")
            time.sleep(1)
            sys.exit()

        # No msg + CLI msg mode
        if (self.CLI_MESSAGE == None) and (self.MSG_MODE == "cli"):
            print("Message is missing for CLI mode")
            print("Exiting.....")
            time.sleep(1)
            sys.exit()

        # ####### Message mode -mmode [none | cli | file | both]
        # -mmode none
        if self.MSG_MODE == "none":
            print("No message send either from file or from commandline tool")

        # ####### Attach mode -amode [none | cli | file | both]
        # -amode mone
        if self.ATTACH_MODE == "none":
            print("No file attached either from file or from commandline tool")

        # Terminate program from running state as no task to do
        if (self.ATTACH_MODE == "none") and (self.MSG_MODE == "none"):
            print("Exiting.....")
            time.sleep(1)
            sys.exit()

    def run(self):
        """This runs after scan"""
        # Driver
        self.driver = webdriver.Firefox(executable_path=self.WEB_DRIVER_PATH)
        self.driver.get("https://web.whatsapp.com/")

        # Until scan
        input('Enter anything after scanning QR code')

        self.iterate_recipients()

    def iterate_recipients(self):
        """This will process files, names & numbers"""
        # Number list contains any number
        if not self.NUMBER_RECIPIENTS == False:
            self.iterate_number()

        # Name or Group present in list 
        if not self.NAME_OR_GROUP_RECIPIENTS == False:
            self.iterate_name_or_group()

        # File present in the list
        if not self.FILE_RECIPIENTS == False:
            self.iterate_file()

    # ##############################################
    # ################## Number ####################
    # ##############################################

    def iterate_number(self):
        """CLI Allowance from flag for messages & attachments"""
        msg_cli_flag = False
        attach_cli_flag = False
        
        if self.MSG_MODE == "cli":
            msg_cli_flag = True

        if self.ATTACH_MODE == "cli":
            attach_cli_flag = True

        self.by_number(msg_cli_flag, attach_cli_flag)

    def by_number(self, msg_cli_flag, attach_cli_flag):
        """Number flags allowance"""
        if (msg_cli_flag  == True) or ((attach_cli_flag == True) and self.CLI_ATTACHMENTS):
            for number in self.NUMBER_RECIPIENTS: 
                if msg_cli_flag  == True:
                    self.driver.get('https://web.whatsapp.com/send?phone=' + str(number) +"&text="+ self.CLI_MESSAGE)

                    time.sleep(10)
                    submit = self.driver.find_element_by_css_selector("._3uMse+ ._1JNuk")
                    submit.click()
                    time.sleep(2)

                if attach_cli_flag == True :
                    for attachment in self.CLI_ATTACHMENTS:
                        print(f"Sending {attachment} to {number}")
                        self.attach_file(file_path=attachment)
                        time.sleep(5)
                        
        

    # ##############################################
    # ################## Name/Group ################
    # ##############################################

    def iterate_name_or_group(self):
        """CLI Allowance from flag for messages & attachments"""
        msg_cli_flag = False
        attach_cli_flag = False

        if self.MSG_MODE == "cli":
            msg_cli_flag = True

        if self.ATTACH_MODE == "cli":
            attach_cli_flag = True
        
        self.by_name_or_group(msg_cli_flag, attach_cli_flag)

    def by_name_or_group(self, msg_cli_flag, attach_cli_flag):
        """Name/Group flags allowance"""
        if (msg_cli_flag  == True) or ((attach_cli_flag == True) and self.CLI_ATTACHMENTS):
            for name in self.NAME_OR_GROUP_RECIPIENTS:
                time.sleep(3)
                searchName = self.driver.find_element_by_xpath('//div[@class = "{}"]'.format("_3FRCZ copyable-text selectable-text")) 
                searchName.click()
                searchName.send_keys(name)
                time.sleep(3)

                user = self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
                user.click()

                if msg_cli_flag  == True:
                    time.sleep(3)
                    msgBox = self.driver.find_element_by_css_selector('#main ._3FRCZ')
                    msgBox.click()
                    msgBox.send_keys(self.CLI_MESSAGE)

                    submit = self.driver.find_element_by_css_selector("._3uMse+ ._1JNuk")
                    submit.click()

                if attach_cli_flag == True :
                    for attachment in self.CLI_ATTACHMENTS:
                        print(f"Sending {attachment} to {name}")
                        self.attach_file(file_path=attachment)
                        time.sleep(5)
                self.driver.get("https://web.whatsapp.com/") 
                time.sleep(10)

    # ##############################################
    # #################### File ####################
    # ##############################################

    def iterate_file(self):
        """CLI Allowance from flag for messages & attachments"""
        msg_cli_flag = False
        msg_file_flag = False
        msg_both_flag = False

        attach_cli_flag = False
        attach_file_flag = False
        attach_both_flag = False

        if self.MSG_MODE == "cli":
            msg_cli_flag = True
        elif self.MSG_MODE == "file":
            msg_file_flag = True
        elif self.MSG_MODE == "both":
            msg_both_flag = True

        if self.ATTACH_MODE == "cli":
            attach_cli_flag = True
        elif self.ATTACH_MODE == "file":
            attach_file_flag = True
        elif self.ATTACH_MODE == "both":
            attach_both_flag = True

        msg_flags_dic = {"cli": msg_cli_flag, "file":msg_file_flag, "both":msg_both_flag}
        attach_flags_dic = {"cli":attach_cli_flag, "file":attach_file_flag, "both":attach_both_flag}

        self.by_file(msg_flag=msg_flags_dic, attach_flag=attach_flags_dic)

    def by_file(self,msg_flag, attach_flag):
        """File flags allowance"""
        if any(msg_flag) or any(attach_flag):
            for _file in self.FILE_RECIPIENTS:
                for name, number, file_message, file_attachments in self.read_file(_file):
                    if msg_flag["both"] == True:
                        lst = [self.CLI_MESSAGE, file_message]
                        approved_messages = lst
                        # print(approved_messages)

                    elif msg_flag["cli"] == True:
                        approved_messages = [self.CLI_MESSAGE]
                    elif msg_flag["file"] == True:
                        approved_messages = [file_message]
                        # print(approved_messages)

                    # 
                    if attach_flag["both"] == True:
                        lst = file_attachments.split(",")
                        for i in self.CLI_ATTACHMENTS:
                            lst.append(i)
                        approved_attachments = lst
                        # print(approved_attachments)

                    elif attach_flag["cli"] == True:
                        approved_attachments = self.CLI_ATTACHMENTS
                        # print(approved_attachments)
                    elif attach_flag["file"] == True:
                        approved_attachments = file_attachments.split(",")
                        # print(approved_attachments)

                    if str(number) != "nan":
                        number = int(number)

                    self.whatsapp_web_control(Name=name, Number=number,
                                    Messages=approved_messages,
                                    Attachments=approved_attachments)

    def read_file(self, filename):
        """File reading"""
        data = pd.read_csv(filename)
        data_dict = data.to_dict('list')
        return zip(data_dict['names'], data_dict['LeadNumber'],
                     data_dict['Message'], list(data_dict['attachment'])) # ((name,number, msg), (name,number, msg))
    
    def whatsapp_web_control(self, Name, Number, Messages, Attachments):
        """Whatsapp control"""
        if str(Number) != "nan":    
            print("1")
            self.from_file_to_number(Number=Number, Messages=Messages, Attachments=Attachments)

        elif str(Name) != "nan":
            print("2")
            self.from_file_to_name_or_group(Name=Name, Messages=Messages, Attachments=Attachments)

    def from_file_to_number(self, Number, Attachments, Messages):
        """Reach to number from file"""
        for msg in Messages:
            print(f"{msg} {Number}")
            if str(msg) == "nan":
                msg = ""
                self.driver.get("https://web.whatsapp.com/send?phone="+ str(Number) +"&text=" + msg)
            else:
                self.driver.get("https://web.whatsapp.com/send?phone="+ str(Number) +"&text=" + msg)


            time.sleep(10)
            submit = self.driver.find_element_by_css_selector("._3uMse+ ._1JNuk")
            submit.click()

            if "nan" not in Attachments:
                for attachment in Attachments:
                    time.sleep(5)
                    print(attachment)
                    self.attach_file(file_path=attachment)
        
    def from_file_to_name_or_group(self, Name, Attachments, Messages):
        """Name/Group of flags allowance""" 
        time.sleep(1)
        searchName = self.driver.find_element_by_xpath('//div[@class = "{}"]'.format("_3FRCZ copyable-text selectable-text")) 
        time.sleep(5)
        searchName.click()
        searchName.send_keys(Name)

        time.sleep(5)
        user = self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(Name))
        user.click()

        if "nan" not in Messages:
            for msg in Messages:
                time.sleep(1)
                msgBox = self.driver.find_element_by_css_selector('#main ._3FRCZ')
                msgBox.click()
                msgBox.send_keys(str(msg))

                submit = self.driver.find_element_by_css_selector("._3uMse+ ._1JNuk")
                submit.click()

        if "nan" not in Attachments:
            for attachment in Attachments:
                time.sleep(1)
                print(attachment)
                self.attach_file(file_path=attachment)
            
    def attach_file(self, file_path):
        """File attachment"""
        time.sleep(5)
        attachment_box = self.driver.find_element_by_xpath('//div[@title = "Attach"]')
        attachment_box.click()

        image_box = self.driver.find_element_by_xpath(
            '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        print(file_path)        
        image_box.send_keys(file_path)
        time.sleep(5)
        

        send_button = self.driver.find_element_by_xpath('//span[@data-icon="send"]')
        send_button.click()

if __name__ == "__main__":
    cli_args =  CLIArguments()  

    RECIPIENTS = cli_args.recipient_arg()
    MESSAGE = cli_args.msg_arg()
    ATTACHMENTS= cli_args.attach_file_arg() 
    MODES = cli_args.implicit_modes()

    WEB_DRIVER_PATH = "/media/hamza/linux1/Coding/Python/Whatsapp_bulk_msg_files_sender/geckodriver" 


    w = WhatsappBot(modes=MODES,                     # ['both', 'both']
                recipients=RECIPIENTS,               # [[923370392561, 923342843869], ['hamza', 'Linear aljebra'], ['file.csv', 'o.xlsx']]
                message=MESSAGE,                     # Hi
                attchments=ATTACHMENTS,              # ['1.png', '2.png']
                web_driver_path=WEB_DRIVER_PATH)
    w.run()

