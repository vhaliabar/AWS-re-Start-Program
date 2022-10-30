full_sequence = ""

with open(r"preproinsulin-seq.txt", 'r') as file_data:
    for line in file_data:
            data = line.split()
            for i in data:
                if i == "ORIGIN" or i == "//" or i.isdigit():
                    continue
                full_sequence += i
chars = [*full_sequence]

lsinsulin = ""
binsulin = ""
cinsulin = ""
ainsulin = ""
for i in range(len(chars)):
    if 0<=i<24:
        lsinsulin += chars[i]
    elif 24<=i<54:
        binsulin += chars[i]
    elif 54<=i<89:
        cinsulin += chars[i]
    else:
        ainsulin += chars[i]
def writeSeqToFile(seq, file):
    f = open(file, "a")
    f.write(seq)
    f.close()
writeSeqToFile(lsinsulin, "lsinsulin-seq-clean.txt")
writeSeqToFile(binsulin, "binsulin-seq-clean.txt")
writeSeqToFile(cinsulin, "cinsulin-seq-clean.txt")
writeSeqToFile(ainsulin, "ainsulin-seq-clean.txt")