import pandas as pd
import re

# Load raw file
df = pd.read_csv("D:/IMDB Project/imdb_scraper/imdb_raw.csv")

# -----------------------------
# 1️⃣ Remove accidental header rows
# -----------------------------
df = df[df["rank"] != "rank"]

# -----------------------------
# 2️⃣ Fix rank
# -----------------------------
df["rank"] = pd.to_numeric(df["rank"], errors="coerce")
df = df.dropna(subset=["rank"])
df["rank"] = df["rank"].astype(int)

# -----------------------------
# 3️⃣ Fix rating & votes
# -----------------------------
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
df["votes"] = pd.to_numeric(df["votes"], errors="coerce")

# -----------------------------
# 4️⃣ Convert duration (PT2H22M → minutes)
# -----------------------------
def convert_duration(duration):
    try:
        if pd.isna(duration):
            return None

        duration = str(duration)

        hours = 0
        minutes = 0

        if "H" in duration:
            hours = int(re.search(r'PT(\d+)H', duration).group(1))
        if "M" in duration:
            minutes = int(re.search(r'(\d+)M', duration).group(1))

        return hours * 60 + minutes

    except:
        return None

df["duration_minutes"] = df["duration"].apply(convert_duration)

# -----------------------------
# 5️⃣ Convert scrape_time safely
# -----------------------------
df["scrape_time"] = pd.to_datetime(df["scrape_time"], errors="coerce")
df = df.dropna(subset=["scrape_time"])

# -----------------------------
# 6️⃣ Save clean file
# -----------------------------
df.to_csv("imdb_clean.csv", index=False)

print("Cleaning completed ✅")