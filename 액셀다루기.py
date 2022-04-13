import win32com.client

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True
wb = excel.Workbooks.Open('C:\\Users\\realadmin\\Desktop\\input.xlsx')
ws = wb.ActiveSheet
ws.Cells(1,2).Value = "is"
ws.Range("C1").Value = "good"
print(ws.Cells(1,3).Value)
excel.Quit()