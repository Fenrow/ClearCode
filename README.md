# ClearCode

The requirements.txt file contains all the necessary plugins

First Task:

Variables:

filename - name of CSV file with data to generate raport. default: 'filename.csv'
raport_filename - name of CSV file with generated data. default: 'raport.csv'

method of operation:

1.Open filename.csv
2.Read header line
3.Read rest of line
3.1.Read date and save in right format
3.2.Check country name if exist save three letters code if not save 'XXX' as code
3.3.Read NOI (number of impressions)
3.4.Calculate NOC (number of clicks) as ( NOI * NOC (from filenmae.csv) ) / 100
4.Write header line in raport file ('Date','Country code','Impressions','Number of clicks')
5.Write rest of data

Second Task:

# I changed all 'http://0.0.0.0:8000' to 'http://localhost:8000' because python
# creating the http.server displays all pages under the address localhost: 8000

Variables:

map it is a dictionary for all links creating a site map
domain_url is a url of site we want to map

method of operation:

1.Creating soup from BeautifulSoup4
2.Searching for all links
2.1.If link end with '.html' or it's a main site append to list
3.Creating a dictionary
4.Checking all links and repeat from point 1.
5.Print full site map
