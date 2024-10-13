import streamlit as st
import time

st.markdown("# Main Page Modul 3 dan 4")
st.sidebar.markdown("# Main Page")
        
# Penggunaan Progress Bar

'Loading... Please wait.'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)
        
for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Finish!'