import glob, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

files = sorted(glob.glob('az104-base-conhecimento-lote*.md'))
print('Found files:', len(files))

total_qs = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    matches = re.findall(r'### Questão (\d+)', content)
    first = matches[0] if matches else "None"
    last = matches[-1] if matches else "None"
    print(f'{f}: {len(matches)} questions (Range: {first} to {last})')
    total_qs += len(matches)

print('Total AZ-104 questions across all lotes:', total_qs)
