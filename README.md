# AAE — Aesthetic Art Ekt

**Created by Milan Tegeltija, May 2025**

## What is AAE?

AAE (Aesthetic Art Ekt) is a proposed tagging and classification standard for visual media that captures the nuanced space between traditional art, sensual aesthetics, and respectful, non-explicit representation. It is not NSFW — it is NIFS: Non-Invasive, Fully Stylized.

## Core Principles

- **Artistic Intent** — Not for shock, but for emotional resonance.
- **Respectful Composition** — Strong, aesthetic, human subjects.
- **Emotional Layer** — Often cinematic, reflective, or narrative in tone.

## Sample Code Use

```json
{
  "tag": "AAE-WTRWND-MSCN-VLU84",
  "description": "A woman with wet hair stands by the window, lit by city lights, wearing a translucent white shirt. Moody, cinematic, contemplative.",
  "attributes": {
    "style": "cinematic",
    "mood": "moody",
    "lighting": "low-key warm",
    "subject": "female athletic",
    "nsfw": false
  }
}
```

## License

This specification is shared under [Creative Commons CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
# ✨ Aesthetic Art Ekt (AAE) Manifesto

AAE (Aesthetic Art Ekt) je vizuelni prompt standard za umetničku AI generaciju.  
Ne spada u NSFW. Ne spada u generičko.  
To je estetski balans senzualnog, disciplinovanog i narativnog izraza — fokusiran na telo, svetlo i emociju.

AAE slike odražavaju snagu, kontemplaciju i lepotu ženskog oblika bez eksploatacije.

---

## 🖋️ Autorstvo
**Autor:** Milan Tегeлтија (Teglaz)  
**Godina:** 2025  
**Prva implementacija:** testirana kroz OpenAI **Sora**  
**Repo:** <https://github.com/Teglaz/aae-spec>

---

## 🇬🇧/🇷🇸 Syntax examples / Sintaksa primera

### Tag format
| Tag | Description / Opis |
|-----|--------------------|
| `AAE` | prefix (standard) |
| `WTRWND` | ambience clue *(water + window)* / ambijent |
| `MSCN` | mood/scene *(moody scene)* |
| `VLU84` | verzija / hash |

### Prompt example
| Language / Jezik | Prompt |
|------------------|--------|
| **English** | *Ultra-realistic portrait of an athletic woman, backlit by warm rain through a window, towel draped, soft shadows.* |
| **Srpski** | *Ultra-realističan portret atletske žene, pozadinsko toplo kišno svetlo kroz prozor, peškir prebačen, meke senke.* |

### How to use / Kako se koristi
* Tag ide u *caption* ili na početak prompta.  
* Prompt opis ostaje čitljiv AI modelima.  
* Zajedno grade AAE kontekst (estetski, nenapadan, nije NSFW).

---

## 📂 Project files
| File | Description |
|------|-------------|
| [`aae-guide.md`](aae-guide.md) | Bilingual AAE guide & syntax |
| [`pitch.md`](pitch.md) | One-page project pitch |
| [`LICENSE`](LICENSE) | MIT open-source license |

---

© 2025 Milan Tegeltija • Released under the MIT License
