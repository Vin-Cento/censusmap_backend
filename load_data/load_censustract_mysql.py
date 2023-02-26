from sqlalchemy import create_engine
import geopandas as gpd

# import logging
import re
import os
from os.path import dirname
import gc

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
    "geo_str"
]

for (root, dirs, file) in os.walk(dirname(__file__)):
    for f in file:
        if re.search(r".shp$", f):

            # read the file
            file_path = root + "/" + f
            polyDf = gpd.read_file(file_path)
            print(f"file_path={file_path}")

            # create state column and fill it base on path of the current loop
            state_name = root.split("/")[-1].replace("_", " ")
            polyDf["state"] = [state_name] * len(polyDf)
            polyDf["geo_str"] = polyDf["geometry"].to_wkt()

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
            print(polyDf.columns)

            polyDf.to_sql(
                "censustract", engine, index=False, if_exists="append"
            )

# update censustract set geometry = ST_GeomFromText(geo_str);
