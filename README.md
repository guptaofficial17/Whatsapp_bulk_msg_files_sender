# Whatsapp bulk Message & files sender

Whatsapp bot that can send files and messags to recipients.
----------------------------------------------------------------

Sends (messages + files) to recipients (files + names + numbers)

## Aguments 
```
Recipients       -r      [ name/group | file.xlsx/file.csv | number(92xxxxxxxxxx) ]
Message          -m      [ String(from CLI) ]
Attachments      -at     [ List(from CLI attachments) ]
Attachment mode  -amode  [ both(cli + file) | file | cli | none ]
Message mode     -mmode  [ both(cli + file) | file | cli | none ]
```

## Mode args for which recipient?

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



