def swapFileData():
    file1 = input("Enter file 1 name: ")
    file2 = input("Enter file 2 name: ")

    dataA = open(file1,'r')
    dataB = open(file2,'r')

    file1R = open(file1, 'a')
    file1R.write(dataB.read())

    file2R = open(file2, 'a')
    file2R.write(dataA.read())

swapFileData()