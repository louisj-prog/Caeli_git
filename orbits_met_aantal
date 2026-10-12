import pandas as pd

# Zorg ervoor dat Pandas alle rijen laat zien en niets afkort
pd.set_option('display.max_rows', None)

# Laad de dataset
dataset = pd.read_csv("MODIS_Juli.csv")

# Tel het aantal rijen per idx_utc en sorteer op tijdstempel (chronologisch)
orbit_counts = dataset['idx_utc'].value_counts().sort_index()

print("--- ALLE IDX_UTC'S OP CHRONOLOGISCHE VOLGORDE ---")
print(orbit_counts)
