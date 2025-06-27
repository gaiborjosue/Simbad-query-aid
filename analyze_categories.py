import pandas as pd
from collections import Counter

# Read the CSV file
df = pd.read_csv('otypes_nodes.csv')

# Get unique categories and count them
categories = df['Category'].dropna().unique()
category_counts = Counter(df['Category'].dropna())

print("SIMBAD Object Types - Category Analysis")
print("=" * 50)
print(f"Total number of unique categories: {len(categories)}")
print()
print("Categories found:")
print("-" * 30)

# Sort categories by their numeric prefix
sorted_categories = sorted(categories, key=lambda x: int(x.split('.')[0]) if x.split('.')[0].isdigit() else 999)

for category in sorted_categories:
    count = category_counts[category]
    print(f"{category}: {count} object types")

print()
print("Summary:")
print(f"- Total object types: {len(df)}")
print(f"- Categories with object types: {len([c for c in categories if category_counts[c] > 0])}")
print(f"- Empty categories: {len([c for c in categories if category_counts[c] == 0])}") 