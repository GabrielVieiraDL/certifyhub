import glob, re, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

for num in [8, 33, 34, 255]:
    # find which lote has this question
    for f in sorted(glob.glob('az104-base-conhecimento-lote*.md')):
        with open(f, 'r', encoding='utf-8') as fp:
            txt = fp.read()
        m = re.search(rf'(### Questão {num:03d}\s*\n[\s\S]*?)(?=### Questão|\Z)', txt)
        if m:
            print(f"=== File: {f} - Questão {num} ===")
            print(m.group(1))
            print()
            break
