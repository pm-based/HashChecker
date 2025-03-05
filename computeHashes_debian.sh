#!/bin/bash

# Controllo se è stata fornita una directory, altrimenti usa la corrente
DIR="${1:-.}"

# Output file
OUTPUT_FILE="file_hashes.txt"

# Numero di CPU disponibili su Debian
NUM_JOBS=$(nproc)

# Rimuove il file di output se esiste
rm -f "$OUTPUT_FILE"

# Trova tutti i file, escludendo quelli di macOS e altri file di sistema non necessari
find "$DIR" -type f \
    ! -name ".DS_Store" \
    ! -name "._*" \
    ! -path "*/.Trashes/*" \
    ! -path "*/.Spotlight-V100/*" \
    ! -path "*/.fseventsd/*" \
    ! -path "*/.TemporaryItems/*" \
    ! -path "*/.DocumentRevisions-V100/*" \
    ! -path "*/lost+found/*" -print0 | \
xargs -0 -n 50 -P "$NUM_JOBS" sh -c '
    for FILE in "$@"; do
        HASH=$(sha256sum "$FILE" | awk "{print \$1}")
        REL_PATH="${FILE#'$DIR'/}"  # Metodo alternativo per ottenere il percorso relativo
        echo "$REL_PATH $HASH" >> "'"$OUTPUT_FILE"'"
    done
' _

echo "File di hash generato: $OUTPUT_FILE"