import csv
import json
import requests
# [01:59.80]

def gettime(line):
	return int(line[1:3])*60 + float(line[4:9])

url = 'https://southeastasia.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment'

lyrics = []
with open('lyrics.lrc', newline='\n') as inputfile:
	for row in csv.reader(inputfile):
		lyrics.append(row)
lyrics = lyrics[4:]

documents = []
for i in range(len(lyrics)):
	d = {}
	d['language'] = 'en'
	d['id'] = i+1
	d['text'] = lyrics[i][0]
	documents.append(d)

j = {}
j['documents'] = documents
data = json.dumps(j)

print(len(lyrics))

headers = {'Content-Type' : 'application/json', 'Ocp-Apim-Subscription-Key' : '22835c7c256b423580c564f2524e4910', 'Accept' : 'application/json'}

response = requests.post(url, headers=headers, data=data)
results = response.json()['documents']

print(len(results))

sentiments = []
cur = 0
time = 0
for i in range(len(lyrics)):
	now = gettime(lyrics[i][0])
	while(time < now):
		sentiments.append(cur)
		time += 0.04
	# Update cur
		cur = results[i]['score']

print(time)
print(now)
print(len(sentiments))
