## remove duplicate and whitespaces from parallel corpus built after merging step 

## below is for dropping duplicate from text file
def drop_duplicate(inFile,outFile):
    lines_seen = set() # holds lines already seen
    outfile = open("{0}".format(outFile), "w")
    for line in open("{0}".format(inFile), "r"):
        if line not in lines_seen: # not a duplicate
           outfile.write(line)
           lines_seen.add(line)
    outfile.close()

## separation into master corpus src and tgt for training. After this tokenization needs to be done(indic nlp),then feed into OpenNMT
def separate_corpus(col_num,inFile,outFile):
    outfile = open("{0}".format(outFile), "w")
    delimiter = "\t"
    for line in open("{0}".format(inFile), "r"):
        # col_data.append(f.readline().split(delimiter)[col_num])
        outfile.write(str(line.split(delimiter)[col_num].replace('\n','')))
        outfile.write("\n")    
    outfile.close()

with open("intermediate-data/src-merged.txt") as xh:
  with open('intermediate-data/tgt-merged.txt') as yh:
    with open("intermediate-data/corpus-remove-duplicate.txt","w") as zh:
      #Read first file
      xlines = xh.readlines()
      #Read second file
      ylines = yh.readlines()
      
      #Write to third file
      for i in range(len(xlines)):
        line = ylines[i].strip() + '\t' + xlines[i]
        zh.write(line)


drop_duplicate("intermediate-data/corpus-remove-duplicate.txt","intermediate-data/corpus-no-duplicate.txt")

separate_corpus(0,"intermediate-data/corpus-no-duplicate.txt","master-corpus/tgt-train-untok.txt")
separate_corpus(1,"intermediate-data/corpus-no-duplicate.txt","master-corpus/src-train-untok.txt")

