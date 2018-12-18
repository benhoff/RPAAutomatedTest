from glob import glob

from testConfig import config

def amazonInformation(*args,**kwargs):
    CSVFiles=glob(f'{config["TEST_RESULTS_FOLDER"][0]}\\Amazon*.csv')
    for amazonCSV in CSVFiles:
        with open(amazonCSV) as f:
            content=f.read()
            if not ('Column2' in content and 'Column1' in content): print(f'Not data in file: {amazonCSV}')
            assert('Column1' in content)
            assert('Column2' in content)

def ebayInformation(*args,**kwargs):
    CSVFiles=glob(f'{config["TEST_RESULTS_FOLDER"][0]}\\ebay*.csv')
    for ebayCSV in CSVFiles:
        with open(ebayCSV,encoding="utf8") as f:
            content=f.read()
            if not ('Column2' in content and 'Column1' in content): print(f'Not data in file: {ebayCSV}')
            assert('Column1' in content)
            assert('Column2' in content)

if __name__=="__main__":
    amazonInformation()
    ebayInformation()
