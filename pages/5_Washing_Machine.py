import streamlit as st

def main():
    st.set_page_config(page_title="LG Washing Machine Finder", page_icon="🧺", layout="wide")

    st.markdown("""
    <style>
    .stApp { background-color: #f6f3eb; }
    div.stButton > button { width: 100%; height: 70px; font-size: 16px !important; font-weight: 500; text-align: left; justify-content: flex-start; padding-left: 20px; background-color: #ffffff; border: 2px solid #e5e5e5; border-radius: 8px; color: #333; transition: all 0.3s ease; margin-bottom: 5px; }
    div.stButton > button:hover { border-color: #ea1917; color: #ea1917; box-shadow: 0 4px 12px rgba(234, 25, 23, 0.1); }
    .lg-card { background-color: #ffffff; border-radius: 12px; padding: 24px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); display: flex; flex-direction: column; height: 100%; border: 1px solid #eaeaea; font-family: 'Arial', sans-serif; }
    .lg-tag-row { display: flex; gap: 8px; margin-bottom: 12px; flex-wrap: wrap; }
    .lg-tag { font-size: 11px; font-weight: bold; padding: 4px 8px; border-radius: 4px; }
    .lg-tag-red { background-color: #ea1917; color: white; }
    .lg-tag-outline { border: 1px solid #ea1917; color: #ea1917; background-color: #fffafb; }
    .lg-title { font-size: 16px; font-weight: 600; line-height: 1.4; color: #000; margin-bottom: 4px; height: 44px; overflow: hidden; }
    .lg-model { font-size: 12px; color: #666; margin-bottom: 12px; }
    .lg-rating { color: #fabb05; font-size: 13px; margin-bottom: 16px; text-align: right;}
    .lg-img-box { text-align: center; padding: 10px 0; border-bottom: 1px solid #eee; margin-bottom: 16px; height: 200px; display: flex; align-items: center; justify-content: center; }
    .lg-energy { font-size: 12px; font-weight: bold; color: #fff; background: #009e49; padding: 2px 6px; border-radius: 2px; display: inline-block;}
    .lg-price-box { margin-top: auto; }
    .lg-save-text { color: #ea1917; font-size: 12px; font-weight: bold; margin-bottom: 4px; }
    .lg-price { font-size: 22px; font-weight: bold; color: #000; }
    .lg-price-old { font-size: 14px; text-decoration: line-through; color: #888; margin-left: 8px; }
    .lg-btn-row { display: flex; gap: 10px; margin-top: 10px; }
    .lg-btn { flex: 1; text-align: center; padding: 12px 0; font-size: 14px; font-weight: bold; border-radius: 6px; cursor: pointer; text-decoration: none; transition: 0.2s; }
    .lg-btn-sec { background-color: white; border: 1px solid #ccc; color: #333; }
    .lg-btn-sec:hover { border-color: #000; }
    .lg-btn-pri { background-color: #e50000; border: 1px solid #e50000; color: white; }
    .lg-btn-pri:hover { background-color: #c40000; }
    </style>
    """, unsafe_allow_html=True)

    if 'wm_step' not in st.session_state:
        st.session_state.wm_step = 1; st.session_state.wm_data = {}

    st.write("<br>", unsafe_allow_html=True)
    st.title("🧺 LG Washing Machine Finder")
    st.markdown("Energy saving & perfect fabric care. Find your ideal washing machine.")
    st.divider()

    if st.session_state.wm_step > 1 and st.session_state.wm_step != 4:
        if st.button("⬅️ Back", key="back_btn_wm"): st.session_state.wm_step -= 1; st.rerun()

    col_q, col_empty = st.columns([2, 1])
    with col_q:
        if st.session_state.wm_step == 1:
            st.subheader("1. How many people are in your household?")
            if st.button("👤 1~2 persons (Frequent small loads / 7-8kg)"): st.session_state.wm_data['capacity'] = "Small"; st.session_state.wm_step = 2; st.rerun()
            if st.button("👨‍👩‍👦 3~4 persons (Standard capacity / 9-10kg)"): st.session_state.wm_data['capacity'] = "Standard"; st.session_state.wm_step = 2; st.rerun()
            if st.button("👨‍👩‍👧‍👦 Large family or bulky items (Max capacity / 11kg+)"): st.session_state.wm_data['capacity'] = "Large"; st.session_state.wm_step = 2; st.rerun()

        elif st.session_state.wm_step == 2:
            st.subheader("2. What form factor are you looking for?")
            if st.button("🧺 Classic washing machine (Front Loader)"): st.session_state.wm_data['type'] = "Washer"; st.session_state.wm_step = 3; st.rerun()
            if st.button("☀️ All-in-one Washer & Dryer (Washer-Dryer)"): st.session_state.wm_data['type'] = "WasherDryer"; st.session_state.wm_step = 3; st.rerun()
            if st.button("📏 Slim design for tight spaces (Slim-Design)"): st.session_state.wm_data['type'] = "Slim"; st.session_state.wm_step = 3; st.rerun()

        elif st.session_state.wm_step == 3:
            st.subheader("3. Which LG core technology is a must-have?")
            if st.button("🧠 Intelligent care based on fabric weight and softness (AI DD™)"): st.session_state.wm_data['feature'] = "AI_DD"; st.session_state.wm_step = 4; st.rerun()
            if st.button("⏱️ Fast and clean wash in 39 minutes (TurboWash™ 360°)"): st.session_state.wm_data['feature'] = "TurboWash"; st.session_state.wm_step = 4; st.rerun()
            if st.button("💨 Steam away allergens and dust mites (Steam™)"): st.session_state.wm_data['feature'] = "Steam"; st.session_state.wm_step = 4; st.rerun()

    if st.session_state.wm_step == 4:
        st.balloons()
        st.markdown("### 🎉 Your Perfect LG Washing Machine")
        st.write("<br>", unsafe_allow_html=True)

        def create_lg_card_html(tags, title, model, rating, save_text, price, old_price, btn1_text, btn2_text, energy_class="A", is_primary=False):
            tag_html = "".join([f"<span class='lg-tag lg-tag-{'red' if 'New' in t or 'Best Seller' in t else 'outline'}'>{t}</span>" for t in tags])
            btn2_class = "lg-btn-pri" if is_primary else ("lg-btn-pri" if "Buy" in btn2_text else "lg-btn-sec")
            return f"""
            <div class="lg-card">
                <div class="lg-tag-row">{tag_html}</div>
                <div class="lg-title">{title}</div>
                <div style="display:flex; justify-content: space-between;"><div class="lg-model">{model}</div><div class="lg-rating">★★★★★ <span style="color:#666;">({rating})</span></div></div>
                <div class="lg-img-box"><h1 style="font-size: 60px; color:#ccc;">🧺</h1></div>
                <div style="margin-bottom: 10px;">
                    <span class="lg-energy">{energy_class}</span> <span style="font-size:12px; color:#666;">Product Data Sheet</span>
                </div>
                <div class="lg-price-box"><div class="lg-save-text">{save_text}</div><div><span class="lg-price">{price}</span> <span class="lg-price-old">{old_price}</span></div></div>
                <div class="lg-btn-row"><a href="#" class="lg-btn lg-btn-sec">{btn1_text}</a><a href="#" class="lg-btn {btn2_class}" style="{'' if is_primary else 'background-color:#e50000; color:white; border:none;'}">{btn2_text}</a></div>
            </div>
            """

        wm_type = st.session_state.wm_data.get('type', '')
        if wm_type == "WasherDryer":
            cards = [
                create_lg_card_html(["Washer-Dryer", "AI DD"], "LG Washer-Dryer (9kg Wash / 6kg Dry)", "V7WD96H1", "120", "Save 150,00 €", "799,00 €", "949,00 €", "More Info", "Buy Now", "E", is_primary=True),
                create_lg_card_html(["Premium", "TurboWash"], "LG SIGNATURE Washer-Dryer (12kg / 7kg)", "LWS27W", "45", "Save 300,00 €", "1.599,00 €", "1.899,00 €", "More Info", "Buy Now", "A"),
                create_lg_card_html(["Steam™", "Compact"], "LG Washer-Dryer Series 5 (8kg / 5kg)", "V5WD85H1", "88", "Save 100,00 €", "649,00 €", "749,00 €", "More Info", "Buy Now", "E")
            ]
        elif wm_type == "Slim":
            cards = [
                create_lg_card_html(["Slim Design", "Steam"], "LG Slim Washing Machine (7kg, 47cm Depth)", "F2WV4S7S1E", "210", "Save 80,00 €", "499,00 €", "579,00 €", "More Info", "Buy Now", "A", is_primary=True),
                create_lg_card_html(["Slim", "AI DD"], "LG Slim Washing Machine Series 5 (8.5kg)", "F4WV508S1E", "150", "Save 100,00 €", "549,00 €", "649,00 €", "More Info", "Buy Now", "A"),
                create_lg_card_html(["Compact", "Direct Drive"], "LG Slim Washing Machine (6.5kg)", "F2WV3S6S3E", "95", "Save 50,00 €", "429,00 €", "479,00 €", "More Info", "Buy Now", "B")
            ]
        else:
            cards = [
                create_lg_card_html(["Best Seller", "A -10%"], "LG Washing Machine Series 7 (10kg) with TurboWash™", "F4V710WTSE", "340", "Save 200,00 €", "699,00 €", "899,00 €", "More Info", "Buy Now", "A", is_primary=True),
                create_lg_card_html(["Large Capacity", "Premium"], "LG Washing Machine Series 9 (11kg) with AI DD™", "F6V9B9W", "180", "Save 250,00 €", "849,00 €", "1.099,00 €", "More Info", "Buy Now", "A"),
                create_lg_card_html(["Eco", "Steam"], "LG Washing Machine Series 5 (8kg) with Steam", "F4V508WSE", "420", "Save 120,00 €", "479,00 €", "599,00 €", "More Info", "Buy Now", "A")
            ]

        col1, col2, col3 = st.columns(3)
        with col1: st.markdown(cards[0], unsafe_allow_html=True)
        with col2: st.markdown(cards[1], unsafe_allow_html=True)
        with col3: st.markdown(cards[2], unsafe_allow_html=True)

        st.write("<br><br>", unsafe_allow_html=True)
        col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
        with col_btn2:
            if st.button("🔄 Restart Finder", use_container_width=True): st.session_state.wm_step = 1; st.session_state.wm_data = {}; st.rerun()

if __name__ == "__main__":
    main()
