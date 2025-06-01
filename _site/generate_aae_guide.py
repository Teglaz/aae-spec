import json

# 1. Učitaj manifest.json
with open("manifest.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 2. Header vodiča
header = """# 🏷️ AAE Example Images Guide

> Sve slike su tagovane, opisane i sačuvane prema AAE standardu.

---
"""

# 3. Generiši markdown sekciju za svaku sliku
def entry_to_md(entry):
    return f"""### {entry['title_en']}

![{entry['title_en']}](examples/{entry['file']})

- **EN:** {entry['description_en']}
- **SR:** {entry['description_sr']}
- **Tags:** `{', '.join(entry['tags'])}`
- **Author:** {entry['author']}
- **Date:** {entry['date']}

---
"""

# 4. Sklopi sve u jedan tekst
body = header + "\n".join([entry_to_md(entry) for entry in data])

# 5. Sačuvaj kao aae-guide.md
with open("aae-guide.md", "w", encoding="utf-8") as f:
    f.write(body)

print("✅ Gotovo! Pogledaj novi aae-guide.md fajl.")
