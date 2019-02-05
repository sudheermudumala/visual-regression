import json

print("hello world")

f=open("backstop_data/html_report/config.js","r")
if f.mode=="r":
	contents=f.read()
#	print(contents)

contents = contents.replace("report(","")
contents = contents.replace(");","")

#print(contents)

contentsJson = json.loads(contents)

#print(contentsJson["tests"])
contentTests = contentsJson["tests"]

for tests in contentTests:
	if tests['status'] == 'fail':
		failLabel = tests['pair']
		print(failLabel['label'])