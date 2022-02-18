# load with default missing

na1 = df_cities1.isna().sum()

# load without missing values except ""
df_cities0 = pd.read_csv("data/cities500.zip",
                         sep="\t",
                         header=None,
                         dtype=str,
                         na_values="",
                         keep_default_na=False,
                         names=['geonameid', 'name', 'asciiname', 'alternatenames', 'latitude', 'longitude', 'feature_class', 'feature_code', 'country_code', 'cc2', 'admin1_code', 'admin2_code', 'admin3_code', 'admin4_code', 'population', 'elevation', 'dem', 'timezone', 'modification_date'])

na0 = df_cities0.isna().sum()

# gap
print(na1 - na0)

# which country codes are interpretted as NaN
na = ((df_cities0["country_code"].value_counts() - df_cities1["country_code"].value_counts())
      .loc[lambda s_: s_ != 0]
      .index
      .tolist()
     )
print(na)

# which admin2 codes are interpretted as NaN
na = ((df_cities0["admin2_code"].value_counts() - df_cities1["admin2_code"].value_counts())
      .loc[lambda s_: s_ != 0]
      .index
      .tolist()
     )
print(na)

# countries with an admin2 code = NA
print(df_cities0.loc[lambda df_: df_["admin2_code"] == "NA", "country_code"]
      .value_counts())
