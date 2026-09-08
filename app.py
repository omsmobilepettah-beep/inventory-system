import streamlit as st
import streamlit.components.v1 as components

# Streamlit page layout සැකසීම
st.set_page_config(page_title="Inventory & Sales System", layout="wide")

# index.html ගොනුව කියවා Streamlit හරහා පෙන්වීම
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_code = f.read()
    components.html(html_code, height=900, scrolling=True)
except FileNotFoundError:
    st.error("index.html ගොනුව සොයාගත නොහැකි විය. කරුණාකර එය GitHub Repository එකේ ප්‍රධාන පිටුවේ (Root directory) අන්තර්ගත කර ඇද්දැයි පරීක්ෂා කරන්න.")