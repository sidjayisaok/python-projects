import matplotlib.pyplot as plt
import csv
import pandas as pd

# with open('fbi-2018-stats.csv','r') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

columns = ["City","Violence"]

data_file = pd.read_csv('fbi-2018-stats.csv',usecols=columns)
data_file.sort_values(by=['City'])

print(data_file)

plt.bar(data_file.City, data_file.Violence, tick_label=data_file.City, width=1, color=['green','blue'])
plt.xlabel('City')
plt.ylabel('Violence')
plt.title('FBI Crime Stats 2018')
plt.grid(True)
plt.show()

# x = [2,3,5,8,13,21]
# y = [1,2,3,4,5,6]
# plt.plot(x, y)
# plt.ylabel('rate of increase')
# plt.xlabel('fibonacci numbers')
# plt.show()