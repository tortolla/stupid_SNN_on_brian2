from  common4 import *
import numpy
import pandas as pd
import sys
import csv


with open('/Users/tortolla/Desktop/retard_model/0.0-0.1/accuracy_220_1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    x1 = []
    for row in csv_reader:
        x1 = row
    print(type(x1))

with open('/Users/tortolla/Desktop/retard_model/0.0-0.1/accuracy_220_2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    x2 = []
    for row in csv_reader:
        x2 = row

    print(x2)

with open('/Users/tortolla/Desktop/retard_model/0.0-0.3/accuracy_220_1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    x3 = []
    for row in csv_reader:
        x3 = row
    print(x3)

with open('/Users/tortolla/Desktop/retard_model/0.0-0.3/accuracy_220_2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    x4 = []
    for row in csv_reader:
        x4 = row
    print(x4)

with open('/Users/tortolla/Desktop/retard_model/0.0-0.5/accuracy_220_1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    x5 = []
    for row in csv_reader:
        x5 = row
    print(x5)


with open('/Users/tortolla/Desktop/retard_model/0.0-0.5/accuracy_220_2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    x6 = []
    for row in csv_reader:
        x6 = row
    print(x6)

with open('/Users/tortolla/Desktop/retard_model/0.0-0.7/accuracy_220_1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    x7 = []
    for row in csv_reader:
        x7 = row
    print(x7)

with open('/Users/tortolla/Desktop/retard_model/0.0-0.7/accuracy_220_2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    x8 = []
    for row in csv_reader:
        x8 = row
    print(x8)

fig1 = plt.figure()
fig2 = plt.figure()

ax1 = fig1.add_subplot(1, 1, 1)
ax2 = fig2.add_subplot(1, 1, 1)

x = [30, 70, 120, 220]
x1 = list(map(float, x1))
x2 = list(map(float, x2))
x3 = list(map(float, x3))
x4 = list(map(float, x4))
x5 = list(map(float, x5))
x6 = list(map(float, x6))
x7 = list(map(float, x7))
x8 = list(map(float, x8))

ax1.plot(x, x1, 'ro', label='0.1')
ax2.plot(x, x2, 'ro', label='0.1')
ax1.plot(x, x3, 'go', label='0.3')
ax2.plot(x, x4, 'go', label='0.3')
ax1.plot(x, x5, 'yo', label='0.5')
ax2.plot(x, x6, 'yo', label='0.5')
ax1.plot(x, x7, 'bo', label='0.7')
ax2.plot(x, x8, 'bo', label='0.7')

ax1.set_xlabel('time')
ax1.set_ylabel('accuracy')
ax1.set_title('finall1')
ax1.legend(loc='center left', bbox_to_anchor=(1, 0.7))
ax2.set_xlabel('time')
ax2.set_ylabel('accuracy')
ax2.set_title('finall1')
ax2.legend(loc='center left', bbox_to_anchor=(1, 0.7))