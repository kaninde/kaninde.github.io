#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Preenche locale_titles em other_apps_carousel.json para os 33 idiomas do l10n.

Fonte: locale_titles.en ou title_default (inglês).
Por padrão não sobrescreve en, pt, pt_BR e pt_PT se já existirem.

Uso:
  python3 tool/translate_carousel_titles.py
  python3 tool/translate_carousel_titles.py --delay 0.3
  python3 tool/translate_carousel_titles.py --apps smst,pms --locales de,fr,ja
  python3 tool/translate_carousel_titles.py --force
  python3 tool/translate_carousel_titles.py --force --force-preserved
  python3 tool/translate_carousel_titles.py --no-preserve-locales --force
  python3 tool/translate_carousel_titles.py --dry-run
"""

from __future__ import annotations

import argparse
import json
import sys
import threading
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from deep_translator import GoogleTranslator

SCRIPT_VERSION = '1.1'
TOOL_DIR = Path(__file__).resolve().parent
REPO_ROOT = TOOL_DIR.parent
DEFAULT_JSON = REPO_ROOT / 'other_apps_carousel.json'

sys.path.insert(0, str(TOOL_DIR))
from l10n_locale_map import (  # noqa: E402
    GOOGLE_CODE_OVERRIDES,
    LOCALE_MAP,
    LOCALES_33,
    LOCALE_TITLE_ORDER,
    PT_VARIANTS,
)

# Nunca sobrescrever se já tiver valor (a menos que --force-preserved)
PRESERVED_LOCALES_DEFAULT = frozenset({'en', 'pt', 'pt_BR', 'pt_PT'})

# google_play_app_id -> regras de tradução do título
#   keep_en  — copia o inglês (marca/descrição já em EN no catálogo)
#   brand    — mantém prefixo; traduz o resto após ": " ou após "<brand> "
#   suffix   — traduz o núcleo; preserva sufixo literal no final (ex.: ": 1337")
#   full     — traduz o título inteiro (padrão)
APP_RULES: Dict[str, Dict[str, str]] = {
    'tf.samir.kaninde.flutter.pms': {'mode': 'keep_en'},
    'tf.samir.kaninde.kotlin.nutrisync': {'mode': 'keep_en'},
    'tf.samir.kaninde.flutter.smst': {
        'mode': 'suffix',
        'suffix': ': 1337',
    },
    'tf.samir.kaninde.flutter.since_us': {
        'mode': 'brand',
        'brand': 'Since Us',
    },
    'tf.samir.kaninde.flutter.sc.speaker_cleaner': {
        'mode': 'brand',
        'brand': 'Speaker Cleaner',
    },
    'tf.samir.kaninde.flutter.pmb.puppy_magic_ball': {
        'mode': 'brand',
        'brand': 'Puppy Magic Ball',
    },
    'tf.samir.kaninde.flutter.tapago.ta_pago': {
        'mode': 'brand',
        'brand': 'Ta Pago',
    },
    'tf.samir.kaninde.flutter.tasohumi.tasohumi': {
        'mode': 'brand',
        'brand': 'Tasohumi',
    },
    'tf.samir.kaninde.kotlin.util.convertool': {
        'mode': 'brand',
        'brand': 'Convertool',
    },
    # PIX QR Code Generator — mode full (padrão)
}

_translator_cache: Dict[str, GoogleTranslator] = {}
_cache_lock = threading.Lock()


@dataclass
class RunConfig:
    delay: float = 0.3
    quiet: bool = False
    force: bool = False
    force_preserved: bool = False
    preserve_locales: frozenset[str] = PRESERVED_LOCALES_DEFAULT
    dry_run: bool = False
    max_retries: int = 3


CFG = RunConfig()


def google_code(locale: str) -> str:
    return GOOGLE_CODE_OVERRIDES.get(locale, LOCALE_MAP.get(locale, locale))


def get_translator(locale: str) -> GoogleTranslator:
    code = google_code(locale)
    with _cache_lock:
        if code not in _translator_cache:
            _translator_cache[code] = GoogleTranslator(source='en', target=code)
        return _translator_cache[code]


def translate_text(text: str, locale: str) -> str:
    if not text or not text.strip():
        return text
    for attempt in range(CFG.max_retries):
        try:
            out = get_translator(locale).translate(text)
            if CFG.delay > 0:
                time.sleep(CFG.delay)
            return out or text
        except Exception as exc:
            if attempt < CFG.max_retries - 1:
                wait = (attempt + 1) * 2
                if not CFG.quiet:
                    print(f'    ⚠ {locale} retry {attempt + 1}: {exc} ({wait}s)')
                time.sleep(wait)
            else:
                if not CFG.quiet:
                    print(f'    ❌ {locale} fallback EN: {exc}')
                return text
    return text


def split_brand_body(brand: str, en_title: str) -> str:
    if ': ' in en_title:
        head, tail = en_title.split(': ', 1)
        if head == brand:
            return tail
    prefix = brand + ' '
    if en_title.startswith(prefix):
        return en_title[len(prefix) :]
    if en_title == brand:
        return ''
    return en_title


def build_title(app_id: str, en_title: str, locale: str) -> str:
    rule = APP_RULES.get(app_id, {'mode': 'full'})
    mode = rule.get('mode', 'full')

    if mode == 'keep_en':
        return en_title

    if mode == 'suffix':
        suffix = rule['suffix']
        if not en_title.endswith(suffix):
            return translate_text(en_title, locale)
        core = en_title[: -len(suffix)]
        return translate_text(core, locale) + suffix

    if mode == 'brand':
        brand = rule['brand']
        body = split_brand_body(brand, en_title)
        if body == en_title and ': ' not in en_title and not en_title.startswith(brand):
            return translate_text(en_title, locale)
        translated = translate_text(body, locale) if body else ''
        return f'{brand}: {translated}' if translated else brand

    return translate_text(en_title, locale)


def ordered_locale_titles(titles: Dict[str, str]) -> Dict[str, str]:
    out: Dict[str, str] = {}
    seen: set[str] = set()
    for key in LOCALE_TITLE_ORDER:
        if key in titles and titles[key]:
            out[key] = titles[key]
            seen.add(key)
    for key in sorted(titles.keys()):
        if key not in seen and titles[key]:
            out[key] = titles[key]
    return out


def parse_csv(raw: str) -> List[str]:
    return [p.strip() for p in raw.split(',') if p.strip()]


def app_matches_filter(app: Dict[str, Any], tokens: List[str]) -> bool:
    if not tokens:
        return True
    app_id = app.get('google_play_app_id', '')
    ios_id = app.get('ios_bundle_id', '')
    short = app_id.rsplit('.', 1)[-1] if app_id else ''
    haystack = {app_id, ios_id, short}
    for token in tokens:
        if token in haystack or app_id.endswith('.' + token):
            return True
    return False


def resolve_locales(raw: str) -> List[str]:
    if not raw:
        return list(LOCALES_33)
    requested = parse_csv(raw)
    invalid = [loc for loc in requested if loc not in LOCALE_MAP]
    if invalid:
        raise SystemExit(
            f'Locales inválidos: {", ".join(invalid)}\n'
            f'Use um dos 33: {", ".join(LOCALES_33)}'
        )
    return requested


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding='utf-8'))


def save_json(path: Path, data: Dict[str, Any]) -> None:
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + '\n',
        encoding='utf-8',
    )


def needs_translation(titles: Dict[str, str], locale: str) -> bool:
    current = titles.get(locale, '').strip()
    if locale in CFG.preserve_locales and current and not CFG.force_preserved:
        return False
    if CFG.force:
        return True
    return not current


def process_carousel(
    json_path: Path,
    app_filter: List[str],
    locales: List[str],
) -> Tuple[int, int]:
    data = load_json(json_path)
    apps = data.get('apps', [])
    translated_count = 0
    skipped_count = 0

    for index, app in enumerate(apps):
        if not app_matches_filter(app, app_filter):
            continue

        app_id = app.get('google_play_app_id', '')
        titles: Dict[str, str] = dict(app.get('locale_titles') or {})
        en = (titles.get('en') or app.get('title_default') or '').strip()
        if not en:
            if not CFG.quiet:
                print(f'⏭️  App #{index}: sem título EN — pulando')
            continue

        titles.setdefault('en', en)
        pending = [loc for loc in locales if needs_translation(titles, loc)]
        if not pending:
            if not CFG.quiet:
                print(f'✓ {en} — {len(locales)} locale(s) já preenchido(s)')
            skipped_count += 1
            continue

        if not CFG.quiet:
            print(f'\n📱 [{index}] {en}')
            print(f'   id: {app_id}')
            print(f'   traduzir: {len(pending)} locale(s)')

        for locale in pending:
            title = build_title(app_id, en, locale)
            titles[locale] = title
            translated_count += 1
            if not CFG.quiet:
                print(f'   {locale}: {title}')

        app['locale_titles'] = ordered_locale_titles(titles)

        if not CFG.dry_run:
            save_json(json_path, data)
            if not CFG.quiet:
                print('   💾 JSON salvo')

    return translated_count, skipped_count


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description='Traduz title_default / locale_titles.en para os 33 idiomas.',
    )
    p.add_argument(
        '--file',
        type=Path,
        default=DEFAULT_JSON,
        help=f'JSON do carrossel (padrão: {DEFAULT_JSON.name})',
    )
    p.add_argument(
        '--apps',
        default='',
        help='Filtrar apps por sufixo do bundle (ex: smst,pms,since_us)',
    )
    p.add_argument(
        '--locales',
        default='',
        help='Locales separados por vírgula (vazio = 33 idiomas)',
    )
    p.add_argument(
        '--delay',
        type=float,
        default=0.3,
        help='Pausa após cada chamada API (s); use 0.3+ se houver rate limit',
    )
    p.add_argument(
        '--force',
        action='store_true',
        help='Retraduzir chaves existentes nos locales alvo (exceto os preservados)',
    )
    p.add_argument(
        '--force-preserved',
        action='store_true',
        help='Com --force, também retraduz en/pt/pt_BR/pt_PT (ou --preserve-locales)',
    )
    p.add_argument(
        '--preserve-locales',
        default='en,pt,pt_BR,pt_PT',
        help='Locales que não serão sobrescritos se já tiverem valor (padrão: en,pt,pt_BR,pt_PT)',
    )
    p.add_argument(
        '--no-preserve-locales',
        action='store_true',
        help='Não preservar nenhum locale (equivalente a --preserve-locales "")',
    )
    p.add_argument(
        '--dry-run',
        action='store_true',
        help='Não grava o JSON',
    )
    p.add_argument('--quiet', action='store_true', help='Menos saída no console')
    return p


def main() -> None:
    global CFG
    args = build_parser().parse_args()

    if args.no_preserve_locales:
        preserve = frozenset()
    elif args.preserve_locales.strip():
        preserve = frozenset(parse_csv(args.preserve_locales))
    else:
        preserve = frozenset()

    CFG = RunConfig(
        delay=max(0.0, args.delay),
        quiet=args.quiet,
        force=args.force,
        force_preserved=args.force_preserved,
        preserve_locales=preserve,
        dry_run=args.dry_run,
    )

    json_path: Path = args.file
    if not json_path.is_file():
        raise SystemExit(f'Arquivo não encontrado: {json_path}')

    locales = resolve_locales(args.locales)
    app_filter = parse_csv(args.apps)

    print(f'📜 translate_carousel_titles.py v{SCRIPT_VERSION}')
    print(f'   JSON: {json_path}')
    loc_preview = ', '.join(locales) if len(locales) <= 12 else ', '.join(locales[:12]) + ', ...'
    print(f'   Locales: {len(locales)} ({loc_preview})')
    preserve_preview = ', '.join(sorted(CFG.preserve_locales)) or '(nenhum)'
    print(
        f'   delay={CFG.delay}s force={CFG.force} force_preserved={CFG.force_preserved} '
        f'preserve=[{preserve_preview}] dry_run={CFG.dry_run}\n'
    )

    translated, skipped = process_carousel(json_path, app_filter, locales)

    print(f'\n{"=" * 50}')
    print(f'✅ Concluído: {translated} tradução(ões), {skipped} app(s) sem pendência')
    if CFG.dry_run:
        print('(dry-run — nenhuma alteração gravada)')


if __name__ == '__main__':
    main()
