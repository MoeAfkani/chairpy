from openpyxl import load_workbook


def excel(file):
    ''' This is function to export Excel file
        to Python list'''

    wb = load_workbook(file)
    ws = wb.active
    return list(ws.values)

class Human:
     def __init__(self,_id,Fname,Lname):
        self.id = _id
        self.Fname = Fname
        self.Lname = Lname



class Student(Human):
      pass




class Teacher(Human):
      pass
