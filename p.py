from selenium import webdriver
import time
import pandas as pd
import numpy as np
import sys


from args import CLIArguments 

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

        # Driver
        self.driver = webdriver.Firefox(executable_path=web_driver_path)
        self.driver.get("https://web.whatsapp.com/")

        # Until scan
        input('Enter anything after scanning QR code')
        
        # print(self.MSG_MODE)
        # print(self.MSG_MODE)
        # print(self.NUMBER_RECIPIENTS)
        # print(self.NAME_OR_GROUP_RECIPIENTS)
        # print(self.FILE_RECIPIENTS)
        # print(self.CLI_MESSAGE)
        # print(self.CLI_ATTACHMENTS)

        



    # ##############################################
    # ################## Methods ###################
    # ##############################################

    def run(self):
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
            time.slee(1)
            sys.exit()

        self.iterate_recipient()

    def iterate_recipient(self):
        # Number list contains any number
        if not self.NUMBER_RECIPIENTS:
            self.iterate_number()

        # Name or Group present in list 
        if not self.NAME_OR_GROUP_RECIPIENTS:
            self.iterate_name_or_group()

        # File present in the list
        if not self.FILE_RECIPIENTS:
            self.iterate_file()

    def iterate_number(self):
        msg_cli_flag = False
        attach_cli_flag = False
        
        if self.MSG_MODE == "cli":
            msg_cli_flag = True
        if self.ATTACH_MODE == "cli":
            attach_cli_flag = True
        
        self.by_number(msg_cli_flag, attach_cli_flag)


        

    def iterate_name_or_group(self):
        pass  

    def iterate_file(self):
        pass

    def whatsapp_control(self):
        pass

    def by_name(self):
        pass

    def by_number(self, msg_cli_flag, attach_cli_flag):
        if msg_cli_flag  == True:
            for number in self.NUMBER_RECIPIENTS:
                if self.CLI_MESSAGE == None:  
                    self.driver.get('https://web.whatsapp.com/send?phone=' + str(number) +"&text=")
                else:
                    self.driver.get('https://web.whatsapp.com/send?phone=' + str(number) +"&text="+ self.CLI_MESSAGE)
                
                time.sleep(4)
                submit = self.driver.find_element_by_css_selector("._3uMse+ ._1JNuk")
                submit.click()
            if attach_cli_flag == True:
                if not self.CLI_ATTACHMENTS:
                    for attachment in Attachments.split(","):
                        time.sleep(1)
                        print(attachment)
                        self.attach_file(file_path=attachment)


    def by_file(self):
        pass

    def attach_file(self):
        time.sleep(1)
        attachment_box = self.driver.find_element_by_xpath('//div[@title = "Attach"]')
        attachment_box.click()

        image_box = self.driver.find_element_by_xpath(
            '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        print(file_path)        
        image_box.send_keys(file_path)
        time.sleep(1)
        

        send_button = self.driver.find_element_by_xpath('//span[@data-icon="send"]')
        send_button.click()

if __name__ == "__main__":
    cli_args =  CLIArguments()  

    RECIPIENTS = cli_args.recipient_arg()
    MESSAGE = cli_args.msg_arg()
    ATTACHMENTS= cli_args.attach_file_arg() 
    MODES = cli_args.implicit_modes()
    # print(f"{recipients} {message} {attachments}")

    WEB_DRIVER_PATH = "/media/hamza/linux1/Coding/Python/Whatsapp_bulk_msg_files_sender" 


    w = WhatsappBot(modes=MODES,                     # ['both', 'both']
                recipients=RECIPIENTS,               # [[923370392561, 923342843869], ['hamza', 'Linear aljebra'], ['file.csv', 'o.xlsx']]
                message=MESSAGE,                     # Hi
                attchments=ATTACHMENTS,              # ['1.png', '2.png']
                web_driver_path=WEB_DRIVER_PATH)
    # w.run()

# python3 args.py -r "hamza,Linear aljebra,923370392561,923342843869,file.csv,o.xlsx" -m "Hi" -amode both -af 1.png,2.png -mmode both
# ['both', 'both'] [[923370392561, 923342843869], ['hamza', 'Linear aljebra'], ['file.csv', 'o.xlsx']] Hi ['1.png', '2.png']


# export PATH=$PATH:/media/hamza/linux1/Coding/Python/whatsapp_bulk_msg_sender/geckodriver