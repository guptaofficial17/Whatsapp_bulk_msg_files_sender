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
                    fileList.append(recipient)
                else:
                    namesList.append(recipient)
        return [numberList, namesList, fileList]

    def msg_arg(self):
        if self.args.msg != None:
            return self.args.msg 
        return None

    def attach_file_arg(self):
        if self.args.attach_files != None:  
            return self.args.attach_files.split(",")
        return None

    def explicit_modes(self):
        if (self.args.msg_mode != None) and (self.args.attach_mode != None):
            return [self.args.msg_mode, self.args.attach_mode]
        elif (self.args.msg_mode != None) and (self.args.attach_mode == None):
            return [self.args.msg_mode, None]
        elif (self.args.msg_mode == None) and (self.args.attach_mode != None):
            return [None, self.args.attach_mode]
        return [None, None]

    def implicit_modes(self):
        senders = self.recipient_arg()
        msg = self.msg_arg()
        attach = self.attach_file_arg() 

        ## "both" mode
        # files(insides msgs) + CLI msg
        if (None not in senders[2]) and (msg != None):
            self.args.msg_mode = "both"

        # files(insides attachments) + CLI attachments
        if (None not in senders[2]) and (None not in attach):
            self.args.attach_mode = "both"

        ## "cli"  mode
        # No files + cli msg
        if (None in senders[2]) and (msg != None):
            self.args.msg_mode = "cli"

        # No files + cli attach
        if (None in senders[2]) and (None not in attach):
            self.args.attach_mode = "cli"

        ## 'file' mode
        # Files + no cli msg
        if (None not in senders[2]) and (msg == None):
            self.args.msg_mode = "file"

        # Files + no cli attaches
        if (None not in senders[2]) and (None in attach):
            self.args.attach_mode = "files"

        ## "none" mode
        # No file + no cli msg
        if (None in senders[2]) and (msg == None):
            self.args.msg_mode = "none"

        # No file + no cli attachments
        if (None in senders[2]) and (None in attach):
            self.args.attach_mode = "none"



if __name__ == "__main__":
    cli_args =  CLIArguments()  

    modes = cli_args.modes()
    recipients = cli_args.recipient_arg()
    message = cli_args.msg_arg()
    attachments= cli_args.attach_file_arg() 

    print(f" {modes} {recipients} {message} {attachments}")

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