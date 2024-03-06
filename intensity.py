import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import csv

w_max = 1.2


def work(model):
	x = []
	index = ['30', '70', '120', '150', '170', '200', '220']
	maximum = ['0.1', '0.2', '0.3', '0.4', '0.5', '0.6']

	fig1 = plt.figure()
	ax1 = fig1.add_subplot(1, 1, 1)
	
	for j in range(len(maximum)):

		finall1 = []
		finall2 = []
		finall3 = []
		finall4 = []
		finall5 = []
		finall6 = []
		finall7 = []
		finall8 = []
		finall9 = []
		finall10 = []
		finall11 = []
		finall12 = []
		finall13 = []
		finall14 = []
		

		x = []

		for i in range(len(index)):
# загрузка данных из CSV файла
			way = f"/Users/tortolla/Desktop/LIF/{maximum[j]}/csv_weights/W_{index[i]}.csv"
			data = pd.read_csv(way, header=None)

# получение массивов с весами для первого и второго нейронов
			weights1 = data.loc[1]
			weights2 = data.loc[2]

# вычисление интенсивности диагональных пикселей для первого и второго нейронов
			def first(array):
				diag = []
				for i in range(0, len(array), 4):
					diag.append(array[i])
				return(diag)

			def diag3(array):
				diag = []
				for i in range(2, len(array), 2):
					if i == 15:
						return(diag)
						break
					diag.append(array[i])

				return(diag)


			weights1diag1 = diag0(weights1)
			weights1diag2 = diag3(weights1)
			weights2diag1 = diag3(weights2)
			weights2diag2 = diag0(weights2)


# вычисление идеальной интенсивности (для полностью белой диагональной линии)
			id = 3*w_max

# вычисление отношения суммарной интенсивности к идеальной интенсивности
			ratio1 = sum(weights1diag1)/ (id) - sum(weights1diag2)/ (id)
			ratio2 = sum(weights2diag1)/ (id) - sum(weights2diag2)/ (id)


			finall1.append(ratio1)
			finall2.append(ratio2)
			x.append(int(index[i]))

		with open(f'/Users/tortolla/Desktop/LIF/{maximum[j]}/accuracy_{index[i]}_1.csv', mode='w+', newline='') as file:
			writer = csv.writer(file)
			writer.writerow(finall1)

		with open(f'/Users/tortolla/Desktop/LIF/{maximum[j]}/accuracy_{index[i]}_2.csv', mode='w+', newline='') as file:
			writer = csv.writer(file)
			writer.writerow(finall2)



		#ax1.plot(x, finall1, 'ro-', label='Series 1')
		#ax1.plot(x, finall2, 'ro-', label='Series 2')
		#ax1.set_xlabel('max_value')
		#ax1.set_ylabel('accuracy')
		#ax1.set_title('finall1')
		#ax1.legend()
		#ax1.set_title(maximum[j])
		#ax1.plot(x, finall2, 'ro-', label='Series 1')
	
# вывод результатов
work('HH')
		