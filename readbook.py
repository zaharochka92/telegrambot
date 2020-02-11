def addread(line):
    with open('reed.txt','a') as f:
        f.write(line)
        f.write('\n')

def readread():
    with open('reed.txt','r') as f:
        return f.read()

def clearread():
    with open('reed.txt', 'w') as f:
        f.write('')
