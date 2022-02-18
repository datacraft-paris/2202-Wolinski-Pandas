def prep_retail(df):
            df.drop_duplicates()
            .astype({"Quantity":"float32", "UnitPrice":"float32"})
            .assign(InvoiceDate=lambda df_: pd.to_datetime(df_.InvoiceDate, format="%m/%d/%Y %H:%M"),
                    Month=lambda df_: df_.InvoiceDate.dt.month_name(),
                    DayOfWeek=lambda df_: df_.InvoiceDate.dt.day_name(),
                    Hour=lambda df_: df_.InvoiceDate.dt.hour,
                    Amount=lambda df_: df_.Quantity * df_.UnitPrice,
                    Type=lambda df_: np.where(df_.Quantity >= 0, "Purchase", "Return"),
                    UK=lambda df_: df_.Country.where(df_.Country=="United Kingdom", "Hors UK"))
            .set_index("InvoiceDate")
            .sort_index()
           )

df_or = prep_retail(df_or)
