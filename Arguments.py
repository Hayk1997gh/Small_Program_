import argparse

parser = argparse.ArgumentParser(description='Defining arguments of the program.')
parser.add_argument('--title', default="New Spreadsheet")
parser.add_argument('--credentials')
parser.add_argument('--email')
parser.add_argument('--csv')

args = parser.parse_args()
