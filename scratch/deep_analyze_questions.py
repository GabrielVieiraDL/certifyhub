import json, re, glob, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Check both parsed sets
with open('scratch/lotes_parsed.json', 'r', encoding='utf-8') as f:
    az900 = json.load(f)

with open('scratch/az104_parsed.json', 'r', encoding='utf-8') as f:
    az104 = json.load(f)

def analyze_multi(qs, name):
    print(f"\n=================== ANALYZING {name} ({len(qs)} questions) ===================")
    
    # 1. Statements that mention multiple answers
    keywords = ['escolha duas', 'escolha três', 'escolha 2', 'escolha 3', 'quais duas', 'quais três', 
                'quais dois', 'quais 2', 'quais 3', 'selecione duas', 'selecione três', 'selecione 2', 'selecione 3',
                'duas opções', 'três opções', 'dois componentes', 'duas responsabilidades', 'duas ações',
                'cada resposta correta apresenta', 'each correct answer']
    
    flagged = []
    for q in qs:
        stmt_lower = q['statement'].lower()
        matched_kw = [kw for kw in keywords if kw in stmt_lower]
        
        # Check how many options are marked correct
        correct_opts = [o for o in q['options'] if o['isCorrect']]
        
        flagged.append({
            "number": q['number'],
            "keywords": matched_kw,
            "correctCount": len(correct_opts),
            "correctLetters": q.get('correctLetters', [o['letter'] for o in correct_opts]),
            "statement": q['statement'],
            "type": q['type']
        })
    
    has_kw_multi_correct = [f for f in flagged if f['keywords'] and f['correctCount'] > 1]
    has_kw_single_correct = [f for f in flagged if f['keywords'] and f['correctCount'] <= 1]
    no_kw_multi_correct = [f for f in flagged if not f['keywords'] and f['correctCount'] > 1]
    
    print(f"Questions explicitly asking for multiple options AND have >1 correct answers: {len(has_kw_multi_correct)}")
    print(f"Questions asking for multiple options BUT currently only have 1 correct answer: {len(has_kw_single_correct)}")
    print(f"Questions with >1 correct answers without explicit keyword: {len(no_kw_multi_correct)}")
    
    if has_kw_single_correct:
        print(f"\nPotential mismatches in {name} (asks for multiple but has single):")
        for m in has_kw_single_correct:
            print(f"  Q#{m['number']}: Keywords={m['keywords']}, Correct={m['correctLetters']}")
            print(f"     Stmt: {m['statement'][:130]}...")

analyze_multi(az900, "AZ-900")
analyze_multi(az104, "AZ-104")
