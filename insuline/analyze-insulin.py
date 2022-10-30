# with open('D:/ALL_TEST_TASKS+PET_PROJECTS/AWSrestart/insuline/ainsulin-seq-clean.txt', 'r') as file:
#     reader = file.readlines()
#     for line in reader:
#         with open('new.txt', 'a') as file2:
#             to_delete = ['ORIGIN', '//']
#             for word in line.split():
#                 if word not in to_delete:
#                     writer = file2.write(word)
                
#                 print(word)
#     print('Done!')

with open('D:/ALL_TEST_TASKS+PET_PROJECTS/AWSrestart/insuline/preproinsulin-seq.txt', 'r') as file:
    reader = file.readlines()
    #print(reader)
    cleaned = ''
    for line in reader:
            to_delete = ['ORIGIN', '//', '1', '61']
            for word in line.split():
                if word not in to_delete:
                    cleaned+=word
                
    #print(cleaned)
    
isinsuline = cleaned[:25]
binsuline = cleaned[25:54]
cinsuline = cleaned[55:89]
ainsuline = cleaned[89:110]
   
def printtofile(filename, content):
    with open(filename, "w") as file:
        file.write(content)
        return f'File {filename} created successfully!'

printtofile("isinsuline.txt", isinsuline)       
printtofile("binsuline.txt", binsuline)
printtofile("cinsuline.txt", cinsuline)
printtofile("ainsuline.txt", ainsuline)

    
print('\n------ ALL Done!--------')
    
    