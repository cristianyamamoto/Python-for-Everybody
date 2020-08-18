# # Assignment 6.5
# text = "X-DSPAM-Confidence:    0.8475"

# place = text.find(":")

# print(float(text[place+5:]))

# # Assignment 7.1
# # Use words.txt as the file name
# fname = input("Enter file name: ")
# fh = open(fname)

# for line in fh:
#     line = line.rstrip()
#     print(line.upper())

# # Assignment 7.2
# # Use the file name mbox-short.txt as the file name
# fname = input("Enter file name: ")
# fh = open(fname)
# soma = 0
# contador = 0
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:") : continue
#     line = line.rstrip()
#     place = line.find(":")
#     soma += float(line[place+1:])
#     contador = contador + 1
# #print(contador)    
# #print(soma)
# print("Average spam confidence:", soma/contador)

# # Assignment 8.4
# fname = input("Enter file name: ")
# fh = open(fname)
# lst = list()
# for line in fh:
#     line = line.rstrip()
#     lineWords = line.split()
#     for words in lineWords:
#         if words not in lst:
#             lst.append(words)

# lst.sort()
# print(lst)

# # Assignment 8.5
# fname = input("Enter file name: ")
# if len(fname) < 1 : fname = "mbox-short.txt"

# fh = open(fname)
# count = 0

# for line in fh:
#     if not line.startswith("From ") : continue
#     line = line.rstrip()
#     lineWords = line.split()
#     print(lineWords[1])
#     count += 1

# print("There were", count, "lines in the file with From as the first word")

# # Assignment 9.4
# name = input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
# handle = open(name)

# counts = dict()
# for line in handle:
#     if not line.startswith("From ") : continue
#     line = line.rstrip()
#     lineWords = line.split()
#     word = lineWords[1]
#     counts[word] = counts.get(word, 0) + 1

# bigcount = None
# bigword = None
# for word,count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count

# print(bigword, bigcount)

# # Assignment 10.2
# name = input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
# handle = open(name)

# counts = dict()
# for line in handle:
#     if not line.startswith("From ") : continue
#     line = line.rstrip()
#     lineWords = line.split()
#     hour = lineWords[5].split(':')
#     counts[hour[0]] = counts.get(hour[0], 0) + 1

# lst = counts.items()
# # for key, val in counts.items():
# #     newtup = (key, val)
# #     lst.append(newtup)
# lst = sorted(lst)

# for key, val in lst:
#     print(key, val)
