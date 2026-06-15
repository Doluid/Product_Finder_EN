import streamlit as st

def main():
    st.set_page_config(page_title="LG Monitor Product Finder", page_icon="🖥️", layout="wide")

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
    .lg-energy { font-size: 12px; font-weight: bold; color: #fff; background: #e3000f; padding: 2px 6px; border-radius: 2px; display: inline-block;}
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
    st.title("🖥️ LG Monitor Product Finder")
    st.markdown("Discover the perfect LG Monitor tailored for your lifestyle.")
    st.divider()

    if st.session_state.step > 1 and st.session_state.step != 4:
        if st.button("⬅️ Back", key="back_btn"):
            if st.session_state.step == 1.1: st.session_state.step = 1
            elif st.session_state.step == 2: st.session_state.step = 1.1 if "Gaming" in st.session_state.data.get('purpose', '') else 1
            elif st.session_state.step == 3: st.session_state.step = 2
            st.rerun()

    col_q, col_empty = st.columns([2, 1])
    with col_q:
        if st.session_state.step == 1:
            st.subheader("1. What excites you the most when sitting at your desk?")
            if st.button("🎮 Thrilling gaming experience (Gaming)"): st.session_state.data['purpose'] = "Gaming"; st.session_state.step = 1.1; st.rerun()
            if st.button("🎨 Precise photo & video editing (Pro-Work)"): st.session_state.data['purpose'] = "Work"; st.session_state.step = 2; st.rerun()
            if st.button("📝 Multitasking & Home Office (Productivity)"): st.session_state.data['purpose'] = "Office"; st.session_state.step = 2; st.rerun()

        elif st.session_state.step == 1.1:
            st.subheader("1-1. What is your ultimate gaming style?")
            if st.button("🔫 Fast-paced competitive FPS (e.g., Valorant)"): st.session_state.data['game_style'] = "FPS"; st.session_state.step = 2; st.rerun()
            if st.button("🌍 Highly realistic Open-World RPGs"): st.session_state.data['game_style'] = "OpenWorld"; st.session_state.step = 2; st.rerun()

        elif st.session_state.step == 2:
            st.subheader("2. How much space do you have on your desk?")
            if st.button("🖥️ Compact size (24~27 inches)"): st.session_state.data['size'] = "27"; st.session_state.step = 3; st.rerun()
            if st.button("📺 Large screen (32~39 inches)"): st.session_state.data['size'] = "32"; st.session_state.step = 3; st.rerun()
            if st.button("↔️ Ultra-wide / 40+ inches"): st.session_state.data['size'] = "40+"; st.session_state.step = 3; st.rerun()

        elif st.session_state.step == 3:
            st.subheader("3. What is the 'one magic feature' you need the most?")
            if st.button("🔋 Clean setup with a single cable (USB-C / Thunderbolt)"): st.session_state.data['feature'] = "Type-C"; st.session_state.step = 4; st.rerun()
            if st.button("🦾 Freedom to adjust to your posture (Ergo Stand)"): st.session_state.data['feature'] = "Ergo"; st.session_state.step = 4; st.rerun()
            if st.button("🛞 Move freely around the house (StandbyMe)"): st.session_state.data['feature'] = "StandbyMe"; st.session_state.step = 4; st.rerun()

    if st.session_state.step == 4:
        st.balloons()
        st.markdown("### 🎉 Your Perfect LG Monitors")
        st.write("Based on your answers, here are our top 3 recommendations.")
        st.write("<br>", unsafe_allow_html=True)

        def create_lg_card_html(tags, title, model, rating, save_text, price, old_price, btn1_text, btn2_text, img_url, is_primary=False):
            tag_html = "".join([f"<span class='lg-tag lg-tag-{'red' if 'Bonus' in t or 'Pre-order' in t else 'outline'}'>{t}</span>" for t in tags])
            btn2_class = "lg-btn-pri" if is_primary else ("lg-btn-pri" if "Buy" in btn2_text else "lg-btn-sec")
            return f"""
            <div class="lg-card">
                <div class="lg-tag-row">{tag_html}</div>
                <div class="lg-title">{title}</div>
                <div style="display:flex; justify-content: space-between;"><div class="lg-model">{model} <span><input type="checkbox"></span></div><div class="lg-rating">★★★★★ <span style="color:#666;">({rating})</span></div></div>
                <div class="lg-img-box"><img src="{img_url}" alt="{model}"></div>
                <div style="margin-bottom: 10px;"><span class="lg-energy">G</span> <span style="font-size:12px; color:#666;">Product Sheet</span></div>
                <div class="lg-price-box"><div class="lg-save-text">{save_text}</div><div><span class="lg-price">{price}</span> <span class="lg-price-old">{old_price}</span></div><div style="font-size: 11px; color: #888;">€74.96 / mo. up to 24 months at 0%</div></div>
                <div class="lg-delivery">🚚 Free Delivery</div>
                <div class="lg-btn-row"><a href="#" class="lg-btn lg-btn-sec">{btn1_text}</a><a href="#" class="lg-btn {btn2_class}" style="{'' if is_primary else 'background-color:#e50000; color:white; border:none;'}">{btn2_text}</a></div>
                <div style="text-align: center; margin-top: 15px; font-size: 12px; color: #666;"><input type="checkbox"> Compare</div>
            </div>
            """

        purpose = st.session_state.data.get('purpose', '')
        cards = []
        if purpose == "Gaming":
            cards = [
                create_lg_card_html(["2% with PayPal"], "52\" UltraGear evo G9, World's Largest 5K2K 240Hz", "52G930B-B", "7", "Save 0,00 €", "1.799,00 €", "1.799,00 €", "More Info", "Notify Me", "https://www.lg.com/content/dam/channel/wcms/de/_it/fcs/52g930b-b/LG-IT_PRJ_Award-Gallery-Images-52G930B-B_2026-03_01_450x450.jpg/jcr:content/renditions/thum-350x350.jpeg"),
                create_lg_card_html(["Pre-order", "5 Yr Warranty"], "39\" UltraGear evo GX9, 5K2K OLED Gaming", "39GX950B-B", "3", "Save 0,01 €", "1.798,99 €", "1.799,00 €", "More Info", "Pre-order", "https://www.lg.com/content/dam/channel/wcms/de/_it/galleries/39gx950b-b/gallery-cards-de/01_39GX950B.jpg/jcr:content/renditions/thum-350x350.jpeg", is_primary=True),
                create_lg_card_html(["€50 Bonus", "2% with PayPal"], "LG UltraGear™ 32\" 4K OLED 240Hz Gaming Monitor", "32GS95UE", "45", "Save 200,00 €", "1.299,00 €", "1.499,00 €", "More Info", "Buy Now", "https://www.lg.com/content/dam/channel/wcms/de/images/monitore/32gs95ux-b/gallery/ultragear-32gs95ue-basic-large.jpg/jcr:content/renditions/thum-350x350.jpeg")
            ]
        else: 
            cards = [
                create_lg_card_html(["Recommended", "2% with PayPal"], "LG UltraFine™ evo 32\" 6K Nano IPS Black (Thunderbolt™ 5)", "32U990A-S", "80", "Save 300,00 €", "1.699,00 €", "1.999,00 €", "More Info", "Buy Now", "https://www.lg.com/content/dam/channel/wcms/de/32u990a-s/LG-IT_PRJ_Award-Gallery-Images-32U990A-S_20260504_01_450%20x%20450.jpg/jcr:content/renditions/thum-350x350.jpeg", is_primary=True),
                create_lg_card_html(["New", "Ergo Stand"], "LG 32\" 4K UHD Ergo Monitor with USB-C", "32UN880-B", "120", "Save 150,00 €", "549,00 €", "699,00 €", "More Info", "Buy Now", "https://www.lg.com/content/dam/channel/wcms/de/images/32un880k-b/gallery/ultrafine-uhd-4k-5k-32un880k-2024-gallery-basic-large.jpg/jcr:content/renditions/thum-350x350.jpeg"),
                create_lg_card_html(["Lifestyle", "Smart"], "LG StanbyME 27\" FHD IPS Touch Screen", "27ART10AKPL", "34", "Save 100,00 €", "999,00 €", "1.099,00 €", "More Info", "Buy Now", "https://www.lg.com/content/dam/channel/wcms/de/2025_ms_lg-com/tv/stanbyme-2/27lx6t/gp1/gallery/basic/450-basic.jpg/jcr:content/renditions/thum-350x350.jpeg")
            ]

        col1, col2, col3 = st.columns(3)
        with col1: st.markdown(cards[0], unsafe_allow_html=True)
        with col2: st.markdown(cards[1], unsafe_allow_html=True)
        with col3: st.markdown(cards[2], unsafe_allow_html=True)

        st.write("<br><br>", unsafe_allow_html=True)
        col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
        with col_btn2:
            if st.button("🔄 Restart Finder", use_container_width=True):
                st.session_state.step = 1; st.session_state.data = {}; st.rerun()

if __name__ == "__main__":
    main()
