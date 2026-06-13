import os

print("Current folder:", os.getcwd())

file = open("sample.log", "r")

content = file.read()

print(content)

file.close()