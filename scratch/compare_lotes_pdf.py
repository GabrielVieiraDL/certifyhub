import json, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('scratch/lotes_parsed.json', 'r', encoding='utf-8') as f:
    lotes = json.load(f)

with open(r'C:\Users\gabri\.gemini\antigravity\brain\33ef2463-6002-4cce-92ff-0598fbb615db\scratch\parsed_questions.json', 'r', encoding='utf-8') as f:
    pdf_qs = json.load(f)

pdf_map = {q['number']: q for q in pdf_qs}
lote_map = {q['number']: q for q in lotes}

print(f"Total in PDF parsed: {len(pdf_qs)}")
print(f"Total in Lotes: {len(lotes)}")

sample_numbers = [2, 7, 10, 443, 451]
for n in sample_numbers:
    print(f"\n================ Question #{n} ================")
    if n in pdf_map:
        print(f"PDF statement: {pdf_map[n]['statement'][:150]}...")
        print(f"PDF answer: {pdf_map[n]['correctAnswer']}")
    else:
        print("PDF: (was skipped in raw PDF extraction because HOTSPOT/DRAG-DROP)")
    
    if n in lote_map:
        print(f"Lote statement: {lote_map[n]['statement'][:150]}...")
        print(f"Lote answer: {lote_map[n]['correctLetters']}")
        print(f"Lote options count: {len(lote_map[n]['options'])}")
        print(f"Lote explanation: {lote_map[n]['explanation'][:120]}...")
