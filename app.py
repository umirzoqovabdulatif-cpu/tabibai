import streamlit.components.v1 as components

# --- ILOVANI UXLATMASLIK UCHUN AVTO-REFRESH ---
components.html(
    """
    <script>
        setTimeout(function(){
            window.location.reload();
        }, 300000); // 300000 millisoniya = 5 daqiqa
    </script>
    """,
    height=0,
)

import streamlit as st
import pandas as pd
import google.generativeai as genai

# --- SAHIFANI SOZLASH ---
st.set_page_config(page_title="Tabib AI - Healthcare Ecosystem", page_icon="💊", layout="wide")

# --- TILNI TANLASH VA TARJIMALAR ---
st.sidebar.title("💊 Tabib AI")
lang = st.sidebar.selectbox("🌐 Language / Til", ["English", "O'zbekcha"])

# Tarjimalar lug'ati
translations = {
    "English": {
        "title": "Welcome to Tabib AI!",
        "subtitle": "Your single digital healthcare ecosystem for Uzbekistan",
        "desc": "1000+ doctors and pharmacies database, AI medical assistant, and buy-now-pay-later (installment) options.",
        "menu": "Select menu:",
        "home": "Home",
        "ai_consult": "AI Consultation",
        "doctors": "Doctors Database",
        "pharmacy": "Online Pharmacy",
        "cart": "Cart",
        "symptom_title": "AI Symptom Analyzer",
        "symptom_prompt": "Describe your symptoms or health issues:",
        "analyze_btn": "Analyze Symptoms",
        "ai_result": "AI Medical Recommendation:",
    },
    "O'zbekcha": {
        "title": "Xush kelibsiz, Tabib AI ga!",
        "subtitle": "O'zbekiston uchun yagona raqamli tibbiy ekotizim",
        "desc": "1000+ shifokorlar va dorixonalar bazasi, AI yordamchi hamda nasiya savdo imkoniyati.",
        "menu": "Bo'limni tanlang:",
        "home": "Bosh sahifa",
        "ai_consult": "AI Konsultatsiya",
        "doctors": "Shifokorlar",
        "pharmacy": "Dorixona",
        "cart": "Savat",
        "symptom_title": "AI Simptom Tahlili",
        "symptom_prompt": "Simptomlaringiz yoki sog'ligingizdagi muammoni yozing:",
        "analyze_btn": "Tahlil qilish",
        "ai_result": "AI Tibbiy Tavsiyasi:",
    }
}

t = translations[lang]

# --- ASOSIY MENYU ---
menu_choice = st.sidebar.radio(t["menu"], [t["home"], t["ai_consult"], t["doctors"], t["pharmacy"], t["cart"]])

# --- 1. BOSH SAHIFA ---
if menu_choice == t["home"]:
    st.title(f"🏥 {t['title']}")
    st.subheader(t["subtitle"])
    st.info(t["desc"])
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Shifokorlar / Doctors", value="1000+")
    with col2:
        st.metric(label="Dorixonalar / Pharmacies", value="500+")

# --- 2. AI KONSULTATSIYA ---
elif menu_choice == t["ai_consult"]:
    st.title(f"🤖 {t['symptom_title']}")
    user_input = st.text_area(t["symptom_prompt"])
    
    if st.button(t["analyze_btn"]):
        if user_input.strip():
            with st.spinner("Analyzing... / Tahlil qilinmoqda..."):
                try:
                    # Gemini API ulanishi (agar kalit kiritilgan bo'lsa)
                    genai.configure(api_key=st.secrets.get("GEMINI_API_KEY", "YOUR_API_KEY"))
                    model = genai.GenerativeModel("gemini-1.5-flash")
                    response = model.generate_content(f"Act as a professional medical assistant. Analyze these symptoms and give recommendations: {user_input}")
                    st.success(t["ai_result"])
                    st.write(response.text)
                except Exception as e:
                    st.warning("AI model demo mode. (API key not configured)")
                    st.write("Please consult a real doctor for accurate diagnosis. / Aniq tashxis uchun shifokorga murojaat qiling.")
        else:
            st.error("Please enter your symptoms. / Iltimos, simptomlarni kiriting.")

# --- 3. SHIFOKORLAR ---
elif menu_choice == t["doctors"]:
    st.title("👨‍⚕️ Doctors Database / Shifokorlar Bazasi")
    st.write("Find certified specialists across Uzbekistan. / O'zbekiston bo'ylab malakali mutaxassislarni toping.")
    
    doc_data = {
        "Name / Ism": ["Dr. Alisher Usmanov", "Dr. Malika Karimova", "Dr. Jasur Rahimov"],
        "Specialty / Mutaxassislik": ["Cardiologist / Kardiolog", "Pediatrician / Pediatr", "Neurologist / Nevropatolog"],
        "Location / Manzil": ["Tashkent", "Samarkand", "Andijan"]
    }
    st.dataframe(pd.DataFrame(doc_data), use_container_width=True)

# --- 4. DORIXONA ---
elif menu_choice == t["pharmacy"]:
    st.title("💊 Online Pharmacy / Onlayn Dorixona")
    st.write("Order medicines with installment options (Buy now, pay later). / Dorilarni nasiya savdo imkoniyati bilan buyurtma qiling.")
    
    med_data = {
        "Medicine / Dori": ["Paracetamol", "Aspirin", "Amoxicillin"],
        "Price / Narxi": ["15,000 UZS", "12,000 UZS", "45,000 UZS"],
        "Installment / Nasiya": ["Available / Mavjud", "Available / Mavjud", "Available / Mavjud"]
    }
    st.dataframe(pd.DataFrame(med_data), use_container_width=True)

# --- 5. SAVAT ---
elif menu_choice == t["cart"]:
    st.title("🛒 Cart / Savatcha")
    st.write("Your cart is empty. / Savatchangiz bo'sh.")
