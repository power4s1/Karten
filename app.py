import streamlit as st

st.set_page_config(page_title="Mein Krypto-Rechner")

st.title(" Mein Bitcoin-Rechner")
st.write("Einfach Bitcoin-Beträge berechnen.")

euro = st.number_input(
    "Wie viel Euro möchtest du umrechnen?",
    min_value=0.0,
    value=100.0
)

btc_kurs = st.number_input(
    "Bitcoin-Kurs in Euro",
    min_value=1.0,
    value=80000.0
)

bitcoin = euro / btc_kurs

st.success(f"Du erhältst {bitcoin:.8f} BTC")

st.caption("Beispielrechnung   kein aktueller B rsenkurs.")
