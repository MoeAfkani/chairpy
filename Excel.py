from openpyxl import load_workbook
wb = load_workbook("Book1.xlsx")
ws = wb.active
save = open("save.txt","a")
for vals in ws.values:
    for i in vals:
        save.write(str(i)+"\t")
    save.write("\n")