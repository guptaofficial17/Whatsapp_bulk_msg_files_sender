from selenium import webdriver
import time
import pandas as pd
import numpy as np

from args import CLIArguments 

class WhatsappBot():
    def __init__(self, modes, recipients, message, attchments):
        pass


    # ##############################################
    # ################## Methods ###################
    # ##############################################

    def run(self):
        pass

    def iterate_recipient(self):
        pass

    def iterate_number(self):
        pass

    def iterate_name_or_group(self):
        pass  

    def iterate_file(self):
        pass

    def whatsapp_control(self):
        pass

    def by_name(self):
        pass

    def by_number_or_group(self):
        pass

    def by_file(self):
        pass

    def attach_file(self):
        pass



if __name__ == "__main__":
    cli_args =  CLIArguments()  

    recipients = cli_args.recipient_arg()
    message = cli_args.msg_arg()
    attachments= cli_args.attach_file_arg() 

    print(f"{recipients} {message} {attachments}")



    # w = WhatsappBot(modes, recipients, message, attchments)
    # w.run()