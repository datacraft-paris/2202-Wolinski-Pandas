# method chaining
def prep_names(df):
    return (df.dropna()
            .loc[lambda df_: df_.name.str.len() > 1]
            .assign(gender=lambda df_: df_.gender.map({1:"M", 2:"F"}),
                    name=lambda df_: df_.name.str.title())
            .astype({'gender':'category', 'year':'uint16', 'births':'uint16'})
            .loc[:, ["year", "name", "gender", "births"]]
            .sort_values(["year", "gender", "births", "name"], ascending=[True, True, False, True])
            .reset_index(drop=True)
    )
