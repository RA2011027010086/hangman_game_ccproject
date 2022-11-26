import socket
import re
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost',8089))
print("Enter word: ")
inp = input()
regex =  re.compile('[@_!#$%^&*()<>?/\|}{~:1234567890]')
if len(inp) <= 14 and regex.search(inp) is None:
    print("Enter hint : ")
    hint  = input()
    inpt = inp + ',' + hint
    clientsocket.send(bytes(inpt, 'UTF-8'))
    print("The message has been sent")
else:
    print("Please add the word of less than 10 characters and with no specail characters ,numbers")