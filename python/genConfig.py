import csv
import os
import sys

os.remove('../urls/test.js')

f=open('../urls/urls_master.csv')
csv_f = csv.reader(f)

csv_heading = next(csv_f)

print len(csv_heading)

colCnt = len(csv_heading)

scenario = "var pathConfig={};\n"
scenario = scenario + "pathConfig.array = [\n"

val = ""
for row in csv_f:

	scenario = scenario + "{\n"
	for x in range(colCnt):

		lstSel = ""
		head = csv_heading[x] 

		if csv_heading[x] == 'selectors':
			det = row[x].split(',')	

			print row[x]

			if len(det[0]) > 0:

				print len(det[0])

				lstSel = lstSel + "[\""
				for sel in det:
					lstSel = lstSel + sel + "\",\""
				val = lstSel[:-3]
				val = val + "\"]"
			else:
				val = "\"\""
		elif csv_heading[x] == 'url':
			val = "\"" + sys.argv[1] + row[x] + "\","
		elif csv_heading[x] == 'referenceUrl':
			val = "\"" + sys.argv[2] + row[x] + "\","
		else:
			val = "\"" + row[x] + "\","
		scenario = scenario + csv_heading[x] + ":" + val + "\n"
	scenario = scenario[:-1] + "},\n"
scenario = scenario[:-2] + "]\n"
scenario = scenario + "module.exports=pathConfig;\n"
print scenario
f.close()


f=open('../urls/test.js','w+')
f.write(scenario)
f.close()


