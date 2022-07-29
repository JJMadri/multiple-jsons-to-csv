#import packages
import json, os
from textwrap import indent
import pandas as pd

#get all folder names from the specific folders
Mainpath = "[YOUR_MAIN_FOLDER_PATH]"
list_subfolders = [f.name for f in os.scandir(Mainpath) if f.is_dir()]

#doing the same procces for every folder name
for p in list_subfolders:
    #defining the path to the folder
    path_to_json = Mainpath + p

    #Getting all json file names
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

    #doing the same process for every file
    for x in json_files:
        #open the file
        with open(path_to_json + '/' + x, 'r+', encoding='utf-8') as file:
            file_data = json.load(file)
        
        #adding the date
        for d in file_data:
            d["date"] = x

        #saving the changes
        with open(path_to_json + '/' + x, 'w') as file:
            json.dump(file_data, file, indent = 4)

    #Defining final jsonfile to convert to csv
    json_final = pd.DataFrame()

    #Merging all json files in one file
    for x in json_files:
        temp = pd.read_json(path_to_json + '/' + x)
        json_final = json_final.append(temp, ignore_index = True)

    #conversion from json to csv
    json_final.to_csv(os.path.join(path_to_json,r'Final_'+ p +'.csv'))
