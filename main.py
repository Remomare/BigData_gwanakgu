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
import sklearn
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols


def main(args):

    
    if args.visualization_pharmacy == True:
        pharmacy_location_data = data_preprocessing.pharmacy_data(args)

        print(pharmacy_location_data)

        map_pharmacy = map.pharmacy_gwnakgu_mapping(args, pharmacy_location_data)

        map_pharmacy.save(args.pharmacy_location_map_path)

        webbrowser.open(args.pharmacy_location_map_file_name)

    if args.visulization_population_of_gwanakgu_by_dong == True:
        population_of_gwankgu_by_dong  = data_preprocessing.population_of_gwanakgu_by_dong_data(args)
        
        x = np.arange(21)
        y = pd.to_numeric(population_of_gwankgu_by_dong['인구수(계)'].str.replace(',', ''))

        plt.rc('font', family='NanumSquareRoundOTF')
        plt.rc('xtick', labelsize=8)
        plt.figure(figsize = (12,5))
        plt.bar(x, y, width=0.8)
        plt.title("관악구 행정동 별 인구수")
        plt.ylabel("인구수")
        plt.xticks(x, population_of_gwankgu_by_dong['행정기관'].to_list())

        print(plt.ylim())
        plt.savefig("bar graph.png")    

    if args.visulization_number_of_pharmacy == True:
        number_of_pharmacy_by_dong = data_preprocessing.pharmacy_location_by_dong_data(args)


    if args.Linear_Regression== True:
        #Linear Regression
        # y= 75*x  Reference Line
        # x = 약사 수 = 약국 수 (약국당 약사 한명만 있다고 가정) #하루 적정 약사당 조제건수 75 #y: 총 조제건수= 수용가능 인구
        #y_dong : 연별 관악구 합계 인구수 #x_dong = 연별 약국(=약사) 수

        population_data_set = data_preprocessing.dapopulation_of_gwanakgu(args)

        x_dong = population_data_set.loc['관악구']
        y_dong = 0

        x = 0

        plot_data = [y_dong,x_dong]

        model = sklearn.linear_model.LinearRegression()    
        model.fit(plot_data[["y_dong"]], plot_data[["x_dong"]]) 

        r_sq = model.score(plot_data[["y_dong"]], plot_data[["x_dong"]])
        print(model.intercept_) 
        print(model.coef_)  

        sns.relplot(x= "x_dong", y = "y_dong", data = plot_data)
        sns.lineplot(x= "x_dong", y = "y_dong", color="r", data = plot_data) 
        plt.plot(y=75*x) #reference line y = 75*x

        #One-Way Anova
        model = ols('y_dong ~ x_dong', data= plot_data).fit() #ols ordinary least square
        sm.stats.anova_lm(model) 
    


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
    

    parser.add_argument('--visualization_pharmacy', default=False, type=bool )
    parser.add_argument('--visulization_population_of_gwanakgu_by_dong', default= True, type=bool)

    parser.add_argument('--population_of_gwanakgu_file_path', default='./population_of_gwanakgu')

    parser.add_argument('--Linear_Regression', default=False)


    args = parser.parse_args()

    main(args)