#!/bin/bash
# Skripti luo .desktop-tiedoston TodistusAppille

# --- Muokkaa nämä ---
APP_NAME="TodistusApp"
PIPEX_BIN="$HOME/.local/bin/todistusapp"    # pipx:n asennuspolku
ICON_PATH="$HOME/koodia/graduprojekti/src/todistusapp/icon.png"  # PNG-kuvake
# ----------------------

DESKTOP_FILE="$HOME/.local/share/applications/todistusapp.desktop"

mkdir -p "$(dirname "$DESKTOP_FILE")"

cat > "$DESKTOP_FILE" <<EOL
[Desktop Entry]
Type=Application
Name=$APP_NAME
Comment=Käynnistä $APP_NAME
Exec=$PIPEX_BIN
Icon=$ICON_PATH
Terminal=false
Categories=Utility;
EOL

chmod +x "$DESKTOP_FILE"

# Päivitä työpöytävalikko
if command -v update-desktop-database >/dev/null 2>&1; then
    update-desktop-database ~/.local/share/applications/ >/dev/null 2>&1
fi

echo "Desktop-tiedosto luotu: $DESKTOP_FILE"
echo "Voit nyt käynnistää sovelluksen valikosta tai työpöydältä."
