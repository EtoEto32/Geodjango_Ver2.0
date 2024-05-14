import os
from map.models import Evacuation
from django.contrib.gis.utils import LayerMapping

# ModelとGeojsonファイルのカラムのマッピング
mapping = {
    "evacuation_site": "指定緊急避難場所",
    "location": "所在地",
    "flood": "洪水",
    "landslides": "がけ崩れ、土石流及び地滑り",
    "storm_surge": "高潮",
    "earthquake": "地震",
    "tsunami": "津波",
    "massive_fire": "大規模な火事",
    "inland_flooding": "内水氾濫",
    "volcanic_phenomena": "火山現象",
    "geom": "POINT",
}

# 2つ目のファイルパス
geojson_file_ishikawa = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "data", "hinanjo_ishikawa.geojson")
)


# 実行
def run(verbose=True):
    # 2つ目のファイルに対する処理
    lm_ishikawa = LayerMapping(
        Evacuation, geojson_file_ishikawa, mapping, transform=False, encoding="UTF-8"
    )
    lm_ishikawa.save(strict=True, verbose=verbose)
