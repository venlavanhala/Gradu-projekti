#!/bin/bash
# ===============================================
# TodistusApp – asennus- ja käynnistysskripti
# Tekijä: Venla :)
# ===============================================

APP_NAME="TodistusApp"
BASE_DIR="$(cd "$(dirname "$0")" && pwd)"
SRC_DIR="$BASE_DIR/src"
DIST_DIR="$SRC_DIR/dist"
DESKTOP_FILE="$BASE_DIR/${APP_NAME}.desktop"
ICON_FILE="$BASE_DIR/logo.png"
EXEC_FILE="$DIST_DIR/index"

echo "🔧 Rakennetaan $APP_NAME..."

# Tarkista että PyInstaller on asennettu
if ! command -v pyinstaller &> /dev/null
then
    echo "❌ PyInstaller ei ole asennettu. Asenna komennolla:"
    echo "   pip install pyinstaller"
    exit 1
fi

# Siirry src-kansioon
cd "$SRC_DIR"

# Rakenna ohjelma
pyinstaller --onefile --windowed \
  --add-data "ui.py:." \
  --add-data "activity.py:." \
  --add-data "change_layout.py:." \
  --add-data "textfields.py:." \
  --hidden-import=tkinter \
  --hidden-import=tkinter.ttk \
  index.py

# Tarkista onnistuiko
if [ ! -f "$EXEC_FILE" ]; then
    echo "❌ Rakennus epäonnistui. Tarkista virheet yllä."
    exit 1
fi

echo "✅ Rakennus valmis!"

# Luo .desktop-tiedosto
echo "🧱 Luodaan .desktop-kuvake..."

cat > "$DESKTOP_FILE" <<EOL
[Desktop Entry]
Version=1.0
Type=Application
Name=$APP_NAME
Comment=Käynnistä $APP_NAME
Exec=$EXEC_FILE
Icon=$ICON_FILE
Path=$SRC_DIR
Terminal=false
Categories=Utility;
EOL

# Anna suoritusoikeudet ja tee tiedostosta "trusted"
chmod +x "$DESKTOP_FILE"
gio set "$DESKTOP_FILE" metadata::trusted true 2>/dev/null || true

# Kopioi työpöydälle
cp "$DESKTOP_FILE" ~/Desktop/ 2>/dev/null || true

echo "🎉 $APP_NAME on valmis!"
echo "➡ Voit nyt käynnistää sovelluksen työpöydän kuvakkeesta."
