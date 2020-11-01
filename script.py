from selenium import webdriver
import time
import pandas as pd
import numpy as np

from args import CLIArguments 

class WhatsappBot():
    def __init__(self, modes, recipients, message, attchments, web_driver_path):
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

    RECIPIENTS = cli_args.recipient_arg()
    MESSAGE = cli_args.msg_arg()
    ATTACHMENTS= cli_args.attach_file_arg() 
    MODES = cli_args.modes()
    print(f"{recipients} {message} {attachments}")

    WEB_DRIVER_PATH = "/media/hamza/linux1/Coding/Python/whatsapp_bulk_msg_sender/geckodriver" 
    w = WhatsappBot(modes=MODES,
                recipients=RECIPIENTS,
                message=MESSAGE,
                attchments=ATTACHMENTS,
                web_driver_path=WEB_DRIVER_PATH)
    # w.run()

# python3 args.py -r "hamza,Linear aljebra,923370392561,923342843869,file.csv,o.xlsx" -m "Hi" -amode both -af 1.png,2.png -mmode both
# ['both', 'both'] [[923370392561, 923342843869], ['hamza', 'Linear aljebra'], ['file.csv', 'o.xlsx']] Hi ['1.png', '2.png']

"""ARGS
REQUIRED
--------
-r  recipients <list of names, numbers, files>

OPTIONAL
--------
-m  message <String>
-mmode msg_mode ("both", "cli", "file", "none")

-at attachment_files <list of files>
-amode attach_mode ("both", "cli", "file", "none")

DEFAULT MODES
-------------
both: when file/s & <numbers/names>
cli: only cli msg(s)/attachment(s) even file is given
file: only applicable when file is given
none: no msg(s)/attachmet(s) even cli/file args given

"""