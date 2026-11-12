import glob, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

for f in ['az900-base-conhecimento-lote1.md', 'az900-base-conhecimento-lote2.md', 'az900-base-conhecimento-lote9.md']:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    # Split by ### Questão
    blocks = re.split(r'(?=### Questão \d+)', content)
    for b in blocks[1:3]:
        print(f"File {f}:")
        print(b[:400])
        print("---")
