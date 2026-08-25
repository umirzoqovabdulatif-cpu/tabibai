import streamlit as st

# Sahifa sozlamalari
st.set_page_config(
    page_title="Tabib AI — Tibbiy Platforma", page_icon="🩺", layout="wide"
)

# ----------------- DIZAYN VA USLUBLAR (CSS) -----------------
st.markdown(
    """
    <style>
    /* Asosiy fon va shrift */
    .stApp {
        background-color: #f8fafc;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Chiroyli sarlavha bloki */
    .hero-banner {
        background: linear-gradient(135deg, #0ea5e9 0%, #2563eb 100%);
        padding: 30px;
        border-radius: 16px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 10px 25px -5px rgba(37, 99, 235, 0.3);
    }
    .hero-title {
        font-size: 28px;
        font-weight: 800;
        margin-bottom: 10px;
    }
    .hero-subtitle {
        font-size: 15px;
        opacity: 0.9;
    }

    /* Shifokor kartochkasi dizayni */
    .doctor-card {
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 22px;
        margin-bottom: 20px;
        background-color: #ffffff;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
    }
    .doctor-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 20px -3px rgba(0, 0, 0, 0.1);
        border-color: #93c5fd;
    }
    .doctor-name {
        font-size: 18px;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 6px;
    }
    .doctor-spec {
        color: #2563eb;
        font-weight: 600;
        font-size: 14px;
        margin-bottom: 10px;
        background: #eff6ff;
        padding: 4px 10px;
        border-radius: 6px;
        display: inline-block;
    }
    .doctor-address {
        color: #475569;
        font-size: 13px;
        margin-bottom: 10px;
    }
    .doctor-rating {
        color: #f59e0b;
        font-size: 14px;
        font-weight: 600;
    }
    
    /* Tugmalar dizayni */
    .stButton>button {
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.2s;
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
        "Reyting": "⭐ 5.0 (24 ta sharh)",
    },
    {
        "Ism": "Dr. Tursunova Dilorom Sabitovna",
        "Mutaxassislik": (
            "Allergolog, Pulmonolog, Immunolog, Terapevt"
        ),
        "Manzil": "Medion Clinic 24-7, Zulfiyaxanum ko`chasi, 18",
        "Reyting": "⭐ 5.0 (42 ta sharh)",
    },
    {
        "Ism": "Dr. Qurbonova Guncha Amangeldievna",
        "Mutaxassislik": "Allergolog, Fizioterapevt, Pulmonolog",
        "Manzil": "M-Clinic, Tantan ko'chasi, 1-uy",
        "Reyting": "⭐ 4.9 (19 ta sharh)",
    },
    {
        "Ism": "Dr. Rumi Linara Rinatovna",
        "Mutaxassislik": "Allergolog",
        "Manzil": "International Allergy Center, Osiyo ko`chasi, 86А",
        "Reyting": "⭐ 4.9 (31 ta sharh)",
    },
    {
        "Ism": "Dr. Abdurahmonov Abdulla Abdukaharovich",
        "Mutaxassislik": "Allergolog, Pulmonolog, Pediatr, Terapevt",
        "Manzil": "Medion Family Hospital, Istiroxat ko'ch., 258",
        "Reyting": "⭐ 5.0 (56 ta sharh)",
    },
    {
        "Ism": "Dr. Rahmonova Shoira Po'latovna",
        "Mutaxassislik": "Allergolog, Nevropatolog",
        "Manzil": "Dusel Medical, To‘kimachi ko‘chasi, 3-uy",
        "Reyting": "⭐ 4.8 (15 ta sharh)",
    },
    {
        "Ism": "Dr. Tkachuk Viktoriya Aleksandrovna",
        "Mutaxassislik": "Allergolog",
        "Manzil": "International Allergy Center / EBM Clinic, Osiyo ko`chasi, 86А",
        "Reyting": "⭐ 5.0 (28 ta sharh)",
    },
    {
        "Ism": "Dr. Saipova Nodira Sagdullayevna",
        "Mutaxassislik": "Allergolog, Dermatolog, Podolog, Kosmetolog",
        "Manzil": "OpenLab tibbiyot markazi, Avliyo ota ko'chasi, 9",
        "Reyting": "⭐ 4.9 (37 ta sharh)",
    },
    {
        "Ism": "Dr. Ismoilova Dilfuza Mirsabitovna",
        "Mutaxassislik": "Allergolog, Pulmonolog, Terapevt",
        "Manzil": "Medion Clinic 24-7, Zulfiyaxanum ko`chasi, 18",
        "Reyting": "⭐ 5.0 (45 ta sharh)",
    },
    {
        "Ism": "Dr. Pulatova Iroda Alijonovna",
        "Mutaxassislik": "Allergolog",
        "Manzil": "M-Clinic, Tantan ko'chasi, 1-uy",
        "Reyting": "⭐ 4.8 (21 ta sharh)",
    },
    {
        "Ism": "Dr. Malikova Alfira Railovna",
        "Mutaxassislik": (
            "Allergolog, Kardiolog, Gastroenterolog, Pulmonolog"
        ),
        "Manzil": "Shams Medical Center, Tallimarjon ko`chasi, 43",
        "Reyting": "⭐ 5.0 (60 ta sharh)",
    },
    {
        "Ism": "Dr. Jurayeva Maftuna Kuvandikovna",
        "Mutaxassislik": "Allergolog",
        "Manzil": "International Allergy Center, Osiyo ko`chasi, 86А",
        "Reyting": "⭐ 4.9 (18 ta sharh)",
    },
    {
        "Ism": "Dr. Miraxmedova Gulnora Turgunovna",
        "Mutaxassislik": "Allergolog, Dermatolog, Pulmonolog",
        "Manzil": "Saba Darmon, Bogkucha ko`chasi, 17A",
        "Reyting": "⭐ 4.9 (29 ta sharh)",
    },
    {
        "Ism": "Dr. Ochilov Sardor Ilxomovich",
        "Mutaxassislik": "Allergolog, Pulmonolog, Immunolog",
        "Manzil": "Shox Med Педиатрия, Xushnavo 4-chi o'tish joyi, 26/2",
        "Reyting": "⭐ 5.0 (33 ta sharh)",
    },
    {
        "Ism": "Dr. Ubaydullaeva Naima Nabixanovna",
        "Mutaxassislik": "Allergolog, Pulmonolog",
        "Manzil": (
            "International Allergy Center / Shahar klinik kasalxonasi №1,"
            " Osiyo ko`chasi, 86А"
        ),
        "Reyting": "⭐ 4.9 (22 ta sharh)",
    },
    {
        "Ism": "Dr. Xudoyqulova Nodira Ulug'bekovna",
        "Mutaxassislik": "Allergolog, Pulmonolog, Terapevt",
        "Manzil": "Darmon Servis, Cho'pon Ota ko`chasi, 18/19",
        "Reyting": "⭐ 4.8 (27 ta sharh)",
    },
    {
        "Ism": "Dr. Ortikxodjayeva Durdona Anvarovna",
        "Mutaxassislik": "Allergolog, Pediatr, Immunolog",
        "Manzil": "Darmon Servis, Cho'pon Ota ko`chasi, 18/19",
        "Reyting": "⭐ 5.0 (39 ta sharh)",
    },
    {
        "Ism": "Dr. Alieva Vasila Shukurullaevna",
        "Mutaxassislik": "Allergolog",
        "Manzil": "Medilux Medical center, Farobiy ko`chasi, 3-B",
        "Reyting": "⭐ 4.9 (16 ta sharh)",
    },
    {
        "Ism": "Dr. Djurayev Abduvaxid Raxmankulovich",
        "Mutaxassislik": "Allergolog, Pulmonolog",
        "Manzil": "Sinomed MD / Darmon Servis, Taxtapul ko`chasi, 341a",
        "Reyting": "⭐ 4.9 (24 ta sharh)",
    },
    {
        "Ism": "Dr. Abdug'aniyev Saidazimxon Usmonxujayevich",
        "Mutaxassislik": "Allergolog, Immunolog, Pulmonolog",
        "Manzil": "Kimyo University Hospital, Bunyodkor ko`ch. Yakkabog` MFY, 19",
        "Reyting": "⭐ 5.0 (51 ta sharh)",
    },
    {
        "Ism": "Fattaxov Bobir Shavkatovich",
        "Mutaxassislik": "Dermatolog, Dermatovenereolog",
        "Manzil": (
            "O'zbekiston dermatovenerologiya va kosmetologiya markazi, Farobiy"
            " ko'chasi, 3A"
        ),
        "Reyting": "⭐ 5.0 (88 ta sharh)",
    },
    {
        "Ism": "Xaldarbekov Madamin Karimjanovich",
        "Mutaxassislik": "Dermatolog, Dermatovenereolog",
        "Manzil": (
            "O'zbekiston dermatovenerologiya va kosmetologiya markazi, Farobiy"
            " ko'chasi, 3A"
        ),
        "Reyting": "⭐ 4.9 (45 ta sharh)",
    },
    {
        "Ism": "Zakirov Rustam Ruxullaevich",
        "Mutaxassislik": "Dermatolog, Dermatovenereolog",
        "Manzil": (
            "Medion Aesthetic and SPA / Medion Clinic 24-7, Zulfiyaxonim ko'chasi,"
            " 18"
        ),
        "Reyting": "⭐ 5.0 (64 ta sharh)",
    },
    {
        "Ism": "Jamolov Davron Nematovich",
        "Mutaxassislik": "Dermatolog",
        "Manzil": "Shox Med Center, Oybek ko`chasi 34",
        "Reyting": "⭐ 4.8 (30 ta sharh)",
    },
    {
        "Ism": "Rasulova Nazira Anvarovna",
        "Mutaxassislik": "Dermatolog",
        "Manzil": (
            "O'zbekiston dermatovenerologiya va kosmetologiya markazi, Farobiy"
            " ko'chasi, 3A"
        ),
        "Reyting": "⭐ 4.9 (41 ta sharh)",
    },
    {
        "Ism": "Alyavi Saidnairxon Farxadovich",
        "Mutaxassislik": "Dermatolog, Venereolog",
        "Manzil": "Doctor D, Usta Olim ko`chasi, 15 uy",
        "Reyting": "⭐ 4.9 (35 ta sharh)",
    },
    {
        "Ism": "Abdullaxo'jayev Kamolliddin Abdurahmonovich",
        "Mutaxassislik": "Dermatolog, Dermatovenereolog",
        "Manzil": (
            "O'zbekiston dermatovenerologiya va kosmetologiya markazi / Doktor"
            " Servis, Farobiy ko'chasi, 3A"
        ),
        "Reyting": "⭐ 5.0 (72 ta sharh)",
    },
    {
        "Ism": "Shoxraxmetov Shoraxmat Shorasulovich",
        "Mutaxassislik": "Dermatolog, Trixolog",
        "Manzil": (
            "Medion Clinic 24-7 / Medion Aesthetic and SPA / Nano Hair Clinic,"
            " Zulfiyaxanum ko`chasi, 18"
        ),
        "Reyting": "⭐ 5.0 (95 ta sharh)",
    },
    {
        "Ism": "Ortiqov Aziz Farruhjonovich",
        "Mutaxassislik": "Dermatolog, Dermatovenereolog",
        "Manzil": (
            "Expert Medical Clinic - Pro Surgery, Yunusobod tumani, kichik"
            " aylana yo'li, 11A"
        ),
        "Reyting": "⭐ 4.9 (38 ta sharh)",
    },
    {
        "Ism": "Askarov Dilshod Alisherovich",
        "Mutaxassislik": "Dermatolog, Dermatovenereolog, Trixolog",
        "Manzil": "B2B Beautyclinic, Bunyodkor prospekti, 8E",
        "Reyting": "⭐ 4.9 (44 ta sharh)",
    },
    {
        "Ism": "Toshmatova Odila Dilshodovna",
        "Mutaxassislik": "Dermatolog, Trixolog, Kosmetolog",
        "Manzil": (
            "O'zbekiston dermatovenerologiya va kosmetologiya markazi, Farobiy"
            " ko'chasi, 3A"
        ),
        "Reyting": "⭐ 5.0 (58 ta sharh)",
    },
    {
        "Ism": "Raximova Zulayxo Tulkinovna",
        "Mutaxassislik": "Dermatolog, Kosmetolog, Venereolog",
        "Manzil": "M-Clinic, Tantan ko'chasi, 1-uy",
        "Reyting": "⭐ 4.8 (26 ta sharh)",
    },
    {
        "Ism": "Urunbayev Nugman Suratovich",
        "Mutaxassislik": "Dermatolog, Dermatovenereolog",
        "Manzil": "MDS Servis, Botkin ko`chasi, 110/3",
        "Reyting": "⭐ 4.9 (33 ta sharh)",
    },
    {
        "Ism": "Abdullayev Umid Ubaydullayevich",
        "Mutaxassislik": "Dermatolog, Oftalmolog",
        "Manzil": "Shox Med Center / Darmon Servis / NIKAMED, Oybek ko`chasi 34",
        "Reyting": "⭐ 5.0 (80 ta sharh)",
    },
    {
        "Ism": "Rahmatullayeva Sevara Nodirbekovna",
        "Mutaxassislik": "Dermatolog, Dermatovenereolog",
        "Manzil": (
            "O'zbekiston dermatovenerologiya va kosmetologiya markazi, Farobiy"
            " ko'chasi, 3A"
        ),
        "Reyting": "⭐ 4.9 (29 ta sharh)",
    },
    {
        "Ism": "Sodiqova Shohida Farxadovna",
        "Mutaxassislik": "Dermatolog, Kosmetolog, Dermatovenereolog",
        "Manzil": (
            "Medion Aesthetic and SPA / Medion Clinic 24-7, Zulfiyaxonim"
            " ko'chasi, 18"
        ),
        "Reyting": "⭐ 5.0 (67 ta sharh)",
    },
    {
        "Ism": "Babaqulova Gulnora Sabirjanovna",
        "Mutaxassislik": "Dermatolog, Kosmetolog",
        "Manzil": (
            "O'zbekiston dermatovenerologiya va kosmetologiya markazi, Farobiy"
            " ko'chasi, 3A"
        ),
        "Reyting": "⭐ 4.8 (34 ta sharh)",
    },
    {
        "Ism": "Eshyozova Dilfuza Yakubbayevna",
        "Mutaxassislik": "Dermatolog, Kosmetolog, LOR (Otolaringolog)",
        "Manzil": "Mevazor Med, Keles Yo`li ko`chasi, 156",
        "Reyting": "⭐ 4.9 (21 ta sharh)",
    },
    {
        "Ism": "Inogamova Malika Abdulxalilovna",
        "Mutaxassislik": "Dermatolog",
        "Manzil": (
            "Kamola Diagnostic Medecine, Olmazor tumani, Birlik ko‘chasi, 2-uy"
        ),
        "Reyting": "⭐ 4.8 (18 ta sharh)",
    },
    {
        "Ism": "Osarov Tolkin Kurbanovich",
        "Mutaxassislik": "Dermatolog, Dermatovenereolog",
        "Manzil": "Global Medical Center, Yangi Sergeli ko`chasi, 35",
        "Reyting": "⭐ 4.9 (40 ta sharh)",
    },
    {
        "Ism": "Myasnik Vladimir Borisovich",
        "Mutaxassislik": "Kardiolog",
        "Manzil": "MDS Servis, Botkin ko`chasi, 110/3",
        "Reyting": "⭐ 5.0 (92 ta sharh)",
    },
    {
        "Ism": "Zhuravleva Yuliya Yuriyevna",
        "Mutaxassislik": "Kardiolog, Terapevt",
        "Manzil": "De Factum Central, Osiyo ko'ch. 86A",
        "Reyting": "⭐ 4.9 (53 ta sharh)",
    },
    {
        "Ism": "Jepparova Liliya Enverovna",
        "Mutaxassislik": "Kardiolog, Terapevt",
        "Manzil": "De Factum Central, Osiyo ko'ch. 86A",
        "Reyting": "⭐ 4.9 (46 ta sharh)",
    },
    {
        "Ism": "Shermatov Gayrat Ermamatovich",
        "Mutaxassislik": "Kardiolog",
        "Manzil": "Doctor D, Usta Olim ko`chasi, 15 uy",
        "Reyting": "⭐ 5.0 (70 ta sharh)",
    },
    {
        "Ism": "Axmedov Gafur Saparbayevich",
        "Mutaxassislik": "Kardiolog, Terapevt",
        "Manzil": "Medion Clinic 24-7 / Humo Med Center, Zulfiyaxanum ko`chasi, 18",
        "Reyting": "⭐ 5.0 (85 ta sharh)",
    },
    {
        "Ism": "Bakieva Malika Alimovna",
        "Mutaxassislik": "Kardiolog, Terapevt",
        "Manzil": "Medion Family Hospital, Istiroxat ko'ch., 258",
        "Reyting": "⭐ 4.9 (39 ta sharh)",
    },
    {
        "Ism": "Pardayev Bobur Baxtiyorovich",
        "Mutaxassislik": "Kardiolog",
        "Manzil": "IP Clinic / New Medical Service, Yassi ko'chasi, 38-uy",
        "Reyting": "⭐ 4.8 (25 ta sharh)",
    },
    {
        "Ism": "Shomatova Nilufar Minavarovna",
        "Mutaxassislik": "Kardiolog, Terapevt",
        "Manzil": "Shox Med Center, Oybek ko`chasi 34",
        "Reyting": "⭐ 4.9 (61 ta sharh)",
    },
    {
        "Ism": "Qayumova Risolat Ro'ziqulovna",
        "Mutaxassislik": "Kardiolog, Terapevt",
        "Manzil": "Shox Med Center, Oybek ko`chasi 34",
        "Reyting": "⭐ 4.9 (48 ta sharh)",
    },
    {
        "Ism": "Qodirov Behzod Baxramovich",
        "Mutaxassislik": "Kardiolog, Reanimatolog",
        "Manzil": "Yurak Markazi, Yangi Qo'yliq, 1B",
        "Reyting": "⭐ 5.0 (110 ta sharh)",
    },
    {
        "Ism": "Salaxitdinov Shuxrat Najmiddinovich",
        "Mutaxassislik": "Kardiolog",
        "Manzil": "M-Clinic, Tantan ko'chasi, 1-uy",
        "Reyting": "⭐ 4.9 (55 ta sharh)",
    },
    {
        "Ism": "Aminov Abduazim Abdullaevich",
        "Mutaxassislik": "Kardiolog",
        "Manzil": (
            "Expert Medical Clinic - Pro Surgery, Yunusobod tumani, kichik"
            " aylana yo'li, 11A"
        ),
        "Reyting": "⭐ 4.8 (31 ta sharh)",
    },
    {
        "Ism": "Ibragimov Muxiddin Nuriddinovich",
        "Mutaxassislik": "Kardiolog",
        "Manzil": "M-Clinic, Tantan ko'chasi, 1-uy",
        "Reyting": "⭐ 4.9 (42 ta sharh)",
    },
    {
        "Ism": "Adilova Ikbol Gafuritdinovna",
        "Mutaxassislik": "Kardiolog",
        "Manzil": (
            "Medion Innovation / Respublika ixtisoslashtirilgan kardiologiya"
            " markazi, Abdulla Qodiriy ko'chasi, 39"
        ),
        "Reyting": "⭐ 5.0 (78 ta sharh)",
    },
    {
        "Ism": "Arnopolskaya Dina Iosifovna",
        "Mutaxassislik": "Kardiolog, Revmatolog, Terapevt",
        "Manzil": (
            "De Factum Megapolis / De Factum Central, Yunusobod massivi, 13"
            " kv-l, 1A"
        ),
        "Reyting": "⭐ 5.0 (99 ta sharh)",
    },
    {
        "Ism": "Xalilova Dilfuza Abduraxmanovna",
        "Mutaxassislik": "Kardiolog, Terapevt",
        "Manzil": "ARK HOSPITAL, Farobi ko'cha, 323",
        "Reyting": "⭐ 4.9 (36 ta sharh)",
    },
    {
        "Ism": "Kazantseva Natalya Vladimirovna",
        "Mutaxassislik": "Kardiolog, Terapevt",
        "Manzil": "Medion Clinic 24-7, Zulfiyaxanum ko`chasi, 18",
        "Reyting": "⭐ 5.0 (65 ta sharh)",
    },
    {
        "Ism": "Kim Sergey Vitalievich",
        "Mutaxassislik": "Kardiolog",
        "Manzil": (
            "Medion Family Hospital / Sinomed MD International Hospital,"
            " Istiroxat ko'ch., 258"
        ),
        "Reyting": "⭐ 5.0 (82 ta sharh)",
    },
    {
        "Ism": "Mirxodjaeva Ibodat Ismoilovna",
        "Mutaxassislik": "Kardiolog, Revmatolog",
        "Manzil": "De Factum Kids, Avliyo-Ota ko`chasi, 1-2",
        "Reyting": "⭐ 4.9 (41 ta sharh)",
    },
    {
        "Ism": "Xalmuratov Mansur Komiljonovich",
        "Mutaxassislik": "Kardiolog, Terapevt",
        "Manzil": "Medion Clinic 24-7 / Samo Medical 24-7, Zulfiyaxanum ko`chasi, 18",
        "Reyting": "⭐ 5.0 (73 ta sharh)",
    },
    {
        "Ism": "Bo'rixodjaeva Gulnora Xulkarovna",
        "Mutaxassislik": "Ginekolog, Akusher",
        "Manzil": "MDS Servis, Botkin ko`chasi, 110/3",
        "Reyting": "⭐ 5.0 (120 ta sharh)",
    },
    {
        "Ism": "Shamsiddinova Nargiza Alixanovna",
        "Mutaxassislik": "Ginekolog",
        "Manzil": "Medion Clinic 24-7, Zulfiyaxanum ko`chasi, 18",
        "Reyting": "⭐ 4.9 (85 ta sharh)",
    },
    {
        "Ism": "Abdusamatova Lola Boltaevna",
        "Mutaxassislik": "Ginekolog, Akusher, Reproduktolog",
        "Manzil": "B2B Beautyclinic, Bunyodkor prospekti, 8E",
        "Reyting": "⭐ 5.0 (104 ta sharh)",
    },
    {
        "Ism": "Shaxmurova Bella Nikolaevna",
        "Mutaxassislik": "Ginekolog, Akusher",
        "Manzil": "De Factum Central, Osiyo ko'ch. 86A",
        "Reyting": "⭐ 4.9 (63 ta sharh)",
    },
    {
        "Ism": "Karimova Zilola Maksimovna",
        "Mutaxassislik": "Ginekolog",
        "Manzil": "Shox Med Center, Oybek ko`chasi 34",
        "Reyting": "⭐ 4.9 (77 ta sharh)",
    },
    {
        "Ism": "Abdumalikova Shohida Mirzaevna",
        "Mutaxassislik": "Ginekolog",
        "Manzil": (
            "De Factum Megapolis / Akusherlik va ginekologiya ilmiy-tadqiqot"
            " instituti, Yunusobod massivi, 13 kv-l, 1A"
        ),
        "Reyting": "⭐ 5.0 (91 ta sharh)",
    },
    {
        "Ism": "Raxmatova Nilufar Boboyorovna",
        "Mutaxassislik": "Ginekolog, Endokrinolog",
        "Manzil": "LA TIVA Birth Home, Istiroxat ko'chasi, 258",
        "Reyting": "⭐ 4.9 (52 ta sharh)",
    },
    {
        "Ism": "Almuxamedova Barno Gulmuhamadovna",
        "Mutaxassislik": "Ginekolog, Onkolog",
        "Manzil": (
            "M-Clinic / Respublika ixtisoslashtirilgan onkologiya va radiologiya"
            " markazi, Tantan ko'chasi, 1-uy"
        ),
        "Reyting": "⭐ 5.0 (89 ta sharh)",
    },
    {
        "Ism": "Mirzaxmedova Nargiza Alisultanova",
        "Mutaxassislik": "Ginekolog, Reproduktolog",
        "Manzil": "Doctor D, Usta Olim ko`chasi, 15 uy",
        "Reyting": "⭐ 4.9 (68 ta sharh)",
    },
    {
        "Ism": "Israilova Zamira Shuxratovna",
        "Mutaxassislik": "Ginekolog, Akusher",
        "Manzil": (
            "O'zbekiston dermatovenerologiya va kosmetologiya markazi / MirMed"
            " Clinic, Farobiy ko'chasi, 3A"
        ),
        "Reyting": "⭐ 4.9 (49 ta sharh)",
    },
    {
        "Ism": "Zohidova Nargis Ravshanovna",
        "Mutaxassislik": "Ginekolog, Akusher",
        "Manzil": "De Factum Central / Ayol Care, Osiyo ko'ch. 86A",
        "Reyting": "⭐ 5.0 (74 ta sharh)",
    },
    {
        "Ism": "Kadirova Nigora Tursunpolatovna",
        "Mutaxassislik": "Ginekolog, Akusher",
        "Manzil": "Dusel Medical, To‘kimachi ko‘chasi, 3-uy",
        "Reyting": "⭐ 4.8 (43 ta sharh)",
    },
    {
        "Ism": "Popov Aleksandr Anatolievich",
        "Mutaxassislik": "Ginekolog, Jarroh, Onkolog",
        "Manzil": "Medion Family Hospital, Istiroxat ko'ch., 258",
        "Reyting": "⭐ 5.0 (115 ta sharh)",
    },
    {
        "Ism": "Romanova Yekaterina Gennadevna",
        "Mutaxassislik": "Ginekolog",
        "Manzil": "De Factum Kids, Avliyo-Ota ko`chasi, 1-2",
        "Reyting": "⭐ 4.9 (56 ta sharh)",
    },
    {
        "Ism": "Fayzliyeva Kamola G'aybiddinovna",
        "Mutaxassislik": "Ginekolog, Akusher",
        "Manzil": (
            "Expert Medical Clinic - Pro Surgery, Yunusobod tumani, kichik"
            " aylana yo'li, 11A"
        ),
        "Reyting": "⭐ 4.9 (62 ta sharh)",
    },
    {
        "Ism": "Luchenko Lia Raufovna",
        "Mutaxassislik": "Ginekolog, Akusher",
        "Manzil": "De Factum Central, Osiyo ko'ch. 86A",
        "Reyting": "⭐ 5.0 (83 ta sharh)",
    },
    {
        "Ism": "Fozilbekov Ro'ziqul Anarkulovich",
        "Mutaxassislik": "Ginekolog",
        "Manzil": "M-Clinic / AKFA Medline, Tantan ko'chasi, 1-uy",
        "Reyting": "⭐ 4.9 (71 ta sharh)",
    },
    {
        "Ism": "Sabirzyanova Liliya Gayratovna",
        "Mutaxassislik": "Ginekolog",
        "Manzil": "Medion Clinic 24-7, Zulfiyaxanum ko`chasi, 18",
        "Reyting": "⭐ 4.9 (59 ta sharh)",
    },
    {
        "Ism": "Buribekova Dildora Shuhratovna",
        "Mutaxassislik": "Ginekolog",
        "Manzil": "ARK HOSPITAL, Farobi ko'cha, 323",
        "Reyting": "⭐ 4.8 (38 ta sharh)",
    },
    {
        "Ism": "Buynova Viktoriya Anatolievna",
        "Mutaxassislik": "Ginekolog, Akusher, Ultratovush mutaxassisi",
        "Manzil": "LA TIVA Birth Home, Istiroxat ko'chasi, 258",
        "Reyting": "⭐ 5.0 (94 ta sharh)",
    },
]

# Savatni xotirada saqlash
if "cart" not in st.session_state:
  st.session_state.cart = []

# ----------------- YON PANEL (SIDEBAR) -----------------
st.sidebar.markdown("### 🩺 Tabib AI Menu")
lang = st.sidebar.selectbox("Language / Til", ["O'zbekcha", "Русский"])

if lang == "O'zbekcha":
  menu_options = [
      "Bosh sahifa",
      "AI Konsultatsiyasi",
      "Shifokorlar",
      "Dorixona",
      f"Savat ({len(st.session_state.cart)})",
  ]
  search_doc_text = (
      "🔍 Shifokor ismi yoki mutaxassisligi bo'yicha qidirish..."
  )
  book_btn = "Qabulga yozilish"
  ai_title = "Sun'iy Intellekt Maslahatchisi"
  ai_desc = (
      "Istalgan tibbiy savolingizni bering va sun'iy intellekt orqali tezkor"
      " tahlil oling."
  )
  ai_placeholder = "Masalan: Bosh og'rig'i nima sababdan bo'lishi mumkin?"
  ai_btn = "Javob olish"
else:
  menu_options = [
      "Главная",
      "AI Консультация",
      "Врачи",
      "Аптека",
      f"Корзина ({len(st.session_state.cart)})",
  ]
  search_doc_text = "🔍 Поиск врача по имени или специальности..."
  book_btn = "Записаться на прием"
  ai_title = "Консультант ИИ"
  ai_desc = "Задайте любой медицинский вопрос."
  ai_placeholder = "Например: Каковы причины головной боли?"
  ai_btn = "Получить ответ"

choice = st.sidebar.radio("Bo'limni tanlang", menu_options)

# ----------------- 1. BOSH SAHIFA -----------------
if choice in ["Bosh sahifa", "Главная"]:
  st.markdown(
      """
        <div class="hero-banner">
            <div class="hero-title">🩺 Tabib AI Platformasiga Xush Kelibsiz!</div>
            <div class="hero-subtitle">Malakali shifokorlarni toping, qabulga yoziling va sun'iy intellekt yordamida tezkor tibbiy maslahat oling.</div>
        </div>
        """,
      unsafe_allow_html=True,
  )

  col1, col2, col3 = st.columns(3)
  with col1:
    st.info("👨‍⚕️ **70+ Mutaxassislar**\n\nEng sara shifokorlar bazasi.")
  with col2:
    st.success(
        "🤖 **AI Tahlil**\n\nSun'iy intellekt orqali dastlabki tavsiyalar."
    )
  with col3:
    st.warning("⚡ **Tezkor yozilish**\n\nNavbatsiz va qulay qabulga yozilish.")

# ----------------- 2. AI KONSULTATSIYASI -----------------
elif choice in ["AI Konsultatsiyasi", "AI Консультация"]:
  st.markdown(f"### 🤖 {ai_title}")
  st.write(ai_desc)
  user_query = st.text_area("Savolingizni kiriting:", placeholder=ai_placeholder)
  if st.button(ai_btn, type="primary"):
    if user_query.strip():
      st.success(
          "💡 **Tabib AI tahlili:** Bergan savolingiz bo'yicha mutaxassis"
          " shifokor ko'rigidan o'tish tavsiya etiladi. Iltimos, o'z vaqtida"
          " shifokorga murojaat qiling."
      )
    else:
      st.warning("Iltimos, avval savolingizni yozing!")

# ----------------- 3. SHIFOKORLAR -----------------
elif choice in ["Shifokorlar", "Врачи"]:
  st.markdown("### 👨‍⚕️ Malakali Shifokorlar Bazasi")
  st.write(f"Jami mavjud shifokorlar: **{len(doctors_list)} nafar**")

  search_query = st.text_input("", placeholder=search_doc_text, label_visibility="collapsed")

  # Qidirish filtri
  filtered_doctors = [
      doc
      for doc in doctors_list
      if search_query.lower() in doc["Ism"].lower()
      or search_query.lower() in doc["Mutaxassislik"].lower()
  ]

  if filtered_doctors:
    cols = st.columns(2)
    for index, row in enumerate(filtered_doctors):
      with cols[index % 2]:
        st.markdown(
            f"""
                <div class="doctor-card">
                    <div class="doctor-name">{row['Ism']}</div>
                    <div class="doctor-spec">{row['Mutaxassislik']}</div>
                    <div class="doctor-address">📍 {row['Manzil']}</div>
                    <div class="doctor-rating">{row['Reyting']}</div>
                </div>
                """,
            unsafe_allow_html=True,
        )
        if st.button(book_btn, key=f"doc_{index}"):
          st.success(
              f"✅ {row['Ism']} qabuliga yozilish uchun so'rov muvaffaqiyatli"
              " yuborildi!"
          )
  else:
    st.warning("Qidiruv bo'yicha hech qanday shifokor topilmadi.")

# ----------------- 4. DORIXONA -----------------
elif choice in ["Dorixona", "Аптека"]:
  st.markdown("### 💊 Dorixona va Dori vositalari")
  st.info("Dorilar katalogi tez kunda ishga tushiriladi.")

# ----------------- 5. SAVAT -----------------
elif choice.startswith("Savat") or choice.startswith("Корзина"):
  st.markdown("### 🛒 Buyurtmalar Savatchasi")
  if st.session_state.cart:
    for i, item in enumerate(st.session_state.cart):
      st.write(f"{i+1}. {item}")
  else:
    st.info("Savatingiz hozircha bo'sh.")
