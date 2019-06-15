import os
import csv
import os.path
from os import path
heading = ["School Name","January","February","March","April","May","June","July","August","September","October","November","December"]

def schoolsIter(schoolName):
	path = '/home/ab.bhatnagar/Downloads/csvFilledData/schools/'+str(schoolName)
	files = []
	for r, d, f in os.walk(path):
	    for file in f:
	        if '.csv' in file:
	            files.append(os.path.join(r, file))
	data = {}
	for f in files:
		with open(f, 'r') as ff:
			reader = csv.reader(ff)
			row_count = list(reader)
			row_count = len(row_count)
			# row_count = sum(1 for row in reader)
			month = f.split('/')[7]
			if not month in data:
				data[month] = 0
			if row_count > 1:
				data[month] += 1
			data['School Name'] = f.split('/')[6]
	values = []
	if 'School Name' in data:
		for headingItr in range(len(heading)):
			values.append(data[heading[headingItr]])
	return values

for dirItr in range(len(os.listdir('.'))):
	schoolName = os.listdir('.')[dirItr]
	csvRow =  schoolsIter(schoolName)
	fileName = "schoolsAttendance.csv"
	if len(csvRow) > 1:
		if path.exists(fileName):
			with open(fileName, "a") as file:
				csv_file = csv.writer(file)
				csv_file.writerow(csvRow)
		else:
			with open(fileName, "a") as file:
				csv_file = csv.writer(file)
				csv_file.writerow(heading)
				csv_file.writerow(csvRow)
