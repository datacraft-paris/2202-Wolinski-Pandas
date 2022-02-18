# Graphique avec le nombre de naissances d'un prénom et d'un genre
def plot_name_gender(df, name, gender):
    """Plot births by year for a given name and gender"""
    return (df.loc[lambda df_: (df_.name==name) & (df_.gender==gender)]
            .plot.line(x="year", y="births", title=f"Nombre de naissances de {name} ({gender})")
            )
