import json

with open('Headline_Trainingdata.json', 'r') as train_data:
 train_data = json.load(train_data)
with open('Headlines_Testdata.json', 'r') as test_data:
 test_data = json.load(test_data)
'''
company_list = []
for i in train_data:
    company_list.append(i['company'])
for i in test_data:
    company_list.append(i['company'])
print(company_list)
'''
fileObject = open('same_title.txt', 'w')
for i in test_data:
    for j in test_data:
        if i['title'] == j['title']:
            if i['id'] < j['id']:
                fileObject.write(i['title'])
                fileObject.write('\n')
        #fileObject.write('\n')
fileObject.close()


