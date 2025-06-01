import json  # ovo služi da pročitamo .json fajl (spisak slika)

# Otvaramo manifest.json i čitamo podatke
with open("manifest.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Ovo je mesto gde ćemo da upišemo tekst
with open("examples.md", "w", encoding="utf-8") as f:
    f.write("# 📸 Galerija slika\n\n")

    for image in data:
        f.write(f"## ![{image['title_sr']}]({image['file']})\n")
        f.write(f"**{image['title_sr']}**  \n")
        f.write(f"📅 {image['date']}  \n")
        f.write(f"🏷️ Tagovi: {', '.join(image['tags'])}  \n")
        f.write(f"📝 {image['description_sr']}  \n")
        f.write("\n---\n\n")
