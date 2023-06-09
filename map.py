import folium
import pandas as pd
import requests
import json
from folium.plugins import MarkerCluster

# 서울 행정구역 json raw파일(githubcontent)
def seoul_geojson_mapping():
    r = requests.get('https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json')
    c = r.content
    seoul_geo = json.loads(c)

    m = folium.Map( location=[37.559819, 126.963895], zoom_start=11)

    folium.GeoJson(seoul_geo, name='지역구').add_to(m)
    return m


def pharmacy_gwnakgu_mapping(args, location_data):

    map_pharmacy = folium.Map(location=[37.475386, 126.953844], zoom_start=14)

    for _, row in location_data.iterrows():
        folium.Circle(location=[row[0],row[1]], radius=80, color="red").add_to(map_pharmacy)

    return map_pharmacy

def mapping():

    m = folium.Map(location=[37.559819, 126.963895], zoom_start=11)

    seoul_geo = '''{
        "type": "Features",
        "features": 
        [
            {
                "type": "Feature",
                "properties": 
                {
                    "code": "11210",
                    "name": "관악구",
                    "name_eng": "Gwanak-gu",
                    "base_year": "2013"
                },
                "geometry": 
                {
                    "type": "Polygon",
                    "coordinates": 
                    [
                        [
                            [126.97901795539295, 37.47376525108475],
                            [126.98367668291802, 37.473856492692086]
                        ]
                    ]
                }
            }
        ]
    }'''

    folium.GeoJson(seoul_geo, name='지역구').add_to(m)
    return m

def tempm_app():
    m = folium.Map(location=[37.475386, 126.953844], zoom_start=13)
    seoul_geo = {
        "type": "FeatureCollection",
        "features":    
        [
            {
                "type": "Feature",
                "properties": 
                {
                    "code": "custom",
                    "name": "Custom Area"
                },
                "geometry": 
                {
                    "type": "Polygon",
                    "coordinates": 
                    [
                        [
                            [126.98367668291802, 37.473856492692086],
                            [126.9846374349825, 37.46996301876212],
                            [126.98662755598336, 37.466937278295305],
                            [126.98896316546526, 37.465041871263544],
                            [126.99026416700147, 37.46271603227842],
                            [126.98956736277059, 37.457600756400446],
                            [126.99072073195462, 37.455326143310025],
                            [126.98484249930785, 37.45391909788938],
                            [126.9829408096241, 37.450206782833206],
                            [126.97835022660695, 37.447659155806164],
                            [126.97608193440507, 37.44478918862847],
                            [126.9731300196836, 37.444722870088114],
                            [126.96650852936277, 37.44276983031553],
                            [126.96618702895445, 37.439376482995094],
                            [126.96520439085143, 37.438249784006246],
                            [126.9614877541633, 37.437956805629675],
                            [126.96054904645496, 37.43673997185797],
                            [126.95527369898224, 37.43673711968809],
                            [126.9473688393239, 37.4347689647565],
                            [126.94440352544498, 37.43476162120059],
                            [126.9415292183489, 37.43315139671158],
                            [126.94037501670272, 37.43462213966344],
                            [126.9405640311191, 37.437501011208845],
                            [126.9376981355065, 37.44041709605302],
                            [126.93312955918624, 37.44290014710262],
                            [126.93309127096236, 37.44533734785938],
                            [126.93084408056525, 37.447382928333994],
                            [126.92527839995981, 37.45161884570837],
                            [126.9245243450059, 37.45392293573877],
                            [126.91887928082078, 37.45495082787016],
                            [126.9167728146601, 37.45490566423789],
                            [126.91641538472182, 37.45870245071989],
                            [126.91495285904284, 37.461166184511065],
                            [126.91584245173756, 37.462474576247985],
                            [126.91374656127704, 37.46375990852858],
                            [126.91032166997253, 37.469818629944285],
                            [126.91280966667205, 37.47083063715413],
                            [126.91405961426707, 37.47416764846582],
                            [126.9115784808617, 37.4753960485947],
                            [126.91181700249076, 37.47814319736339],
                            [126.90276666415615, 37.47652007992712],
                            [126.90156094129895, 37.47753842789901],
                            [126.90531975801812, 37.48218087575429],
                            [126.90805655355825, 37.48218338568103],
                            [126.91533979779165, 37.484392208242134],
                            [126.91916807529428, 37.48660606817164],
                            [126.92639563063156, 37.48715979752876],
                            [126.92869559665061, 37.49132126714011],
                            [126.92981699800066, 37.49218420958284],
                            [126.93346386636452, 37.49043826776755],
                            [126.93669800083833, 37.49026778789087],
                            [126.93844070234584, 37.4893532861132],
                            [126.94373156012337, 37.48938843727846],
                            [126.94922661389508, 37.49125437495649],
                            [126.95396955055433, 37.48955250290043],
                            [126.9559655046206, 37.48820165625994],
                            [126.95881175306481, 37.48874989165474],
                            [126.96329694970828, 37.4905835370787],
                            [126.96291787066104, 37.48803272157808],
                            [126.96443983219191, 37.48442261322104],
                            [126.9634428120456, 37.48067931902171],
                            [126.9725891850662, 37.472561363278125],
                            [126.97901795539295, 37.47376525108475],
                            [126.98367668291802, 37.473856492692086]
                        ]
                    ]
                }
            }
        ]
    }
    
    folium.GeoJson(seoul_geo, name='관악구').add_to(m)

    folium.Circle([37.486291, 126.947371], popup='밝은미소약국',radius=70, color="orange").add_to(m)
    folium.Circle([37.484570, 126.930107], popup='365열린약국',radius=100, color="orange").add_to(m)
    folium.Circle([37.484419, 126.927725], popup='호호약국',radius=100, color="orange").add_to(m)
    folium.Circle([37.486291, 126.947373], popup='가까운약국',radius=100, color="orange").add_to(m)
    folium.Circle([37.476589, 126.958770], popup='대림약국',radius=100, color="orange").add_to(m)
    folium.Circle([37.475452, 126.965446], popup='새태평양온누리약국',radius=100, color="orange").add_to(m)
    folium.Circle([37.484563, 126.942898], popup='두산약국',radius=100, color="orange").add_to(m)
    folium.Circle([37.482163, 126.942714], popup='봉천프라자약국',radius=100, color="orange").add_to(m)
    folium.Circle([37.482622, 126.942692], popup='육당약국',radius=100, color="orange").add_to(m)
    folium.Circle([37.482724, 126.942778], popup='휴베이스다정약국',radius=100, color="orange").add_to(m)
    return m