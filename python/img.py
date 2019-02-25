import os
from PIL import Image

listOfFiles = os.listdir('backstop_data/bitmaps_reference')

ads = []
cnt = 0

for entry in listOfFiles:
	
	img = Image.open('backstop_data/bitmaps_reference/' + entry)

	extrema = img.convert("L").getextrema()
	
	if extrema[0] == extrema[1]:
	    print(entry)
	    ads.append(entry)
	    cnt = cnt + 1

if cnt == 0:
	print ("All Ads are displayed")
else:
	print("Below Ads are not displayed in Today Page")
	print (ads)
