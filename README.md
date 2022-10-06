# stravart : strava analysis

All the process is located in the main folder

First you need to download : 
- [7zip](https://www.7-zip.org/download.html)
- [fitSDK](https://developer.garmin.com/fit/download/)

Then python and the following libraries : 
- simplekml
- gpxpy

The structure of folder should be :

- project_name
- - this current repo
- - data
- - - name1
- - - - his strava data folder
- - - name2
- - - - his strava data folder
- - - processed_data
- - - - name1
- - - - - csv
- - - - - kml
- - - - name2
- - - - - csv
- - - - - kml
The output is located in the kml folder

Then the process is as follow : 

- 1. Unzip all the .gz files in the nameX/activity/ folder with unzip_files.bat (you have to locate your terminal inside this folder)
- 2. Run fit2raw_csv.ipynb
- 3. Run raw_csv2csv.ipynb
- 4. Run generate_kml_tracemap.ipynb
- 5. The map is created in the kml folder !
