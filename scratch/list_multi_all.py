import json, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('scratch/lotes_parsed.json', 'r', encoding='utf-8') as f:
    az900 = json.load(f)

with open('scratch/az104_parsed.json', 'r', encoding='utf-8') as f:
    az104 = json.load(f)

print("=== AZ-900 MultipleChoice questions ===")
for q in az900:
    if q['type'] == 'MultipleChoice' or len(q['correctLetters']) > 1:
        print(f"Q#{q['number']}: Type={q['type']}, Correct={q['correctLetters']}")
        print(f"   Stmt: {q['statement'][:100]}...")
        for o in q['options']:
            print(f"     {o['letter']}) [Correct={o['isCorrect']}] {o['text'][:60]}")

print("\n=== AZ-104 MultipleChoice questions ===")
for q in az104:
    if q['type'] == 'MultipleChoice' or len(q['correctLetters']) > 1:
        print(f"Q#{q['number']}: Type={q['type']}, Correct={q['correctLetters']}")
        print(f"   Stmt: {q['statement'][:100]}...")
        for o in q['options']:
            print(f"     {o['letter']}) [Correct={o['isCorrect']}] {o['text'][:60]}")
