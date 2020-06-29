file1 = open('abc.txt','r')
lines = file1.readlines()
count = 0
for line in lines:
    print("line{}: {}".format(count,line.strip()))
    count=count+1
