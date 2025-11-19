import os
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# === Muhit sozlamalari ===
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["TRANSFORMERS_VERBOSITY"] = "error"

# === Model manzili ===
model_path = r"D:\Tarjima_SI\models\facebook\nllb-200-1.3B"

print("🔄 Model yuklanmoqda (bir marta internet kerak)...")

# === Modelni yuklash (avval mahalliydan tekshiradi) ===
if os.path.exists(model_path):
    print(f"📂 Mahalliy model topildi: {model_path}")
    model_name = model_path
else:
    print("🌐 Internet orqali model yuklanmoqda (bir marta)...")
    model_name = "facebook/nllb-200-1.3B"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name, torch_dtype=torch.float32)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

print("✅ Model yuklandi va tayyor!\n")

# === Universal tarjima funksiyasi ===
def translate_text(text, src_lang="uzn_Latn", tgt_lang="rus_Cyrl"):
    try:
        tokenizer.src_lang = src_lang
        inputs = tokenizer(text, return_tensors="pt").to(device)

        # --- Universal target ID aniqlash ---
        if hasattr(tokenizer, "lang_code_to_id"):
            bos_token_id = tokenizer.lang_code_to_id.get(tgt_lang, tokenizer.bos_token_id)
        else:
            # yangi versiyalar uchun fallback
            try:
                bos_token_id = tokenizer.convert_tokens_to_ids(tgt_lang)
                if bos_token_id is None:
                    bos_token_id = tokenizer.bos_token_id
            except Exception:
                bos_token_id = tokenizer.bos_token_id

        # --- Model orqali tarjima ---
        outputs = model.generate(
            **inputs,
            forced_bos_token_id=bos_token_id,
            max_new_tokens=160,
            do_sample=True,
            top_p=0.9,
            temperature=0.7,
            repetition_penalty=1.15,
        )

        result = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return result
    except Exception as e:
        return f"⚠️ Xato: {str(e)}"

# === Interaktiv konsol ===
print("🟢 Tarjimon ishga tushdi (O'zbek → Rus)")
print("Til kodi namunasi: uzn_Latn → rus_Cyrl\n")

direction = input("Tarjima yo‘nalishini tanlang (1=uz→ru, 2=ru→uz): ")
if direction == "2":
    src, tgt = "rus_Cyrl", "uzn_Latn"
else:
    src, tgt = "uzn_Latn", "rus_Cyrl"

print("🟢 Tarjimon ishga tushdi (O'zbek ↔ Rus)")
print("Til kodi namunasi: uzn_Latn ↔ rus_Cyrl\n")

# 🔄 Tarjima yo‘nalishini tanlash (foydalanuvchi tanlaydi)
direction = input("Tarjima yo‘nalishini tanlang (1=uz→ru, 2=ru→uz): ").strip()

if direction == "2":
    src, tgt = "rus_Cyrl", "uzn_Latn"
    print("🌐 Tanlangan yo‘nalish: Ruscha → O‘zbekcha\n")
else:
    src, tgt = "uzn_Latn", "rus_Cyrl"
    print("🌐 Tanlangan yo‘nalish: O‘zbekcha → Ruscha\n")

# 🔁 Asosiy tarjima tsikli
while True:
    text = input("📝 Matn kiriting (yoki 'exit'): ").strip()
    if text.lower() == "exit":
        print("👋 Dasturdan chiqildi.")
        break
    if not text:
        continue

    print("🧠 Tarjima qilinmoqda...")
    result = translate_text(text, src_lang=src, tgt_lang=tgt)
    print("🔹 Natija:", result)

while True:
    text = input("📝 Matn kiriting (yoki 'exit'): ").strip()
    if text.lower() == "exit":
        break
    if not text:
        continue
    print("🧠 Tarjima qilinmoqda...")
    print("🔹 Natija:", translate_text(text))
    print()