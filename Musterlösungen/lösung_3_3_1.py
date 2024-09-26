import random
from typing import List, Dict

alters_liste: List[int] = [25, 27, 30, 35, 40]
name_dict: Dict[str, int] = {"Peter": 25, "Anna": 27, "Hans": 30, "Lisa": 35, "Max": 40}

# 1. Zufälliges Alter auswählen
alter = random.choice(alters_liste)
print("Das Alter ist:", alter)

# 2. Name anhand des Alters auswählen
for name, age in name_dict.items():
    if age == alter:
        print("Der Name ist:", name)
        break
