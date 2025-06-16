import sys
from pathlib import Path

# Caminhos de input/output
input_file = sys.argv[1]
output_file = sys.argv[2]
amostra = Path(input_file).stem

with open(input_file, "r") as vcf, open(output_file, "w") as output:
    for line in vcf:

        if line.startswith('#'):
            continue

        col= line.strip().split('\t')
        chrom,pos,ref,alt=col[0], int(col[1]), col[3], col[4]

        alternativos=alt.split(',')

        for alternativo in alternativos:

            if alternativo =='*':
                    continue

            # Cópias para este alternativo
            ref_atual = ref
            alt_atual = alternativo

            #deleção
            if len(ref_atual) > len(alt_atual):
                end = pos + (len(ref_atual) - 1)
                shared_len = len(alt_atual)
                if ref_atual[:shared_len] == alt_atual:
                    alt_atual = '-'
                    ref_atual = ref_atual[shared_len:]
                    start = pos + shared_len
                else:
                    start = pos

            #inserção
            elif len(ref_atual) < len(alt_atual):
                shared_len = len(ref_atual)
                if alt_atual[:shared_len] == ref_atual:
                    ref_atual = '-'
                    alt_atual = alt_atual[shared_len:]
                start = pos
                end = pos

            
            else:
                start=pos
                end=pos

            if not ref_atual:
                ref_atual = '-'
            if not alt_atual:
                alt_atual = '-'


            output.write(f"{chrom}\t{start}\t{end}\t{ref_atual}\t{alt_atual}\t{amostra}\n")
