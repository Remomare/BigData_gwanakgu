import json
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon 
import folium
import webbrowser

from map import seoul_geojson_mapping, pharmacy_gwnakgu_mapping

def open_gwnaku_ploygon():
    with open("location.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # Polygon 좌표 추출
    coordinates = data['features'][0]['geometry']['coordinates'][0]

    # Polygon 객체 생성
    polygon = Polygon(coordinates, closed=True, edgecolor='r', linewidth=2, fill=False)

    # 그래프에 Polygon 추가
    fig, ax = plt.subplots()
    ax.add_patch(polygon)

    # 축 범위 설정
    min_x, max_x = min(x for x, _ in coordinates), max(x for x, _ in coordinates)
    min_y, max_y = min(y for _, y in coordinates), max(y for _, y in coordinates)
    ax.set_xlim(min_x, max_x)
    ax.set_ylim(min_y, max_y)

    # 그래프 표시
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Polygon Visualization')
    plt.grid(True)
    plt.show()


if __name__  == "__name__":
    pharmacy = pharmacy_gwnakgu_mapping()