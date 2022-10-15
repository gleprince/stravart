# stravart : strava analysis

## Project Description

TODO:
- add description
- add screenshots

## How-to

All the process is located in the main folder

First you need to download : 
- [7zip](https://www.7-zip.org/download.html)
- [fitSDK](https://developer.garmin.com/fit/download/)

Then python and the following libraries : 
- simplekml
- gpxpy

The structure of folder should be :

```
.
└── project_name
    ├── data
    │   ├── processed_data
    │   │   ├── user1
    │   │   │   ├── csv
    │   │   │   └── kml
    │   │   └── user2
    │   │       ├── csv
    │   │       └── kml
    │   ├── user1
    │   │   └── all_strava_data_from_user1
    │   └── user2
    │       └── all_strava_data_from_user2
    └── stravart
```


The output is located in the kml folder

Then the process is as follow : 

1. Unzip all the .gz files in the nameX/activity/ folder with unzip_files.bat (you have to locate your terminal inside this folder)
2. Run fit2raw_csv.ipynb
3. Run raw_csv2csv.ipynb
4. Run generate_kml_tracemap.ipynb
5. The map is created in the kml folder !


## Contribute :factory-worker:

* Install [poetry](https://python-poetry.org/)
* Run the following commands in you cloned version of this repo
  ```sh
  poetry install
  poetry shell
  jupyter-lab
  ```
