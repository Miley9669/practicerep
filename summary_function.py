def summ_data(df, col):
    s = df[col].sum()
    print(f"{col} sum: {s}")