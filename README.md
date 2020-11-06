# Whatsapp bulk Messages & files sender

Whatsapp bot that can send files and messags to recipients.
----------------------------------------------------------------

Sends (messages + files) to recipients (files + names + numbers)

![]( image.png )

## Arguments 
```
Recipients       -r      [ name/group | file.xlsx/file.csv | number(92xxxxxxxxxx) ]
Message          -m      [ String(from CLI) ]
Attachments      -at     [ List(from CLI attachments) ]
Attachment mode  -amode  [ both(cli + file) | file | cli | none ]
Message mode     -mmode  [ both(cli + file) | file | cli | none ]
```

## Mode args for recipients?

### Name recipient
Files have two options:
```
1. cli(i.e; messages & attachments only from cli) -> Default
2. none(i.e; neither file nor cli)
```

### File recipient
Files have four options:
```
1. both(file + cli) -> Default
2. file(i.e; messages & attachments only from file)
3. cli(i.e; messages & attachments only from cli)
4. none(i.e; neither file nor cli)
```

### Number recipient
Files have two options:
```
1. cli(i.e; messages & attachments only from cli) -> Default
2. none(i.e; neither file nor cli)
```

## Usage
### Default (No mode arg used)

#### Command
```
python3 script.py\
 -r "file1.xlsx,file2.csv,Twilio, Mehmud,92xxxxxxxxxx"\ -m "Hi from CLI" 
 -af ./file.png 
```

#### Description
```
File recipient: Send messages & attachments from CLI and files also.
Name recipient: Send attachments & messge from CLI only.
Number recipient: Send attachments & messge from CLI only.
```

### Custom args(Mode args used) 

#### Command
```
python3 script.py\
 -r "file1.xlsx,file2.csv,Twilio, Mehmud,92xxxxxxxxxx"\
 -m "Hi from cli" -mmode cli\
 -af 3.svg -amode both
```

#### Description
```
File recipient: Send message from CLI only but send attachments from CLI and file also.
Name recipient: Send attachments & messge from CLI only.
Number recipient: Send attachments & messge from CLI only.
```



