import pandas as pd
import pyproj


def pharmacy_data(args):
    
    filepath = args.pharmacy_data_path

    if filepath == None:
        filepath = "./pharmacy_regulatory_gwnakgu.csv"

    data_set = pd.read_csv(filepath)

    mask_1 = data_set["영업상태코드"] == 1

    filtered_data = data_set.loc[mask_1, : ]
    location_data = filtered_data[["좌표정보(X)", "좌표정보(Y)"]]
    
    location_data = location_data.dropna(how='all')
    
    transformer = pyproj.Transformer.from_crs("epsg:2097", "EPSG:4326")

    for idx, row in location_data.iterrows():
        origin_x = row[0]
        origin_y = row[1]

        change_x, change_y = transformer.transform(origin_x, origin_y)

        location_data.loc[idx] = [change_x, change_y]
    
    return location_data

def main():
    location_data = pharmacy_data()

    print(location_data)

    return


if __name__ == "__main__" :
    main()