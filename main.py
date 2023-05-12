import json
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon 
import folium
import webbrowser
import data_preprocessing
import argparse
import map


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

        #print(population_of_gwankgu_by_dong)
        print(number_of_pharmacy_by_dong)


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


    args = parser.parse_args()

    main(args)