import json
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon 
import folium
import webbrowser
import pharmacy_data_pre
import argparse











def main(args):

    pharmacy_location_data = pharmacy_data_pre.pharmacy_data(args)

    

    return

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('--pharmacy_data_path', default = './pharmacy_regulatory_gwnakgu.csv', type=str, 
                        help='pharmacy data path')

    args = parser.parse_args()

    main(args)