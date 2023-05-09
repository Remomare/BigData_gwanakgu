import pandas as pd


def pharmacy_data():
    
    filepath = "./pharmacy_regulatory_gwnakgu.csv"

    data_set = pd.read_csv(filepath)

    mask_1 = data_set["영업상태코드"] == 1

    filtered_data = data_set.loc[mask_1, : ]
    location_data = filtered_data[["좌표정보(X)", "좌표정보(Y)"]]
    print(location_data)

    return

def main():
    pharmacy_data()

    return


if __name__ == "__main__" :
    main()