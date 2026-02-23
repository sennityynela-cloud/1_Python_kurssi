pituus=int(input("Minkä pituinen kuha on (senttimetreinä)?"))
import math
if pituus < 37:
    print("Laske kuha takaisin järveen.")
    print(f"Kuha on",37-pituus,"senttimetriä alimmasta sallitusta pyyntimitasta.")