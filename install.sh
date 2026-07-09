#!/bin/bash

echo " Summer Assistant - Installation des dépendances Python"
echo "------------------------------------------------------"

if command -v apt >/dev/null 2>&1; then
    echo " Distribution Debian/Ubuntu détectée"

    sudo apt update
    sudo apt install -y git python3 python3-pip python3-venv

elif command -v dnf >/dev/null 2>&1; then
    echo " Distribution Fedora détectée"

    sudo dnf install -y git python3 python3-pip

elif command -v pacman >/dev/null 2>&1; then
    echo " Distribution Arch détectée"

    sudo pacman -Sy --needed git python python-pip

else
    echo " Distribution non supportée"
    echo "Installez manuellement Python 3 et pip."
    exit 1
fi


echo ""
echo " Installation de CustomTkinter..."

python3 -m pip install --user customtkinter


echo ""
echo " Vérification Python..."

python3 - <<EOF
import subprocess
import customtkinter

print("Python OK")
print("Subprocess OK")
print("CustomTkinter OK")
EOF


echo ""
echo " Installation terminée !"
echo ""
echo "Pour lancer votre application :"
echo "python3 main.py"
