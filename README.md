**DESCRIPTION**

The small project is for creating Google spreadsheet and uploading CSV files

**Requirements**

- Gspread 
- Oauth2client
- Python 3.x

*Install all necessary packages*

- $. Install package for Gspread framework
- $. Install package for Oauth2client
- $. Obtain OAuth2 credentials from Google Developers Console 'https://gspread.readthedocs.io/en/latest/oauth2.html'
     (Also You can use the default one in resources folder)

  To run the code you need to pass program the following arguments.

**CMD arguments**

--title : choose title for your spreadsheet name.
--credentials : choose file from where the google credentials will be read (path).
--email : choose email to share the spreadsheet with.
--csv : choose csv file to import into spreadsheet (path).

**Run command example**

python Sheet_CSV.py --title New_Spreadsheet --credentials /home/hayk/Downloads/My_Project_56597-7c4c5d90719d.json --email hkazaryan.97@gmail.com --csv /home/hayk/Downloads/annual-enterprise-survey-2017-financial-year-provisional-csv.csv
