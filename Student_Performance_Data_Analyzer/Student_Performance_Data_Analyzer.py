
# EXERCISE 2: STUDENT PERFORMANCE DATA ANALYZER

import random
from collections import defaultdict

LAST_NAME = "Ogena"
SEED_NUM = 2
FAVORITE_ARTIST = "Yeng Constantino"
STUDENT_ID = "TUPM-26-7952"  # Replace if needed

def make_rng(offset=0):
    artist_value = sum(
        (i + 1) * ord(char)
        for i, char in enumerate(FAVORITE_ARTIST)
    )
    return random.Random(SEED_NUM + artist_value + offset)

rng = make_rng(2)

students = [f"{LAST_NAME}_S{i}" for i in range(1, 6)]
subjects = [
    "PROGRAMMING", "MATHEMATICS", "ELECTRONICS",
    "PHYSICS", "ENGLISH"
]

records = []
for student in students:
    for subject in subjects:
        records.append({
            "student": student,
            "subject": subject,
            "score": rng.randint(50, 100)
        })

# One missing score
records[4]["score"] = None

# One repeated student-subject record
records.append(records[0].copy())

def performance(score):
    if score is None:
        return "INCOMPLETE"
    if score >= 90:
        return "EXCELLENT"
    if score >= 80:
        return "VERY GOOD"
    if score >= 75:
        return "SATISFACTORY"
    if score >= 60:
        return "NEEDS IMPROVEMENT"
    return "FAILING"

print("=" * 85)
print("STUDENT PERFORMANCE DATA ANALYZER")
print("=" * 85)
print(f"LAST NAME: {LAST_NAME}")
print(f"ID: {STUDENT_ID}")
print(f"Seed: {SEED_NUM}")
print(f"Favorite Artist: {FAVORITE_ARTIST}")
print(f"Total Records: {len(records)}")

print("\nGENERATED PERFORMANCE RECORDS")
print(f"{'NO.':<5}{'STUDENT':<18}{'SUBJECT':<18}"
      f"{'SCORE':<10}{'CATEGORY'}")

seen = set()
duplicate_count = 0
for i, r in enumerate(records, 1):
    key = (r["student"], r["subject"])
    flag = " DUPLICATE" if key in seen else ""
    if key in seen:
        duplicate_count += 1
    seen.add(key)

    score_text = "MISSING" if r["score"] is None else str(r["score"])
    print(
        f"{i:<5}{r['student']:<18}{r['subject']:<18}"
        f"{score_text:<10}{performance(r['score'])}{flag}"
    )

print("\nSTUDENT SUMMARIES")
for student in students:
    scores = [
        r["score"] for r in records
        if r["student"] == student and r["score"] is not None
    ]
    if scores:
        print(
            f"{student:<18} Count={len(scores):<3} "
            f"Average={sum(scores)/len(scores):.2f} "
            f"Highest={max(scores)} Lowest={min(scores)}"
        )

print("\nSUBJECT SUMMARIES")
for subject in subjects:
    scores = [
        r["score"] for r in records
        if r["subject"] == subject and r["score"] is not None
    ]
    if scores:
        print(
            f"{subject:<18} Count={len(scores):<3} "
            f"Average={sum(scores)/len(scores):.2f} "
            f"Highest={max(scores)} Lowest={min(scores)}"
        )

print("\nREPEATED/INCOMPLETE RECORDS")
print(f"Total records: {len(records)}")
print(f"Distinct student-subject pairs: {len(seen)}")
print(f"Repeated records: {duplicate_count}")
print(f"Records with missing scores: "
      f"{sum(r['score'] is None for r in records)}")

print("\nORDERED RESULTS (highest score first)")
valid_records = [r for r in records if r["score"] is not None]
for r in sorted(valid_records, key=lambda x: x["score"], reverse=True):
    print(
        f"{r['student']:<18} {r['subject']:<18} "
        f"{r['score']:<5} {performance(r['score'])}"
    )

print("\nFINAL SUMMARY")
print(f"Valid scores: {len(valid_records)}")
if valid_records:
    scores = [r["score"] for r in valid_records]
    print(f"Overall average: {sum(scores)/len(scores):.2f}")
    print(f"Highest score: {max(scores)}")
    print(f"Lowest score: {min(scores)}")
print("Final Student Performance Report: COMPLETE")