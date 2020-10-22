import gspread
import soundscrape
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('./creds/rapturecast_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open('RN').sheet1

# soundscrap set up
vargs =	{
'artist_url': 'https://soundcloud.com/auratekh/sets/sonic-rites',
'num_tracks': 9223372036854775807,
'group': False,
'bandcamp': False,
'mixcloud': False,
'audiomack': False,
'hive': False,
'likes': False,
'login': 'soundscrape123@mailinator.com',
'downloadable': False,
'track': '',
'folders': False,
'path': './music',
'password': 'soundscraperocks',
'open': False,
'keep': False,
'version': False
}

links = sheet.get_all_records()
for x in links:
    url = x.get("LINK")
    print (url)
    vargs['artist_url'] = url
    soundscrape.process_soundcloud(vargs)
