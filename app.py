import streamlit as st
import pandas as pd
import google.generativeai as genai

# --- STREAMLIT-NING UXLAB QOLISHINING OLDINI OLISH (PING ENDPOINT) ---
# Agar brauzer yoki UptimeRobot /?ping so'rovini yuborsa, ilova darhol javob beradi va uxlamaydi
try:
    query_params = st.query_params
    if "ping" in query_params:
        st.write("pong")
        st.stop()
except Exception:
    pass

# --- SAHIFANI SOZLASH ---
st.set_page_config(page_title="Tabib AI - Healthcare Ecosystem", page_icon="🏥", layout="wide")

# --- TILNI TANLASH VA TARJIMALAR ---
st.sidebar.title("🏥 Tabib AI")
lang = st.sidebar.selectbox("🌐 Language / Til", ["English", "O'zbekcha"])

translations = {
    "English": {
        "menu_home": "🏠 Home",
        "menu_ai": "🤖 AI Consultation",
        "menu_doctors": "👨‍⚕️ Doctors",
        "menu_pharmacy": "💊 Pharmacy",
        "cart": "🛒 Cart",
        "welcome_title": "🏥 Welcome to Tabib AI!",
        "welcome_sub": "Unified Digital Healthcare Ecosystem for Uzbekistan",
        "welcome_desc": "1000+ doctors and pharmacies database, AI assistant, and installment shopping options.",
        "doc_base": "👨‍⚕️ Doctors Database",
        "ai_analysis": "💡 AI Symptom Analysis",
        "installment": "💳 Installment (Buy Now, Pay Later)",
        "ai_title": "🤖 AI Symptom Analysis",
        "ai_prompt": "Enter your symptoms (e.g., 'I have a headache')",
        "ai_btn": "Analyze",
        "doc_title": "👨‍⚕️ Qualified Doctors List",
        "doc_search": "🔍 Search by doctor name or specialty",
        "book_btn": "Book Appointment",
        "pharmacy_title": "💊 Online Pharmacy (Uzum Market Style)",
        "pharm_search": "🔍 Search medicine name",
        "add_cart": "Add to Cart",
        "cart_title": "🛒 Your Shopping Cart",
        "order_btn": "Place Order",
        "nasiya_btn": "Buy with Installments",
        "tabib_ai_header": "🩺 Tabib AI — AI Medical Assistant",
        "tabib_ai_desc": "Ask any medical question: symptoms, test results, or medications, and the AI will explain in detail.",
        "tabib_input": "Type your question or complaint here:",
        "tabib_btn": "Get AI Response",
        "spinner": "Tabib AI is analyzing...",
        "warning_symp": "Please enter your symptoms!",
        "warning_q": "Please type your question first!",
        "success_book": " successfully booked!",
        "success_cart": " added to cart!",
        "success_order": "Order accepted!",
        "success_nasiya": "Installment plan processed!",
        "empty_cart": "Your cart is empty.",
        "doc_not_found": "Doctor not found.",
        "med_not_found": "Medicine not found."
    },
    "O'zbekcha": {
        "menu_home": "🏠 Bosh sahifa",
        "menu_ai": "🤖 AI Konsultatsiya",
        "menu_doctors": "👨‍⚕️ Shifokorlar",
        "menu_pharmacy": "💊 Dorixona",
        "cart": "🛒 Savat",
        "welcome_title": "🏥 Xush kelibsiz, Tabib AI ga!",
        "welcome_sub": "O'zbekiston uchun yagona raqamli tibbiy ekotizim",
        "welcome_desc": "1000+ shifokorlar va dorixonalar bazasi, AI yordamchi hamda nasiya savdo imkoniyati.",
        "doc_base": "👨‍⚕️ Shifokorlar bazasi",
        "ai_analysis": "💡 AI Simptom Tahlili",
        "installment": "💳 Nasiya savdo",
        "ai_title": "🤖 AI Simptom Tahlili",
        "ai_prompt": "Alomatlarni kiriting (Masalan: 'Boshim og'riyapti')",
        "ai_btn": "Tahlil qilish",
        "doc_title": "👨‍⚕️ Malakali Shifokorlar Ro'yxati",
        "doc_search": "🔍 Shifokor ismi yoki mutaxassisligi bo'yicha qidiring",
        "book_btn": "Qabulga yozilish",
        "pharmacy_title": "💊 Onlayn Dorixona (Uzum Market uslubida)",
        "pharm_search": "🔍 Dori nomini qidiring",
        "add_cart": "Savatga qo'shish",
        "cart_title": "🛒 Sizning savatingiz",
        "order_btn": "Buyurtma berish",
        "nasiya_btn": "Nasiyaga olish",
        "tabib_ai_header": "🩺 Tabib AI — Sun'iy Intellekt Maslahatchisi",
        "tabib_ai_desc": "Istalgan tibbiy savolingizni bering: simptomlar, tahlil natijalari yoki dori vositalari haqida sun'iy intellekt batafsil tushuntirib beradi.",
        "tabib_input": "Savolingizni yoki shikoyatingizni shu yerga yozing:",
        "tabib_btn": "AI dan javob olish",
        "spinner": "Tabib AI tahlil qilmoqda...",
        "warning_symp": "Iltimos, alomatlarni yozing!",
        "warning_q": "Iltimos, avval savolingizni yozing!",
        "success_book": " qabuliga yozildingiz!",
        "success_cart": " savatga qo'shildi!",
        "success_order": "Buyurtma qabul qilindi!",
        "success_nasiya": "Nasiya rasmiylashtirildi!",
        "empty_cart": "Savatingiz bo'sh.",
        "doc_not_found": "Shifokor topilmadi.",
        "med_not_found": "Dori topilmadi."
    }
}

t = translations[lang]

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
        doctors_df = pd.read_csv("shifokorlar.csv")
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
st.sidebar.markdown("---")
cart_count = len(st.session_state.cart)
app_mode = st.sidebar.radio(
    "Menu" if lang == "English" else "Bo'limni tanlang",
    [t["menu_home"], t["menu_ai"], t["menu_doctors"], t["menu_pharmacy"], f"{t['cart']} ({cart_count})"]
)

# --- 1. BOSH SAHIFA ---
if app_mode == t["menu_home"]:
    st.title(t["welcome_title"])
    st.markdown("---")
    st.markdown(f"""
        <div class="custom-card" style="border-left: 5px solid #2ecc71;">
            <div style="font-size: 1.2rem; font-weight: 600; color: #2c3e50; margin-bottom: 10px;">{t['welcome_sub']}</div>
            <div style="color: #7f8c8d;">{t['welcome_desc']}</div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.info(t["doc_base"])
    with col2:
        st.success(t["ai_analysis"])
    with col3:
        st.warning(t["installment"])

# --- 2. AI KONSULTATSIYA ---
elif app_mode == t["menu_ai"]:
    st.title(t["ai_title"])
    st.markdown("---")
    user_symptoms = st.text_area(t["ai_prompt"], height=150)
    if st.button(t["ai_btn"]):
        if user_symptoms:
            if lang == "English":
                direction = "We recommend a consultation with a **General Practitioner (GP)**."
                if "head" in user_symptoms.lower():
                    direction = "You need a consultation with a **Neurologist**."
                elif "teeth" in user_symptoms.lower() or "tooth" in user_symptoms.lower():
                    direction = "You need a consultation with a **Dentist**."
            else:
                direction = "Sizga **Terapevt** ko'rigi tavsiya etiladi."
                if "bosh" in user_symptoms.lower():
                    direction = "Sizga **Nevropatolog** ko'rigi kerak."
                elif "tish" in user_symptoms.lower():
                    direction = "Sizga **Stomatolog** ko'rigi kerak."
            st.success(direction)
        else:
            st.warning(t["warning_symp"])

# --- 3. SHIFOKORLAR ---
elif app_mode == t["menu_doctors"]:
    st.title(t["doc_title"])
    st.markdown("---")
    search_term = st.text_input(t["doc_search"])
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
                        if st.button(t["book_btn"], key=f"doc_{i+j}"):
                            st.success(f"{row['Ism']}{t['success_book']}")
    else:
        st.info(t["doc_not_found"])

# --- 4. DORIXONA ---
elif app_mode == t["menu_pharmacy"]:
    st.title(t["pharmacy_title"])
    st.markdown("---")
    med_search = st.text_input(t["pharm_search"])
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
                        if st.button(t["add_cart"], key=f"med_{i+j}"):
                            st.session_state.cart.append(row.to_dict())
                            st.success(f"'{row['Nomi']}'{t['success_cart']}")
    else:
        st.info(t["med_not_found"])

# --- 5. SAVAT ---
elif app_mode.startswith("🛒 Savat") or app_mode.startswith("🛒 Cart"):
    st.title(t["cart_title"])
    st.markdown("---")
    if len(st.session_state.cart) > 0:
        cart_df = pd.DataFrame(st.session_state.cart)
        st.dataframe(cart_df[['Nomi', 'Turi', 'Narxi', 'Holat']], use_container_width=True)
        col1, col2 = st.columns(2)
        with col1:
            if st.button(t["order_btn"]):
                st.success(t["success_order"])
                st.session_state.cart = []
        with col2:
            if st.button(t["nasiya_btn"]):
                st.success(t["success_nasiya"])
                st.session_state.cart = []
    else:
        st.info(t["empty_cart"])

# ==========================================
# TABIB AI QISMI (GEMINI)
# ==========================================
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
_tabib_ai_model = genai.GenerativeModel("gemini-2.5-flash")

st.markdown("---")
st.header(t["tabib_ai_header"])
st.write(t["tabib_ai_desc"])

_ai_input = st.text_area(
    t["tabib_input"],
    placeholder="Masalan: Bosh og'rig'i nima sababdan bo'lishi mumkin?" if lang == "O'zbekcha" else "Example: What causes a headache?",
    key="tabib_ai_text_input",
)

if st.button(t["tabib_btn"], key="tabib_ai_btn"):
    if _ai_input.strip() != "":
        with st.spinner(t["spinner"]):
            if lang == "English":
                _ai_prompt = (
                    "You are working as an AI medical assistant. "
                    "Provide clear, accurate, and helpful information in English "
                    f"regarding the user's medical question, symptoms, or tests: {_ai_input}"
                )
            else:
                _ai_prompt = (
                    "Siz tibbiy yordamchi sun'iy intellekt sifatida ishlayapsiz."
                    " Foydalanuvchining har qanday tibbiy savoliga, simptomlariga yoki"
                    " tahlillariga o'zbek tilida aniq, tushunarli va foydali ma'lumot"
                    f" berib tushuntirib bering: {_ai_input}"
                )
            _ai_response = _tabib_ai_model.generate_content(_ai_prompt)
            st.subheader("🤖 Tabib AI response:" if lang == "English" else "🤖 Tabib AI javobi:")
            st.write(_ai_response.text)
    else:
        st.warning(t["warning_q"])
