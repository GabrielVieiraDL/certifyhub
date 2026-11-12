import json, sys, io, re
from collections import Counter

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('scratch/lotes_parsed.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

print(f"Total questions in lotes: {len(qs)}")

def normalize(s):
    return re.sub(r'\s+', ' ', s.lower().strip())

seen_stmt = {}
dupes_exact = []
repeated_scenario = []

for q in qs:
    stmt = normalize(q['statement'])
    opts = '|'.join(normalize(o['text']) for o in q['options'])
    full = f"{stmt}##{opts}"
    
    if full in seen_stmt:
        dupes_exact.append((q['number'], seen_stmt[full]))
    else:
        seen_stmt[full] = q['number']

print(f"Exact duplicates (identical statement and identical options): {len(dupes_exact)}")
for d in dupes_exact:
    print(f"  Q{d[0]} is exact duplicate of Q{d[1]}")

opt_counts = Counter(len(q['options']) for q in qs)
print(f"\nOption count distribution: {dict(opt_counts)}")

correct_counts = Counter(len(q['correctLetters']) for q in qs)
print(f"Correct answer counts (single vs multi): {dict(correct_counts)}")

has_no_correct = [q for q in qs if not any(o['isCorrect'] for o in q['options'])]
print(f"Questions where no option is marked correct: {len(has_no_correct)}")
if has_no_correct:
    for q in has_no_correct[:5]:
        print(f"  Q{q['number']}: correctLetters={q['correctLetters']}")
