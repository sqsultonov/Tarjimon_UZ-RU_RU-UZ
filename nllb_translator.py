import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

print("🔄 Model yuklanmoqda...")
model_name = "facebook/nllb-200-distilled-600M"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

print("🟢 Tarjimon tayyor!")

while True:
    text = input("📝 Matn kiriting (exit = chiqish): ")
    if text.lower() == "exit":
        break

    tokenizer.src_lang = "uzn_Latn"
    inputs = tokenizer(text, return_tensors="pt")

    # MUHIM O'ZGARISH: forced_bos_token_id
    bos_id = tokenizer.convert_tokens_to_ids("rus_Cyrl")

    output = model.generate(
        **inputs,
        forced_bos_token_id=bos_id
    )

    translation = tokenizer.decode(output[0], skip_special_tokens=True)
    print("🔹 Tarjima:", translation)
    print("-" * 40)
