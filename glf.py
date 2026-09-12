
# A Streamlit alkalmazás a mosási tömegveszteség kiszámítására

import streamlit as st

# Az oldal címe és leírása
st.title("Mosási tömegveszteség számító")
st.write("Add meg a tömegeket grammban a százalékos veszteség kiszámításához.")

# Beviteli mezők a számokhoz (alapértelmezett érték: 0.0)
me = st.number_input("Mosás előtt [g]:", min_value=0.0, format="%.2f")
mu = st.number_input("Mosás után [g]:", min_value=0.0, format="%.2f")

# Egy gomb, amire kattintva elindul a számolás
if st.button("Számítás"):
    # Biztonsági ellenőrzés nullával való osztás ellen
    if me == 0:
        st.error("Hiba: A mosás előtti tömeg nem lehet 0!")
    else:
        # A számítás elvégzése
        eredmeny = (100 * (me - mu)) / me
        
        # Eredmény megjelenítése egy szép zöld dobozban
        st.success(f"Eredmény: {eredmeny:.2f}%")
