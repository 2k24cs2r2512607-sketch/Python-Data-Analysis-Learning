# ✅ How to print lines as normal text instead of a list
# 1. Using a loop:
'''
with open("iram.txt",mode="r") as handle:
    lines=handle.readlines()
for line in lines:
    print(line.strip())'''


# 2. Read the whole file as a single string (no list):
with open('iram.txt','r') as file:
    content=file.read()
print(content)