import streamlit as st

# penggunaan display text
st.title("This is a title :smile:")
st.header("This is a header")
st.subheader("This is a subheader")
st.caption("This is a caption")
st.text("This is a text")
st.write("We can write like this")

# penggunaan metric dan columns
st.metric(label="Likes", value=3600, delta=500)
st.metric(label="New subscribers", value=1000, delta=20)
col1, col2, col3, col4 = st.columns(4)
col1.metric("New video", "1 video", "-3 videos")
col2.metric("Average duration", "170 min", "10 minutes")
col3.metric("Engagement", "70%", "-5%")
col4.metric("Total subscribers", "2500 subs", "20 subscribers")