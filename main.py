import json
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon 
import folium
import webbrowser
import data_preprocessing
import argparse
import pandas as pd
import map
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols
import math

def main(args):
    
    if args.visualization_pharmacy == True:
        pharmacy_location_data = data_preprocessing.pharmacy_data(args)

        print(pharmacy_location_data)

        map_pharmacy = map.pharmacy_gwnakgu_mapping(args, pharmacy_location_data)

        map_pharmacy.save(args.pharmacy_location_map_path)

        webbrowser.open(args.pharmacy_location_map_file_name)

    if args.visulization_population_of_gwanakgu_by_dong == True:
        population_of_gwankgu_by_dong  = data_preprocessing.population_of_gwanakgu_by_dong_data(args)
        number_of_pharmacy_by_dong = data_preprocessing.pharmacy_location_by_dong_data(args)

        
        x = np.arange(22)
        y1 = pd.to_numeric(population_of_gwankgu_by_dong['인구수(계)'].str.replace(',', ''))
        y1['봉천동'] = 0
        y2 = number_of_pharmacy_by_dong.loc[0]

        plt.rc('font', family='NanumSquareRoundOTF')
        plt.rc('xtick', labelsize=8)
        plt.figure(figsize = (12,5))

        ax1 = plt.subplot()

        ax1.bar(x-0.2, y1, width=0.4, color='red')
        ax1.set_ylabel("인구 수")
        ax1.set_ylim(10000,40000)

        ax2 = ax1.twinx()

        ax2.bar(x+0.2,y2, width=0.4, color='green')
        ax2.set_ylim(0,110)
        ax2.set_ylabel("약국 수")

        plt.title("관악구 행정동 별 인구 수 & 약국 수")
        plt.xticks(x, number_of_pharmacy_by_dong.columns.to_list())

        plt.savefig("bar graph.png")    


    if args.Linear_Regression== True:
        #Linear Regression
        # y= 75*x  Reference Line
        # x = 약사 수 = 약국 수 (약국당 약사 한명만 있다고 가정) #하루 적정 약사당 조제건수 75 #y: 총 조제건수= 수용가능 인구
        #y_dong : 연별 관악구 합계 인구수 #x_dong = 연별 약국(=약사) 수

        population_data_set = data_preprocessing.population_of_gwanakgu(args)
        number_of_pharmacy = data_preprocessing.pharmacy_location_by_dong_data(args)

        population_data = pd.to_numeric(population_data_set.loc['합계'].str.replace(',', ''))

        y_dong = population_data
        x_dong = np.repeat(number_of_pharmacy.loc[0].sum(),population_data.count())

        x = np.arange(population_data.count())
        y = 75*x
        plot_data = [[y_dong.transpose()], [x_dong]]

        model = LinearRegression()
        model.fit( y_dong.to_numpy().reshape(-1,1) ,x_dong.reshape(-1,1) ) 

        r_sq = model.score(x_dong.reshape(-1,1), y_dong.to_numpy())
        print(model.intercept_) 
        print(model.coef_)  

        plt.rc('font', family='NanumSquareRoundOTF')
        plt.figure(figsize = (12,5))
        plt.title("model result")

        plt.plot(x, x_dong * 75, color = 'red') #reference line y = 75*x
        plt.plot(x, np.exp(model.predict(x_dong.reshape(-1,1))* 75), color='blue')

        plt.savefig("model result.png")

    return

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('--pharmacy_data_path', default = './pharmacy_regulatory_gwnakgu.csv', type=str, 
                        help='pharmacy data path')
    parser.add_argument('--pharmacy_location_map_file_name', default='location_of_pharmacy.html', type=str)
    parser.add_argument('--pharmacy_location_map_path', default='./location_of_pharmacy.html', type=str,
                        help="pharmacy location map path")
    
    parser.add_argument('--population_of_gwanakgu_by_dong', default="./population_of_gwanakgu_by_dong_20220930.csv", type=str)

    parser.add_argument('--parmacy_location_by_dong_file_path', default="./pharmacy_gwanakgu_20220809.csv", type=str)
    
    parser.add_argument('--population_of_gwanakgu_file_path', default='./gwanakgu_population.csv')

    parser.add_argument('--visualization_pharmacy', default=False, type=bool )
    parser.add_argument('--visulization_population_of_gwanakgu_by_dong', default= False, type=bool)
    parser.add_argument('--Linear_Regression', default=True)


    args = parser.parse_args()

    main(args)