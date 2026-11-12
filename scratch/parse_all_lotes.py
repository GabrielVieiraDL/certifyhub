import glob, re, sys, io, json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

files = sorted(glob.glob('az900-base-conhecimento-lote*.md'))

questions = []
errors = []

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by ### Questão
    blocks = re.split(r'(?=### Questão \d+)', content)
    
    for block in blocks:
        if not block.strip().startswith('### Questão'):
            continue
        
        num_match = re.search(r'### Questão (\d+)', block)
        if not num_match:
            continue
        qnum = int(num_match.group(1))
        
        # Domain
        domain_match = re.search(r'\*\*Domínio:\*\*\s*(.+)', block)
        domain = domain_match.group(1).strip() if domain_match else ""
        
        # Enunciado
        stmt_match = re.search(r'\*\*Enunciado:\*\*\s*(.+?)(?=\n\*\*Opções:\*\*)', block, re.DOTALL)
        if not stmt_match:
            errors.append((qnum, filepath, "Missing Enunciado"))
            continue
        statement = stmt_match.group(1).strip()
        
        # Opções
        opts_match = re.search(r'\*\*Opções:\*\*\s*(.+?)(?=\n\*\*Resposta Correta:\*\*)', block, re.DOTALL)
        if not opts_match:
            errors.append((qnum, filepath, "Missing Opções"))
            continue
        opts_raw = opts_match.group(1).strip()
        
        # Parse individual options: - A) Text or - A. Text
        option_lines = re.findall(r'-\s*([A-E])[\)\.]\s*(.+)', opts_raw)
        if len(option_lines) < 2:
            errors.append((qnum, filepath, f"Invalid options count: {len(option_lines)}"))
            continue
        
        # Resposta Correta
        resp_match = re.search(r'\*\*Resposta Correta:\*\*\s*([A-E\s,]+)', block)
        if not resp_match:
            errors.append((qnum, filepath, "Missing Resposta Correta"))
            continue
        correct_raw = resp_match.group(1).strip()
        # Clean correct answers (e.g. "A, B" or "AB" or "A")
        correct_letters = set(re.findall(r'[A-E]', correct_raw))
        
        # Explicação Técnica
        expl_match = re.search(r'\*\*Explicação Técnica:\*\*\s*(.+?)(?=\n###|\Z)', block, re.DOTALL)
        explanation = expl_match.group(1).strip() if expl_match else f"A resposta correta é {','.join(sorted(correct_letters))}."
        # Remove trailing markdown dividers
        explanation = re.sub(r'\n---.*', '', explanation).strip()
        
        options = []
        for letter, text in option_lines:
            options.append({
                "letter": letter,
                "text": text.strip(),
                "isCorrect": letter in correct_letters
            })
        
        is_multi = len(correct_letters) > 1
        qtype = "MultipleChoice" if is_multi else "SingleChoice"
        
        questions.append({
            "number": qnum,
            "domain": domain,
            "type": qtype,
            "statement": statement,
            "options": options,
            "correctLetters": sorted(list(correct_letters)),
            "explanation": explanation,
            "sourceFile": filepath
        })

print(f"Total parsed questions from lotes: {len(questions)}")
print(f"Errors: {len(errors)}")
for err in errors:
    print("  Error:", err)

# Check domain distribution
from collections import Counter
domain_counts = Counter(q['domain'] for q in questions)
print("\nDomain counts:")
for d, c in domain_counts.items():
    print(f"  {d}: {c}")

with open('scratch/lotes_parsed.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)
