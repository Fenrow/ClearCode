"""
Python Intern Task - CSV Report Processing

Input format: UTF-8 or UTF-16 CSV file (with any kind of line endings), with
columns:
date (MM/DD/YYYY),
state name,
number of impressions,
CTR percentage.

Output format: UTF-8 CSV file with Unix line endings, with columns:
date (YYYY-MM-DD),
three letter country code (or XXX for unknown states),
number of impressions,
number of clicks (rounded, assuming the CTR is exact).
Rows are sorted lexicographically by date followed by the country code.
"""
import csv
from datetime import datetime
import pycountry

#Filename input CSV file
filename = 'filename.csv'
#Filename output CSV file
raport_filename = 'raport.csv'

#noi - number of impressions, noc - number of clicks
dates, codes, noi, noc = [], [], [], []

countries_sub=list(pycountry.subdivisions)#List of countries subdivisions

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        current_date = datetime.strptime(row[0], "%m/%d/%Y")
        dates.append(current_date.date()) #Append date in output format Y-M-D

        exist = False

        for s in countries_sub:
            if s.name == row[1]:
                country = pycountry.countries.get(alpha_2=s.country_code)
                exist = True
                break

        if exist:
            codes.append(country.alpha_3)
        else:
            codes.append('XXX')

        noi.append(row[2])
        row[3] = row[3].replace('%','')
        current_noc = (int(row[2]) * float(row[3])) / 100
        noc.append(int(current_noc))

#Save first row with headers
with open(raport_filename, 'w', newline='') as f:
    header = ['Date','Country Code','Impressions','Number of clicks']
    writer = csv.writer(f)
    writer.writerow(header)

#Save rest of data
for i in range(0,len(dates)):
    lines_to_csv = []
    lines_to_csv.append(dates[i])
    lines_to_csv.append(codes[i])
    lines_to_csv.append(noi[i])
    lines_to_csv.append(noc[i])

    with open(raport_filename, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(lines_to_csv)
