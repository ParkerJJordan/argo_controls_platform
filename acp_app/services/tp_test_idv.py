# Truthtable Parser Test File | Parker Jordan
# Tests specified truthtables and sequences for excution and correntness

from truthtable_parser import TruthtableDB
import pandas as pd
from pathlib import Path

#seqs = pd.DataFrame()
#seq_num = 4

#### IX Train 1 ####
# def test_ixa():
#     tt = '41IXA'
#     seq_val = seq_num
#     df = parse_truthtable(tt, seq_val)
#     seqs[tt] = df['Step Number']

# def test_ixb():
#     tt = '41IXB'
#     seq_val = seq_num
#     df = parse_truthtable(tt, seq_val)
#     seqs[tt] = df['Step Number']
    
# def test_ixc():
#     tt = '41IXC'
#     seq_val = seq_num
#     df = parse_truthtable(tt, seq_val)
#     seqs[tt] = df['Step Number']

# #### IX Train 2 ####
# def test_ixd():
#     tt = '41IXD'
#     seq_val = seq_num
#     df = parse_truthtable(tt, seq_val)
#     seqs[tt] = df['Step Number']
    
# def test_ixe():
#     tt = '41IXE'
#     seq_val = seq_num
#     df = parse_truthtable(tt, seq_val)
#     seqs[tt] = df['Step Number']
    
# def test_ixf():
#     tt = '41IXF'
#     seq_val = seq_num
#     df = parse_truthtable(tt, seq_val)
#     seqs[tt] = df['Step Number']
    
# #### IX Train 3 ####
# def test_ixg():
#     tt = '41IXG'
#     seq_val = seq_num
#     df = parse_truthtable(tt, seq_val)
#     seqs[tt] = df['Step Number']
    
# def test_ixh():
#     tt = '41IXH'
#     seq_val = seq_num
#     df = parse_truthtable(tt, seq_val)
#     seqs[tt] = df['Step Number']
    
# def test_ixi():
#     tt = '41IXI'
#     seq_val = seq_num
#     df = parse_truthtable(tt, seq_val)
#     seqs[tt] = df['Step Number']
    
# #### IX Swing X ####
# def test_ix1x():
#     tt = '41IX1X'
#     seq_val = seq_num
#     df = parse_truthtable(tt, seq_val)
#     seqs[tt] = df['Step Number']
    
# def test_ix2x():
#     tt = '41IX2X'
#     seq_val = seq_num
#     df = parse_truthtable(tt, seq_val)
#     seqs[tt] = df['Step Number']
    
# def test_ix3x():
#     tt = '41IX3X'
#     seq_val = seq_num
#     df = parse_truthtable(tt, seq_val)
#     seqs[tt] = df['Step Number']
    
# def test_ix49x():
#     tt = '49IXX'
#     seq_val = seq_num
#     df = parse_truthtable(tt, seq_val)
#     seqs[tt] = df['Step Number']
    
# def test_ix42x():
#     tt = '42IX2X'
#     seq_val = seq_num
#     df = parse_truthtable(tt, seq_val)
#     seqs[tt] = df['Step Number']
    
# #### IX Swing Y ####
# def test_ix1y():
#     tt = '41IX1Y'
#     seq_val = seq_num
#     df = parse_truthtable(tt, seq_val)
#     seqs[tt] = df['Step Number']

# def test_ix2y():
#     tt = '41IX2Y'
#     seq_val = seq_num
#     df = parse_truthtable(tt, seq_val)
#     seqs[tt] = df['Step Number']
    
# def test_ix3y():
#     tt = '41IX3Y'
#     seq_val = seq_num
#     df = parse_truthtable(tt, seq_val)
#     seqs[tt] = df['Step Number']
    
# def test_ix49y():
#     tt = '49IXY'
#     seq_val = seq_num
#     df = parse_truthtable(tt, seq_val)
#     seqs[tt] = df['Step Number']
    
# #### IX Swing Z ####
# def test_ix1z():
#     tt = '41IX1Z'
#     seq_val = seq_num
#     df = parse_truthtable(tt, seq_val)
#     seqs[tt] = df['Step Number']

# def test_ix2z():
#     tt = '41IX2Z'
#     seq_val = seq_num
#     df = parse_truthtable(tt, seq_val)
#     seqs[tt] = df['Step Number']
    
# def test_ix3z():
#     tt = '41IX3Z'
#     seq_val = seq_num
#     df = parse_truthtable(tt, seq_val)
#     seqs[tt] = df['Step Number']
    
# def test_ix49z():
#     tt = '49IXZ'
#     seq_val = seq_num
#     df = parse_truthtable(tt, seq_val)
#     seqs[tt] = df['Step Number']
all_tts = []
path = 'C:/Users/pjordan/TruthtablesTest'

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


#test_ixa()
#test_ixb()
#test_ixc()
#test_ixd()
#test_ixe()
#test_ixf()
#test_ixg()
#test_ixh()
#test_ixi()
#test_ix1x()
#test_ix2x()
#test_ix3x()
#test_ix49x() #Seq 5 doesn't work
#test_ix42x()
#test_ix1y()
#test_ix2y() #Seq 3 doesn't work. Seq 5 doesn't work (error '40')
#test_ix3y()
#test_ix49y()
#test_ix1z()
#test_ix2z() #Seq 3 doesn't work. Seq 5 doesn't work (error '40')
#test_ix3z()
#test_ix49z()
# Every sequence 4 passes
# Every sequence 2 passes

#seqs.to_clipboard(index=False, excel=True)