with open('testfile.txt', 'r') as rf:
    with open('testwrite.txt', 'w') as wf:
        wf.write(rf.read()[::-1])

print(open('testfile.txt', 'r').read(), '\n\n---------------------------------\n')
print(open('testwrite.txt', 'r').read(), '\n\n---------------------------------\n')

with open('testfile.txt', 'r') as rf:
    a = rf.readlines()[::-1]
    with open('testwrite.txt', 'w') as wf:
        wf.writelines(a)

print(open('testwrite.txt', 'r').read())
