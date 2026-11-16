
import streamlit as st

st.set_page_config(
    page_title="Euro-Bitcoin-Rechner",
    page_icon="₿",
    layout="centered"
)

st.title("₿ Euro ↔ Bitcoin Rechner")
st.write("Einfach Euro und Bitcoin umrechnen.")

st.divider()

# Bitcoin-Kurs eingeben
kurs = st.number_input(
    "Aktueller Bitcoin-Kurs in Euro (€)",
    min_value=0.01,
    value=90000.00,
    step=100.00
)

st.caption(f"Dein eingegebener BTC-Kurs: {kurs:,.2f} €")

st.divider()

# Umrechnungsrichtung
richtung = st.radio(
    "Was möchtest du umrechnen?",
    ["Euro in Bitcoin (BTC)", "Bitcoin (BTC) in Euro"]
)

if richtung == "Euro in Bitcoin (BTC)":

    euro = st.number_input(
        "Euro-Betrag (€)",
        min_value=0.0,
        value=1000.0,
        step=100.0
    )

    if kurs > 0:
        btc = euro / kurs

        st.success(
            f"{euro:,.2f} € entsprechen {btc:.8f} BTC"
        )

else:

    btc = st.number_input(
        "Bitcoin-Betrag (BTC)",
        min_value=0.0,
        value=0.01,
        step=0.001,
        format="%.8f"
    )

    euro = btc * kurs

    st.success(
        f"{btc:.8f} BTC entsprechen {euro:,.2f} €"
    )

st.divider()

st.caption(
    "Hinweis: Der Bitcoin-Kurs wird manuell eingegeben. "
    "Gebühren und Kursschwankungen sind nicht berücksichtigt."
)
