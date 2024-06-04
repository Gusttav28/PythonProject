import pandas as pd
import openpyxl
import requests
import json

# extracting the data from the page and converted into a json file
rute = requests.get("http://jsonplaceholder.typicode.com/posts").text

# locking into the page and make it readable and saving it in a variable
jsonObj = json.loads(rute)

# checking if everyting goes well, and printing the data in the terminal
for i in jsonObj:
    print(i, "\n")

# process to converted the data finally into a json file
with open("jsonFile.json", "w") as file:
    json.dump(jsonObj, file, indent=4, separators=(",", " : "))


json_file_rute = pd.read_json('jsonFile.json')
excel_file = json_file_rute.to_excel("excel_file.xlsx")


