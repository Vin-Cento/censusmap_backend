from os.path import dirname
import geopandas as gpd


def create_geojson(unclean_str):
    # Example: "POLYGON((-86.419951 32.474125,-86.415518 32.476692,-86.412478 32.477032,-86.411845 32.478527,-86.411675 32.459798,-86.418088 32.46049,-86.418266 32.470672,-86.418582 32.47193,-86.418724 32.47227,-86.419951 32.474125))";
    type_geo = unclean_str.split(" ", maxsplit=1)[0]
    unclean_str = unclean_str.split(" ", maxsplit=1)[1]
    print(unclean_str)
    clean_str = ""
    for i in range(len(unclean_str)):
        if unclean_str[i] == "(":
            if unclean_str[i + 1] == "(":
                clean_str += "["
            else:
                clean_str += "[["
        elif unclean_str[i] == ")":
            try:
                if unclean_str[i + 1] == ")":
                    clean_str += "]"
                else:
                    clean_str += "]]"
            except:
                clean_str += "]]"
        elif unclean_str[i] == " ":
            if unclean_str[i - 1] == ",":
                continue
            else:
                clean_str += ","
        elif unclean_str[i] == ",":
            clean_str += "],["
        else:
            clean_str += unclean_str[i]
    return type_geo, clean_str


root = dirname(__file__)
file_path = root + "/" + "states_shapefile/american_samoa/cb_2021_60_bg_500k.shp"
polyDf = gpd.read_file(file_path)
print(f"file_path={file_path}")
#
polyDf["geo_str"] = polyDf["geometry"].to_wkt()
polyDf["type_geo"], polyDf["geo_str"] = zip(*polyDf["geo_str"].apply(create_geojson))
print(polyDf.head())
