import pandas as pd
from datetime import datetime

print("Starting product update...")

try:
    df = pd.read_csv("chop_search_daily_update.csv")
    df['Last_Updated'] = datetime.now().strftime("%Y-%m-%d %H:%M")
    df.to_csv("chop_search_daily_update.csv", index=False)
    print("CSV updated successfully!")
except Exception as e:
    print(f"Error: {e}")
