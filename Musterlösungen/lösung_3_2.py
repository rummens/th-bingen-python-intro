import random
from typing import List, Dict

alters_liste: List[int] = [25, 27, 30, 35, 40]
namen_dict: Dict[int, str] = {25: "Peter", 27: "Anna", 30: "Hans", 35: "Lisa", 40: "Max"}

# 1. Zufälliges Alter auswählen
alter = random.choice(alters_liste)
print("Das Alter ist:", alter)

# 2. Name anhand des Alters auswählen
name = namen_dict[alter]
print("Der Name ist:", name)