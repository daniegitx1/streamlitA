import requests
import streamlit as st
import streamlit_extras
from streamlit_extras.stylable_container import stylable_container

st.subheader('Bitcoin converter')

# Helper functions
def fetch_btc_zar_price():
    """Fetch the BTC/ZAR price from the API."""
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=zar"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        price_btc_to_zar = data.get("bitcoin", {}).get("zar", 0)
        return price_btc_to_zar
    except requests.RequestException as e:
        st.error(f"Error fetching BTC to ZAR price: {e}")
        return 0

def perform_conversion(amount, convert_from, convert_to):
    """Perform the currency conversion."""
    try:
        amount = float(amount)
    except ValueError:
        return "Invalid amount. Please enter a numeric value."

    price_btc_to_zar = fetch_btc_zar_price()
    sats_per_btc = 100_000_000  # 1 BTC = 100,000,000 Satoshi
    price_sat_to_zar = price_btc_to_zar / sats_per_btc

    if convert_from == "BTC" and convert_to == "SAT":
        return f"{amount * sats_per_btc:.0f} SAT"
    elif convert_from == "SAT" and convert_to == "BTC":
        return f"{amount / sats_per_btc:.8f} BTC"
    elif convert_from == "BTC" and convert_to == "ZAR":
        return f"{amount * price_btc_to_zar:,.2f} ZAR".replace(",", " ")
    elif convert_from == "ZAR" and convert_to == "BTC":
        return f"{amount / price_btc_to_zar:.8f} BTC"
    elif convert_from == "SAT" and convert_to == "ZAR":
        return f"{amount * price_sat_to_zar:,.2f} ZAR".replace(",", " ")
    elif convert_from == "ZAR" and convert_to == "SAT":
        return f"{amount / price_sat_to_zar:.0f} SAT"
    elif convert_from == convert_to:
        return f"{amount:,.2f} {convert_from}".replace(",", " ")
    else:
        return "Invalid conversion type."

# Conversion selection
col1, col2, col3 = st.columns(3)
with col1:
    with stylable_container(
        key="convert_from_container",
        css_styles="""{
            border: 1px solid rgba(49, 51, 63, 0.2);
            border-radius: 0.5rem;
            padding: calc(1em - 1px);
        }"""
    ):
        convert_from = st.radio(
            "convert from:",
            ["BTC", "SAT", "ZAR"],
            key="convert_from"
        )

with col2:
    with stylable_container(
        key="convert_to_container",
        css_styles="""{
            border: 1px solid rgba(49, 51, 63, 0.2);
            border-radius: 0.5rem;
            padding: calc(1em - 1px);
        }"""
    ):
        convert_to = st.radio(
            "convert to:",
            ["BTC", "SAT", "ZAR"],
            key="convert_to"
        )

# Layout for amount input
col1, col2, col3 = st.columns(3)
with col1:
    with stylable_container(
        key="amount_input_container",
        css_styles="""{
            border: 1px solid rgba(49, 51, 63, 0.2);
            border-radius: 0.5rem;
            padding: calc(1em - 1px);
        }"""
    ):
        amount = st.text_input('enter amount:', value="1")


# Result container with pink background
with col2:
    with stylable_container(
        key="result_container",
        css_styles="""{
            border: 1px solid rgba(49, 51, 63, 0.2);
            border-radius: 0.5rem;
            padding: calc(1em - 1px);
            background-color: #ffe6e6;
        }"""
    ):
        st.caption("result:")
        if amount:
            result = perform_conversion(amount, convert_from, convert_to)
        else:
            result = "Please enter an amount."
        st.write(result)

with col3:
    st.write("")


