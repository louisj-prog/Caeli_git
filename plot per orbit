# CAELI - AOD kaart maken

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# 1. Dataset inladen
# -------------------------

dataset = pd.read_csv("MODIS_Juli_810.csv", sep = ';')


# -------------------------
# 2. Kleurenschaal bepalen
# -------------------------

vmin = dataset["optical_depth_055"].quantile(0.01)
vmax = dataset["optical_depth_055"].quantile(0.99)


# -------------------------
# 3. Kaart maken
# -------------------------

plt.figure(figsize=(12, 8))

kaart = plt.scatter(
    dataset["idx_lon"],
    dataset["idx_lat"],
    c=dataset["optical_depth_055"],
    cmap="viridis",
    vmin=vmin,
    vmax=vmax,
    marker="s",
    s=0.5,
    linewidths=0
)

# Stel de longitude (X-as) vast in van 1 tot 10
plt.xlim(1, 10)

# Kleurenbalk
cbar = plt.colorbar(kaart)
cbar.set_label("Optical Depth 0.55 µm")

# Assen
plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.title("Aerosol Optical Depth - Juli 2026")

plt.grid(alpha=0.2)

plt.show()
