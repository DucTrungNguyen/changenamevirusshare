import os
import sys
def change(source_folder, FOLDER_CHANGENAME):

    for filename in os.listdir(source_folder):
        pathOldName = os.path.join(source_folder, filename)
        name  = filename
        if name.endswith(".apk"):
            if name.startswith("VirusShare_"):
                arr = name.split("_")
                pathNewName = os.path.join(source_folder, arr[1])
                os.rename(pathOldName, pathNewName)
        else:
            if name.startswith("VirusShare_"):
                arr = name.split("_")
                pathNewName = os.path.join(source_folder, arr[1] + ".apk")
                os.rename(pathOldName, pathNewName)
            else:
                pathNewName = os.path.join(source_folder, name + ".apk")
                os.rename(pathOldName, pathNewName)

    print("End change name VirusShare")
