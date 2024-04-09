import streamlit as st
import src.visualization.visualize as viz
from src.data import make_dataset
import pandas as pd
import statsmodels.formula.api as smf

st.header("Nossa aplicação")

df = make_dataset.read_and_process_data("https://github.com/CardosoJr/bootcamp/raw/main/Datasets/Melbourne/MELBOURNE_HOUSE_PRICES_LESS.pq")
fig = viz.plot_histograms(df)
st.plotly_chart(fig)



model = smf.ols("Price ~ Rooms + Distance", df).fit()

rooms = st.number_input("Number of Rooms:", min_value = 1, max_value = 20, value = 2)
distance = st.number_input("Distance:", min_value = 1.0, max_value = 20.0, value = 5.0)

if st.button("Calcular Preço"):
    new_houses = pd.DataFrame({'Rooms' : [rooms], 'Distance' : [distance]})
    predict_price = model.predict(new_houses)[0]
    st.write(f"Predicted price is ${predict_price:,.2f}")
