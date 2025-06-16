#!/usr/bin/env python3
import csv
import sys

# Dicionário das famílias (45 famílias, 96 amostras)
FAMILIES = {
    "18":  ["HPC18","HPC109","HPC505"],
    "25":  ["HPC8","HPC25"],
    "29":  ["HPC29","HPC77","HPC84"],
    "32":  ["HPC31","HPC32"],
    "33":  ["HPC33","HPC39","HPC56"],
    "52":  ["HPC52","HPC417"],
    "57":  ["HPC57","HPC79","HPC80"],
    "62":  ["HPC21","HPC62"],
    "67":  ["HPC67","HPC110"],
    "102": ["HPC102","HPC107"],
    "112": ["HPC112","HPC124"],
    "120": ["HPC120","HPC397","HPC488"],
    "123": ["HPC123","HPC206","HPC495"],
    "136": ["HPC136","HPC502"],
    "164": ["HPC164","HPC486"],
    "172": ["HPC172","HPC489"],
    "176": ["HPC176","HPC212"],
    "181": ["HPC181","HPC525"],
    "192": ["HPC192","HPC209"],
    "199": ["HPC199","HPC484"],
    "201": ["HPC201","HPC520"],
    "204": ["HPC204","HPC503"],
    "213": ["HPC213","HPC509"],
    "214": ["HPC214","HPC261"],
    "220": ["HPC220","HPC528"],
    "229": ["HPC229","HPC401"],
    "232": ["HPC232","HPC529"],
    "234": ["HPC234","HPC518"],
    "241": ["HPC241","HPC491"],
    "258": ["HPC128","HPC258"],
    "259": ["HPC259","HPC521"],
    "264": ["HPC210","HPC264"],
    "267": ["HPC267","HPC514"],
    "282": ["HPC282","HPC511"],
    "304": ["HPC304","HPC459"],
    "325": ["HPC193","HPC325"],
    "328": ["HPC328","HPC513"],
    "329": ["HPC329","HPC506"],
    "331": ["HPC331","HPC482"],
    "387": ["HPC387","HPC516"],
    "420": ["HPC420","HPC507"],
    "460": ["HPC460","HPC522"],
    "470": ["HPC470","HPC512"],
    "510": ["HPC114","HPC510"],
    "524": ["HPC524","HPC527"],
}

def assign_family(sample_list):
    """Retorna todas as famílias (separadas por virgulas) onde ≥2 membros têm a variante."""
    samples = set(s.strip() for s in sample_list.split(',') if s.strip())
    matched = []
    for fam_id, fam_members in FAMILIES.items():
        if len(samples & set(fam_members)) >= 2:
            matched.append(fam_id)
    return ",".join(matched) if matched else "."

def main(input_csv, output_csv):
    with open(input_csv, newline='') as fin, open(output_csv, 'w', newline='') as fout:
        reader = csv.DictReader(fin)
        # Insere "Family" logo após "Samples"
        fieldnames = []
        for fn in reader.fieldnames:
            fieldnames.append(fn)
            if fn == "Samples":
                fieldnames.append("Family")
        writer = csv.DictWriter(fout, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            row["Family"] = assign_family(row.get("Samples",""))
            writer.writerow(row)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("USO: add_family.py input.csv output.csv")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
