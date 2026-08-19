import streamlit as st
import pandas as pd

# --- SAHIFANI SOZLASH ---
st.set_page_config(page_title="Tabib AI - Tibbiy Yordam", page_icon="🏥", layout="wide")

# --- SAVATNI XOTIRADA SAQLASH ---
if 'cart' not in st.session_state:
    st.session_state.cart = []

# --- CSS USLUBLARI ---
st.markdown("""
    <style>
    .stApp {
        background-color: #f8f9fa;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    h1, h2, h3 {
        color: #2c3e50;
        font-weight: 700;
    }
    .custom-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-left: 5px solid #3498db;
    }
    .stButton>button {
        background-color: #3498db;
        color: white;
        border-radius: 10px;
        padding: 0.5rem 2rem;
        border: none;
        font-weight: 600;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #2980b9;
    }
    </style>
""", unsafe_allow_html=True)

# --- MA'LUMOTLARNI YUKLASH ---
@st.cache_data
def load_data():
    try:
        shifokorlar_df = pd.read_csv("shifokorlar.csv")
    except:
        doctors_df = pd.DataFrame([
            {"Ism": "Dr. Alisher Karimov", "Mutaxassislik": "Kardiolog", "Manzil": "Toshkent sh.", "Reyting": "⭐⭐⭐⭐⭐", "Rasm": "https://via.placeholder.com/150"},
            {"Ism": "Dr. Malika Umarova", "Mutaxassislik": "Pediatr", "Manzil": "Samarqand sh.", "Reyting": "⭐⭐⭐⭐⭐", "Rasm": "https://via.placeholder.com/150"}
        ])
        
    try:
        meds_df = pd.read_csv("meds.csv")
    except:
        meds_df = pd.DataFrame([
            {"Nomi": "Paratsetamol 500mg", "Turi": "Og'riq qoldiruvchi", "Narxi": "12,000 UZS", "Holat": "Mavjud", "Rasm": "https://via.placeholder.com/150"},
            {"Nomi": "Amoksillin 250mg", "Turi": "Antibiotik", "Narxi": "45,000 UZS", "Holat": "Mavjud", "Rasm": "https://via.placeholder.com/150"}
        ])
        
    return doctors_df, meds_df

doctors_db, meds_db = load_data()

# --- ASOSIY MENYU (SIDEBAR) ---
st.sidebar.title("🏥 Tabib AI")
st.sidebar.markdown("---")

cart_count = len(st.session_state.cart)
app_mode = st.sidebar.radio(
    "Bo'limni tanlang", 
    ["🏠 Bosh sahifa", "🤖 AI Konsultatsiya", "👨‍⚕️ Shifokorlar", "💊 Dorixona", f"🛒 Savat ({cart_count})"]
)

# --- 1. BOSH SAHIFA ---
if app_mode == "🏠 Bosh sahifa":
    st.title("🏥 Xush kelibsiz, Tabib AI ga!")
    st.markdown("---")
    st.markdown("""
        <div class="custom-card" style="border-left: 5px solid #2ecc71;">
            <div style="font-size: 1.2rem; font-weight: 600; color: #2c3e50; margin-bottom: 10px;">O'zbekiston uchun yagona raqamli tibbiy ekotizim</div>
            <div style="color: #7f8c8d;">1000+ shifokorlar va dorixonalar bazasi, AI yordamchi hamda nasiya savdo imkoniyati.</div>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info(f"👨‍⚕️ Shifokorlar bazasi")
    with col2:
        st.success("💡 AI Simptom Tahlili")
    with col3:
        st.warning("💳 Nasiya savdo")

# --- 2. AI KONSULTATSIYA ---
elif app_mode == "🤖 AI Konsultatsiya":
    st.title("🤖 AI Simptom Tahlili")
    st.markdown("---")
    user_symptoms = st.text_area("Alomatlarni kiriting (Masalan: 'Boshim og'riyapti')", height=150)
    if st.button("Tahlil qilish"):
        if user_symptoms:
            direction = "Sizga **Terapevt** ko'rigi tavsiya etiladi."
            if "bosh" in user_symptoms.lower():
                direction = "Sizga **Nevropatolog** ko'rigi kerak."
            elif "tish" in user_symptoms.lower():
                direction = "Sizga **Stomatolog** ko'rigi kerak."
            st.success(direction)
        else:
            st.warning("Iltimos, alomatlarni yozing!")

# --- 3. SHIFOKORLAR ---
elif app_mode == "👨‍⚕️ Shifokorlar":
    st.title("👨‍⚕️ Malakali Shifokorlar Ro'yxati")
    st.markdown("---")
    search_term = st.text_input("🔍 Shifokor ismi yoki mutaxassisligi bo'yicha qidiring")
    filtered_doctors = doctors_db[doctors_db.astype(str).apply(lambda row: row.str.contains(search_term, case=False).any(), axis=1)] if search_term else doctors_db

    if not filtered_doctors.empty:
        for i in range(0, len(filtered_doctors), 3):
            cols = st.columns(3)
            for j in range(3):
                if i + j < len(filtered_doctors):
                    row = filtered_doctors.iloc[i + j]
                    with cols[j]:
                        st.markdown(f"""
                            <div style="background: white; padding: 15px; border-radius: 12px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); margin-bottom: 15px; text-align: center;">
                                <img src="{row.get('Rasm', 'https://via.placeholder.com/150')}" style="width: 90px; height: 90px; object-fit: cover; border-radius: 50%; margin-bottom: 10px;">
                                <div style="font-weight: 600; color: #2c3e50;">{row['Ism']}</div>
                                <div style="color: #3498db; font-size: 0.9rem; margin-top: 5px;">{row['Mutaxassislik']}</div>
                                <div style="color: #7f8c8d; font-size: 0.85rem; margin-top: 5px;">📍 {row['Manzil']}</div>
                                <div style="color: #f39c12; font-size: 0.85rem; margin-top: 5px;">{row.get('Reyting', '⭐⭐⭐⭐⭐')}</div>
                            </div>
                        """, unsafe_allow_html=True)
                        if st.button("Qabulga yozilish", key=f"doc_{i+j}"):
                            st.success(f"{row['Ism']} qabuliga yozildingiz!")
    else:
        st.info("Shifokor topilmadi.")

# --- 4. DORIXONA ---
elif app_mode == "💊 Dorixona":
    st.title("💊 Onlayn Dorixona (Uzum Market uslubida)")
    st.markdown("---")
    med_search = st.text_input("🔍 Dori nomini qidiring")
    filtered_meds = meds_db[meds_db.astype(str).apply(lambda row: row.str.contains(med_search, case=False).any(), axis=1)] if med_search else meds_db
        
    if not filtered_meds.empty:
        for i in range(0, len(filtered_meds), 3):
            cols = st.columns(3)
            for j in range(3):
                if i + j < len(filtered_meds):
                    row = filtered_meds.iloc[i + j]
                    with cols[j]:
                        st.markdown(f"""
                            <div style="background: white; padding: 15px; border-radius: 12px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); margin-bottom: 15px; text-align: center;">
                                <img src="{row.get('Rasm', 'https://via.placeholder.com/150')}" style="width: 100%; height: 130px; object-fit: cover; border-radius: 8px;">
                                <div style="font-weight: 600; margin-top: 10px; color: #2c3e50;">{row['Nomi']}</div>
                                <div style="color: #7f8c8d; font-size: 0.85rem;">{row['Turi']}</div>
                                <div style="margin-top: 10px; font-weight: 700; color: #e74c3c; font-size: 1.1rem;">{row['Narxi']}</div>
                            </div>
                        """, unsafe_allow_html=True)
                        if st.button("Savatga qo'shish", key=f"med_{i+j}"):
                            st.session_state.cart.append(row.to_dict())
                            st.success(f"'{row['Nomi']}' savatga qo'shildi!")
    else:
        st.info("Dori topilmadi.")

# --- 5. SAVAT ---
elif app_mode.startswith("🛒 Savat"):
    st.title("🛒 Sizning savatingiz")
    st.markdown("---")
    if len(st.session_state.cart) > 0:
        cart_df = pd.DataFrame(st.session_state.cart)
        st.dataframe(cart_df[['Nomi', 'Turi', 'Narxi', 'Holat']], use_container_width=True)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Buyurtma berish"):
                st.success("Buyurtma qabul qilindi!")
                st.session_state.cart = []
        with col2:
            if st.button("Nasiyaga olish"):
                st.success("Nasiya rasmiylashtirildi!")
                st.session_state.cart = []
    else:
        st.info("Savatingiz bo'sh.")
# ==========================================
# TABIB AI QISMI (Eski kodlarga tegmasdan oxiriga qo'shiladi)
# ==========================================
import google.generativeai as genai

# API kalitingizni shu yerga qo'shtirnoq ichiga yozasiz
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
_tabib_ai_model = genai.GenerativeModel("gemini-1.5-flash")

st.markdown("---")
st.header("🩺 Tabib AI — Sun'iy Intellekt Maslahatchisi")
st.write(
    "Istalgan tibbiy savolingizni bering: simptomlar, tahlil natijalari yoki"
    " dori vositalari haqida sun'iy intellekt batafsil tushuntirib beradi."
)

_ai_input = st.text_area(
    "Savolingizni yoki shikoyatingizni shu yerga yozing:",
    placeholder="Masalan: Bosh og'rig'i nima sababdan bo'lishi mumkin?",
    key="tabib_ai_text_input",
)

if st.button("AI dan javob olish", key="tabib_ai_btn"):
  if _ai_input.strip() != "":
    with st.spinner("Tabib AI tahlil qilmoqda..."):
      _ai_prompt = (
          "Siz tibbiy yordamchi sun'iy intellekt sifatida ishlayapsiz."
          " Foydalanuvchining har qanday tibbiy savoliga, simptomlariga yoki"
          " tahlillariga o'zbek tilida aniq, tushunarli va foydali ma'lumot"
          f" berib tushuntirib bering: {_ai_input}"
      )
      _ai_response = _tabib_ai_model.generate_content(_ai_prompt)
      st.subheader("🤖 Tabib AI javobi:")
      st.write(_ai_response.text)
  else:
    st.warning("Iltimos, avval savolingizni yozing!")
