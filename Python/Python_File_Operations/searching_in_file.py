with open("D:\Python-Data-Analysis-Learning\Python\Python_File_Operations\sample.txt",'r') as f:
    data=True
    while data:
        data=f.readline()
        if 'AI0' in data:
            print(True)
            break
    else:
        print(False)