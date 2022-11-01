import json

def readJsonFile(fileName):
    data=""  
    try:
        with open('D:/ALL_TEST_TASKS+PET_PROJECTS/AWSrestart/test_task/files/insulin.json') as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")

    return data