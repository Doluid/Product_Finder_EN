import streamlit as st

def main():
    st.set_page_config(page_title="LG OLED TV Finder", page_icon="📺", layout="wide")

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

    if 'tv_step' not in st.session_state:
        st.session_state.tv_step = 1; st.session_state.tv_data = {}

    st.write("<br>", unsafe_allow_html=True)
    st.title("📺 LG OLED TV Finder")
    st.markdown("Absolute black. Find the perfect OLED TV to complete your living room.")
    st.divider()

    if st.session_state.tv_step > 1 and st.session_state.tv_step != 4:
        if st.button("⬅️ Back", key="back_btn_tv"): st.session_state.tv_step -= 1; st.rerun()

    col_q, col_empty = st.columns([2, 1])
    with col_q:
        if st.session_state.tv_step == 1:
            st.subheader("1. What moment do you look forward to the most when turning on the TV?")
            if st.button("🎬 Cinematic immersion, like moving the theater to your room"): st.session_state.tv_data['purpose'] = "Movie"; st.session_state.tv_step = 2; st.rerun()
            if st.button("⚽ Fast and vivid sports broadcasting without blur"): st.session_state.tv_data['purpose'] = "Sports"; st.session_state.tv_step = 2; st.rerun()
            if st.button("🎮 100% next-gen console (PS5/Xbox) gaming performance"): st.session_state.tv_data['purpose'] = "Game"; st.session_state.tv_step = 2; st.rerun()

        elif st.session_state.tv_step == 2:
            st.subheader("2. How large is the space where the TV will be installed?")
            if st.button("🛏️ Perfect for a bedroom or smaller room (42~55 inches)"): st.session_state.tv_data['size'] = "Small"; st.session_state.tv_step = 3; st.rerun()
            if st.button("🛋️ Standard large screen for typical living rooms (65~77 inches)"): st.session_state.tv_data['size'] = "Large"; st.session_state.tv_step = 3; st.rerun()
            if st.button("🏰 Massive premium screen for home theaters (83~97 inches)"): st.session_state.tv_data['size'] = "ExtraLarge"; st.session_state.tv_step = 3; st.rerun()

        elif st.session_state.tv_step == 3:
            st.subheader("3. What is your preferred interior and installation style?")
            if st.button("🖼️ Flush against the wall like an art gallery (Wall-mount)"): st.session_state.tv_data['style'] = "Gallery"; st.session_state.tv_step = 4; st.rerun()
            if st.button("🔌 Clean space without complex cables (Zero Connect Wireless)"): st.session_state.tv_data['style'] = "Wireless"; st.session_state.tv_step = 4; st.rerun()
            if st.button("📺 Classic and stable installation (Stand)"): st.session_state.tv_data['style'] = "Stand"; st.session_state.tv_step = 4; st.rerun()

    if st.session_state.tv_step == 4:
        st.balloons()
        st.markdown("### 🎉 Your Perfect LG OLED TV")
        st.write("<br>", unsafe_allow_html=True)

        def create_lg_card_html(tags, title, model, rating, save_text, price, old_price, btn1_text, btn2_text, is_primary=False):
            tag_html = "".join([f"<span class='lg-tag lg-tag-{'red' if 'New' in t or 'OLED' in t else 'outline'}'>{t}</span>" for t in tags])
            btn2_class = "lg-btn-pri" if is_primary else ("lg-btn-pri" if "Buy" in btn2_text else "lg-btn-sec")
            return f"""
            <div class="lg-card">
                <div class="lg-tag-row">{tag_html}</div>
                <div class="lg-title">{title}</div>
                <div style="display:flex; justify-content: space-between;"><div class="lg-model">{model}</div><div class="lg-rating">★★★★★ <span style="color:#666;">({rating})</span></div></div>
                <div class="lg-img-box"><h1 style="font-size: 60px; color:#ccc;">📺</h1></div>
                <div class="lg-price-box"><div class="lg-save-text">{save_text}</div><div><span class="lg-price">{price}</span> <span class="lg-price-old">{old_price}</span></div></div>
                <div class="lg-btn-row"><a href="#" class="lg-btn lg-btn-sec">{btn1_text}</a><a href="#" class="lg-btn {btn2_class}" style="{'' if is_primary else 'background-color:#e50000; color:white; border:none;'}">{btn2_text}</a></div>
            </div>
            """

        cards = [
            create_lg_card_html(["OLED evo", "Best Seller"], "LG OLED evo C4 (Gaming & All-Around)", "OLED65C47LA", "450", "Save 400,00 €", "2.199,00 €", "2.599,00 €", "More Info", "Buy Now", is_primary=True),
            create_lg_card_html(["Gallery Design", "Premium"], "LG OLED evo G4 (Zero Gap Wall-mount)", "OLED77G48LW", "210", "Save 600,00 €", "3.899,00 €", "4.499,00 €", "More Info", "Buy Now"),
            create_lg_card_html(["Zero Connect", "New"], "LG SIGNATURE OLED M (Wireless TV)", "OLED83M39LA", "45", "Save 1.000,00 €", "6.499,00 €", "7.499,00 €", "More Info", "Buy Now")
        ]

        col1, col2, col3 = st.columns(3)
        with col1: st.markdown(cards[0], unsafe_allow_html=True)
        with col2: st.markdown(cards[1], unsafe_allow_html=True)
        with col3: st.markdown(cards[2], unsafe_allow_html=True)

        st.write("<br><br>", unsafe_allow_html=True)
        col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
        with col_btn2:
            if st.button("🔄 Restart Finder", use_container_width=True): st.session_state.tv_step = 1; st.session_state.tv_data = {}; st.rerun()

if __name__ == "__main__":
    main()
