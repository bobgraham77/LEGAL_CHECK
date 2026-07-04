import re

class LegalParser:
    """Parseur Regex pour extraire les citations juridiques."""
    
    CODE_MAPPING = {
        "CASF": "Code de l'action sociale et des familles",
        "CJA": "Code de justice administrative",
        "CSS": "Code de la sécurité sociale",
        "CRPA": "Code des relations entre le public et l'administration",
        "CP": "Code pénal",
        "CC": "Code civil",
        "CT": "Code du travail"
    }

    ARTICLE_PATTERN = r"(?i)article\s+([L|R|D]?\.?\s?\d+(?:[-─]\d+)*[a-z]*)\s+du\s+((?:Code\s+[^,\.;\n]+?)|(?:[A-Z]{2,}))(?=\s+(?:prévoit|dispose|stipule|est|doit|peut|a)|[\.,;]|$)"

    @classmethod
    def extract_citations(cls, text):
        citations = []
        matches = re.finditer(cls.ARTICLE_PATTERN, text, re.IGNORECASE)
        for match in matches:
            article_num = match.group(1).strip()
            code_raw = match.group(2).strip()
            
            code_clean = code_raw.replace("*", "").strip()
            stop_words = ["prévoit", "dispose", "stipule", "est", "doit", "peut", "impose", "subordonne", "prévoit", "relatif"]
            for word in stop_words:
                if f" {word} " in f" {code_clean.lower()} ":
                    code_clean = re.split(f" {word} ", code_clean, flags=re.IGNORECASE)[0].strip()
            
            code_name = cls.CODE_MAPPING.get(code_clean.upper(), code_clean)
            
            citations.append({
                "full_match": match.group(0),
                "article_num": article_num,
                "code_name": code_name,
                "context": text[max(0, match.start()-100):min(len(text), match.end()+100)]
            })
        return citations
