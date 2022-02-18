import re

def prep_change(df, currencies):

    def rename_column(col):
        if col == "Titre :":
            return "Date"
        else:
            m = re.search(r'\(([A-Z]{3})\)$', col)
            return m.group(1) if m else col

    return (df.rename(columns=lambda col: rename_column(col))
            .assign(Date=lambda df_: pd.to_datetime(df_["Date"], format='%d/%m/%Y', errors='ignore'))
            .set_index("Date")
            .loc[:, currencies]
            .dropna()
            .sort_index()
           )

df_change1 = prep_change(df_change, ["USD", "CHF", "GBP", "JPY", "RUB", "CNY"])
