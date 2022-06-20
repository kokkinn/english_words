import openpyxl
import json

loc = "Untitled_spreadsheet.xlsx"

wb_obj = openpyxl.load_workbook(loc)


sheet = wb_obj.active
jsonfile = open("words.json", "w", encoding="utf-8")
tempdict = {}
for i in range(2, 11):
    tempdict[sheet[f"B{i}"].value] = sheet[f"C{i}"].value

jsonfile.write(json.dumps(tempdict, ensure_ascii=False))
jsonfile.close()
