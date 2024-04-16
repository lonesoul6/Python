# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
import math
import slope
x1 = 2;
x2 = 6;
y1 = 2;
y2 = 10;

slopes =y2-y1/x2-x1;

print('slope is: ', slopes);
if(slopes!=slope):
    {
        print("slopes aren't equal")
    }


distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print('eucladean distance is: ', distance)