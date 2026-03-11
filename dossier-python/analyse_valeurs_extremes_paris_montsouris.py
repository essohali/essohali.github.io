import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import genextreme, genpareto

# -------------------------------------------------------------------
# Analyse des valeurs extrêmes de précipitations journalières
# Station NOAA GHCN-Daily : FRM00007156 (PARIS-MONTSOURIS)
# Période d'étude : 1950-01-01 à 2024-12-31
# -------------------------------------------------------------------

def parse_ghcn_dly_prcp(path):
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            sid = line[0:11]
            year = int(line[11:15])
            month = int(line[15:17])
            element = line[17:21]
            if element != "PRCP":
                continue
            for day in range(1, 32):
                start = 21 + (day - 1) * 8
                value = int(line[start:start+5])
                mflag = line[start+5:start+6]
                qflag = line[start+6:start+7]
                sflag = line[start+7:start+8]
                if value == -9999:
                    continue
                try:
                    date = pd.Timestamp(year=year, month=month, day=day)
                except ValueError:
                    continue
                rows.append({
                    "station_id": sid,
                    "date": date,
                    "prcp_mm": value / 10.0,
                    "mflag": mflag.strip(),
                    "qflag": qflag.strip(),
                    "sflag": sflag.strip(),
                })
    return pd.DataFrame(rows).sort_values("date").reset_index(drop=True)

# 1) Chargement des données brutes NOAA
raw = parse_ghcn_dly_prcp("FRM00007156.dly")

# 2) Contrôle qualité et fenêtre d'étude
df = raw[(raw["qflag"] == "")].copy()
df = df[(df["date"] >= "1950-01-01") & (df["date"] <= "2024-12-31")].copy()
df["year"] = df["date"].dt.year

# 3) Statistiques descriptives
print(df["prcp_mm"].describe())
print("\n95e percentile =", round(df["prcp_mm"].quantile(0.95), 2), "mm")
print("99e percentile =", round(df["prcp_mm"].quantile(0.99), 2), "mm")

# 4) Maxima annuels et ajustement GEV
annual = df.groupby("year", as_index=False)["prcp_mm"].max().rename(columns={"prcp_mm":"annual_max_mm"})
shape, loc, scale = genextreme.fit(annual["annual_max_mm"].values)
print("\nParamètres GEV")
print("shape =", shape)
print("loc   =", loc)
print("scale =", scale)

return_periods = [2, 5, 10, 20, 50, 100]
for T in return_periods:
    zT = genextreme.ppf(1 - 1/T, shape, loc=loc, scale=scale)
    print(f"GEV : T={T} ans -> {zT:.2f} mm")

# 5) POT-GPD
u = df["prcp_mm"].quantile(0.95)
exc = df.loc[df["prcp_mm"] > u, "prcp_mm"] - u
xi, _, beta = genpareto.fit(exc.values, floc=0)
years_span = (df["date"].max() - df["date"].min()).days / 365.2425
lambda_u = len(exc) / years_span

def pot_return_level(T_years, u, xi, beta, lambda_u):
    if abs(xi) < 1e-8:
        return u + beta * np.log(lambda_u * T_years)
    return u + (beta / xi) * ((lambda_u * T_years)**xi - 1)

for T in return_periods:
    zT = pot_return_level(T, u, xi, beta, lambda_u)
    print(f"POT-GPD : T={T} ans -> {zT:.2f} mm")

# 6) Graphiques
plt.figure(figsize=(10, 4.8))
plt.plot(df["date"], df["prcp_mm"], linewidth=0.6)
plt.title("Précipitations quotidiennes à Paris-Montsouris")
plt.xlabel("Date")
plt.ylabel("Précipitations (mm)")
plt.show()

plt.figure(figsize=(8, 4.8))
plt.hist(df["prcp_mm"], bins=80)
plt.title("Distribution empirique")
plt.xlabel("Précipitations (mm)")
plt.ylabel("Fréquence")
plt.show()

plt.figure(figsize=(8, 4.8))
plt.plot(annual["year"], annual["annual_max_mm"], marker="o")
plt.title("Maxima annuels")
plt.xlabel("Année")
plt.ylabel("Maximum annuel (mm)")
plt.show()