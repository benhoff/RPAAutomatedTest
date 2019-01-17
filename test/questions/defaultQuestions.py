from glob import glob
from testConfig import config
import pandas as pd

def switchTheState(*args,**kwargs):
    df = pd.read_excel(f'{config["RPA_TASK_FOLDER"]}//Inputs//{kwargs["In"]}')
    dfToList = df[kwargs["of"]].tolist()
    for row in dfToList:
        assert(row==kwargs["to"])