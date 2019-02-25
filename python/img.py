import os
from PIL import Image

listOfFiles = os.listdir('backstop_data/bitmaps_reference')

print listOfFiles

for entry in listOfFiles:
	
	img = Image.open('backstop_data/bitmaps_reference/' + entry)

	extrema = img.convert("L").getextrema()
	
	print("Below Ads are not displayed in Today Page")
	if extrema[0] == extrema[1]:
	    print(entry)
	