from sqlalchemy import create_engine
import geopandas as gpd

# import logging
import re
import os
from os.path import dirname
import gc

# table = "censustract"
table = "censustract_new"
col = [
    "CENSUSCODE",
    "STATEFP",
    "COUNTYFP",
    "TRACTCE",
    "BLKGRPCE",
    "AFFGEOID",
    "GEOID",
    "LSAD",
    "ALAND",
    "AWATER",
    "state",
    # "geo_str",
    "geo_text",
    # "type",
]


def create_geojson(unclean_str):
    # Example: "POLYGON((-86.419951 32.474125,-86.415518 32.476692,-86.412478 32.477032,-86.411845 32.478527,-86.411675 32.459798,-86.418088 32.46049,-86.418266 32.470672,-86.418582 32.47193,-86.418724 32.47227,-86.419951 32.474125))";
    type_geo = unclean_str.split(" ", maxsplit=1)[0]
    unclean_str = unclean_str.split(" ", maxsplit=1)[1]
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


for root, dirs, file in os.walk(dirname(__file__)):
    for f in file:
        if re.search(r".shp$", f):
            # read the file
            file_path = root + "/" + f
            polyDf = gpd.read_file(file_path)
            print(f"file_path={file_path}")

            # create state column and fill it base on path of the current loop
            state_name = root.split("/")[-1].replace("_", " ")
            polyDf["state"] = [state_name] * len(polyDf)
            polyDf["geo_text"] = polyDf["geometry"].to_wkt()

            # create censuscode
            polyDf["CENSUSCODE"] = (
                polyDf["STATEFP"] + polyDf["COUNTYFP"] + polyDf["TRACTCE"]
            )
            polyDf["CENSUSCODE"] = polyDf["CENSUSCODE"].str.lstrip("0")
            engine = create_engine(
                "mysql+pymysql://vinny:ewy8kb2LDeyQT5o3BjvNLFpW2YE1g3NmZoIFPzXiL4GX7U5ect@localhost:3306/test_django"
            )

            # sort
            polyDf = polyDf[col]
            polyDf.columns = [x.lower() for x in col]
            gc.collect
            # polyDf.to_sql(table, engine, index=False, if_exists="append")

# update censustract set geometry = ST_GeomFromText(geo_str);
