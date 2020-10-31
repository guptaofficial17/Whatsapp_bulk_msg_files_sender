import argparse

class CLIArguments:
    def __init__(self):
        parser = argparse.ArgumentParser(description="Bulk msg sender")
        
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
            # default="both",
            help='''File/s to import.\
                That will send to all targeted recipients'''
        )
        self.args = parser.parse_args()


    # def recipient_arg(self):    
    #     # Sender handling
    #     if self.args.file != None:
    #         return self.args.file
    #     elif self.args.name != None:
    #         return self.args.name
    #     elif self.args.number != None:
    #         return self.args.number

    # def msg_arg_with_mode(self):
    #     if self.args.msg != None:
    #         if self.args.msg_mode == "both":
    #             return self.args.msg, "both"
    #         elif self.args.msg_mode == "cli":
    #             return self.args.msg, "cli"
    #         elif (self.args.msg_mode == "file") and (self.args.file != None):
    #             return self.args.msg, "file"        
    #     # elif self.args.msg == 
    #     return None, None

    # def attach_file_arg_with_mode(self):
    #     if self.args.attach_files != None:
    #         if self.args.attach_mode == "both":
    #             return self.args.attach_files.split(","), 'both'
    #         elif self.args.attach_mode == "cli":
    #             return self.args.attach_files.split(","), 'cli'
    #         elif self.args.attach_mode == "file":
    #             return self.args.attach_files.split(","), 'file'
    #     return None, None

if __name__ == "__main__":
    cli_args =  CLIArguments()  

    # recipients = cli_args.recipient_arg()
    # message, mm = cli_args.msg_arg_with_mode()
    # attachments, am = cli_args.attach_file_arg_with_mode() 

    # print(f"{recipients} {message}:{mm} {attachments}:{am}")

# python3 args.py -r hamza -m "Hi" -af 1.png
