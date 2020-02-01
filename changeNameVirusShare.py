import os
import sys
import shutil
import argparse

from changeName import change
from classify_VirusShare import  classify

# Define folder
FOLDER_CHANGENAME = "/changeName"
FOLDER_CLASSIFY     = "/classify"

def main():
    print("Start change name and extension VirusShare\n")
    parse = argparse.ArgumentParser("Start change name and extension VirusShare")

    parse.add_argument('-s','--source', help='Source directory for APKs VirusShare', required=True )

    parse.add_argument('-c','--changename', help = 'Change name APKs VirusShare', required = False, default= False, action='store_true')

    parse.add_argument('-cl', '--classify', help='Classify APKs VirusShare', default = False, required= False , action='store_true')



    if len(sys.argv) == 1:
        help()
        sys.exit(1)

    args = parse.parse_args()

    changeName = True
    classify   = False

    source_folder = args.source
    changeName = args.changename
    classify = args.classify

    #source_folder = "/home/nguyentrung/testChangeName"
    #changeName = True;
    #classify = True;
    run(source_folder = source_folder, changeName = changeName, classify = classify)



def run(source_folder, changeName, classify):
    if changeName:
        print("Start change name and extension Virushare\n")
        change(source_folder = source_folder, FOLDER_CHANGENAME = FOLDER_CHANGENAME)
    if classify:
        print("Start classify VirusShare\n")
        classify(source_folder= source_folder)

    return 0;


def help():
    print ()




if __name__ == "__main__":
    main()