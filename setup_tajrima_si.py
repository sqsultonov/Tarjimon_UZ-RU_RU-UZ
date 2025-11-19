import os
import subprocess
from pathlib import Path

# Loyihaning asosiy yo‘li
BASE_DIR = Path(r"D:\Tarjima_SI")
SRC_DIR = BASE_DIR / "src"
VENV_DIR = BASE_DIR / ".venv"

def run(cmd, check=True):
    subprocess.run(cmd, check=check)

# 1️⃣ Papkalarni yaratish
def setup_folders():
    for folder in [SRC_DIR, BASE_DIR / "models", BASE_DIR / "data", BASE_DIR / "logs"]:
        folder.mkdir(parents=True, exist_ok=True)
    print("📁 Papkalar yaratildi")

# 2️⃣ Virtual muhitni yaratish
def setup_venv():
    if not VENV_DIR.exists():
        run(["python", "-m", "venv", str(VENV_DIR)])
        print("✅ Virtual muhit yaratildi (.venv)")
    else:
        print("ℹ️ Virtual muhit allaqachon mavjud")

# 3️⃣ Kutubxonalarni o‘rnatish
def install_libs():
    pip = VENV_DIR / "Scripts" / "pip.exe"
    run([str(pip), "install", "torch", "transformers", "sentencepiece", "huggingface_hub", "psutil"])
    print("📦 Kutubxonalar o‘rnatildi")

# 4️⃣ Tarjimon faylini yaratish
def create_translator():
    code = r'''
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

print("🔄 Model yuklanmoqda (bir marta internet kerak)...")
model_name = "facebook/nllb-200-distilled-600M"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name, torch_dtype=torch.float32)

print("✅ Model yuklandi va tayyor!\n")
print("🟢 Tarjimon ishga tushdi (O'zbek → Rus)")

while True:
    text = input("📝 Matn kiriting (yoki 'exit'): ")
    if text.lower().strip() == "exit":
        print("👋 Dasturdan chiqildi.")
        break
    tokenizer.src_lang = "uzn_Latn"
    inputs = tokenizer(text, return_tensors="pt")
    output = model.generate(**inputs, forced_bos_token_id=tokenizer.lang_code_to_id["rus_Cyrl"])
    translation = tokenizer.decode(output[0], skip_special_tokens=True)
    print("🔹 Tarjima:", translation)
    print("-" * 60)
'''
    (SRC_DIR / "nllb_translator.py").write_text(code, encoding="utf-8")
    print("🧠 Tarjimon fayli yaratildi!")

# 5️⃣ Asosiy funksiyalarni ishga tushirish
if __name__ == "__main__":
    print("🚀 Tarjima_SI loyihasini 0 dan sozlash...")
    setup_folders()
    setup_venv()
    install_libs()
    create_translator()
    print("\n✅ Hammasi tayyor!")
    print("➡️ Virtual muhitni faollashtiring:")
    print(r"   D:\Tarjima_SI\.venv\Scripts\activate")
    print("➡️ Tarjimonni ishga tushiring:")
    print(r"   python src\nllb_translator.py")
