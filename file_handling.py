#opening a file
file = open("example.txt","w")

#writing in a file
file.write("Hello World!\n")
file.write("This is a second line")

#reading a file
file = open("example.txt","r")
content=file.read()
print(content)

#appending a file
file = open("example.txt","a")
file.write("\nThis is an appended line")

#closing a file
file.close()

#checking if file exists
import os

if os.path.exists("example.txt"):
    print("file exists")
else:
    print("File does not exists")

#reading and writing (r+ mode)
file = open("example.txt","r+")
file.write("Overwritten line in r+ mode.\n")
file.seek(0)
print("\n--- r+ mode content ---")
print(file.read())
file.close()

#  Writing and reading (w+ mode) 
file = open("example.txt", "w+")
file.write("W+ mode overwrites everything.\n")
file.seek(0)
print("\n--- w+ mode content ---")
print(file.read())
file.close()

 # Appending and reading (a+ mode) ===
file = open("example.txt", "a+")
file.write("Appended again using a+ mode.\n")
file.seek(0)
print("\n--- a+ mode content ---")
print(file.read())
file.close()

