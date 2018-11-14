import paramiko

ip='135.249.191.197'
port=22
username='root'
password='snr@1234'

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip,port,username,password)

with open("cmdInput.txt") as inputFile:
    for line in inputFile:
        #print (line)

        lineStrip = line.strip("\n")


        lc = "echo " + lineStrip + " >> output.txt"
       # print(lc)
        stdin,stdout,stderr=ssh.exec_command(lc)
        lex = line + lineStrip + " &>> output.txt"
        print (lex)
        stdin,stdout,stderr=ssh.exec_command(lex)

ssh.close()


