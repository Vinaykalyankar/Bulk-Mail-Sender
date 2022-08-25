with open("file2.txt", "r") as read_file:
    data = read_file.read()
    l=[]
    for i in data.split():
        l.append(i)
    # print(len(l))
    # for i in l[0:10]:
    #     print(i)
    with open("value.txt",'r') as f: #open a file in the same folder
        a = f.readlines()            #read from file to variable a
    #use the data read
    b = int(a[0])                    #get integer at first position
    val = b+1000                          #increment
    with open("value.txt",'w') as f: #open same file
        f.write(str(val))
    begin=b
    end=val
    print("Range Begin:{}, End: {}".format(begin,end))

    with open("to.txt", "w") as write_file:
        for item in l[begin:end]:
            write_file.write("%s\n" % item)
