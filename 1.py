import cv2
import numpy as np
import csv
import os

##First of all it will ask the index of the image you want to plot the graph for from the "graphs" folder. Put your image in that folder
##Now the graph image will open (if not poped up watch it somewhere behind the open windows). CAUTION: DO NOT CLICK TWICE ON THE POPED UP IMAGE BEFORE ANSWERING THE INPUT.
##Now, PRESS 'o' to select origin of the graph.
##After selecting origin, PRESS 'x' to select any point on x-axis (just one click).
##It will ask the distance between origin and the point on x-axis which has just been selected.
##Following this it will ask if there is any zero offset i.e. if the origin represent 0 on the x-axis.
##After answering the length of line segment selected, zero offset and pressing enter PRESS 'y' for y-axis calibration and follow the same procedure as used for x-axis.
##After completion of caliberation now PRESS 'p' to select data point on graph for which coordinates has to be digitized.
##PRESS 's' to save the image of graph with selected points.
##PRESS 'f' to finish.
##Check "plotDataFiles" folder for .csv file generated and "plots" folder for the saved map image.



arr = os.listdir("graphs") #list the directory files
print("Please select the file you want to print x,y co-ordinates")
for i, filename in enumerate(arr):
    print(str(i+1)+". "+filename)
    
file_index=int(input())
selected_file_name= arr[file_index-1]
print(arr[file_index-1]+" selected")

clicks = [['x', 'y']]
originC = []
XC = []
YC = []
origin = False
plots = False
axisX = False
axisY = False

def draw_circle(event,x,y,flags,param):
    #BGR
    if event == cv2.EVENT_LBUTTONDOWN:
        if origin == True:
            cv2.circle(img,(x,y),5,(0,255,0),2)
            originC.extend((x, y))
            print("origin:",originC)
        elif axisX == True:
            cv2.circle(img,(x,y),5,(255,0,0),2)
            XC.extend((x, y))
            print("X:",XC)
            print("Enter the length of x-axis")
            xl = float(input())
            print("Enter the zero offset for x axis")
            global x_zero_offset
            x_zero_offset = float(input())
            global x_PixLength
            x_PixLength = float(euclidean(originC[0], originC[1], XC[0], XC[1]))
            global x_pixToUnitRatio
            x_pixToUnitRatio = float(x_PixLength)/float(xl)
            global cosine
            cosine = (XC[0]-originC[0])/x_PixLength
        elif axisY == True:
            cv2.circle(img,(x,y),5,(255,0,0),2)
            YC.extend((x, y))
            print("Y:",YC)
            print("Enter the length of y-axis")
            yl = float(input())
            print("Enter the zero offset for y axis")
            global y_zero_offset
            y_zero_offset = float(input())
            global y_PixLength
            y_PixLength = float(euclidean(originC[0], originC[1], YC[0], YC[1]))
            global y_pixToUnitRatio
            y_pixToUnitRatio = float(y_PixLength)/float(yl)
        elif plots == True:
            cv2.circle(img,(x,y),5,(0,0,255),2)
            clicks.append(coordinate_calculator(x, y))

#Distance formula
def euclidean(x1, y1, x2, y2):
    return np.sqrt((x2-x1)*2 + (y2-y1)*2)

#Equation of Line y=mx+c
def x_axis(x):
    return ((XC[1]-originC[1])/abs(XC[0]-originC[0]))*abs(x-originC[0]) + originC[1]

#Equation of Line x=my+c
def y_axis(y):
    return ((YC[0]-originC[0])/abs(YC[1]-originC[1]))*abs(y-originC[1]) + originC[0]

#Convert pixels to unt
def x_pixToUnit(pixels):
    return float(pixels)/float(x_pixToUnitRatio)

def y_pixToUnit(pixels):
    return float(pixels)/float(y_pixToUnitRatio)

#calculate the co-ordinates
def coordinate_calculator(x, y):
    eu_x = euclidean(x, y, y_axis(y), y)
    y_unit = y_pixToUnit(euclidean(x, y, x, x_axis(x))*cosine)+y_zero_offset
    x_unit = x_pixToUnit(euclidean(x, y, y_axis(y), y)*cosine)+x_zero_offset
    return [x_unit, y_unit]

#print("Enter image name with extension")
img_file = selected_file_name  #read image file
img = cv2.imread("graphs\\"+img_file)
cv2.namedWindow('image')   #Show the imgage in a window named 'image'
cv2.setMouseCallback('image',draw_circle)  #handle mouse click events and call draw_Circle function


#infinite loop to imshow the image and keep capturing the key press
while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord("o"):
        origin = True
        plots = False
        axisX = False
        axisY = False
    elif k == ord("x"):
        origin = False
        plots = False
        axisX = True
        axisY = False
    elif k == ord("y"):
        origin = False
        plots = False
        axisX = False
        axisY = True
    elif k == ord("p"):
        origin = False
        plots = True
        axisX = False
        axisY = False
    elif k == ord("s"):
        cv2.imwrite("plots\\"+img_file+"_plot.png", img)
        print("Plot image saved!")
    elif k == ord("f"):
        break
cv2.destroyAllWindows()

print("Enter the file name to which you need to save data")
F_name = input()


#Export the points in a csv
with open("plotDataFiles\\"+F_name+'.csv', 'w') as csvFile:
    print(clicks)
    writer = csv.writer(csvFile)
    writer.writerows(clicks)

csvFile.close()
print("done!")
