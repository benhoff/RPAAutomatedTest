from glob import glob
import os
from os.path import basename
from os.path import join
from os.path import normpath
import shutil

def deleteFiles(PathDirectory,Pattern):
	Files=glob(join(PathDirectory,Pattern))
	for File in Files:
		os.remove(File)

def copyFiles(srcFolder, dstFolder):
    for file in glob(join(f'{srcFolder}','*')):
        shutil.copy(
            src=file,
            dst=join(dstFolder,basename(normpath(file)))
        )

def copyFile(srcFile, dstFile):
    shutil.copy(
        src=srcFile,
        dst=dstFile
    )
