import languages.pt_br as pt
import languages.en_us as en

class LanguageManager:
    def __init__(self, language="pt"):
        if language == "en":
            self.texts = en.TEXTS
        elif language == "pt":
            self.texts = pt.TEXTS
        else:
            raise ValueError("Unsupported language")

    def get(self, key, **kwargs):
        if key not in self.texts:
            raise KeyError(f"Missing translation key: {key}")
        return self.texts[key].format(**kwargs)

