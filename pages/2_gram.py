import streamlit as st

def main():
    st.set_page_config(page_title="LG Gram Product Finder", page_icon="💻", layout="wide")

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
    .lg-img-box img { max-width: 100%; max-height: 180px; object-fit: contain; }
    .lg-price-box { margin-top: auto; }
    .lg-save-text { color: #ea1917; font-size: 12px; font-weight: bold; margin-bottom: 4px; }
    .lg-price { font-size: 22px; font-weight: bold; color: #000; }
    .lg-price-old { font-size: 14px; text-decoration: line-through; color: #888; margin-left: 8px; }
    .lg-delivery { font-size: 12px; font-weight: bold; color: #d86c00; background: #fff4e6; padding: 6px 12px; border-radius: 4px; display: inline-block; margin: 12px 0; }
    .lg-btn-row { display: flex; gap: 10px; margin-top: 10px; }
    .lg-btn { flex: 1; text-align: center; padding: 12px 0; font-size: 14px; font-weight: bold; border-radius: 6px; cursor: pointer; text-decoration: none; transition: 0.2s; }
    .lg-btn-sec { background-color: white; border: 1px solid #ccc; color: #333; }
    .lg-btn-sec:hover { border-color: #000; }
    .lg-btn-pri { background-color: #e50000; border: 1px solid #e50000; color: white; }
    .lg-btn-pri:hover { background-color: #c40000; }
    </style>
    """, unsafe_allow_html=True)

    if 'step' not in st.session_state:
        st.session_state.step = 1
        st.session_state.data = {}

    st.write("<br>", unsafe_allow_html=True)
    st.title("💻 LG Gram Product Finder")
    st.markdown("More than just lightweight. Find the perfect LG Gram for your daily life.")
    st.divider()

    if st.session_state.step > 1 and st.session_state.step != 4:
        if st.button("⬅️ Back", key="back_btn"): st.session_state.step -= 1; st.rerun()

    col_q, col_empty = st.columns([2, 1])
    with col_q:
        if st.session_state.step == 1:
            st.subheader("1. What is the main role of the laptop in your bag?")
            if st.button("📝 Documents, web surfing, and daily tasks (Standard)"): st.session_state.data['persona'] = "Standard"; st.session_state.step = 2; st.rerun()
            if st.button("🎬 Heavy tasks like video editing, 3D, and coding (Pro/Creator)"): st.session_state.data['persona'] = "Pro"; st.session_state.step = 2; st.rerun()
            if st.button("🎨 Folding the screen to sketch and take notes freely (Artist/2-in-1)"): st.session_state.data['persona'] = "2-in-1"; st.session_state.step = 4; st.rerun() 

        elif st.session_state.step == 2:
            st.subheader("2. The weight is light anyway. What screen size do you prefer?")
            if st.button("🎒 Ultimate portability, fits in any bag (14~15.6 inches)"): st.session_state.data['size'] = "14/15"; st.session_state.step = 3; st.rerun()
            if st.button("⚖️ Perfect balance of portability and workspace (16 inches)"): st.session_state.data['size'] = "16"; st.session_state.step = 3; st.rerun()
            if st.button("🖥️ Massive workspace replacing a desktop (17 inches)"): st.session_state.data['size'] = "17"; st.session_state.step = 3; st.rerun()

        elif st.session_state.step == 3:
            st.subheader("3. Finally, what display magic pleases your eyes the most?")
            if st.button("☀️ Comfortable viewing even in bright cafes (Anti-glare IPS)"): st.session_state.data['display'] = "IPS"; st.session_state.step = 4; st.rerun()
            if st.button("🌌 Perfect black for Netflix and photo editing (OLED)"): st.session_state.data['display'] = "OLED"; st.session_state.step = 4; st.rerun()
            if st.button("⚡ Overwhelmingly smooth scrolling (144Hz / VRR)"): st.session_state.data['display'] = "144Hz"; st.session_state.step = 4; st.rerun()

    if st.session_state.step == 4:
        st.balloons()
        st.markdown("### 🎉 Your Perfect LG Gram")
        st.write("Based on your answers, here are our top recommendations.")
        st.write("<br>", unsafe_allow_html=True)

        def create_lg_card_html(tags, title, model, rating, save_text, price, old_price, btn1_text, btn2_text, img_url, is_primary=False):
            tag_html = "".join([f"<span class='lg-tag lg-tag-{'red' if 'New' in t or 'Best Seller' in t else 'outline'}'>{t}</span>" for t in tags])
            btn2_class = "lg-btn-pri" if is_primary else ("lg-btn-pri" if "Buy" in btn2_text else "lg-btn-sec")
            return f"""
            <div class="lg-card">
                <div class="lg-tag-row">{tag_html}</div>
                <div class="lg-title">{title}</div>
                <div style="display:flex; justify-content: space-between;"><div class="lg-model">{model} <span><input type="checkbox"></span></div><div class="lg-rating">★★★★★ <span style="color:#666;">({rating})</span></div></div>
                <div class="lg-img-box"><img src="{img_url}" alt="{model}"></div>
                <div style="margin-bottom: 10px;"><span style="font-size:12px; color:#666;">Intel® Core™ Ultra Processor</span></div>
                <div class="lg-price-box"><div class="lg-save-text">{save_text}</div><div><span class="lg-price">{price}</span> <span class="lg-price-old">{old_price}</span></div><div style="font-size: 11px; color: #888;">€74.96 / mo. up to 24 months at 0%</div></div>
                <div class="lg-delivery">🚚 Free Delivery</div>
                <div class="lg-btn-row"><a href="#" class="lg-btn lg-btn-sec">{btn1_text}</a><a href="#" class="lg-btn {btn2_class}" style="{'' if is_primary else 'background-color:#e50000; color:white; border:none;'}">{btn2_text}</a></div>
                <div style="text-align: center; margin-top: 15px; font-size: 12px; color: #666;"><input type="checkbox"> Compare</div>
            </div>
            """

        persona = st.session_state.data.get('persona', '')
        img_pro_16 = "https://www.lg.com/content/dam/channel/wcms/de/images/laptops/16z90sp-g.ad78g/gallery/16Z90SP-G-Large-01.jpg/jcr:content/renditions/thum-350x350.jpeg"
        img_gram_17 = "https://www.lg.com/content/dam/channel/wcms/de/images/laptops/17z90r-g.aa79g/gallery/17Z90R-G-Large-01.jpg/jcr:content/renditions/thum-350x350.jpeg"
        img_2in1 = "https://www.lg.com/content/dam/channel/wcms/de/images/laptops/16t90r-g.aa76g/gallery/16T90R-G-Large-01.jpg/jcr:content/renditions/thum-350x350.jpeg"

        cards = []
        if persona == "2-in-1":
            cards = [
                create_lg_card_html(["Recommended"], "LG gram 14 2-in-1 (14\" WUXGA Touch)", "14T90R-G", "85", "Save 200,00 €", "1.499,00 €", "1.699,00 €", "More Info", "Buy Now", img_2in1),
                create_lg_card_html(["New", "Best Seller"], "LG gram 16 2-in-1 (16\" WQXGA Touch & Pen)", "16T90R-G", "120", "Save 300,00 €", "1.699,00 €", "1.999,00 €", "More Info", "Buy Now", img_2in1, is_primary=True),
                create_lg_card_html(["OLED"], "LG gram Style 16 (Aurora White, Hidden Touchpad)", "16Z90RS-G", "45", "Save 150,00 €", "1.749,00 €", "1.899,00 €", "More Info", "Buy Now", img_gram_17)
            ]
        elif persona == "Pro":
            cards = [
                create_lg_card_html(["Creator"], "LG gram Pro 16 (Intel Core Ultra 7, 144Hz)", "16Z90SP-G", "60", "Save 250,00 €", "1.849,00 €", "2.099,00 €", "More Info", "Buy Now", img_pro_16, is_primary=True),
                create_lg_card_html(["RTX 3050", "Gaming"], "LG gram Pro 17 (NVIDIA Dedicated Graphics)", "17Z90SP-G", "38", "Save 300,00 €", "2.199,00 €", "2.499,00 €", "More Info", "Buy Now", img_gram_17),
                create_lg_card_html(["New"], "LG gram 16 (Intel Core Ultra 5, High-Res)", "16Z90S-G", "95", "Save 100,00 €", "1.599,00 €", "1.699,00 €", "More Info", "Buy Now", img_pro_16)
            ]
        else:
            cards = [
                create_lg_card_html(["Ultra Light"], "LG gram 14 (999g, Max Battery Life)", "14Z90S-G", "150", "Save 100,00 €", "1.299,00 €", "1.399,00 €", "More Info", "Buy Now", img_pro_16),
                create_lg_card_html(["Best Seller", "IPS"], "LG gram 16 (16:10 Display, 1.19kg)", "16Z90S-G", "320", "Save 200,00 €", "1.499,00 €", "1.699,00 €", "More Info", "Buy Now", img_pro_16, is_primary=True),
                create_lg_card_html(["Desktop-Replacement"], "LG gram 17 (17\" Display, Numeric Keypad)", "17Z90S-G", "210", "Save 250,00 €", "1.649,00 €", "1.899,00 €", "More Info", "Buy Now", img_gram_17)
            ]

        col1, col2, col3 = st.columns(3)
        with col1: st.markdown(cards[0], unsafe_allow_html=True)
        with col2: st.markdown(cards[1], unsafe_allow_html=True)
        with col3: st.markdown(cards[2], unsafe_allow_html=True)

        st.write("<br><br>", unsafe_allow_html=True)
        col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
        with col_btn2:
            if st.button("🔄 Restart Finder", use_container_width=True): st.session_state.step = 1; st.session_state.data = {}; st.rerun()

if __name__ == "__main__":
    main()
