# Investigating the Genomic Profile of Inherited Prostate Cancer
## Background

Prostate cancer is the second most common cancer in men and a leading cause of cancer-related death worldwide. While hereditary factors account for approximately 20% of cases, the contribution of rare and low-frequency genetic variants remains underexplored. Genome-wide association studies have identified common SNPs with modest risk increases, but the cumulative effect of numerous low-penetrance variants may have a significant impact on disease susceptibility.

## Objectives
This project aims to bridge the gap between studies focusing on common variants and those on extremely rare variants by:
- Investigating the mutational landscape of rare and low-frequency single nucleotide variants.
- Identifying significantly impacted genes linked to PrCa predisposition.
- Detecting enriched biological pathways that may contribute to increased susceptibility.

## Methods Summary
- **Dataset:** WES data from 96 PrCa patients in 45 families.
- **Data Processing:** Quality control, alignment (BWA), duplicate removal (Picard), variant calling (multiple tools), and annotation using ANNOVAR.
- **Gene Analysis:** Significant gene identification using tools like MutSigCV and OncodriveFML.
- **Enrichment Analysis:** Gene set enrichment analysis (GSEA) with DAVID, Enrichr, and g:Profiler to assess pathways via KEGG, Reactome, and Gene Ontology (GO).

## Repository Structure
