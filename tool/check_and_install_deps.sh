#!/bin/bash
# Verifica deep-translator para tool/translate_carousel_titles.py

echo "🔍 Verificando ambiente Python..."
which python3
python3 --version
echo ""

if python3 -c "from deep_translator import GoogleTranslator" 2>/dev/null; then
    echo "✅ deep_translator já está instalado!"
else
    echo "❌ Instalando deep-translator..."
    python3 -m pip install deep-translator --user || pip3 install deep-translator --user
fi

echo ""
echo "✅ Pronto. Exemplos:"
echo "   python3 tool/translate_carousel_titles.py"
echo "   python3 tool/translate_carousel_titles.py --delay 0.3"
echo "   python3 tool/translate_carousel_titles.py --apps smst,since_us --locales he,nl,sv"
echo "   python3 tool/translate_carousel_titles.py --force"
echo "   python3 tool/translate_carousel_titles.py --force --force-preserved"
