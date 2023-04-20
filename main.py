import matplotlib.pyplot as plt

# Количество графиков на одно полотно
n = 3

# Выбранные х, у
x = 0.7676767676768
y = 0.4583333333333

arrX = []
arrY = []
arrF = []

for i in range(0, n):
    # Здесь меняем если необходимо изменить вектор направления
    # arrX.append([])
    arrY.append([])
    arrF.append([])

    title = "input" + str(i + 1) + ".txt"
    try:
        with open(title, 'r') as f:
            for line in f.readlines():
                ass = line.split()
                # Здесь меняем если необходимо изменить вектор направления
                # if float(ass[1]) == y:
                if float(ass[0]) == x:
                    # arrX[i].append(float(ass[0])
                    arrY[i].append(float(ass[1]))
                    arrF[i].append(float(ass[2]))
    except:
        print ("file: " + title + " doesn't exist!")

# Здесь добавляем количество графиков соответствующее количеству тестов
plt.plot(arrY[0], arrF[0], label = "Re = 75", color = "green")
plt.plot(arrY[1], arrF[1], label = "Re = 50", color = "blue")
plt.plot(arrY[2], arrF[2], label = "Re = 25", color = "red")

plt.plot([-5, 5], [0, 0], color = 'black')

plt.xlim([0.0, 1.0])

plt.title("График")
plt.legend(loc = 'upper right')

plt.minorticks_on()

plt.grid(which = 'major')
plt.grid(which = 'minor', linestyle=':')
plt.tight_layout()

plt.show()