import json  # ovo služi da pročitamo .json fajl (spisak slika)
import argparse

REQUIRED_KEYS = ["file", "title_sr", "date", "tags", "description_sr"]

def validate_entry(entry, index):
    missing = [k for k in REQUIRED_KEYS if k not in entry]
    if missing:
        print(f"⚠️  Unos #{index} nema obavezna polja: {missing}")
        return False
    return True

def main():
    parser = argparse.ArgumentParser(description="Generiši examples.md iz manifest.json")
    parser.add_argument("--manifest", default="manifest.json", help="Putanja do manifest.json")
    parser.add_argument("--output", default="examples.md", help="Putanja do izlaznog fajla")
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

    try:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write("# 📸 Galerija slika\n\n")
            for image in valid_entries:
                f.write(f"## ![{image['title_sr']}]({image['file']})\n")
                f.write(f"**{image['title_sr']}**  \n")
                f.write(f"📅 {image['date']}  \n")
                f.write(f"🏷️ Tagovi: {', '.join(image['tags'])}  \n")
                f.write(f"📝 {image['description_sr']}  \n")
                f.write("\n---\n\n")
    except IOError as e:
        print(f"❌ Greška pri pisanju '{args.output}': {e}")
        exit(1)

    print(f"✅ Gotovo! Generisano {len(valid_entries)} unosa → {args.output}")

if __name__ == "__main__":
    main()
