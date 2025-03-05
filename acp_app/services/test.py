from truthtable_parser import TruthtableDB

file = "C:/Users/pjordan/Truthtables/ref2/44S1.xls"
tt = TruthtableDB(file)
tt.to_clipboard()