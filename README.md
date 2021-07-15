# Data-Extraction-From-Graphs

[![sa](https://user-images.githubusercontent.com/62691542/125805584-bcdbe448-0846-4c1b-9506-7ecd3c90a38c.png)
](![sa](https://user-images.githubusercontent.com/62691542/125805584-bcdbe448-0846-4c1b-9506-7ecd3c90a38c.png)
)

## Introduction
A python based program which extracts coordinates of required points form a graph given in pdf format. 
The program is a semi-automated tool that makes this process extremely easy.

## Demo
 Clone this repo and make a new folder "graphs" and put all the images in pdf file in that folder and then follow the below steps:
 
- Enter the index of the image you want to plot the graph for from the "graphs" folder. Put your image in that folder.
- The graph image will open, if not watch it somewhere behind the open windows.
- `DO NOT CLICK TWICE ON THE POPED UP IMAGE BEFORE ANSWERING THE INPUT`. 
- PRESS `o` to select origin of the graph. After selecting origin, PRESS 'x' to select any point on x-axis (click once).
- Enter the distance between origin and the point on x-axis which has just been selected.
- Enter the zero offset if present.
- After answering the length of line segment selected, zero offset and pressing enter PRESS 'y' for y-axis calibration and follow the same procedure as used for x-axis.
- After completion of caliberation now PRESS 'p' to select data point on graph for which coordinates has to be digitized.
- Click `s` to save the image of graph with selected points.
- Click `f` to finish.
- Check "plotDataFiles" folder for .csv file generated and "plots" folder for the saved map image.

## Features

- User can select as many coordinates according to the requirement.
- Returns coordinates of any type of curve irrespective of graph background, type, color.
- Works for mutliple curves too.
- Returns output coordinates upto 6 decimal precision.
- Output is saved automatically in the excel sheet.


## Programming Language Used

- Python
### Libraries Used
- NumPy
- Open CV
- CSV







