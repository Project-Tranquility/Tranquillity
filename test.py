import spacy
import yaml
import random
from rapidfuzz import fuzz

nlp = spacy.load("fr_core_news_sm")

INTENT_MAP = {
    "montrer":  ("ls -l", True),
    "montre":   ("ls -l", True),
    "afficher": ("ls -l", True),
    "affiche":  ("ls -l", True),
    "lister":   ("ls -l", True),
    "liste":    ("ls -l", True),
    "aller":    ("cd", True),
    "va":       ("cd", True),
    "rentrer":  ("cd", True),
    "rentre":   ("cd", True),
    "naviguer": ("cd", True),
    "navigue":  ("cd", True),
    "créer":    ("mkdir", True),
    "crée":     ("mkdir", True),
    "trouver":  ("find", True),
    "trouve":   ("find", True),
}

LOCATION_KEYWORDS = {"dossier", "répertoire", "fichier"}

POSITION_KEYWORDS = {"actuel"}

def check_respons(dico, text):
    best_score = 0
    best_entry = None
    for entry in dico:
        for trigger in entry["trigger"]:
            score = fuzz.partial_ratio(trigger.lower(), text)
            print(score)
            if score > best_score:
                best_score = score
                best_entry = entry
    if best_score > 80 and best_entry:
        return random.choice(best_entry["respons"])
    return None

def parse_intent(text):
    doc = nlp(text.lower())

    cmd = None
    needs_arg = False

    for token in doc:
        key = token.lemma_ if token.lemma_ in INTENT_MAP else token.text
        if key in INTENT_MAP:
            cmd, needs_arg = INTENT_MAP[key]
            break

    if not cmd:
        return None

    for token in doc:
        if token.text in POSITION_KEYWORDS:
            return f"{cmd} ."

    arg = None
    if needs_arg:
        for token in doc:
            if token.pos_ in ("NOUN", "PROPN") and token.text not in LOCATION_KEYWORDS:
                arg = token.text

    if needs_arg and arg:
        return f"{cmd} ~/{arg}"
    return cmd if not needs_arg else None

def main():
    
    with open("data.yaml", "r") as file:
        dico = yaml.safe_load(file)
    print(dico)
    print("\n")

    while True:
        text = input("> ").strip()
        if not text:
            continue

        response = check_respons(dico, text)
        print(response)

        result = parse_intent(text)
        print(result if result else "[aucune commande trouvée]")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nArrêt.")