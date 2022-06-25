import plotly.express as px
import pandas as pd
import statistics
import csv
import plotly.graph_objects as go
import random


df = pd.read_csv("savings_data_final.csv")
fig = px.scatter(df,y="quant_saved", color = "rem_any")
fig.show()

with open("savings_data_final.csv", newline="") as f:
    reader = csv.reader(f)
    savings_data = list(reader)
savings_data.pop(0)
print(savings_data[0][0])

quant_saved = []

for i in range(0, len(savings_data)):
    quant_saved.append(float(savings_data[i][0]))

total_entries = len(savings_data)
total_people_given_reminder =  0
for data in savings_data:
    if(int(data[3]) ==  1):
        total_people_given_reminder += 1
fig = go.Figure(go.Bar(x=["Reminded", "Not Reminded"], y = [total_people_given_reminder, (total_entries - total_people_given_reminder)]))
fig.show()

savings_array = []
for data in savings_data:
    savings_array.append(float(data[0]))
print(f"Mean of saving- {statistics.mean(savings_array)}")
print(f"Median of saving - {statistics.median(savings_array)}")
print(f"Mode of saving - {statistics.mode(savings_array)}")


remainded_array = []
not_remainded_array = []

for data in savings_data:
    if(int(data[3]) == 1):
        remainded_array.append(float(data[0]))
    else:
        not_remainded_array.append(float(data[0]))

print(f"Mean of remainded people - {statistics.mean(remainded_array)}")
print(f"Median of remainded people - {statistics.median(remainded_array)}")
print(f"Mode of remainded people - {statistics.mode(remainded_array)}")

print(f"Mean of not remainded people- {statistics.mean(not_remainded_array)}")
print(f"Median of not remainded people - {statistics.median(not_remainded_array)}")
print(f"Mode of not remainded people - {statistics.mode(not_remainded_array)}")

std_deviation_remainded = statistics.stdev(remainded_array)
std_deviation_not_remainded = statistics.stdev(not_remainded_array)
print(f"Std deviation for Remainded people : {std_deviation_remainded}")
print(f"Std deviation for Not Remainded people : {std_deviation_not_remainded}")


def random_set_of_mean(counter):
    data_Set = []
    for i in range(0, counter):
        random_index = random.randint(0, len(quant_saved)-1)
        value = quant_saved[random_index]
        data_Set.append(value)
    mean = statistics.mean(data_Set)
    return mean

mean_list=[]
def setup():
    
    for i in range(0,1000):
        random_means = random_set_of_mean(30)
        mean_list.append(random_means)

setup()

std_deviation_means = statistics.stdev(mean_list)
print(f"Std deviation for sample mean : {std_deviation_means}")
    