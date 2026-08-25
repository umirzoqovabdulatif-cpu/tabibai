import streamlit as st

# Sahifa konfiguratsiyasi
st.set_page_config(
    page_title="Tabib AI — Tibbiy Platforma", page_icon="🩺", layout="wide"
)

# ----------------- DIZAYN VA USLUBLAR (CSS) -----------------
st.markdown(
    """
    <style>
    /* Asosiy fon rangi */
    .stApp {
        background-color: #fcfcfd;
    }
    
    /* Chiroyli sarlavha konteyneri */
    .main-header {
        background: linear-gradient(135deg, #2b6cb0 0%, #3182ce 100%);
        padding: 24px 30px;
        border-radius: 14px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(49, 130, 206, 0.2);
    }
    .main-header h1 {
        color: white !important;
        font-size: 26px;
        margin-bottom: 5px;
    }
    .main-header p {
        color: #e2e8f0;
        font-size: 14px;
        margin: 0;
    }

    /* Shifokor kartochkasi */
    .doctor-card {
        background: #ffffff;
        border: 1px solid #edf2f7;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 16px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.02);
        transition: all 0.2s ease-in-out;
    }
    .doctor-card:hover {
        border-color: #3182ce;
        box-shadow: 0 5px 15px rgba(49, 130, 206, 0.08);
        transform: translateY(-2px);
    }
    .doc-name {
        font-size: 17px;
        font-weight: 700;
        color: #2d3748;
        margin-bottom: 4px;
    }
    .doc-spec {
        font-size: 13px;
        font-weight: 600;
        color: #3182ce;
        background: #ebf8ff;
        padding: 3px 8px;
        border-radius: 4px;
        display: inline-block;
        margin-bottom: 8px;
    }
    .doc-address {
        font-size: 13px;
        color: #718096;
        margin-bottom: 8px;
    }
    .doc-rating {
        font-size: 13px;
        color: #d69e2e;
        font-weight: 600;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# ----------------- SHIFOKORLARNING TO'LIQ BAZASI -----------------
doctors_list = [
    {
        "Ism": "Dr. Ismatova Moxigul Kabulovna",
        "Mutaxassislik": "Allergolog",
        "Manzil": "International Allergy Center, Osiyo ko`chasi, 86А",
        "Reyting": "⭐⭐⭐⭐⭐ (5.0)",
    },
    {
        "Ism": "Dr. Tursunova Dilorom Sabitovna",
        "Mutaxassislik": (
            "Allergolog, Pulmonolog, Immunolog, Terapevt"
        ),
        "Manzil": "Medion Clinic 24-7, Zulfiyaxanum ko`chasi, 18",
        "Reyting": "⭐⭐⭐⭐⭐ (5.0)",
    },
    {
        "Ism": "Dr. Qurbonova Guncha Amangeldievna",
        "Mutaxassislik": "Allergolog, Fizioterapevt, Pulmonolog",
        "Manzil": "M-Clinic, Tantan ko'chasi, 1-uy",
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Dr. Rumi Linara Rinatovna",
        "Mutaxassislik": "Allergolog",
        "Manzil": "International Allergy Center, Osiyo ko`chasi, 86А",
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Dr. Abdurahmonov Abdulla Abdukaharovich",
        "Mutaxassislik": "Allergolog, Pulmonolog, Pediatr, Terapevt",
        "Manzil": "Medion Family Hospital, Istiroxat ko'ch., 258",
        "Reyting": "⭐⭐⭐⭐⭐ (5.0)",
    },
    {
        "Ism": "Dr. Rahmonova Shoira Po'latovna",
        "Mutaxassislik": "Allergolog, Nevropatolog",
        "Manzil": "Dusel Medical, To‘kimachi ko‘chasi, 3-uy",
        "Reyting": "⭐⭐⭐⭐⭐ (4.8)",
    },
    {
        "Ism": "Dr. Tkachuk Viktoriya Aleksandrovna",
        "Mutaxassislik": "Allergolog",
        "Manzil": "International Allergy Center / EBM Clinic, Osiyo ko`chasi, 86А",
        "Reyting": "⭐⭐⭐⭐⭐ (5.0)",
    },
    {
        "Ism": "Dr. Saipova Nodira Sagdullayevna",
        "Mutaxassislik": "Allergolog, Dermatolog, Podolog, Kosmetolog",
        "Manzil": "OpenLab tibbiyot markazi, Avliyo ota ko'chasi, 9",
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Dr. Ismoilova Dilfuza Mirsabitovna",
        "Mutaxassislik": "Allergolog, Pulmonolog, Terapevt",
        "Manzil": "Medion Clinic 24-7, Zulfiyaxanum ko`chasi, 18",
        "Reyting": "⭐⭐⭐⭐⭐ (5.0)",
    },
    {
        "Ism": "Dr. Pulatova Iroda Alijonovna",
        "Mutaxassislik": "Allergolog",
        "Manzil": "M-Clinic, Tantan ko'chasi, 1-uy",
        "Reyting": "⭐⭐⭐⭐⭐ (4.8)",
    },
    {
        "Ism": "Dr. Malikova Alfira Railovna",
        "Mutaxassislik": (
            "Allergolog, Kardiolog, Gastroenterolog, Pulmonolog"
        ),
        "Manzil": "Shams Medical Center, Tallimarjon ko`chasi, 43",
        "Reyting": "⭐⭐⭐⭐⭐ (5.0)",
    },
    {
        "Ism": "Dr. Jurayeva Maftuna Kuvandikovna",
        "Mutaxassislik": "Allergolog",
        "Manzil": "International Allergy Center, Osiyo ko`chasi, 86А",
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Dr. Miraxmedova Gulnora Turgunovna",
        "Mutaxassislik": "Allergolog, Dermatolog, Pulmonolog",
        "Manzil": "Saba Darmon, Bogkucha ko`chasi, 17A",
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Dr. Ochilov Sardor Ilxomovich",
        "Mutaxassislik": "Allergolog, Pulmonolog, Immunolog",
        "Manzil": "Shox Med Педиатрия, Xushnavo 4-chi o'tish joyi, 26/2",
        "Reyting": "⭐⭐⭐⭐⭐ (5.0)",
    },
    {
        "Ism": "Dr. Ubaydullaeva Naima Nabixanovna",
        "Mutaxassislik": "Allergolog, Pulmonolog",
        "Manzil": (
            "International Allergy Center / Shahar klinik kasalxonasi №1,"
            " Osiyo ko`chasi, 86А"
        ),
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Dr. Xudoyqulova Nodira Ulug'bekovna",
        "Mutaxassislik": "Allergolog, Pulmonolog, Terapevt",
        "Manzil": "Darmon Servis, Cho'pon Ota ko`chasi, 18/19",
        "Reyting": "⭐⭐⭐⭐⭐ (4.8)",
    },
    {
        "Ism": "Dr. Ortikxodjayeva Durdona Anvarovna",
        "Mutaxassislik": "Allergolog, Pediatr, Immunolog",
        "Manzil": "Darmon Servis, Cho'pon Ota ko`chasi, 18/19",
        "Reyting": "⭐⭐⭐⭐⭐ (5.0)",
    },
    {
        "Ism": "Dr. Alieva Vasila Shukurullaevna",
        "Mutaxassislik": "Allergolog",
        "Manzil": "Medilux Medical center, Farobiy ko`chasi, 3-B",
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Dr. Djurayev Abduvaxid Raxmankulovich",
        "Mutaxassislik": "Allergolog, Pulmonolog",
        "Manzil": "Sinomed MD / Darmon Servis, Taxtapul ko`chasi, 341a",
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Dr. Abdug'aniyev Saidazimxon Usmonxujayevich",
        "Mutaxassislik": "Allergolog, Immunolog, Pulmonolog",
        "Manzil": "Kimyo University Hospital, Bunyodkor ko`ch. Yakkabog` MFY, 19",
        "Reyting": "⭐⭐⭐⭐⭐ (5.0)",
    },
    {
        "Ism": "Fattaxov Bobir Shavkatovich",
        "Mutaxassislik": "Dermatolog, Dermatovenereolog",
        "Manzil": (
            "O'zbekiston dermatovenerologiya va kosmetologiya markazi, Farobiy"
            " ko'chasi, 3A"
        ),
        "Reyting": "⭐⭐⭐⭐⭐ (5.0)",
    },
    {
        "Ism": "Xaldarbekov Madamin Karimjanovich",
        "Mutaxassislik": "Dermatolog, Dermatovenereolog",
        "Manzil": (
            "O'zbekiston dermatovenerologiya va kosmetologiya markazi, Farobiy"
            " ko'chasi, 3A"
        ),
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Zakirov Rustam Ruxullaevich",
        "Mutaxassislik": "Dermatolog, Dermatovenereolog",
        "Manzil": (
            "Medion Aesthetic and SPA / Medion Clinic 24-7, Zulfiyaxonim ko'chasi,"
            " 18"
        ),
        "Reyting": "⭐⭐⭐⭐⭐ (5.0)",
    },
    {
        "Ism": "Jamolov Davron Nematovich",
        "Mutaxassislik": "Dermatolog",
        "Manzil": "Shox Med Center, Oybek ko`chasi 34",
        "Reyting": "⭐⭐⭐⭐⭐ (4.8)",
    },
    {
        "Ism": "Rasulova Nazira Anvarovna",
        "Mutaxassislik": "Dermatolog",
        "Manzil": (
            "O'zbekiston dermatovenerologiya va kosmetologiya markazi, Farobiy"
            " ko'chasi, 3A"
        ),
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Alyavi Saidnairxon Farxadovich",
        "Mutaxassislik": "Dermatolog, Venereolog",
        "Manzil": "Doctor D, Usta Olim ko`chasi, 15 uy",
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Abdullaxo'jayev Kamolliddin Abdurahmonovich",
        "Mutaxassislik": "Dermatolog, Dermatovenereolog",
        "Manzil": (
            "O'zbekiston dermatovenerologiya va kosmetologiya markazi / Doktor"
            " Servis, Farobiy ko'chasi, 3A"
        ),
        "Reyting": "⭐⭐⭐⭐⭐ (5.0)",
    },
    {
        "Ism": "Shoxraxmetov Shoraxmat Shorasulovich",
        "Mutaxassislik": "Dermatolog, Trixolog",
        "Manzil": (
            "Medion Clinic 24-7 / Medion Aesthetic and SPA / Nano Hair Clinic,"
            " Zulfiyaxanum ko`chasi, 18"
        ),
        "Reyting": "⭐⭐⭐⭐⭐ (5.0)",
    },
    {
        "Ism": "Ortiqov Aziz Farruhjonovich",
        "Mutaxassislik": "Dermatolog, Dermatovenereolog",
        "Manzil": (
            "Expert Medical Clinic - Pro Surgery, Yunusobod tumani, kichik"
            " aylana yo'li, 11A"
        ),
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Askarov Dilshod Alisherovich",
        "Mutaxassislik": "Dermatolog, Dermatovenereolog, Trixolog",
        "Manzil": "B2B Beautyclinic, Bunyodkor prospekti, 8E",
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Toshmatova Odila Dilshodovna",
        "Mutaxassislik": "Dermatolog, Trixolog, Kosmetolog",
        "Manzil": (
            "O'zbekiston dermatovenerologiya va kosmetologiya markazi, Farobiy"
            " ko'chasi, 3A"
        ),
        "Reyting": "⭐⭐⭐⭐⭐ (5.0)",
    },
    {
        "Ism": "Raximova Zulayxo Tulkinovna",
        "Mutaxassislik": "Dermatolog, Kosmetolog, Venereolog",
        "Manzil": "M-Clinic, Tantan ko'chasi, 1-uy",
        "Reyting": "⭐⭐⭐⭐⭐ (4.8)",
    },
    {
        "Ism": "Urunbayev Nugman Suratovich",
        "Mutaxassislik": "Dermatolog, Dermatovenereolog",
        "Manzil": "MDS Servis, Botkin ko`chasi, 110/3",
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Abdullayev Umid Ubaydullayevich",
        "Mutaxassislik": "Dermatolog, Oftalmolog",
        "Manzil": "Shox Med Center / Darmon Servis / NIKAMED, Oybek ko`chasi 34",
        "Reyting": "⭐⭐⭐⭐⭐ (5.0)",
    },
    {
        "Ism": "Rahmatullayeva Sevara Nodirbekovna",
        "Mutaxassislik": "Dermatolog, Dermatovenereolog",
        "Manzil": (
            "O'zbekiston dermatovenerologiya va kosmetologiya markazi, Farobiy"
            " ko'chasi, 3A"
        ),
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Sodiqova Shohida Farxadovna",
        "Mutaxassislik": "Dermatolog, Kosmetolog, Dermatovenereolog",
        "Manzil": (
            "Medion Aesthetic and SPA / Medion Clinic 24-7, Zulfiyaxonim"
            " ko'chasi, 18"
        ),
        "Reyting": "⭐⭐⭐⭐⭐ (5.0)",
    },
    {
        "Ism": "Babaqulova Gulnora Sabirjanovna",
        "Mutaxassislik": "Dermatolog, Kosmetolog",
        "Manzil": (
            "O'zbekiston dermatovenerologiya va kosmetologiya markazi, Farobiy"
            " ko'chasi, 3A"
        ),
        "Reyting": "⭐⭐⭐⭐⭐ (4.8)",
    },
    {
        "Ism": "Eshyozova Dilfuza Yakubbayevna",
        "Mutaxassislik": "Dermatolog, Kosmetolog, LOR (Otolaringolog)",
        "Manzil": "Mevazor Med, Keles Yo`li ko`chasi, 156",
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Inogamova Malika Abdulxalilovna",
        "Mutaxassislik": "Dermatolog",
        "Manzil": (
            "Kamola Diagnostic Medecine, Olmazor tumani, Birlik ko‘chasi, 2-uy"
        ),
        "Reyting": "⭐⭐⭐⭐⭐ (4.8)",
    },
    {
        "Ism": "Osarov Tolkin Kurbanovich",
        "Mutaxassislik": "Dermatolog, Dermatovenereolog",
        "Manzil": "Global Medical Center, Yangi Sergeli ko`chasi, 35",
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Myasnik Vladimir Borisovich",
        "Mutaxassislik": "Kardiolog",
        "Manzil": "MDS Servis, Botkin ko`chasi, 110/3",
        "Reyting": "⭐⭐⭐⭐⭐ (5.0)",
    },
    {
        "Ism": "Zhuravleva Yuliya Yuriyevna",
        "Mutaxassislik": "Kardiolog, Terapevt",
        "Manzil": "De Factum Central, Osiyo ko'ch. 86A",
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Jepparova Liliya Enverovna",
        "Mutaxassislik": "Kardiolog, Terapevt",
        "Manzil": "De Factum Central, Osiyo ko'ch. 86A",
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Shermatov Gayrat Ermamatovich",
        "Mutaxassislik": "Kardiolog",
        "Manzil": "Doctor D, Usta Olim ko`chasi, 15 uy",
        "Reyting": "⭐⭐⭐⭐⭐ (5.0)",
    },
    {
        "Ism": "Axmedov Gafur Saparbayevich",
        "Mutaxassislik": "Kardiolog, Terapevt",
        "Manzil": "Medion Clinic 24-7 / Humo Med Center, Zulfiyaxanum ko`chasi, 18",
        "Reyting": "⭐⭐⭐⭐⭐ (5.0)",
    },
    {
        "Ism": "Bakieva Malika Alimovna",
        "Mutaxassislik": "Kardiolog, Terapevt",
        "Manzil": "Medion Family Hospital, Istiroxat ko'ch., 258",
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Pardayev Bobur Baxtiyorovich",
        "Mutaxassislik": "Kardiolog",
        "Manzil": "IP Clinic / New Medical Service, Yassi ko'chasi, 38-uy",
        "Reyting": "⭐⭐⭐⭐⭐ (4.8)",
    },
    {
        "Ism": "Shomatova Nilufar Minavarovna",
        "Mutaxassislik": "Kardiolog, Terapevt",
        "Manzil": "Shox Med Center, Oybek ko`chasi 34",
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Qayumova Risolat Ro'ziqulovna",
        "Mutaxassislik": "Kardiolog, Terapevt",
        "Manzil": "Shox Med Center, Oybek ko`chasi 34",
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Qodirov Behzod Baxramovich",
        "Mutaxassislik": "Kardiolog, Reanimatolog",
        "Manzil": "Yurak Markazi, Yangi Qo'yliq, 1B",
        "Reyting": "⭐⭐⭐⭐⭐ (5.0)",
    },
    {
        "Ism": "Salaxitdinov Shuxrat Najmiddinovich",
        "Mutaxassislik": "Kardiolog",
        "Manzil": "M-Clinic, Tantan ko'chasi, 1-uy",
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Aminov Abduazim Abdullaevich",
        "Mutaxassislik": "Kardiolog",
        "Manzil": (
            "Expert Medical Clinic - Pro Surgery, Yunusobod tumani, kichik"
            " aylana yo'li, 11A"
        ),
        "Reyting": "⭐⭐⭐⭐⭐ (4.8)",
    },
    {
        "Ism": "Ibragimov Muxiddin Nuriddinovich",
        "Mutaxassislik": "Kardiolog",
        "Manzil": "M-Clinic, Tantan ko'chasi, 1-uy",
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Adilova Ikbol Gafuritdinovna",
        "Mutaxassislik": "Kardiolog",
        "Manzil": (
            "Medion Innovation / Respublika ixtisoslashtirilgan kardiologiya"
            " markazi, Abdulla Qodiriy ko'chasi, 39"
        ),
        "Reyting": "⭐⭐⭐⭐⭐ (5.0)",
    },
    {
        "Ism": "Arnopolskaya Dina Iosifovna",
        "Mutaxassislik": "Kardiolog, Revmatolog, Terapevt",
        "Manzil": (
            "De Factum Megapolis / De Factum Central, Yunusobod massivi, 13"
            " kv-l, 1A"
        ),
        "Reyting": "⭐⭐⭐⭐⭐ (5.0)",
    },
    {
        "Ism": "Xalilova Dilfuza Abduraxmanovna",
        "Mutaxassislik": "Kardiolog, Terapevt",
        "Manzil": "ARK HOSPITAL, Farobi ko'cha, 323",
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Kazantseva Natalya Vladimirovna",
        "Mutaxassislik": "Kardiolog, Terapevt",
        "Manzil": "Medion Clinic 24-7, Zulfiyaxanum ko`chasi, 18",
        "Reyting": "⭐⭐⭐⭐⭐ (5.0)",
    },
    {
        "Ism": "Kim Sergey Vitalievich",
        "Mutaxassislik": "Kardiolog",
        "Manzil": (
            "Medion Family Hospital / Sinomed MD International Hospital,"
            " Istiroxat ko'ch., 258"
        ),
        "Reyting": "⭐⭐⭐⭐⭐ (5.0)",
    },
    {
        "Ism": "Mirxodjaeva Ibodat Ismoilovna",
        "Mutaxassislik": "Kardiolog, Revmatolog",
        "Manzil": "De Factum Kids, Avliyo-Ota ko`chasi, 1-2",
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Xalmuratov Mansur Komiljonovich",
        "Mutaxassislik": "Kardiolog, Terapevt",
        "Manzil": "Medion Clinic 24-7 / Samo Medical 24-7, Zulfiyaxanum ko`chasi, 18",
        "Reyting": "⭐⭐⭐⭐⭐ (5.0)",
    },
    {
        "Ism": "Bo'rixodjaeva Gulnora Xulkarovna",
        "Mutaxassislik": "Ginekolog, Akusher",
        "Manzil": "MDS Servis, Botkin ko`chasi, 110/3",
        "Reyting": "⭐⭐⭐⭐⭐ (5.0)",
    },
    {
        "Ism": "Shamsiddinova Nargiza Alixanovna",
        "Mutaxassislik": "Ginekolog",
        "Manzil": "Medion Clinic 24-7, Zulfiyaxanum ko`chasi, 18",
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Abdusamatova Lola Boltaevna",
        "Mutaxassislik": "Ginekolog, Akusher, Reproduktolog",
        "Manzil": "B2B Beautyclinic, Bunyodkor prospekti, 8E",
        "Reyting": "⭐⭐⭐⭐⭐ (5.0)",
    },
    {
        "Ism": "Shaxmurova Bella Nikolaevna",
        "Mutaxassislik": "Ginekolog, Akusher",
        "Manzil": "De Factum Central, Osiyo ko'ch. 86A",
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Karimova Zilola Maksimovna",
        "Mutaxassislik": "Ginekolog",
        "Manzil": "Shox Med Center, Oybek ko`chasi 34",
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Abdumalikova Shohida Mirzaevna",
        "Mutaxassislik": "Ginekolog",
        "Manzil": (
            "De Factum Megapolis / Akusherlik va ginekologiya ilmiy-tadqiqot"
            " instituti, Yunusobod massivi, 13 kv-l, 1A"
        ),
        "Reyting": "⭐⭐⭐⭐⭐ (5.0)",
    },
    {
        "Ism": "Raxmatova Nilufar Boboyorovna",
        "Mutaxassislik": "Ginekolog, Endokrinolog",
        "Manzil": "LA TIVA Birth Home, Istiroxat ko'chasi, 258",
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Almuxamedova Barno Gulmuhamadovna",
        "Mutaxassislik": "Ginekolog, Onkolog",
        "Manzil": (
            "M-Clinic / Respublika ixtisoslashtirilgan onkologiya va radiologiya"
            " markazi, Tantan ko'chasi, 1-uy"
        ),
        "Reyting": "⭐⭐⭐⭐⭐ (5.0)",
    },
    {
        "Ism": "Mirzaxmedova Nargiza Alisultanova",
        "Mutaxassislik": "Ginekolog, Reproduktolog",
        "Manzil": "Doctor D, Usta Olim ko`chasi, 15 uy",
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Israilova Zamira Shuxratovna",
        "Mutaxassislik": "Ginekolog, Akusher",
        "Manzil": (
            "O'zbekiston dermatovenerologiya va kosmetologiya markazi / MirMed"
            " Clinic, Farobiy ko'chasi, 3A"
        ),
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Zohidova Nargis Ravshanovna",
        "Mutaxassislik": "Ginekolog, Akusher",
        "Manzil": "De Factum Central / Ayol Care, Osiyo ko'ch. 86A",
        "Reyting": "⭐⭐⭐⭐⭐ (5.0)",
    },
    {
        "Ism": "Kadirova Nigora Tursunpolatovna",
        "Mutaxassislik": "Ginekolog, Akusher",
        "Manzil": "Dusel Medical, To‘kimachi ko‘chasi, 3-uy",
        "Reyting": "⭐⭐⭐⭐⭐ (4.8)",
    },
    {
        "Ism": "Popov Aleksandr Anatolievich",
        "Mutaxassislik": "Ginekolog, Jarroh, Onkolog",
        "Manzil": "Medion Family Hospital, Istiroxat ko'ch., 258",
        "Reyting": "⭐⭐⭐⭐⭐ (5.0)",
    },
    {
        "Ism": "Romanova Yekaterina Gennadevna",
        "Mutaxassislik": "Ginekolog",
        "Manzil": "De Factum Kids, Avliyo-Ota ko`chasi, 1-2",
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Fayzliyeva Kamola G'aybiddinovna",
        "Mutaxassislik": "Ginekolog, Akusher",
        "Manzil": (
            "Expert Medical Clinic - Pro Surgery, Yunusobod tumani, kichik"
            " aylana yo'li, 11A"
        ),
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Luchenko Lia Raufovna",
        "Mutaxassislik": "Ginekolog, Akusher",
        "Manzil": "De Factum Central, Osiyo ko'ch. 86A",
        "Reyting": "⭐⭐⭐⭐⭐ (5.0)",
    },
    {
        "Ism": "Fozilbekov Ro'ziqul Anarkulovich",
        "Mutaxassislik": "Ginekolog",
        "Manzil": "M-Clinic / AKFA Medline, Tantan ko'chasi, 1-uy",
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Sabirzyanova Liliya Gayratovna",
        "Mutaxassislik": "Ginekolog",
        "Manzil": "Medion Clinic 24-7, Zulfiyaxanum ko`chasi, 18",
        "Reyting": "⭐⭐⭐⭐⭐ (4.9)",
    },
    {
        "Ism": "Buribekova Dildora Shuhratovna",
        "Mutaxassislik": "Ginekolog",
        "Manzil": "ARK HOSPITAL, Farobi ko'cha, 323",
        "Reyting": "⭐⭐⭐⭐⭐ (4.8)",
    },
    {
        "Ism": "Buynova Viktoriya Anatolievna",
        "Mutaxassislik": "Ginekolog, Akusher, Ultratovush mutaxassisi",
        "Manzil": "LA TIVA Birth Home, Istiroxat ko'chasi, 258",
        "Reyting": "⭐⭐⭐⭐⭐ (5.0)",
    },
]

# Savatni xotirada saqlash
if "cart" not in st.session_state:
  st.session_state.cart = []

# ----------------- YON PANEL (SIDEBAR) -----------------
st.sidebar.title("🩺 Tabib AI")
lang = st.sidebar.selectbox("Til / Language", ["O'zbekcha", "Русский"])

if lang == "O'zbekcha":
  menu_options = [
      "Bosh sahifa",
      "AI Maslahatchi",
      "Shifokorlar",
      "Dorixona",
      f"Savat ({len(st.session_state.cart)})",
  ]
  search_placeholder = "🔍 Shifokor ismi yoki mutaxassisligi..."
  book_btn_text = "Qabulga yozilish"
else:
  menu_options = [
      "Главная",
      "AI Консультант",
      "Врачи",
      "Аптека",
      f"Корзина ({len(st.session_state.cart)})",
  ]
  search_placeholder = "🔍 Поиск врача или специальности..."
  book_btn_text = "Записаться"

choice = st.sidebar.radio("Navigatsiya", menu_options)

# ----------------- 1. BOSH SAHIFA -----------------
if choice in ["Bosh sahifa", "Главная"]:
  st.markdown(
      """
        <div class="main-header">
            <h1>🩺 Tabib AI Tibbiy Platformasiga Xush Kelibsiz!</h1>
            <p>Malakali shifokorlarni toping, onlayn qabulga yoziling va sun'iy intellekt yordamida tezkor tibbiy maslahat oling.</p>
        </div>
        """,
      unsafe_allow_html=True,
  )

  col1, col2, col3 = st.columns(3)
  with col1:
    st.info("👨‍⚕️ **70+ Mutaxassislar**\n\nShahrimizning eng sara shifokorlari.")
  with col2:
    st.success(
        "🤖 **AI Yordamchi**\n\nTibbiy savollaringizga sun'iy intellekt"
        " javoblari."
    )
  with col3:
    st.warning("⚡ **Qulay Navbat**\n\nTezkor va oson qabulga yozilish tizimi.")

# ----------------- 2. AI MASLAHATCHI -----------------
elif choice in ["AI Maslahatchi", "AI Консультант"]:
  st.title("🤖 Tabib AI — Sun'iy Intellekt Maslahatchisi")
  st.write(
      "Sizni bezovta qilayotgan alomatlar yoki tibbiy savollaringizni yozib"
      " qoldiring:"
  )

  query = st.text_area(
      "Savol yoki simptomlar:",
      placeholder="Masalan: Bosh og'rig'i va holsizlik nima sababdan bo'lishi"
      " mumkin?",
  )
  if st.button("Javob olish", type="primary"):
    if query:
      st.success(
          "💡 **AI Tahlili:** Bergan ma'lumotlaringizga ko'ra, umumiy terapevt"
          " yoki mutaxassis shifokor ko'rigidan o'tishingiz tavsiya etiladi."
          " Iltimos, o'z vaqtida shifokorga murojaat qiling!"
      )
    else:
      st.warning("Iltimos, avval savolingizni yozing.")

# ----------------- 3. SHIFOKORLAR -----------------
elif choice in ["Shifokorlar", "Врачи"]:
  st.title("👨‍⚕️ Malakali Shifokorlar Bazasi")
  st.write(f"Jami shifokorlar soni: **{len(doctors_list)} nafar**")

  search_query = st.text_input("", placeholder=search_placeholder, label_visibility="collapsed")

  # Filtrlash
  filtered = [
      d
      for d in doctors_list
      if search_query.lower() in d["Ism"].lower()
      or search_query.lower() in d["Mutaxassislik"].lower()
  ]

  if filtered:
    cols = st.columns(2)
    for idx, doc in enumerate(filtered):
      with cols[idx % 2]:
        st.markdown(
            f"""
                <div class="doctor-card">
                    <div class="doc-name">{doc['Ism']}</div>
                    <div class="doc-spec">{doc['Mutaxassislik']}</div>
                    <div class="doc-address">📍 {doc['Manzil']}</div>
                    <div class="doc-rating">{doc['Reyting']}</div>
                </div>
                """,
            unsafe_allow_html=True,
        )
        if st.button(book_btn_text, key=f"b_{idx}"):
          st.success(f"✅ {doc['Ism']} qabuliga yozilish uchun so'rov ketdi!")
  else:
    st.warning("Hech qanday shifokor topilmadi.")

# ----------------- 4. DORIXONA -----------------
elif choice in ["Dorixona", "Аптека"]:
  st.title("💊 Dorixona Bo'limi")
  st.info("Dorilar va tibbiy buyumlar katalogi tez kunda ishga tushadi.")

# ----------------- 5. SAVAT -----------------
elif choice.startswith("Savat") or choice.startswith("Корзина"):
  st.title("🛒 Buyurtmalar Savatchasi")
  if st.session_state.cart:
    for i, item in enumerate(st.session_state.cart):
      st.write(f"{i+1}. {item}")
  else:
    st.info("Savatingiz hozircha bo'sh.")
