result = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id, range=range_name).execute()
rows = result.get('values', [])
print('{0} rows retrieved.'.format(len(rows)))
