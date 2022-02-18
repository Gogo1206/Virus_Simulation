import xlwt

wb = xlwt.Workbook()
sheet1 = wb.add_sheet('Data')

def start():
    write(0,0,"Hour #")
    write(0,1,"S #")
    write(0,2,"I #")
    write(0,3,"R #")
    write(0,4,"infection rate")
    write(0,5,"recovery rate")

def write(row,column,context):
    sheet1.write(row, column, context)
    wb.save('Data.xls')