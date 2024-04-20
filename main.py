import streamlit as st

conn = st.connection('bio-tools_db', type='sql')

df = conn.query('select * from platforms_id')
st.dataframe(df)
