from matplotlib.ticker import FuncFormatter

# Volume des transactions par heure
fig, ax = plt.subplots()

(df_or.groupby("Hour")
 .size()
 .plot.bar(title="Volume des transactions par heure", rot=0, ax=ax)
);

# Volume des transactions UK / Non UK
fig, ax = plt.subplots()

(df_or.UK.value_counts()
 .sort_index(ascending=False)
 .plot.pie(title="Volume des transactions UK / Non UK", autopct='%.1f%%', ax=ax)
 .set_ylabel("")
);

# Montant des transactions UK / Hors UK
fig, ax = plt.subplots()

(df_or.groupby("UK")["Amount"]
 .sum()
 .sort_index(ascending=False)
 .plot.pie(title="Montant des transactions UK / Non UK", autopct='%.1f%%', ax=ax)
 .set_ylabel("")
);

# Volume des transactions par pays Non UK
fig, ax = plt.subplots(figsize=(10, 8))

(df_or.Country.value_counts()
 .drop("United Kingdom")
 .plot.barh(title="Volume des transactions par pays Non UK", ax=ax)
)

ax.get_xaxis().set_major_formatter(FuncFormatter(lambda x, p: f"{int(x/1000)}K"))

# Montant des transactions par pays Non UK
fig, ax = plt.subplots(figsize=(10, 8))

(df_or.groupby("Country")["Amount"].sum()
 .drop("United Kingdom")
 .sort_values(ascending=False)
 .plot.barh(title="Montant des transactions par pays Non UK", ax=ax)
)

ax.get_xaxis().set_major_formatter(FuncFormatter(lambda x, p: f"{int(x/1000)}K"))
ax.set_ylabel("");

# Volume des transactions par type

fig, ax = plt.subplots(figsize=(10, 6))

(df_or
 .groupby([pd.Grouper(freq='M'), 'Type']).size()
 .unstack()
 .plot.bar(title="Volume des transactions par type", color=['g', 'r'], rot=0, ax=ax)
)

ax.set_xticklabels([f"{x:%b %y}" for x in df_or.resample('M').size().index])
ax.get_yaxis().set_major_formatter(FuncFormatter(lambda x, p: f"{int(x/1000)}K"))

# Montant des transactions par type
fig, ax = plt.subplots(figsize=(10, 6))

(df_or
 .groupby([pd.Grouper(freq='M'), 'Type'])['Amount']
 .sum()
 .unstack()
 .plot.bar(title="Montant des transactions par type", color=['g', 'r'], rot=0, ax=ax)
)

ax.set_xticklabels([f"{x:%b %y}" for x in df_or.resample('M').size().index])
ax.axhline(y=0, color='k', ls=':')
ax.get_yaxis().set_major_formatter(FuncFormatter(lambda x, p: f"{int(x/1000)}K"))

# sparklines
(df_or.loc[lambda df_: df_.Amount>0.0]
 .groupby("Country")
 .agg(mean=("Amount", lambda s_: s_.mean().round(2)),
      trend=("Amount", lambda s_: sparkl(s_.resample('Q').mean().fillna(0))))
)
