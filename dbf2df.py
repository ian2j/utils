from dbfread import DBF
import pandas as pd

def dbf2DF(dbf):
    '''
    Helper function to load a .dbf file and convert to pandas DataFrame
    ----------
    Arguments:
    ----------
    dbf  : (string) - location of input dbf file
    '''
    dbf_table = DBF(dbf, load=True)
    df = pd.DataFrame(dbf_table.records[:])
    return df
    
