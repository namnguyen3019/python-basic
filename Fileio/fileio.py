# openNam = open("sample.txt")
#
# for line in openNam:
#     print(line)
# openNam.close()

# with open("sample.txt", 'r') as openNam:
#     for line in openNam:
#         print(line, end='')

# with open('sample.txt', 'r') as openName:
#     line = openName.readline()
#     while line:
#         print(line, end='')
#         line = openName.readline()

with open('sample.txt', 'r') as openName:
    lines = openName.readlines()
    for line in lines:
        print(line, end = '')


