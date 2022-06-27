from itertools import count
import pandas
from sympy import N

def color_counter():
    datas = pandas.read_csv("2018_Cental_Packs_Census.csv")
    
#def gray_counter():   
    number_gray = 0
    n_gray = datas["Primary Fur Color"].to_list()
    for gray in n_gray:
        if gray == "Gray":
            number_gray = number_gray + 1
    #print(f"Number of Gray is {number_gray}")
    
#def cinnamon_counter():
    number_cinnamon = 0
    n_cinnamon = datas["Primary Fur Color"].to_list()
    for cinnamon in n_cinnamon:
        if cinnamon == "Cinnamon":
            number_cinnamon = number_cinnamon + 1
    #print(f"Number of Cinnamon is {number_cinnamon}")

#def black_counter():
    number_black = 0
    n_black = datas["Primary Fur Color"].to_list()
    for black in n_black:
        if black == "Black":
            number_black = number_black + 1
    #print(f"Number of Black is {number_black}")

    data_dict = {
        "Fur Color": ["Gray","Cinnamon","Black"],
        "Counts": [number_gray,number_cinnamon,number_black]
    }
    # Creating a dataframe 
    data_frame = pandas.DataFrame(data_dict)
    data_frame.to_csv("Counts of data.csv")
    with open("Counts of data.csv") as color_data:
        print(color_data.read())
    
color_counter()            
   
    


    
    
