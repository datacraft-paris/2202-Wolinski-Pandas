# Taux de change divisés par la moyenne
fig, ax = plt.subplots(figsize=(10,6))

(df_change1.pipe(lambda df_: df_.div(df_.mean()))
 .plot.line(title="Taux de change divisés par la moyenne", ax=ax)
 .legend(bbox_to_anchor=(1.05, 1.0))
);

# Taux de change divisés par la dernière valeur
fig, ax = plt.subplots(figsize=(10,6))

(df_change1.pipe(lambda df_: df_.div(df_.iloc[-1]))
 .plot.line(title="Taux de change divisés par la dernière valeur", ax=ax)
 .legend(bbox_to_anchor=(1.05, 1.0))
);
# Moyenne glissante sur 30 jours
fig, ax = plt.subplots(figsize=(10,6))

(df_change1.pipe(lambda df_: df_.div(df_.mean()))
 .rolling(30)
 .mean()
 .plot.line(title="Moyenne glissante sur 30 jours", ax=ax)
 .legend(bbox_to_anchor=(1.05, 1.0))
);

# Maximum glissant sur 100 jours
fig, ax = plt.subplots(figsize=(10,6))

(df_change1.pipe(lambda df_: df_.div(df_.mean()))
 .rolling(100)
 .max()
 .plot.line(title="Maximum glissant sur 100 jours", ax=ax)
 .legend(bbox_to_anchor=(1.05, 1.0))
);

# moyenne et tendance pour USD
(df_change1.groupby(pd.Grouper(freq='A'))
 .agg(USD=('USD', lambda s_: s_.mean().round(3)),
     trend_USD=('USD', lambda s_: sparkl(s_.resample('Q').mean())))
)

# moyenne et tendance pour toutes les devises
def mean_trend_year(year):
    return (df_change1.loc[str(year)]
           .pipe(lambda df_: pd.concat([df_.mean(), (df_.resample('Q')
                                                     .mean()
                                                     .apply(sparkl))],
                             axis=1))
           .rename({0: 'mean', 1:'trend'}, axis=1)
           )
