# # Assignment: Finding Numbers in a Haystack
# import re
# handle = open('regex_sum_907674.txt')
# soma = 0

# for line in handle:
#     line = line.rstrip()
#     strNumbers = re.findall('[0-9]+', line)
#     if len(strNumbers) < 1 : continue
#     fltNumbers = [float(i) for i in strNumbers]
#     #print(fltNumbers)
#     #print(sum(fltNumbers))
#     soma += sum(fltNumbers)

# print(soma)

# Assignment: Exploring the HyperText Transport Protocol
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
