import paramiko
import os


class SSHClient:

    def __init__(self, hostname, user, pwd, port=22):
        self.s = paramiko.SSHClient()
        self.s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.s.connect(hostname, port, user, pwd)

    def exec(self, command):
        stdin, stdout, stderr = self.s.exec_command(command)
        if stdout:
            stdout = bytes.decode(stdout.read())
            print(stdout)
        if stderr:
            stderr = bytes.decode(stderr.read())
            print(stderr)

    def put_file(self, src, target):
        sftp = paramiko.SFTPClient.from_transport(self.s)
        if os.path.isfile(src):
            sftp.put(src, target)

    def __del__(self):
        self.s.close()