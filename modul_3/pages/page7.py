import streamlit as st

st.markdown("# Page 7 : Session & Callback")
st.sidebar.markdown("# Page 7 : Session & Callback")
    
# Initialization, it’s just a dictionary
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'
    
# Session State also supports attribute based syntax
if 'key' not in st.session_state:
    st.session_state.key = 'value'
    
# Updates the state
st.session_state.key = 'value2' # Attribute API
st.session_state['key'] = 'value2' # Dictionary like API

# Delete a single key-value pair
del st.session_state[key]
    
# Delete all the items in Session state
for key in st.session_state.keys():
    del st.session_state[key]