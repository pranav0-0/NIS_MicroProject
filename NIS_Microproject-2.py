#Dependency
import base64
import pyperclip

#Take Input
stringLength = int(input("Enter the length of the string: "))

#Processing
with open("Test.png", "rb") as image_file:
    cString = base64.b64encode(image_file.read())
l = len(cString)
cString = cString[1::l//stringLength]
cString = cString.decode("utf-8")

#Print to Screen
print(cString)

#Copy to Clipboard
pyperclip.copy(cString)
print("Copied to Clipboard")