import pandas as pd
from datetime import datetime

# Load your CSV
df = pd.read_csv("chop_search_daily_update.csv")

# Example: You can add logic here later to update prices
# For now, we just add a timestamp column to show it ran
df['Last_Updated'] = datetime.now().strftime("%Y-%m-%d %H:%M")

# Save it back
df.to_csv("chop_search_daily_update.csv", index=False)

print("CSV updated successfully!")
