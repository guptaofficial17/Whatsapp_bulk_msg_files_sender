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
            choices=("both, cli, file, no"),
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
            choices=("both, cli, file, no"),
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

    def modes(self):
        if (self.args.msg_mode != None) and (self.args.attach_mode != None):
            return [self.args.msg_mode, self.args.attach_mode]
        elif (self.args.msg_mode != None) and (self.args.attach_mode == None):
            return [self.args.msg_mode, None]
        elif (self.args.msg_mode == None) and (self.args.attach_mode != None):
            return [None, self.args.attach_mode]
        return [None, None]

if __name__ == "__main__":
    cli_args =  CLIArguments()  

    modes = cli_args.modes()
    recipients = cli_args.recipient_arg()
    message = cli_args.msg_arg()
    attachments= cli_args.attach_file_arg() 

    print(f" {modes} {recipients} {message} {attachments}")

# python3 args.py -r "hamza,Linear aljebra,923370392561,923342843869,file.csv,o.xlsx" -m "Hi" -amode both -af 1.png,2.png -mmode both
# ['both', 'both'] [[923370392561, 923342843869], ['hamza', 'Linear aljebra'], ['file.csv', 'o.xlsx']] Hi ['1.png', '2.png']
