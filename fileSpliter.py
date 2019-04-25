## To split the IITB groups into groups containing domain specific sentences
## GNOME			        1
# KDE			        145706
# Quran			        242933
# Chats			        430013
# Movie Dialogs		    434711
# General			    438933
# Hi-Eng Word-Linkage	712818
# Admin Dictionary  	887993
# Admin Examples		954457
# Admin Definitions	    1001292
# TED Talks		        1047815
# Indic Multi-Parallel	1090398
# Judicial I		    1100747
# Judicial II		    1105754
# Govt Websites		    1109481
# Wikipedia		        1232841
# Book Translations	    1265704
# Govt Website II		1492827
# 	     		        1561840

import itertools

startLine = 438933
endLine = 712818

pairs = [(1,145706),(145706,242933),(242933,430013),(430013,434711),(434711,438933),(438933,712818),(712818,887993),(887993,954457),(954457,1001292),(1001292,1047815),
        (1047815,1090398),(1090398,1100747),(1100747,1105754),(1105754,1109481),(1109481,1232841),(1232841,1265704),(1265704,1492827),(1492827,1561840)]

for a,b in pairs:
    with open("data/IITB.en-hi-en.txt", "r") as text_file:
        with open("IITB-splitted-data/en-set-{0}-{1}".format(a,b),"w") as zh:
            for line in itertools.islice(text_file, a, b):
                 zh.write(line)
            # print(line)

    with open("data/IITB.en-hi-hi.txt", "r") as text_file:
        with open("IITB-splitted-data/hi-set-{0}-{1}".format(a,b),"w") as zh:
            for line in itertools.islice(text_file, a, b):
                zh.write(line)
            # print(line)
    

