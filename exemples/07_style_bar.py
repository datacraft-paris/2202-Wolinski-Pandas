# bar
(df_of.notna()
 .sum()
 .to_frame()
 .rename({0: "completion"}, axis=1)
 .style.bar(color='lightgreen')
)
