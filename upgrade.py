import paramiko

ip='135.249.191.197'
port=22
username='root'
password='snr@1234'

with open("cmdOutput.txt","a") as outputFile:

    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port,username,password)

    with open("cmdInput.txt") as inputFile:
        for line in inputFile:
            print (line)
            outputFile.write(line)
            outputFile.write("-"*10)
            outputFile.write("\n")
            stdin,stdout,stderr=ssh.exec_command(line)
            outlines=stdout.readlines()
            resp = ''.join(outlines)
            outputFile.write(resp)

            errlines=stderr.readlines()
            err=''.join(errlines)
            if err != "":
                outputFile.write("PrintError:")
                outputFile.write(err)

            outputFile.write("=" * 79)
            outputFile.write("\n")



    ssh.close()


