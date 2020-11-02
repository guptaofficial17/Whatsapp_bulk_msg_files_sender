"""ARGS
========

REQUIRED
--------
-r  recipients <list of names, numbers, files>

OPTIONAL
--------
-m  message <String>
-mmode msg_mode ("both", "cli", "file", "none")

-at attachment_files <list of files>
-amode attach_mode ("both", "cli", "file", "none")


"""

"""
DEFAULT MODES
-------------
both: when file/s & <numbers/names>
cli: only cli msg(s)/attachment(s) even file is given
file: only applicable when file is given
none: no msg(s)/attachmet(s) even cli/file args given

MSG
====
1. -r "file.csv,o.xlsx,hamza" -m "Hi"   > ['both', 'files']
2. -r "hamza" -m "Hi"                   > ['cli', 'none']
3. -r "file.csv,o.xlsx,hamza"           > ['file', 'files']
4. -r "hamza"                           > ["none", "none"]

Attachment
===========
1. -r "file.csv,o.xlsx"  -af "1.png,2.png" > ['file', 'both']
2. -r 03003501901  -af "1.png,2.png"       > ['none', 'cli']
3. -r "file.csv,o.xlsx"                    > ['file', 'files']
4. -r 03003501901                          > ['none', 'none']


python3 args.py -r "hamza,Linear aljebra,923370392561,923342843869,file.csv,o.xlsx" -m "Hi" -amode both -af 1.png,2.png -mmode both
 ['both', 'both'] [[923370392561, 923342843869], ['hamza', 'Linear aljebra'], ['file.csv', 'o.xlsx']] Hi ['1.png', '2.png']
"""
import argparse

class CLIArguments():
    def __init__(self):
        parser = argparse.ArgumentParser(description="Bulk msg sender with files")
        
        # recipients related
        parser.add_argument(
            "-r", "--recipients",
            required=True,
            help= "Name or Group or file(s) Containing Recipient(s)\n"+
                  "=================================================\n"+
                  "This args provides target to send message(s) or attachment(s)\n"+
                                                                            
                  "\nRequired: True"
        )

        # msg related
        parser.add_argument(
            "-m" ,'--msg',
            help='Msg send to targeted recipients.'
        )
        parser.add_argument(
            "-mmode" ,'--msg_mode',
            choices=("both, cli, file, none"),
            help='Msg send to targeted recipients.'
        )

        # attch file related
        parser.add_argument(
            '-af','--attach_files',
            help='''File/s to import.\
                That will send to all targeted recipients'''
        )
        
        parser.add_argument(
            '-amode','--attach_mode',
            choices=("both, cli, file, none"),
            help='''File/s to import.\
                That will send to all targeted recipients'''
        )
        self.args = parser.parse_args()


    def recipient_arg(self):    
        # -r "hamza,Linear aljebra,923370392561,923342843869,file.csv,o.xlsx" -> 
        # [[923370392561, 923342843869], ['file.csv', 'o.xlsx'], ['hamza', 'Linear aljebra']]
        
        # Sender handling
        numberList = []
        fileList = []
        namesList = []
        for recipient in self.args.recipients.split(","):
            try:
                numberList.append(int(recipient)) 
            except ValueError:
                if recipient[-5:] == ".xlsx" or (recipient[-4:] == ".csv"):
                    fileList.append(recipient.strip())
                else:
                    namesList.append(recipient.strip())
        return [numberList, namesList, fileList]

    def msg_arg(self):
        if self.args.msg != None:
            return self.args.msg 
        return None

    def attach_file_arg(self):
        if self.args.attach_files != None:  
            return self.args.attach_files.split(",")
        return None

    def modes_cli_status(self):
        # Msg mode cli + Attach mode cli
        if (self.args.msg_mode != None) and (self.args.attach_mode != None):
            return True, True

        # Msg cli mode + no attach cli mode    
        elif (self.args.msg_mode != None) and (self.args.attach_mode == None):
            return True, False

        # no msg cli mode  + attach cli mode
        elif (self.args.msg_mode == None) and (self.args.attach_mode != None):
            return False, False

        # no msgg cli mode + no attach mode
        return False, False


    def implicit_modes(self):
        senders = self.recipient_arg()
        msg = self.msg_arg()
        attach = self.attach_file_arg() 

        no_defalut_msg_mode, no_default_attach_mode = self.modes_cli_status()
        if no_defalut_msg_mode == False:
            ######## Msg
            ## "both" mode
            # files(insides msgs) + CLI msg
            if (not(not senders[2])) and (msg != None):
                self.args.msg_mode = "both"

            ## "cli"  mode
            # No files + cli msg
            elif (not senders[2]) and (msg != None):
                self.args.msg_mode = "cli"

            ## 'file' mode
            # Files + no cli msg
            elif (not(not senders[2])) and (msg == None):
                self.args.msg_mode = "file"

            ## "none" mode
            # No file + no cli msg
            elif (not senders[2]) and (msg == None):
                self.args.msg_mode = "none"

        if no_default_attach_mode == False:
            ############## Attachment
            # files(insides attachments) + CLI attachments
            if (not(not senders[2])) and (not(not attach)):
                self.args.attach_mode = "both"

            # No files + cli attach
            elif (not senders[2]) and (not(not attach)):
                self.args.attach_mode = "cli"

            # Files + no cli attaches
            elif (not(not senders[2])) and (not attach):
                self.args.attach_mode = "files"

            # No file + no cli attachments
            elif (not senders[2]) and (not attach):
                self.args.attach_mode = "none"
            
        return [self.args.msg_mode, self.args.attach_mode]



if __name__ == "__main__":
    cli_args =  CLIArguments()  

    recipients = cli_args.recipient_arg()
    message = cli_args.msg_arg()
    attachments= cli_args.attach_file_arg() 
    implicit_modes = cli_args.implicit_modes()
    print(f" {implicit_modes} {recipients} {message} {attachments}")

