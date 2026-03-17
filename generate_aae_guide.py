import json
import argparse

REQUIRED_KEYS = ["file", "title_en", "title_sr", "description_en", "description_sr", "tags", "author", "date"]

def validate_entry(entry, index):
    missing = [k for k in REQUIRED_KEYS if k not in entry]
    if missing:
        print(f"⚠️  Unos #{index} nema obavezna polja: {missing}")
        return False
    return True

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

def main():
    parser = argparse.ArgumentParser(description="Generiši aae-guide.md iz manifest.json")
    parser.add_argument("--manifest", default="manifest.json", help="Putanja do manifest.json")
    parser.add_argument("--output", default="aae-guide.md", help="Putanja do izlaznog fajla")
    args = parser.parse_args()

    try:
        with open(args.manifest, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ Greška: '{args.manifest}' nije pronađen.")
        exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ Greška: neispravan JSON u '{args.manifest}' — {e}")
        exit(1)

    if not isinstance(data, list):
        print("❌ Greška: manifest.json mora biti niz (lista) unosa.")
        exit(1)

    valid_entries = [entry for i, entry in enumerate(data) if validate_entry(entry, i + 1)]

    if not valid_entries:
        print("❌ Greška: nema validnih unosa u manifestu.")
        exit(1)

    header = """# 🏷️ AAE Example Images Guide

> Sve slike su tagovane, opisane i sačuvane prema AAE standardu.

---
"""

    body = header + "\n".join([entry_to_md(entry) for entry in valid_entries])

    try:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(body)
    except IOError as e:
        print(f"❌ Greška pri pisanju '{args.output}': {e}")
        exit(1)

    print(f"✅ Gotovo! Generisano {len(valid_entries)} unosa → {args.output}")

if __name__ == "__main__":
    main()
