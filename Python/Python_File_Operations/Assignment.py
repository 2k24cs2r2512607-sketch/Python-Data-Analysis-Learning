with open(r"D:\Python-Data-Analysis-Learning\Python\Python_File_Operations\names.txt",'w') as f:
    for _ in range(5):
        name=input("Enter name-")
        f.write(name+"\n")