import xlrd

book = xlrd.open_workbook('resources/file_example_XLS_10.xls')
print(book.nsheets)
print(book.sheet_names())
sheet = book.sheet_by_index(0)
print(f'{sheet.ncols} X {sheet.nrows}')
print(sheet.cell(rowx=9, colx=3).value)

for row in range(sheet.nrows):
    print(sheet.row(rowx=row))
