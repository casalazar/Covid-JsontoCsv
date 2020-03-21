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

    path_bio = '/Users/carlosandressalazar/Downloads/2020-03-13/biorxiv_medrxiv/'
    path_comm = '/Users/carlosandressalazar/Downloads/2020-03-13/comm_use_subset/'


    for root, dirs, files in os.walk(path_bio, topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            with open(filename, 'r') as myfile:
                try:
                    obj = json.load(myfile)
                    try:
                        print str(obj["metadata"]["title"])
                    except IndexError:
                        gotdata = 'null'
                except ValueError:
                    gotdata = 'null'

    
    for root, dirs, files in os.walk(path_comm, topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            with open(filename, 'r') as myfile:
                try:
                    obj = json.load(myfile)
                    try:
                        print str(obj["metadata"]["title"])
                    except IndexError:
                        gotdata = 'null'
                except ValueError:
                    gotdata = 'null'


    with open('testcovid_biorxiv_medrxiv.csv', 'w') as csv_file_covid_bio:
            csv_writer_covid_bio = csv.writer(csv_file_covid_bio)
            csv_writer_covid_bio.writerow(['title','abstract','bodytext'])

            for root, dirs, files in os.walk(path_bio, topdown=False):
                for namecsv_bio in files:
                    filenamecsv_bio = os.path.join(root, namecsv_bio)
                    with open(filenamecsv_bio, 'r') as myfilecsv_bio:
                        try:
                            objcsv_bio = json.load(myfilecsv_bio)
                            try:
                                csv_title_bio = str(objcsv_bio["metadata"]["title"])
                                csv_abstract_bio = str(objcsv_bio["abstract"][0]["text"])
                                csv_bodytext_bio = str(objcsv_bio["body_text"][0]["text"])
                                csv_writer_covid_bio.writerow([csv_title_bio] + [csv_abstract_bio] + [csv_bodytext_bio]) 
                            except IndexError:
                                gotdata = 'null'
                        except ValueError:
                            gotdata = 'null'

    with open('testcovid_comm_use_subset.csv', 'w') as csv_file_covid_comm:
            csv_writer_covid_comm = csv.writer(csv_file_covid_comm)
            csv_writer_covid_comm.writerow(['title','abstract','bodytext'])

            for root, dirs, files in os.walk(path_comm, topdown=False):
                for namecsv_comm in files:
                    filenamecsv_comm = os.path.join(root, namecsv_comm)
                    with open(filenamecsv_comm, 'r') as myfilecsv_comm:
                        try:
                            objcsv_comm = json.load(myfilecsv_comm)
                            try:
                                csv_title_comm = str(objcsv_comm["metadata"]["title"])
                                csv_abstract_comm = str(objcsv_comm["abstract"][0]["text"])
                                csv_bodytext_comm = str(objcsv_comm["body_text"][0]["text"])
                                csv_writer_covid_comm.writerow([csv_title_comm] + [csv_abstract_comm] + [csv_bodytext_comm]) 
                            except IndexError:
                                gotdata = 'null'
                        except ValueError:
                            gotdata = 'null'


if __name__ == '__main__':
    main()