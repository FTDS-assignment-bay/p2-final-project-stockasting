import streamlit as st
import pandas as pd
import pickle

#Load the files
with open('best_finance_svr_model.pkl', 'rb') as file_1:
    fin_model = pickle.load(file_1)

def run():

    st.title('Enter Your Data Here !')

    with st.form(key='form parameters'):
        emiten_code = st.text_input('Emiten Code', 'ARTO')
        year = st.number_input('Year', min_value = 1900, max_value = 2100, value = 2025)
        date = st.selectbox('Date', ['Q1', 'Q2', 'Q3', 'Q4'], index = 2)
        eps = st.number_input('EPS', value=2.59)
        per = st.number_input('PER', value=1177.61)
        pbv = st.number_input('PBV', value=4.99)
        bvps = st.number_input('BVPS', value=611.09)
        ebitda = st.number_input('EBITDA', value=109000000000, step=1000000000)
        roa = st.number_input('ROA', value=0.13)
        roe = st.number_input('ROE', value=0.42)
        fcf = st.number_input('FCF', value=1359000000000, step=1000000000)
        fcf_ps = st.number_input('FCF per Share', value=98.06)
        gdp_forecast = st.number_input('GDP Forecast', value=5.0)
        political_stability = st.number_input('Political Stability', value=17.1)
        inflation_forecast = st.number_input('Inflation Forecast', value=2.5)
        
        submit_button = st.form_submit_button(label='Submit')
        
    data = {
        'emiten_code': emiten_code,
        'year': year,
        'date': date,
        'eps': eps,
        'per': per,
        'pbv': pbv,
        'bvps': bvps,
        'ebitda': ebitda,
        'roa': roa,
        'roe': roe,
        'fcf': fcf,
        'fcf_ps': fcf_ps,
        'gdp_forecast': gdp_forecast,
        'political_stability': political_stability,
        'inflation_forecast': inflation_forecast,
    }

    data = pd.DataFrame([data])
    st.dataframe(data)

    if submit_button:
        st.subheader("Prediction Result")
  
        pred = fin_model.predict(data)

        st.success(f"📌 **Predicted Value:** {pred[0]:,.6f}")


if __name__ == '__main__':
    run()