import glob, re, sys, io, json
from collections import Counter

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

files = sorted(glob.glob('az104-base-conhecimento-lote*.md'))

questions = []
errors = []

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
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
        correct_letters = set(re.findall(r'[A-E]', correct_raw))
        
        # Explicação Técnica
        expl_match = re.search(r'\*\*Explicação Técnica:\*\*\s*(.+?)(?=\n###|\Z)', block, re.DOTALL)
        explanation = expl_match.group(1).strip() if expl_match else f"A resposta correta é {','.join(sorted(correct_letters))}."
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
            "rawDomain": domain,
            "type": qtype,
            "statement": statement,
            "options": options,
            "correctLetters": sorted(list(correct_letters)),
            "explanation": explanation,
            "sourceFile": filepath
        })

print(f"Total AZ-104 parsed questions: {len(questions)}")
print(f"Parsing errors: {len(errors)}")
for err in errors:
    print("  Error:", err)

# Check domain classification
# We want to map each question to one of the 5 official AZ-104 domains:
# 1. Gerenciar identidades e governança do Azure (25%)
# 2. Implementar e gerenciar armazenamento (20%)
# 3. Implantar e gerenciar recursos de computação do Azure (25%)
# 4. Configurar e gerenciar redes virtuais (20%)
# 5. Monitorar e manter recursos do Azure (10%)

def map_domain(raw):
    r = raw.lower()
    if "identidade" in r or "governança" in r or "governance" in r or "entra" in r or "policy" in r or "rbac" in r or "acesso" in r or "permissão" in r:
        return 1
    elif "armazenamento" in r or "storage" in r or "blob" in r or "arquivo" in r or "files" in r or "disco" in r:
        return 2
    elif "computação" in r or "compute" in r or "máquina virtual" in r or "vm" in r or "contêiner" in r or "container" in r or "aks" in r or "app service" in r:
        return 3
    elif "rede" in r or "network" in r or "vnet" in r or "bastion" in r or "load balancer" in r or "gateway" in r or "dns" in r:
        return 4
    elif "monitor" in r or "proteger" in r or "backup" in r or "log" in r or "alerta" in r or "watcher" in r or "manter" in r:
        return 5
    else:
        return 1

for q in questions:
    q['domainId'] = map_domain(q['rawDomain'])

domain_counts = Counter(q['domainId'] for q in questions)
print("\nDomain counts:")
domain_names = {
    1: "Gerenciar identidades e governança do Azure (25%)",
    2: "Implementar e gerenciar armazenamento (20%)",
    3: "Implantar e gerenciar recursos de computação do Azure (25%)",
    4: "Configurar e gerenciar redes virtuais (20%)",
    5: "Monitorar e manter recursos do Azure (10%)"
}
for d_id, count in sorted(domain_counts.items()):
    print(f"  Domínio {d_id}: {domain_names[d_id]} -> {count} questões ({round(count/len(questions)*100, 1)}%)")

# Check for questions with 0 correct options
has_no_correct = [q for q in questions if not any(o['isCorrect'] for o in q['options'])]
print(f"\nQuestions where no option is marked correct: {len(has_no_correct)}")

# Check duplicate statements
def normalize(s):
    return re.sub(r'\s+', ' ', s.lower().strip())

seen = {}
dupes = []
for q in questions:
    stmt = normalize(q['statement'])
    opts = '|'.join(normalize(o['text']) for o in q['options'])
    full = f"{stmt}##{opts}"
    if full in seen:
        dupes.append((q['number'], seen[full]))
    else:
        seen[full] = q['number']

print(f"Exact duplicates: {len(dupes)}")

with open('scratch/az104_parsed.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)
