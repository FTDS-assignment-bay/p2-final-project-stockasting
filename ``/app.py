import streamlit as st
import fnb_pred 
import fin_pred 
import homepage

nav = st.sidebar.selectbox('Navigate:',('Financial Companies', 'FnB Companies', 'Homepage'))

if nav == 'Homepage':
    homepage.run()
elif nav == 'FnB Companies':
    fnb_pred.run()
else :
    fin_pred.run()