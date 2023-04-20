import matplotlib.pyplot as plt
import numpy as np 

n = 3

x = 0.7676767676768
y = 0.4583333333333

arrX = []
arrY = []
arrF = []

for i in range(0, n):
    arrY.append([])
    arrF.append([])

    title = "input" + str(i + 1) + ".txt"
    try:
        with open(title, 'r') as f:
            for line in f.readlines():
                ass = line.split()
                if float(ass[0]) == x:
                    arrY[i].append(float(ass[1]))
                    arrF[i].append(float(ass[2]))
    except:
        print ("file: " + title + " doesn't exist!")


plt.plot(arrY[0], arrF[0], label = "Re = 75", color = "green")
plt.plot(arrY[1], arrF[1], label = "Re = 50", color = "blue")
plt.plot(arrY[2], arrF[2], label = "Re = 25", color = "red")
plt.plot([-5, 5], [0, 0], color = 'black')

plt.xlim([0.0, 1.0])

plt.title("Govno ili Zalupa")
plt.legend(loc = 'upper right')

plt.minorticks_on()

plt.grid(which = 'major')
plt.grid(which = 'minor', linestyle=':')
plt.tight_layout()

plt.show()


'''
import matplotlib as mpl
x = np.arange   ( start = 0.    # upper limit
                , stop  = 6.    # lower limit
                , step  = 0.05  # step-size (distance between the points)
                ) # generate points between start and stop with distances of step apart from each other
thisLegend = []
mpl.use('Agg')   # avoid displaying the figure in Python environment
for thisAlpha in [0.2,0.4,0.6,0.8,1.0]:
    plt.plot( x, thisAlpha*x, 'b-.', alpha = thisAlpha );   # -. represents dashed-dotted line-style
    thisLegend.append("alpha = {}".format(thisAlpha))
plt.legend( thisLegend );
plt.savefig("transparency.png")'''