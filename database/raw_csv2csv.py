
import os
import subprocess
import re

path = "C:\\Users\\guilhem.leprince\\Documents\\strava"

# imp module
# assign directory
directory = path + "\\data\\remi\\activities"
FIT_FILE = re.compile("\\d+.fit(?!.gz)")
GPX_FILE = re.compile("\\d+.gpx")
CSV_FILE = re.compile("\\d+.csv")

list_of_fit_files=[]
list_of_gpx_files = []
list_of_raw_csv_files = []

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f) and FIT_FILE.match(filename):
        list_of_fit_files.append(f)
    if os.path.isfile(f) and GPX_FILE.match(filename):
        list_of_gpx_files.append(f)


# Use only when decoding fit file needed
for fit_file in list_of_fit_files:
    subprocess.call("java -jar C:\\Users\\guilhem.leprince\\Documents\\strava\\sdk\\java\\FitCSVTool.jar " + fit_file)

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f) and CSV_FILE.match(filename):
        list_of_raw_csv_files.append(f)

print("A total of " + str(len(list_of_raw_csv_files)) + " csv file found")



