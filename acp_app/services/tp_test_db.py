# Truthtable Parser Test File | Parker Jordan
# Tests all truthtables and sequences for excution and correntness

from truthtable_parser import TruthtableDB
import pandas as pd
from pathlib import Path

all_tts = []
path = 'C:/Users/pjordan/TruthtablesTest/ref1'

files = Path(path).glob('**/*.xls')
for file in files:
    truthtable = TruthtableDB(file)
    all_tts.append(truthtable.tt)
tt_master = pd.concat(all_tts)


#result = TruthtableDB('C:/Users/pjordan/Truthtables/ref1/41IXA.xls')

#ttx = result._tt_name_lst
#sqnumx = result._seq_num_lst
#snx = result._seq
#tt = result.tt
#trudev = result._true_devices

#test = pd.DataFrame(list(zip(ttx, sqnumx, snx)), columns=['Truthtable', 'Sequence Number','Step Number'])
