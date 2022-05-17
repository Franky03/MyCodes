import csv
import pandas as pd
# # with open('./Udemy/WeatherPandas/weather_data.csv') as file:
# #     data= csv.reader(file)
# #     temp=[]
# #     for row in data:
# #         if row[1] != 'temp':
# #             temp.append(int(row[1]))
            

# #     print(temp)

# data= pd.read_csv("./Udemy/WeatherPandas/weather_data.csv")
# print(data)

# data_dict= data.to_dict()
# # print(data_dict)
# # null= data['temp'].isna()
# # print(null)
# media= data['temp'].mean()
# # print(round(media))
# # max= data['temp'].max()
# # print(max)
# # print(data[data.temp== data.temp.max()])

# monday= data[data.day=='Monday']
# monday_temp= int(monday.temp)
# new= (((9*monday_temp)+160)/5)
# print(new)

# create a dataframe from scratch
# data_dict= {'students': ['Anya', 'James', 'Angela'], 'scores': [76, 56, 65]}
# df= pd.DataFrame(data_dict)
# df.to_csv('new_data.csv')

data= pd.read_csv("./Udemy/WeatherPandas/squirrel_count.csv")
# for colun in data.columns:
#     print(colun)
# gray_squirrel_count= len(data[data['Primary Fur Color'] == 'Gray'])
# black_squirrel_count= len(data[data['Primary Fur Color'] == 'Black'])
# cinnamon_squirrel_count= len(data[data['Primary Fur Color'] == 'Cinnamon'])
# print(gray_squirrel_count)
# print(black_squirrel_count)
# print(cinnamon_squirrel_count)

count= data['Primary Fur Color'].value_counts()
all_count= count.to_dict()
data_dict={'Fur Color': [], 'Count': []}
for k, v in all_count.items():
    data_dict['Fur Color'].append(k)
    data_dict['Count'].append(v)

print(data_dict)
df= pd.DataFrame(data_dict)
df.to_csv("./Udemy/WeatherPandas/new_squirrel.csv")