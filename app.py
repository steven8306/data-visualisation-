import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

fifa_data = pd.read_csv("./data_sets/fifa.csv",index_col="Date",parse_dates=True)
delay_data = pd.read_csv("./data_sets/flight_delays.csv",index_col="Month")
insurance_path = pd.read_csv("./data_sets/insurance.csv")
irs_data = pd.read_csv("./data_sets/iris.csv",index_col="Id")
#unit of size is inch
# plt.figure(figsize=(16,6))
# plt.title("fifa")

# plt.figure(figsize=(10,6))
# plt.title("delay")

plt.figure(figsize=(14,7))
plt.title("average delay")

#bar chart for delay
# sns.barplot(x=delay_data.index,y=delay_data["NK"])
# plt.ylabel("delay in minutes")

#heatmap for aircraft_delay
#annot is used to show the number of delay for each airline. if remove it, can't see the number
# sns.heatmap(data=delay_data,annot=True)
# plt.xlabel("airline")

#lineplot for fifa
# sns.lineplot(data=fifa_data["ARG"],label="ARG")
# sns.lineplot(data=fifa_data["BRA"],label="BRA")

#plot 
#sns.lineplot(data=fifa_data)

#scatter plot for insurance
# sns.scatterplot(x=insurance_path["bmi"],y=insurance_path["charges"],hue=insurance_path['smoker'])
# sns.swarmplot(x=insurance_path['smoker'],
#               y=insurance_path["charges"])

#histogram
sns.histplot(irs_data['Petal Length (cm)'])

plt.xlabel("bmi")
plt.ylabel("charges")
plt.show()
