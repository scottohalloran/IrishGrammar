import gspread

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('1p64P57jLJdIFkOicnGyzK4MJZiLplyVIfZLD6U6QHdo')
worksheet = sh.worksheet("Adjectives")

res = worksheet.get_all_values()
print(res)
#res = worksheet.row_values(1)
#res = worksheet.col_values(1)
#user = ["Susan", 25, "Sydney"]
#


