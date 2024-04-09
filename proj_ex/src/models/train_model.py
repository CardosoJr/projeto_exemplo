def train(df):
    model = smf.ols("Price ~ Rooms + Distance", df).fit()
    return model