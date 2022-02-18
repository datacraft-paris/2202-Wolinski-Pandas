# Top N prénoms de la décennie
def plot_topn_names_decade(df, year, n=5):
    """Plot births by year for the top n names given in a decade"""

    fig, ax = plt.subplots(figsize=(10, 6))

    return (df.loc[df.name.isin(topn_names_decade(df, year, n))]
            .pivot_table(index="year",
                         columns="name",
                         values="births",
                         fill_value=0)
            # plot
            .plot.line(title=f"Top {n} prénoms de la décennie {year}-{year+9}", ax=ax)
            .legend(bbox_to_anchor=(1.15, 1.0))
           )
