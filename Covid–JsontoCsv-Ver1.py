import urllib
import json
import csv
import os

import sys
reload(sys)
sys.setdefaultencoding('utf8')

print("hello world")
print("iuta")

def main():

    path = '/Users/carlosandressalazar/Downloads/2020-03-13/biorxiv_medrxiv/'
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            with open(filename, 'r') as myfile:
                try:
                    obj = json.load(myfile)
                    try:
                        print str(obj["metadata"]["authors"][0]["last"])
                    except IndexError:
                        gotdata = 'null'
                except ValueError:
                    gotdata = 'null'


    with open('testcovid.csv', 'w') as csv_file_covid:
            csv_writer_covid = csv.writer(csv_file_covid)
            csv_writer_covid.writerow(['title','authors'])

            for root, dirs, files in os.walk(path, topdown=False):
                for namecsv in files:
                    filenamecsv = os.path.join(root, namecsv)
                    with open(filenamecsv, 'r') as myfilecsv:
                        try:
                            objcsv = json.load(myfilecsv)
                            try:
                                csv_title = str(objcsv["metadata"]["title"])
                                csv_abstract = str(objcsv["metadata"]["authors"][0]["last"])
                                csv_writer_covid.writerow([csv_title] + [csv_abstract]) 
                            except IndexError:
                                gotdata = 'null'
                        except ValueError:
                            gotdata = 'null'
if __name__ == '__main__':
    main()