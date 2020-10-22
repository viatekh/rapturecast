import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)


#todo parse sheet number at runtime
sheet = client.open("RN").sheet1


# Extract and print all of the values
# list_of_hashes = sheet.get_all_records()
# print(list_of_hashes)

maxrows = 39
# print (maxrows)

row = 1
# wh not for i in int? why i for int(range)?
for row in range(1, maxrows):
#check for text "albums:" or "EPs:" beleive : is giving error
#review not published yet needs work
# if sheet.cell(row,1).value not in ("-", "Albums:", "EPs:", "review not published yet", "TBC"):
#
#     if sheet.cell(row,2).value in ("review not published yet"):
#         sheet.update_cell(row,3,"review not published yet")
#         sheet.update_cell(row,5,"review not published yet")
#         sheet.update_cell(row,4,"review not published yet")
#     else:

    currentRow = sheet.row_values(row,value_render_option='FORMATTED_VALUE')
    # raLink = currentRow[1]
    link = currentRow[0]

    print link
