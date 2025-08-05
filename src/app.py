from utils import db_connect
engine = db_connect()

# your code here
import streamlit as st
from pickle import load
import sklearn

model = load(open("/workspaces/AL-y-RN/Modelo_ArbolD.pkl", "rb"))
class_dict = {1:"si", 0: "no"}

var1 = st.slider('Numero de Embarazos', min_value=0.0, max_value=15.0, step=1.0)

