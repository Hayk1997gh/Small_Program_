from __future__ import print_function
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import Arguments

def main():

    args = Arguments.args
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        args.credentials, scope)

    gc = gspread.authorize(credentials)
    sh = gc.create(args.title)
    sh.share(args.email, perm_type='user', role='writer')
    sh = gc.open(args.title)
    content = open(args.csv, 'r').read()
    gc.import_csv(sh.id, content)

if __name__ == '__main__':
    main()