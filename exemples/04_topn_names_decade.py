# Top N prénoms de la décennie
def topn_names_decade(df, year, n=5):
    """Return list of top 7 names given in a decade"""
    return (df.loc[df.year.isin(range(year, year+10))]
            .groupby("name")["births"]
            .sum()
            .nlargest(n)
            .index
           )
