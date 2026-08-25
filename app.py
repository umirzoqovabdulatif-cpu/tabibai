import streamlit as st

# Sahifa sozlamalari
st.set_page_config(
    page_title="Tabib AI — Tibbiy Platforma", page_icon="🩺", layout="wide"
)

# ----------------- DIZAYN VA USLUBLAR (CSS) -----------------
st.markdown(
    """
    <style>
    .doctor-card {
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        background-color: #ffffff;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        transition: transform 0.2s ease;
    }
    .doctor-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
    }
    .doctor-name {
        font-size: 18px;
        font-weight: 700;
        color: #1a202c;
        margin-bottom: 5px;
    }
    .doctor-spec {
        color: #2b6cb0;
        font-weight: 600;
        font-size: 14px;
        margin-bottom: 10px;
    }
    .doctor-address {
        color: #4a5568;
        font-size: 13px;
        margin-bottom: 10px;
    }
    .doctor-rating {
        color: #d69e2e;
        font-size: 14px;
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
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Dr. Tursunova Dilorom Sabitovna",
        "Mutaxassislik": (
            "Allergolog, Pulmonolog, Immunolog, Terapevt"
        ),
        "Manzil": "Medion Clinic 24-7, Zulfiyaxanum ko`chasi, 18",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Dr. Qurbonova Guncha Amangeldievna",
        "Mutaxassislik": "Allergolog, Fizioterapevt, Pulmonolog",
        "Manzil": "M-Clinic, Tantan ko'chasi, 1-uy",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Dr. Rumi Linara Rinatovna",
        "Mutaxassislik": "Allergolog",
        "Manzil": "International Allergy Center, Osiyo ko`chasi, 86А",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Dr. Abdurahmonov Abdulla Abdukaharovich",
        "Mutaxassislik": "Allergolog, Pulmonolog, Pediatr, Terapevt",
        "Manzil": "Medion Family Hospital, Istiroxat ko'ch., 258",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Dr. Rahmonova Shoira Po'latovna",
        "Mutaxassislik": "Allergolog, Nevropatolog",
        "Manzil": "Dusel Medical, To‘kimachi ko‘chasi, 3-uy",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Dr. Tkachuk Viktoriya Aleksandrovna",
        "Mutaxassislik": "Allergolog",
        "Manzil": "International Allergy Center / EBM Clinic, Osiyo ko`chasi, 86А",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Dr. Saipova Nodira Sagdullayevna",
        "Mutaxassislik": "Allergolog, Dermatolog, Podolog, Kosmetolog",
        "Manzil": "OpenLab tibbiyot markazi, Avliyo ota ko'chasi, 9",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Dr. Ismoilova Dilfuza Mirsabitovna",
        "Mutaxassislik": "Allergolog, Pulmonolog, Terapevt",
        "Manzil": "Medion Clinic 24-7, Zulfiyaxanum ko`chasi, 18",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Dr. Pulatova Iroda Alijonovna",
        "Mutaxassislik": "Allergolog",
        "Manzil": "M-Clinic, Tantan ko'chasi, 1-uy",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Dr. Malikova Alfira Railovna",
        "Mutaxassislik": (
            "Allergolog, Kardiolog, Gastroenterolog, Pulmonolog"
        ),
        "Manzil": "Shams Medical Center, Tallimarjon ko`chasi, 43",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Dr. Jurayeva Maftuna Kuvandikovna",
        "Mutaxassislik": "Allergolog",
        "Manzil": "International Allergy Center, Osiyo ko`chasi, 86А",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Dr. Miraxmedova Gulnora Turgunovna",
        "Mutaxassislik": "Allergolog, Dermatolog, Pulmonolog",
        "Manzil": "Saba Darmon, Bogkucha ko`chasi, 17A",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Dr. Ochilov Sardor Ilxomovich",
        "Mutaxassislik": "Allergolog, Pulmonolog, Immunolog",
        "Manzil": "Shox Med Педиатрия, Xushnavo 4-chi o'tish joyi, 26/2",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Dr. Ubaydullaeva Naima Nabixanovna",
        "Mutaxassislik": "Allergolog, Pulmonolog",
        "Manzil": (
            "International Allergy Center / Shahar klinik kasalxonasi №1,"
            " Osiyo ko`chasi, 86А"
        ),
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Dr. Xudoyqulova Nodira Ulug'bekovna",
        "Mutaxassislik": "Allergolog, Pulmonolog, Terapevt",
        "Manzil": "Darmon Servis, Cho'pon Ota ko`chasi, 18/19",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Dr. Ortikxodjayeva Durdona Anvarovna",
        "Mutaxassislik": "Allergolog, Pediatr, Immunolog",
        "Manzil": "Darmon Servis, Cho'pon Ota ko`chasi, 18/19",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Dr. Alieva Vasila Shukurullaevna",
        "Mutaxassislik": "Allergolog",
        "Manzil": "Medilux Medical center, Farobiy ko`chasi, 3-B",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Dr. Djurayev Abduvaxid Raxmankulovich",
        "Mutaxassislik": "Allergolog, Pulmonolog",
        "Manzil": "Sinomed MD / Darmon Servis, Taxtapul ko`chasi, 341a",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Dr. Abdug'aniyev Saidazimxon Usmonxujayevich",
        "Mutaxassislik": "Allergolog, Immunolog, Pulmonolog",
        "Manzil": "Kimyo University Hospital, Bunyodkor ko`ch. Yakkabog` MFY, 19",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Fattaxov Bobir Shavkatovich",
        "Mutaxassislik": "Dermatolog, Dermatovenereolog",
        "Manzil": (
            "O'zbekiston dermatovenerologiya va kosmetologiya markazi, Farobiy"
            " ko'chasi, 3A"
        ),
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Xaldarbekov Madamin Karimjanovich",
        "Mutaxassislik": "Dermatolog, Dermatovenereolog",
        "Manzil": (
            "O'zbekiston dermatovenerologiya va kosmetologiya markazi, Farobiy"
            " ko'chasi, 3A"
        ),
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Zakirov Rustam Ruxullaevich",
        "Mutaxassislik": "Dermatolog, Dermatovenereolog",
        "Manzil": (
            "Medion Aesthetic and SPA / Medion Clinic 24-7, Zulfiyaxonim ko'chasi,"
            " 18"
        ),
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Jamolov Davron Nematovich",
        "Mutaxassislik": "Dermatolog",
        "Manzil": "Shox Med Center, Oybek ko`chasi 34",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Rasulova Nazira Anvarovna",
        "Mutaxassislik": "Dermatolog",
        "Manzil": (
            "O'zbekiston dermatovenerologiya va kosmetologiya markazi, Farobiy"
            " ko'chasi, 3A"
        ),
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Alyavi Saidnairxon Farxadovich",
        "Mutaxassislik": "Dermatolog, Venereolog",
        "Manzil": "Doctor D, Usta Olim ko`chasi, 15 uy",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Abdullaxo'jayev Kamolliddin Abdurahmonovich",
        "Mutaxassislik": "Dermatolog, Dermatovenereolog",
        "Manzil": (
            "O'zbekiston dermatovenerologiya va kosmetologiya markazi / Doktor"
            " Servis, Farobiy ko'chasi, 3A"
        ),
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Shoxraxmetov Shoraxmat Shorasulovich",
        "Mutaxassislik": "Dermatolog, Trixolog",
        "Manzil": (
            "Medion Clinic 24-7 / Medion Aesthetic and SPA / Nano Hair Clinic,"
            " Zulfiyaxanum ko`chasi, 18"
        ),
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Ortiqov Aziz Farruhjonovich",
        "Mutaxassislik": "Dermatolog, Dermatovenereolog",
        "Manzil": (
            "Expert Medical Clinic - Pro Surgery, Yunusobod tumani, kichik"
            " aylana yo'li, 11A"
        ),
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Askarov Dilshod Alisherovich",
        "Mutaxassislik": "Dermatolog, Dermatovenereolog, Trixolog",
        "Manzil": "B2B Beautyclinic, Bunyodkor prospekti, 8E",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Toshmatova Odila Dilshodovna",
        "Mutaxassislik": "Dermatolog, Trixolog, Kosmetolog",
        "Manzil": (
            "O'zbekiston dermatovenerologiya va kosmetologiya markazi, Farobiy"
            " ko'chasi, 3A"
        ),
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Raximova Zulayxo Tulkinovna",
        "Mutaxassislik": "Dermatolog, Kosmetolog, Venereolog",
        "Manzil": "M-Clinic, Tantan ko'chasi, 1-uy",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Urunbayev Nugman Suratovich",
        "Mutaxassislik": "Dermatolog, Dermatovenereolog",
        "Manzil": "MDS Servis, Botkin ko`chasi, 110/3",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Abdullayev Umid Ubaydullayevich",
        "Mutaxassislik": "Dermatolog, Oftalmolog",
        "Manzil": "Shox Med Center / Darmon Servis / NIKAMED, Oybek ko`chasi 34",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Rahmatullayeva Sevara Nodirbekovna",
        "Mutaxassislik": "Dermatolog, Dermatovenereolog",
        "Manzil": (
            "O'zbekiston dermatovenerologiya va kosmetologiya markazi, Farobiy"
            " ko'chasi, 3A"
        ),
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Sodiqova Shohida Farxadovna",
        "Mutaxassislik": "Dermatolog, Kosmetolog, Dermatovenereolog",
        "Manzil": (
            "Medion Aesthetic and SPA / Medion Clinic 24-7, Zulfiyaxonim"
            " ko'chasi, 18"
        ),
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Babaqulova Gulnora Sabirjanovna",
        "Mutaxassislik": "Dermatolog, Kosmetolog",
        "Manzil": (
            "O'zbekiston dermatovenerologiya va kosmetologiya markazi, Farobiy"
            " ko'chasi, 3A"
        ),
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Eshyozova Dilfuza Yakubbayevna",
        "Mutaxassislik": "Dermatolog, Kosmetolog, LOR (Otolaringolog)",
        "Manzil": "Mevazor Med, Keles Yo`li ko`chasi, 156",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Inogamova Malika Abdulxalilovna",
        "Mutaxassislik": "Dermatolog",
        "Manzil": (
            "Kamola Diagnostic Medecine, Olmazor tumani, Birlik ko‘chasi, 2-uy"
        ),
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Osarov Tolkin Kurbanovich",
        "Mutaxassislik": "Dermatolog, Dermatovenereolog",
        "Manzil": "Global Medical Center, Yangi Sergeli ko`chasi, 35",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Myasnik Vladimir Borisovich",
        "Mutaxassislik": "Kardiolog",
        "Manzil": "MDS Servis, Botkin ko`chasi, 110/3",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Zhuravleva Yuliya Yuriyevna",
        "Mutaxassislik": "Kardiolog, Terapevt",
        "Manzil": "De Factum Central, Osiyo ko'ch. 86A",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Jepparova Liliya Enverovna",
        "Mutaxassislik": "Kardiolog, Terapevt",
        "Manzil": "De Factum Central, Osiyo ko'ch. 86A",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Shermatov Gayrat Ermamatovich",
        "Mutaxassislik": "Kardiolog",
        "Manzil": "Doctor D, Usta Olim ko`chasi, 15 uy",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Axmedov Gafur Saparbayevich",
        "Mutaxassislik": "Kardiolog, Terapevt",
        "Manzil": "Medion Clinic 24-7 / Humo Med Center, Zulfiyaxanum ko`chasi, 18",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Bakieva Malika Alimovna",
        "Mutaxassislik": "Kardiolog, Terapevt",
        "Manzil": "Medion Family Hospital, Istiroxat ko'ch., 258",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Pardayev Bobur Baxtiyorovich",
        "Mutaxassislik": "Kardiolog",
        "Manzil": "IP Clinic / New Medical Service, Yassi ko'chasi, 38-uy",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Shomatova Nilufar Minavarovna",
        "Mutaxassislik": "Kardiolog, Terapevt",
        "Manzil": "Shox Med Center, Oybek ko`chasi 34",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Qayumova Risolat Ro'ziqulovna",
        "Mutaxassislik": "Kardiolog, Terapevt",
        "Manzil": "Shox Med Center, Oybek ko`chasi 34",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Qodirov Behzod Baxramovich",
        "Mutaxassislik": "Kardiolog, Reanimatolog",
        "Manzil": "Yurak Markazi, Yangi Qo'yliq, 1B",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Salaxitdinov Shuxrat Najmiddinovich",
        "Mutaxassislik": "Kardiolog",
        "Manzil": "M-Clinic, Tantan ko'chasi, 1-uy",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Aminov Abduazim Abdullaevich",
        "Mutaxassislik": "Kardiolog",
        "Manzil": (
            "Expert Medical Clinic - Pro Surgery, Yunusobod tumani, kichik"
            " aylana yo'li, 11A"
        ),
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Ibragimov Muxiddin Nuriddinovich",
        "Mutaxassislik": "Kardiolog",
        "Manzil": "M-Clinic, Tantan ko'chasi, 1-uy",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Adilova Ikbol Gafuritdinovna",
        "Mutaxassislik": "Kardiolog",
        "Manzil": (
            "Medion Innovation / Respublika ixtisoslashtirilgan kardiologiya"
            " markazi, Abdulla Qodiriy ko'chasi, 39"
        ),
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Arnopolskaya Dina Iosifovna",
        "Mutaxassislik": "Kardiolog, Revmatolog, Terapevt",
        "Manzil": (
            "De Factum Megapolis / De Factum Central, Yunusobod massivi, 13"
            " kv-l, 1A"
        ),
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Xalilova Dilfuza Abduraxmanovna",
        "Mutaxassislik": "Kardiolog, Terapevt",
        "Manzil": "ARK HOSPITAL, Farobi ko'cha, 323",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Kazantseva Natalya Vladimirovna",
        "Mutaxassislik": "Kardiolog, Terapevt",
        "Manzil": "Medion Clinic 24-7, Zulfiyaxanum ko`chasi, 18",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Kim Sergey Vitalievich",
        "Mutaxassislik": "Kardiolog",
        "Manzil": (
            "Medion Family Hospital / Sinomed MD International Hospital,"
            " Istiroxat ko'ch., 258"
        ),
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Mirxodjaeva Ibodat Ismoilovna",
        "Mutaxassislik": "Kardiolog, Revmatolog",
        "Manzil": "De Factum Kids, Avliyo-Ota ko`chasi, 1-2",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Xalmuratov Mansur Komiljonovich",
        "Mutaxassislik": "Kardiolog, Terapevt",
        "Manzil": "Medion Clinic 24-7 / Samo Medical 24-7, Zulfiyaxanum ko`chasi, 18",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Bo'rixodjaeva Gulnora Xulkarovna",
        "Mutaxassislik": "Ginekolog, Akusher",
        "Manzil": "MDS Servis, Botkin ko`chasi, 110/3",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Shamsiddinova Nargiza Alixanovna",
        "Mutaxassislik": "Ginekolog",
        "Manzil": "Medion Clinic 24-7, Zulfiyaxanum ko`chasi, 18",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Abdusamatova Lola Boltaevna",
        "Mutaxassislik": "Ginekolog, Akusher, Reproduktolog",
        "Manzil": "B2B Beautyclinic, Bunyodkor prospekti, 8E",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Shaxmurova Bella Nikolaevna",
        "Mutaxassislik": "Ginekolog, Akusher",
        "Manzil": "De Factum Central, Osiyo ko'ch. 86A",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Karimova Zilola Maksimovna",
        "Mutaxassislik": "Ginekolog",
        "Manzil": "Shox Med Center, Oybek ko`chasi 34",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Abdumalikova Shohida Mirzaevna",
        "Mutaxassislik": "Ginekolog",
        "Manzil": (
            "De Factum Megapolis / Akusherlik va ginekologiya ilmiy-tadqiqot"
            " instituti, Yunusobod massivi, 13 kv-l, 1A"
        ),
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Raxmatova Nilufar Boboyorovna",
        "Mutaxassislik": "Ginekolog, Endokrinolog",
        "Manzil": "LA TIVA Birth Home, Istiroxat ko'chasi, 258",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Almuxamedova Barno Gulmuhamadovna",
        "Mutaxassislik": "Ginekolog, Onkolog",
        "Manzil": (
            "M-Clinic / Respublika ixtisoslashtirilgan onkologiya va radiologiya"
            " markazi, Tantan ko'chasi, 1-uy"
        ),
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Mirzaxmedova Nargiza Alisultanova",
        "Mutaxassislik": "Ginekolog, Reproduktolog",
        "Manzil": "Doctor D, Usta Olim ko`chasi, 15 uy",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Israilova Zamira Shuxratovna",
        "Mutaxassislik": "Ginekolog, Akusher",
        "Manzil": (
            "O'zbekiston dermatovenerologiya va kosmetologiya markazi / MirMed"
            " Clinic, Farobiy ko'chasi, 3A"
        ),
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Zohidova Nargis Ravshanovna",
        "Mutaxassislik": "Ginekolog, Akusher",
        "Manzil": "De Factum Central / Ayol Care, Osiyo ko'ch. 86A",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Kadirova Nigora Tursunpolatovna",
        "Mutaxassislik": "Ginekolog, Akusher",
        "Manzil": "Dusel Medical, To‘kimachi ko‘chasi, 3-uy",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Popov Aleksandr Anatolievich",
        "Mutaxassislik": "Ginekolog, Jarroh, Onkolog",
        "Manzil": "Medion Family Hospital, Istiroxat ko'ch., 258",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Romanova Yekaterina Gennadevna",
        "Mutaxassislik": "Ginekolog",
        "Manzil": "De Factum Kids, Avliyo-Ota ko`chasi, 1-2",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Fayzliyeva Kamola G'aybiddinovna",
        "Mutaxassislik": "Ginekolog, Akusher",
        "Manzil": (
            "Expert Medical Clinic - Pro Surgery, Yunusobod tumani, kichik"
            " aylana yo'li, 11A"
        ),
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Luchenko Lia Raufovna",
        "Mutaxassislik": "Ginekolog, Akusher",
        "Manzil": "De Factum Central, Osiyo ko'ch. 86A",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Fozilbekov Ro'ziqul Anarkulovich",
        "Mutaxassislik": "Ginekolog",
        "Manzil": "M-Clinic / AKFA Medline, Tantan ko'chasi, 1-uy",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Sabirzyanova Liliya Gayratovna",
        "Mutaxassislik": "Ginekolog",
        "Manzil": "Medion Clinic 24-7, Zulfiyaxanum ko`chasi, 18",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Buribekova Dildora Shuhratovna",
        "Mutaxassislik": "Ginekolog",
        "Manzil": "ARK HOSPITAL, Farobi ko'cha, 323",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
    {
        "Ism": "Buynova Viktoriya Anatolievna",
        "Mutaxassislik": "Ginekolog, Akusher, Ultratovush mutaxassisi",
        "Manzil": "LA TIVA Birth Home, Istiroxat ko'chasi, 258",
        "Reyting": "⭐⭐⭐⭐⭐",
    },
]

# Savatni xotirada saqlash
if "cart" not in st.session_state:
  st.session_state.cart = []

# ----------------- YON PANEL (SIDEBAR) -----------------
st.sidebar.title("🩺 Tabib AI")
lang = st.sidebar.selectbox("Language / Til", ["O'zbekcha", "Русский"])

if lang == "O'zbekcha":
  menu_title = "Bo'limni tanlang"
  menu_options = [
      "Bosh sahifa",
      "AI Konsultatsiyasi",
      "Shifokorlar",
      "Dorixona",
      f"Savat ({len(st.session_state.cart)})",
  ]
  search_doc_text = "🔍 Shifokor ismi yoki mutaxassisligi bo'yicha qidiring"
  book_btn = "Qabulga yozilish"
  ai_title = "Tabib AI — Sun'iy Intellekt Maslahatchisi"
  ai_desc = "Istalgan tibbiy savolingizni bering va tushuntirib beramiz."
  ai_placeholder = "Masalan: Bosh og'rig'i nima sababdan bo'lishi mumkin?"
  ai_btn = "AI dan javob olish"
else:
  menu_title = "Выберите раздел"
  menu_options = [
      "Главная",
      "AI Консультация",
      "Врачи",
      "Аптека",
      f"Корзина ({len(st.session_state.cart)})",
  ]
  search_doc_text = "🔍 Поиск врача по специальности или имени"
  book_btn = "Записаться на прием"
  ai_title = "Tabib AI — Консультант ИИ"
  ai_desc = "Задайте любой медицинский вопрос."
  ai_placeholder = "Например: Каковы причины головной боли?"
  ai_btn = "Получить ответ от AI"

choice = st.sidebar.radio(menu_title, menu_options)

# ----------------- 1. BOSH SAHIFA -----------------
if choice in ["Bosh sahifa", "Главная"]:
  st.title("🩺 Tabib AI Platformasiga Xush Kelibsiz!")
  st.markdown(
      "Bu platforma orqali malakali shifokorlarni topishingiz va sun'iy"
      " intellekt yordamida tezkor tibbiy maslahat olishingiz mumkin."
  )
  st.info("Chap tarafdagi menyu orqali kerakli bo'limni tanlang.")

# ----------------- 2. AI KONSULTATSIYASI -----------------
elif choice in ["AI Konsultatsiyasi", "AI Консультация"]:
  st.markdown(f"### 🤖 {ai_title}")
  st.write(ai_desc)
  user_query = st.text_area("", placeholder=ai_placeholder)
  if st.button(ai_btn):
    if user_query.strip():
      st.success(
          "Sun'iy intellekt tahlili: Mutaxassis shifokor ko'rigidan o'tish"
          " tavsiya etiladi."
      )
    else:
      st.warning("Iltimos, savolingizni yozing!")

# ----------------- 3. SHIFOKORLAR -----------------
elif choice in ["Shifokorlar", "Врачи"]:
  st.title("👨‍⚕️ Malakali Shifokorlar Ro'yxati")
  st.write(f"Jami shifokorlar bazasi: **{len(doctors_list)} ta** shifokor")

  search_query = st.text_input(search_doc_text)

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
                    <div class="doctor-spec">🩺 {row['Mutaxassislik']}</div>
                    <div class="doctor-address">📍 {row['Manzil']}</div>
                    <div class="doctor-rating">{row['Reyting']}</div>
                </div>
                """,
            unsafe_allow_html=True,
        )
        if st.button(book_btn, key=f"doc_{index}"):
          st.success(
              f"✅ {row['Ism']} qabuliga yozilish uchun so'rov yuborildi!"
          )
  else:
    st.warning("Hech qanday shifokor topilmadi.")

# ----------------- 4. DORIXONA -----------------
elif choice in ["Dorixona", "Аптека"]:
  st.title("💊 Dorixona")
  st.info("Dorilar ro'yxati tez kunda qo'shiladi.")

# ----------------- 5. SAVAT -----------------
elif choice.startswith("Savat") or choice.startswith("Корзина"):
  st.title("🛒 Savatcha")
  if st.session_state.cart:
    for i, item in enumerate(st.session_state.cart):
      st.write(f"{i+1}. {item}")
  else:
    st.info("Savatingiz bo'sh.")
