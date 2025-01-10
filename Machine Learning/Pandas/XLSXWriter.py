import os
import fnmatch
from sys import argv
import xlsxwriter

def ExcelCreate(name):
    workbook = xlsxwriter.Workbook(name)
    worksheet = workbook.add_worksheet()
    
    worksheet.write('A1', 'Name')
    worksheet.write('B1', 'College')
    worksheet.write('C1', 'Mail ID')
    worksheet.write('D1', 'Mobile')
    
    workbook.close()

def main():
    print("---- Marvellous Infosystems by Piyush Khairnar -----")
    print("Application name: " + argv[0])

if __name__ == "__main__":
    main()
