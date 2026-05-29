# -*- coding: utf-8 -*-
"""Locale key -> Google Translator language code (deep_translator)."""

from typing import Dict, List, Tuple

LOCALE_MAP: Dict[str, str] = {
    'ar': 'ar',
    'bn': 'bn',
    'cs': 'cs',
    'da': 'da',
    'de': 'de',
    'es': 'es',
    'fa': 'fa',
    'fi': 'fi',
    'fil': 'tl',
    'fr': 'fr',
    'ha': 'ha',
    'he': 'iw',
    'hi': 'hi',
    'hu': 'hu',
    'id': 'id',
    'it': 'it',
    'ja': 'ja',
    'ko': 'ko',
    'ms': 'ms',
    'nl': 'nl',
    'no': 'no',
    'pl': 'pl',
    'ro': 'ro',
    'ru': 'ru',
    'sk': 'sk',
    'sv': 'sv',
    'sw': 'sw',
    'th': 'th',
    'tr': 'tr',
    'uk': 'uk',
    'ur': 'ur',
    'vi': 'vi',
    'zh': 'zh-CN',
}

GOOGLE_CODE_OVERRIDES = {
    'fil': 'tl',
    'he': 'iw',
    'zh': 'zh-CN',
}

LOCALES_33: Tuple[str, ...] = tuple(sorted(LOCALE_MAP.keys()))

PT_VARIANTS: Tuple[str, ...] = ('pt', 'pt_BR', 'pt_PT')

LOCALE_TITLE_ORDER: List[str] = ['en', *LOCALES_33, *PT_VARIANTS]
