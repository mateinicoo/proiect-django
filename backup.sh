#!/bin/bash

export PGPASSWORD="matei"

OUTPUT_FILE="fisier.sql"

if [ -f "$OUTPUT_FILE" ]; then
    rm "$OUTPUT_FILE"
fi

echo "Realizăm procesarea tabelelor..."

TABELE=(
    "aplicatie_exemplu_autor"
    "aplicatie_exemplu_editura"
    "aplicatie_exemplu_categorie"
    "aplicatie_exemplu_carte"
    "aplicatie_exemplu_copiecarte"
    "aplicatie_exemplu_oferta"
    "aplicatie_exemplu_antichitate"
    "aplicatie_exemplu_abonament"
    "aplicatie_exemplu_carte_autor"
    "aplicatie_exemplu_comanda"
    "aplicatie_exemplu_utilizator"
    "aplicatie_exemplu_voucher"
)

for t in "${TABELE[@]}"; do
    echo "Tabelul $t"
    
    pg_dump \
        --column-inserts \
        --data-only \
        --inserts \
        -h localhost \
        -U matei \
        -p 5432 \
        -d dj2025 \
        -t "$t" >> "$OUTPUT_FILE"
    
    if [ $? -ne 0 ]; then
        echo "Eroare la procesarea tabelului $t. Oprire."
        exit 1
    fi
done

echo "Procesare terminată. Datele se află în $OUTPUT_FILE"

unset PGPASSWORD