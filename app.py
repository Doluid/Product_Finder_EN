import streamlit as st

st.set_page_config(page_title="LG Product Finder Portal", page_icon="LG", layout="wide")

st.markdown("""
<style>
.stApp { background-color: #f6f3eb; }
div.stButton > button {
    width: 100%; height: 160px; font-size: 18px !important; font-weight: 600;
    text-align: center; display: flex; flex-direction: column; justify-content: center;
    align-items: center; background-color: #ffffff; border: 2px solid #e5e5e5;
    border-radius: 12px; color: #333; transition: all 0.3s ease; box-shadow: 0 4px 10px rgba(0,0,0,0.05); white-space: pre-wrap;
}
div.stButton > button:hover { border-color: #ea1917; color: #ea1917; transform: translateY(-5px); box-shadow: 0 8px 20px rgba(234, 25, 23, 0.15); }
</style>
""", unsafe_allow_html=True)

st.title("LG Electronics Product Finder DE 🇩🇪")
st.markdown("### Welcome! Which product are you looking for?")
st.divider()

st.write("Click on the product cards below to find the perfect LG match for your lifestyle.")
st.write("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🖥️ Monitor Finder\n\nFind the perfect display for your desk"): st.switch_page("pages/1_Monitor.py")
with col2:
    if st.button("💻 gram Finder\n\nMore than just lightweight. Find your laptop"): st.switch_page("pages/2_gram.py")
with col3:
    if st.button("📺 OLED TV Finder\n\nAbsolute black. Perfect your living room"): st.switch_page("pages/3_OLED_TV.py")

st.write("<br>", unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)
with col4:
    if st.button("🧊 Refrigerator Finder\n\nElevate your kitchen with LG"): st.switch_page("pages/4_REF.py")
with col5:
    if st.button("🧺 Washing Machine Finder\n\nEnergy saving & Perfect fabric care"): st.switch_page("pages/5_Washing_Machine.py")
with col6:
    st.empty() 

st.write("<br><br><br><br>", unsafe_allow_html=True)
st.caption("© 2026 LG Electronics Prototype. Built with Streamlit.")
