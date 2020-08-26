jabber = open('sample.txt', 'r')

for line in jabber:
    print(line)

jabber.close()
# need to close file


with open('sample.txt', 'r') as jabber:
    for line in jabber:
        if 'JAB' in line.upper():
            print(line, end='')
# no need to close file
