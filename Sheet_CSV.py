from __future__ import print_function
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import Arguments

args = Arguments.args

def authorization():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        args.credentials, scope)
    return gspread.authorize(credentials)

def create_spreadsheet(client):
    speadsheet = client.create(args.title)
    speadsheet.share(args.email, perm_type='user', role='writer')

def import_csv(client):
    speadsheet = client.open(args.title)
    content = open(args.csv, 'r').read()
    client.import_csv(speadsheet.id, content)

if __name__ == '__main__':
    client = authorization()
    create_spreadsheet(client)
    import_csv(client)
