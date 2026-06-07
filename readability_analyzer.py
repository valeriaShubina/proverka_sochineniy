# spellchecker.py
import re
from typing import List, Dict, Set

def _load_dictionary() -> Set[str]:
    return {
        "мама", "мыла", "раму", "папа", "пил", "чай", "кот", "спал", "диване",
        "привет", "мир", "как", "дела", "хорошо", "день", "солнце", "дом",
        "искусственный", "интеллект", "машинное", "обучение", "программа"
    }

def _levenshtein_distance(a: str, b: str) -> int:
    if len(a) < len(b):
        return _levenshtein_distance(b, a)
    if len(b) == 0:
        return len(a)
    previous = list(range(len(b) + 1))
    for i, ca in enumerate(a):
        current = [i + 1]
        for j, cb in enumerate(b):
            insert = previous[j + 1] + 1
            delete = current[j] + 1
            substitute = previous[j] + (ca != cb)
            current.append(min(insert, delete, substitute))
        previous = current
    return previous[-1]

def _get_suggestions(word: str, dictionary: Set[str], max_suggestions: int = 3) -> List[str]:
    word_lower = word.lower()
    candidates = []
    for dict_word in dictionary:
        if abs(len(word_lower) - len(dict_word)) > 3:
            continue
        dist = _levenshtein_distance(word_lower, dict_word)
        candidates.append((dict_word, dist))
    candidates.sort(key=lambda x: x[1])
    return [c[0] for c in candidates[:max_suggestions]]

def check_spelling(text: str) -> List[Dict]:
    if not text or not text.strip():
        return []
    
    dictionary = _load_dictionary()
    pattern = re.compile(r'[а-яё]+', re.IGNORECASE)
    errors = []
    
    for match in pattern.finditer(text):
        original_word = match.group()
        word_lower = original_word.lower()
        position = match.start()
        
        if word_lower in dictionary or original_word.isdigit():
            continue
        
        suggestions = _get_suggestions(original_word, dictionary)
        errors.append({
            "word": original_word,
            "position": position,
            "suggestions": suggestions
        })
    
    return errors

if __name__ == "__main__":
    test_text = "Привет миррр как деллла"
    result = check_spelling(test_text)
    print(result)