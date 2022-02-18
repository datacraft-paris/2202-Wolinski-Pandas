# cmap
(df_of.notna()
 .sum()
 .mul(100/len(df_of))
 .to_frame()
 .rename({0: "completion"}, axis=1)
 .style.background_gradient(cmap="RdYlGn")
 .format("{:.1f}%")
)
