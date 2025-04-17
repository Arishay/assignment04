import streamlit as st
import pandas as pd

st.title("BMI Calculator by Arisha Ghaffar 😊")

height = st.slider("📏Enter your height (in cm)", 100, 250, 175)
weight = st.slider("⚖️Enter your weight (in kg)", 20, 200, 70)

bmi = weight/((height/100) ** 2)

st.write(f"Your BMI IS {bmi:.2f}")

st.write("### BMI CATEGORIES")
st.write("-- Underweight : BMI less than 18.5")
st.write("-- Normal weight : BMI between 18.5 and 24.9")
st.write("-- Overweight : BMI between 25 and 29.9")
st.write("-- Obesity: : BMI 30 or greater")