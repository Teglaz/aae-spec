import json
import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from aae_utils import load_manifest, validate_entry, get_valid_entries, REQUIRED_KEYS


VALID_ENTRY = {
    "file": "test-image.jpg",
    "title_en": "Test Image EN",
    "title_sr": "Test Slika SR",
    "description_en": "English description.",
    "description_sr": "Srpski opis.",
    "tags": ["TAG1", "TAG2"],
    "author": "Test Author",
    "date": "2025-01-01"
}


class TestLoadManifest:
    def test_ucitava_validan_manifest(self, tmp_path):
        manifest = tmp_path / "manifest.json"
        manifest.write_text(json.dumps([VALID_ENTRY]), encoding="utf-8")
        data = load_manifest(str(manifest))
        assert len(data) == 1
        assert data[0]["file"] == "test-image.jpg"

    def test_greška_ako_fajl_ne_postoji(self, tmp_path):
        with pytest.raises(FileNotFoundError):
            load_manifest(str(tmp_path / "ne_postoji.json"))

    def test_greška_za_neispravan_json(self, tmp_path):
        bad = tmp_path / "manifest.json"
        bad.write_text("ovo nije json {{{", encoding="utf-8")
        with pytest.raises(ValueError, match="Neispravan JSON"):
            load_manifest(str(bad))

    def test_greška_ako_nije_lista(self, tmp_path):
        manifest = tmp_path / "manifest.json"
        manifest.write_text(json.dumps({"key": "value"}), encoding="utf-8")
        with pytest.raises(ValueError, match="lista"):
            load_manifest(str(manifest))

    def test_ucitava_vise_unosa(self, tmp_path):
        entries = [VALID_ENTRY, {**VALID_ENTRY, "file": "second.jpg"}]
        manifest = tmp_path / "manifest.json"
        manifest.write_text(json.dumps(entries), encoding="utf-8")
        data = load_manifest(str(manifest))
        assert len(data) == 2


class TestValidateEntry:
    def test_validan_unos_prolazi(self):
        assert validate_entry(VALID_ENTRY, 1) is True

    def test_unos_bez_obaveznog_polja_pada(self):
        incomplete = {k: v for k, v in VALID_ENTRY.items() if k != "file"}
        assert validate_entry(incomplete, 1) is False

    def test_unos_bez_vise_polja_pada(self):
        incomplete = {"file": "x.jpg"}
        assert validate_entry(incomplete, 1) is False

    def test_custom_required_keys(self):
        entry = {"file": "x.jpg", "title_sr": "Test"}
        assert validate_entry(entry, 1, required_keys=["file", "title_sr"]) is True

    def test_custom_required_keys_nedostaje(self):
        entry = {"file": "x.jpg"}
        assert validate_entry(entry, 1, required_keys=["file", "title_sr"]) is False


class TestGetValidEntries:
    def test_vraca_validne_unose(self):
        data = [VALID_ENTRY, {**VALID_ENTRY, "file": "second.jpg"}]
        result = get_valid_entries(data)
        assert len(result) == 2

    def test_filtrira_nevalidne_unose(self):
        data = [VALID_ENTRY, {"file": "incomplete.jpg"}]
        result = get_valid_entries(data)
        assert len(result) == 1
        assert result[0]["file"] == "test-image.jpg"

    def test_prazna_lista(self):
        result = get_valid_entries([])
        assert result == []

    def test_svi_nevalidni(self):
        data = [{"file": "a.jpg"}, {"file": "b.jpg"}]
        result = get_valid_entries(data)
        assert result == []
