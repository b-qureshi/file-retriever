import os
from os import path
import sys
import shutil
import pathlib


def file_mover(parent, dest, Type):
    for r, d, f in os.walk(parent):
        for file_name in f:
            if file_name.endswith(Type.lower()) or file_name.endswith(Type.upper()):
                if path.exists(pathlib.PurePath(dest, file_name)):
                    pass
                else:
                    shutil.move(os.path.join(r, file_name), dest)
                    print("Moved " + file_name)
            else:
                currentPath = pathlib.PurePath(parent, file_name)
                if os.path.isdir(currentPath):
                    file_mover(currentPath, dest, Type)


srcPath = input("Source Path: ")
destPath = input("Destination Path: ")
fileType = input("File type: ")
fileMover(srcPath, destPath, fileType)
print("\n Done")
