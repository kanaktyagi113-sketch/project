from pathlib import Path
import glob
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
raw_file = glob.glob(str(ROOT / "data" / "raw" / "*.xls*"))[0]
print("Raw file:", raw_file)
df = pd.read_excel(raw_file)

for c in ["List Price", "Sales"]:
    df[c] = pd.to_numeric(df[c].astype("string").str.replace(",", ""), errors="coerce")
df["Order Date"] = pd.to_datetime(df["Order Date"], format="%d-%m-%Y", errors="coerce")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="%d-%m-%Y", errors="coerce")
df = df.drop(columns=["Internal Notes"], errors="ignore")

for c in ["City", "Order Priority", "Gift Wrap", "Warehouse Code", "Sales Rep ID"]:
    df[c] = df[c].fillna("Not Given")

df["Month"] = df["Order Date"].dt.to_period("M").dt.to_timestamp()
df["Ship Days"] = (df["Ship Date"] - df["Order Date"]).dt.days

out = ROOT / "data" / "processed"
out.mkdir(parents=True, exist_ok=True)
df.to_csv(out / "ecommerce_sales_clean.csv", index=False)
print("Cleaned data saved:", df.shape)