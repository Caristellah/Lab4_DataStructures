
# EXERCISE 1: ENGINEERING TEST DATA ORGANIZER

import random
from collections import defaultdict

LAST_NAME = "Ogena"
SEED_NUM = 2
FAVORITE_ARTIST = "Yeng Constantino"
STUDENT_ID = "TUPM-26-7952"  # Replace with your actual ID if needed

def make_rng(offset=0):
    artist_value = sum(
        (i + 1) * ord(char)
        for i, char in enumerate(FAVORITE_ARTIST)
    )
    return random.Random(SEED_NUM + artist_value + offset)

rng = make_rng(1)

sources = ["T1", "T2", "T3", "T4", "T5"]
categories = [
    "TEMPERATURE", "VOLTAGE", "CURRENT", "PRESSURE", "SPEED"
]

records = []
for category in categories:
    for source in sources:
        records.append({
            "category": category,
            "source": source,
            "measurement": round(rng.uniform(25, 48), 2)
        })

# One repeated source/category record
records.append(records[10].copy())

organized = defaultdict(list)
for record in records:
    organized[record["category"]].append(record)

print("=" * 78)
print("ENGINEERING TEST DATA ORGANIZER")
print("=" * 78)
print(f"LAST NAME: {LAST_NAME}")
print(f"ID: {STUDENT_ID}")
print(f"Seed: {SEED_NUM}")
print(f"Favorite Artist: {FAVORITE_ARTIST}")
print(f"Total Records: {len(records)}")

print("\nGENERATED TEST DATA")
print(f"{'NO.':<5}{'CATEGORY':<18}{'SOURCE':<10}{'MEASUREMENT':<15}")

seen = set()
for i, r in enumerate(records, 1):
    key = (r["category"], r["source"])
    flag = "DUPLICATE" if key in seen else ""
    seen.add(key)
    print(
        f"{i:<5}{r['category']:<18}{r['source']:<10}"
        f"{r['measurement']:<15.2f}{flag}"
    )

print("\nCATEGORY SUMMARIES")
print(f"{'CATEGORY':<18}{'SOURCES':<10}{'AVG':<10}"
      f"{'MAX':<10}{'MIN':<10}{'PASS':<8}")

for category in categories:
    values = [r["measurement"] for r in organized[category]]
    passed = sum(30 <= v <= 45 for v in values)

    print(
        f"{category:<18}{len(values):<10}"
        f"{sum(values)/len(values):<10.2f}"
        f"{max(values):<10.2f}{min(values):<10.2f}"
        f"{passed:<8}"
    )

all_values = [r["measurement"] for r in records]
print("\nREPEATED/DISTINCT DATA")
print(f"Total records: {len(records)}")
print(f"Distinct source/category pairs: {len(seen)}")
print(f"Repeated records: {len(records) - len(seen)}")

print("\nORDERED RESULTS (highest measurement first)")
for r in sorted(records, key=lambda x: x["measurement"], reverse=True):
    print(
        f"{r['category']:<18} {r['source']:<5} "
        f"{r['measurement']:.2f}"
    )

print("\nFINAL SUMMARY")
print(f"Total measurements: {len(all_values)}")
print(f"Overall average: {sum(all_values)/len(all_values):.2f}")
print(f"Maximum: {max(all_values):.2f}")
print(f"Minimum: {min(all_values):.2f}")
print("Final Organized and Summarized Test Dataset: COMPLETE")
