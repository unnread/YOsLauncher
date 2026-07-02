# YOsLauncher
# YosLaunch

Un petit lanceur d'applications créé en Python avec CustomTkinter.

## Fonctionnalités

- Ouvrir Firefox
- Ouvrir VS Code
- Ouvrir un terminal (LXTerminal)
- Interface moderne avec thème sombre

## Capture

Interface simple avec 3 boutons :

- Ouvrir Firefox
- Ouvrir VS Code
- Ouvrir Terminal

## Installation

### Cloner le dépôt

```bash
git clone https://github.com/unnread/YOsLauncher.git
cd YOsLauncher
```

### Installer les dépendances

```bash
pip install customtkinter
```

## Lancement

```bash
python index.py
```

## Configuration

Par défaut le programme utilise :

- Firefox
- VS Code (`code`)
- LXTerminal

Si vous utilisez d'autres applications, modifiez les commandes dans :

```python
subprocess.Popen("firefox")
subprocess.Popen("code")
subprocess.Popen("lxterminal")
```

## Technologies

- Python
- CustomTkinter
- Subprocess

## Version

Version 0

> "La première et la dernière. (quoi que peut etre une mise a jour summer)"

## Auteur

Youness (Yos)

Premier projet de lanceur d'applications réalisé avec Python.
