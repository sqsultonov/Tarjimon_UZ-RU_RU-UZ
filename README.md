# Tarjimon_UZ-RU_RU-UZ
O'zbek tilidan Rus tiliga hamda teskarisiga, gapning manosini buzmasdan offlayn tarjima qilish loyiham.  

# NLLB-200 Tarjimon (O‘zbek ↔ Rus)

Ushbu loyiha Meta AI tomonidan yaratilgan **NLLB-200 (No Language Left Behind)** modelidan foydalanib matnlarni avtomatik tarjima qiladi.
Loyiha o‘zbek tilidan rus tiliga hamda aksincha tarjima qiluvchi kichik terminal dasturi shaklida yozilgan.

## Xususiyatlar
- 200 ta tilni qo‘llab-quvvatlaydigan NLLB modelidan foydalanadi  
- GPU bo‘lsa avtomatik aniqlab ishlaydi  
- O‘zbek → Rus tarjimasi misolida ishlaydi (oson kengaytiriladi)  
- Bir marta yuklanganidan keyin offline ishlaydi  
- CLI (terminal) interfeys  

---

## O‘rnatish

### 1. Repozitoriyani yuklab olish:
git clone https://github.com/sqsultonov/Tarjimon_UZ-RU_RU-UZ.git

2. Kerakli kutubxonalarni o‘rnatish:
pip install -r requirements.txt

Ishga tushirish
python src/nllb_translator.py

Model yuklanishi

Model birinchi marta ishga tushganda avtomatik ravishda HuggingFace’dan yuklanadi:

Model nomi:

facebook/nllb-200-distilled-600M


Siz qo‘lda hech narsa yuklamaysiz - dasturning o‘zi yuklaydi.

Papka tuzilmasi
Tarjima_SI/
│
├── setup_tajrima_si.py
├── requirements.txt
├── README.md
│
├── src/
│   └── nllb_translator.py
│
├── models/   (bo‘sh – model avtomatik keladi)
├── data/     (ixtiyoriy papka)
└── logs/     (ixtiyoriy papka)

Foydalanilgan texnologiyalar

PyTorch

HuggingFace Transformers

NLLB-200 Model

SentencePiece Tokenizer

Muallif
Sardorbek Sultonov
