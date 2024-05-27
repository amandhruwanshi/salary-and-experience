import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from PIL import Image
from matplotlib import pyplot
from plotly import graph_objs as go
import numpy as np

data = pd.read_csv('Salary_Data.csv')

st.title("Salary v/s Experience")

nav = st.sidebar.radio("Navigation",["Home","Prediction","Contribute"])
img = Image.open("d2.jpg")
st.image(
    img,
    caption="Salary v/s Prediction",
    width=650,
)
if nav == "Home":

    if st.checkbox("Show table"):
        st.table(data)

    graph = st.selectbox("what kind of graph ?",["Interactive","Non-Interactive"])

    val = st.slider("Filter data using years", 0,20)
    data = data.loc[data["YearsExperience"]>=val]

    if graph == "Non-Interactive":
        plt.figure(figsize=(10,5))
        plt.scatter(data["YearsExperience"],data["Salary"])
        plt.ylim(0)
        plt.xlabel("Years of Experience")
        plt.ylabel("Salary")
        plt.tight_layout()
        st.pyplot()
    if graph == "Interactive":
        layout = go.Layout(
            xaxis = dict(range =[0,16]),
            yaxis = dict(range = [0,2100000])
        )
        fig = go.Figure(data = go.Scatter(x=data["YearsExperience"], y = data["Salary"],mode ="markers"),
        layout=layout)
        st.plotly_chart(fig)


if nav == "Prediction":
    st.header("Know Your Salary")
    val = st.number_input("Enter your Experience",0.00,20.00,step =0.25)
    st.error("This Part Is Not Yet Completed Sorry for inconvenience ")


if nav == "Contribute":
    st.header("Contribute to our Dataset")
    ex = st.number_input("Enter Your Experience",0.00,20.00)
    sal = st.number_input("Enter Your Salary",0.00,1000000.00,step = 1000.00)
    if st.button("Submit"):
      st.success("Submitted")

