## merge files (all src and all tgt ) -vertical join

## From IITB corpus currently we are keeping the data from these groups -chats, Movie Dialogs, general,Hi-Eng Word-Linkage,Admin Dictionary,
#  Admin Examples,Admin Definitions, ted talks, Indic Multi-Parallel, JudicialI, Govt Websites, Book Translations,  

filenames = ['IITB-splitted-data/hi-set-430013-434711', 'IITB-splitted-data/hi-set-434711-438933','IITB-splitted-data/hi-set-438933-712818','IITB-splitted-data/hi-set-712818-887993',
             'IITB-splitted-data/hi-set-887993-954457','IITB-splitted-data/hi-set-954457-1001292','IITB-splitted-data/hi-set-1001292-1047815','IITB-splitted-data/hi-set-1047815-1090398',
             'IITB-splitted-data/hi-set-1090398-1100747','IITB-splitted-data/hi-set-1100747-1105754','IITB-splitted-data/hi-set-1109481-1232841','IITB-splitted-data/hi-set-1265704-1492827']
with open('intermediate-data/src-merged.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)

filenames = ['IITB-splitted-data/en-set-430013-434711', 'IITB-splitted-data/en-set-434711-438933','IITB-splitted-data/en-set-438933-712818','IITB-splitted-data/en-set-712818-887993',
             'IITB-splitted-data/en-set-887993-954457','IITB-splitted-data/en-set-954457-1001292','IITB-splitted-data/en-set-1001292-1047815','IITB-splitted-data/en-set-1047815-1090398',
             'IITB-splitted-data/en-set-1090398-1100747','IITB-splitted-data/en-set-1100747-1105754','IITB-splitted-data/en-set-1109481-1232841','IITB-splitted-data/en-set-1265704-1492827']
with open('intermediate-data/tgt-merged.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)                


