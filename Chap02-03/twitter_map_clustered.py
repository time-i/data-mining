# Chap02-03/twitter_map_clustered.py
from argparse import ArgumentParser
import folium


def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--geojson', type=str, default='geo.json')
    parser.add_argument('--map', type=str, default='example2_map.html')
    return parser


def make_map(geojson_file, map_file):
    tweet_map = folium.Map(location=[50, 5],
                           zoom_start=5)
    marker_cluster = folium.MarkerCluster().add_to(tweet_map)

    geojson_layer = folium.GeoJson(open(geojson_file),
                                   name='geojson')
    geojson_layer.add_to(marker_cluster)
    tweet_map.save(map_file)


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    make_map(args.geojson, args.map)
