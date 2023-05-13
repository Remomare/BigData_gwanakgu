import pandas as pd
import pyproj


def pharmacy_data(args):
    
    filepath = args.pharmacy_data_path

    if filepath == None:
        filepath = "./pharmacy_regulatory_gwnakgu.csv"

    data_set = pd.read_csv(filepath, encoding="utf-8")

    mask_1 = data_set["영업상태코드"] == 1

    filtered_data = data_set.loc[mask_1, : ]
    location_data = filtered_data[["좌표정보(X)", "좌표정보(Y)"]]
    
    location_data = location_data.dropna(how='all')
    
    transformer = pyproj.Transformer.from_crs("epsg:2097", "epsg:4326")

    for idx, row in location_data.iterrows():
        origin_x = row[0]
        origin_y = row[1]

        change_x, change_y = transformer.transform(origin_x, origin_y)

        location_data.loc[idx] = [change_x, change_y]
    
    return location_data

def population_of_gwanakgu_by_dong_data(args):

    file_path = args.population_of_gwanakgu_by_dong

    if file_path is None:
        file_path = "./population_of_gwanakgu_by_dong_20220930.csv"

    data_set = pd.read_csv(file_path, encoding="utf-8")

    data_set.drop(['구성비(계)','구성비(남)','구성비(여)','성비','세대수','세대당인구'], axis=1, inplace=True)

    return data_set

def pharmacy_location_by_dong_data(args):

    filepath = args.pharmacy_data_path

    if filepath == None:
        filepath = "./pharmacy_regulatory_gwnakgu.csv"

    data_set = pd.read_csv(filepath, encoding="utf-8", index_col=0)

    mask_1 = data_set["영업상태코드"] == 1
    filtered_data = data_set.loc[mask_1, : ]

    location_data = filtered_data[['지번주소']]

    location_data = location_data.dropna(how='all')

    dong_list = ['보라매동', '청림동', '성현동', '행운동', '낙성대동', '청룡동',
                '은천동', '중앙동', '인헌동', '남현동', '서원동', '신원동', '서림동',
                '신사동', '신림동', '난향동', '조원동', '대학동', '삼성동', '미성동', '난곡동', '봉천동']
        
    pharmacy_number_set = pd.DataFrame(index=[0], columns=dong_list)

    for dong in dong_list:
        count = 0
        for _ ,row in location_data.iterrows():
            if(dong in row['지번주소']):
                count += 1
        pharmacy_number_set.loc[0, dong] = count
    
    return pharmacy_number_set

def population_of_gwanakgu(args):

    file_path = args.population_of_gwanakgu_file_path

    data_set = pd.read_csv(file_path, encoding='utf-8', index_col=0)

    data_set.dropna(axis=1, inplace=True)

    return data_set
