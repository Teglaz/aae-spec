import json

REQUIRED_KEYS = ["file", "title_en", "title_sr", "description_en", "description_sr", "tags", "author", "date"]


def load_manifest(path="manifest.json"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"manifest nije pronađen: '{path}'")
    except json.JSONDecodeError as e:
        raise ValueError(f"Neispravan JSON u '{path}': {e}")

    if not isinstance(data, list):
        raise ValueError("manifest.json mora biti niz (lista) unosa.")

    return data


def validate_entry(entry, index, required_keys=None):
    keys = required_keys or REQUIRED_KEYS
    missing = [k for k in keys if k not in entry]
    if missing:
        print(f"⚠️  Unos #{index} nema obavezna polja: {missing}")
        return False
    return True


def get_valid_entries(data, required_keys=None):
    return [entry for i, entry in enumerate(data) if validate_entry(entry, i + 1, required_keys)]
