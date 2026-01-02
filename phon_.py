import re 
def normalize_phone_number(phone_number: str) -> str: 
    cleaned = re.sub(r"[^/d+]", "",phone_number) 
    if cleaned.startswith("+"):
        digits = cleaned[1:] 
        if digits.startswith("038") and len(digits) >= 9:
            return f"+{digits}" 
        elif len(digits) >= 10: 
            return f"+{digits}" 
        else:
            return f"+38{digits}" 
    else:
        if cleaned.startswith("038") and len(cleaned) >= 9:
            return f"+{cleaned}"
        elif cleaned.startswith("0") and len(cleaned) >= 10:
            return f"+38{cleaned}"
        elif len(cleaned) >= 9:
            return f"+38{cleaned}"
        else:
            return f"+380{cleaned}" 
        
