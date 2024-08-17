#!/bin/bash

# Répertoire des logs
LOG_DIR="/home/kkmagloire/Documents/fic-dev/Automation/logs"

# Préfixe du nom du fichier de log
LOG_PREFIX="mon_log"

# Trouver le plus grand numéro de fichier existant
LATEST_LOG=$(ls ${LOG_DIR}/${LOG_PREFIX}[0-9]*.log 2>/dev/null | sort -V | tail -n 1)

if [ -z "$LATEST_LOG" ]; then
    # Aucun fichier de log trouvé, commencer avec 1
    NEXT_LOG_NUM=1
else
    # Extraire le numéro du dernier fichier de log et incrémenter
    LATEST_LOG_NUM=$(echo "$LATEST_LOG" | grep -o '[0-9]*' | tail -n 1)
    NEXT_LOG_NUM=$((LATEST_LOG_NUM + 1))
fi

# Définir le nouveau nom de fichier de log
LOG_FILE="${LOG_DIR}/${LOG_PREFIX}${NEXT_LOG_NUM}.log"

# Exécuter le script Python et rediriger la sortie vers le nouveau fichier de log
python3 /home/kkmagloire/Documents/fic-dev/Automation/rpa.py > "$LOG_FILE" 2>&1

