#!/usr/bin/env python3
import pandas as pd

input_csv = "/mnt/f/Projeto_Bioinf/annovar/maf_menos_1_percent/humandb.hg19_multianno_pl_NFE_lt01_with_samples.csv"
output_csv = "/mnt/f/Projeto_Bioinf/annovar/maf_menos_1_percent/potentionaly_pathogenic_2.csv"

df = pd.read_csv(input_csv, low_memory=False)

#Identifica variantes clinvar positivas
clinvar_positive = df['CLNSIG'].isin(['Pathogenic', 'Likely_pathogenic'])

#Preditores de patogenicidade categóricos
cat_preds = [
    'SIFT_pred','Polyphen2_HDIV_pred','LRT_pred',
    'MutationTaster_pred','MutationAssessor_pred',
    'FATHMM_pred','PROVEAN_pred','MetaSVM_pred','MetaLR_pred'
]
cat_count = df[cat_preds].apply(lambda col: col.isin(['D','P','H'])).sum(axis=1)

#Preditores numéricos
num_preds = {'VEST3_rankscore': 0.606, 'CADD_phred': 23.95}
num_count = pd.Series(0, index=df.index)
for col, thr in num_preds.items():
    vals = pd.to_numeric(df[col], errors='coerce')
    num_count += (vals >= thr).fillna(False).astype(int)

pred_count = cat_count + num_count
predictor_filter = pred_count >= 9

#Preditores de conservação
cons_preds = [
    'GERP++_RS_rankscore',
    'phyloP100way_vertebrate_rankscore',
    'phastCons100way_vertebrate_rankscore',
    'SiPhy_29way_logOdds_rankscore'
]
cons_count = pd.Series(0, index=df.index)
for col in cons_preds:
    vals = pd.to_numeric(df[col], errors='coerce')
    cons_count += (vals > 0.50).fillna(False).astype(int)
conservation_filter = cons_count >= 3

# Combina a lógica:
#    - Inclui todas variantes clinvar positivas
#    - Para as restantes, exige predictor_filter & conservation_filter
final_filter = clinvar_positive | (~clinvar_positive & predictor_filter & conservation_filter)

# 7) Subconjunto e grava
filtered = df[final_filter]
filtered.to_csv(output_csv, index=False)

print(f"Filtragem completa: {len(filtered)} variantes guardadas em {output_csv}")
