import os
import operator
import defcon

class StandardizeStartPoint():

    def __init__(self, contour):

        self.contour = contour
        self.contour.addObserver(self, "changedCallback", "Contour.Changed")

    def changedCallback(self, notification):

        print("glyph changed")

for file in os.listdir():
    
    if file[-4:] == ".ufo":
        
        font = defcon.Font(file)
        
        exists = "a" in font
        
        if exists:

            testGlyph = font["a"]

            for contour in testGlyph:

                pointList = []

                for point in contour.onCurvePoints:

                    temp = (point.x, point.y, point)

                    pointList.append(temp)

                sortedList = sorted(pointList, key=operator.itemgetter(1, 0))

                startPointi = contour.index(sortedList[0][2])

                contour.setStartPoint(startPointi)

            font.save()
            
        else:

            print(f"{file} does not have the glyph a")
            
    else:

        continue
