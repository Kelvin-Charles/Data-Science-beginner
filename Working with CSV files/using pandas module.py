
import pandas

data = pandas.read_csv("weather_data.csv")
#print(data["temp"])

## FInding Average temperature ###

####### Using manual way ###
temperature = data['temp'].to_list()
total = sum(temperature)
# avg = total/len(temperature)

####### Using pandas method ###
avg = data["temp"].mean()
#print(avg)

##  Finding the Maximum Tempereture ## in Finding minimum use will use the .min() method
max_temp = data["temp"].max()
#print(max_temp)

#####    How to Get data of a specific row    ####
manday_weather = data[data.day == "Monday"]
#print(manday_weather)

####      Finding data from row of highest temperature day ####
highest_temp_day = data[data.temp == max_temp]
#print(highest_temp_day)

####  Finding and printing a specific day temp in Fahrenheit

print(f'{(9/5)*int(data[data.day == "Monday"].temp) + 32}F')