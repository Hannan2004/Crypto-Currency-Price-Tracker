import yfinance as yf
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

st.title('Crypto Currency Tracker')

# Sidebar
st.sidebar.title('options')
st.sidebar.selectbox('Select a crypto currency', ['BTC-USD', 'ETH-USD', 'LTC-USD'])