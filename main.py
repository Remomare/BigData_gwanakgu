import json
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon 
import folium
import webbrowser
import pharmacy_data_pre
import argparse
import map

def visualizaition_pharmacy_location(args):
    


    return


def main(args):

    
    if args.visualization_pharmacy == True:
        pharmacy_location_data = pharmacy_data_pre.pharmacy_data(args)

        print(pharmacy_location_data)

        map_pharmacy = map.pharmacy_gwnakgu_mapping(args, pharmacy_location_data)

        map_pharmacy.save(args.pharmacy_location_map_path)

        webbrowser.open(args.pharmacy_location_map_file_name)

    return

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('--pharmacy_data_path', default = './pharmacy_regulatory_gwnakgu.csv', type=str, 
                        help='pharmacy data path')
    parser.add_argument('--pharmacy_location_map_file_name', default='location_of_pharmacy.html', type=str)
    parser.add_argument('--pharmacy_location_map_path', default='./location_of_pharmacy.html', type=str,
                        help="pharmacy location map path")
    

    parser.add_argument('--visualization_pharmacy', default=True, type=bool )


    args = parser.parse_args()

    main(args)