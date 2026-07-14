#!/usr/bin/env python3
"""Generate samir.tf portfolio HTML from projects.json."""

from __future__ import annotations

import html
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def esc(s: str) -> str:
    return html.escape(s or "", quote=True)


def initials(name: str) -> str:
    parts = [p for p in name.replace(":", " ").split() if p and p[0].isalnum()]
    if not parts:
        return "?"
    if len(parts) == 1:
        return parts[0][:2].upper()
    return (parts[0][0] + parts[1][0]).upper()


def status_label(status: str) -> str:
    return "publicado" if status == "publicado" else "docs"


def play_url(app_id: str | None) -> str | None:
    if not app_id:
        return None
    return f"https://play.google.com/store/apps/details?id={app_id}"


def nav(current: str | None) -> str:
    items = [
        ("projects", "/projects/", "Projetos"),
        ("about", "/about/", "Sobre"),
    ]
    links = []
    for key, href, label in items:
        cur = ' aria-current="page"' if key == current else ""
        links.append(f'<a href="{href}"{cur}>{label}</a>')
    return f"""  <header class="site-header">
    <div class="wrap">
      <a class="brand" href="/">samir.tf</a>
      <nav class="nav" aria-label="Principal">
        {" ".join(links)}
      </nav>
    </div>
  </header>"""


def footer() -> str:
    return """  <footer class="site-footer">
    <div class="wrap">
      <span>© samir.tf — atelier de apps</span>
      <span>
        <a href="/projects/">Projetos</a>
        ·
        <a href="/about/">Sobre</a>
      </span>
    </div>
  </footer>
  <script src="/assets/js/site.js"></script>"""


def head(title: str, description: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="pt">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}">
  <link rel="stylesheet" href="/assets/css/site.css">
</head>"""


def write_index() -> None:
    page = f"""{head("samir.tf — apps, projetos e atelier", "Portfolio pessoal de Samir: apps mobile, projetos e notas sobre o que gosto de construir.")}
<body>
{nav(None)}
  <main>
    <section class="hero wrap" aria-label="Apresentação">
      <div class="hero-grid">
        <div>
          <p class="eyebrow reveal-brand">atelier digital</p>
          <h1 class="hero-brand reveal-brand">samir.tf</h1>
          <div class="reveal-copy">
            <p class="hero-headline">Apps offline-first, ferramentas úteis e experimentos no telemóvel.</p>
            <p class="lede">Um canto para mostrar o que construo, o que me interessa e os projetos em andamento.</p>
            <div class="cta-row">
              <a class="btn btn-primary" href="/projects/">Ver projetos</a>
              <a class="btn btn-ghost" href="/about/">Sobre mim</a>
            </div>
          </div>
        </div>
        <div class="hero-visual reveal-visual" role="img" aria-label="Painel visual abstrato do atelier">
          <span class="hero-visual-label">grid · pulse · craft</span>
        </div>
      </div>
    </section>
  </main>
{footer()}
</body>
</html>
"""
    (ROOT / "index.html").write_text(page)


def write_about() -> None:
    page = f"""{head("Sobre — samir.tf", "Quem sou, o que construo e alguns gostos — página pessoal em samir.tf.")}
<body>
{nav("about")}
  <main class="wrap">
    <header class="page-hero reveal">
      <p class="eyebrow">sobre</p>
      <h1 class="display">Quem está por detrás do samir.tf</h1>
      <p class="lede" style="margin-top:1rem">Construtor de apps mobile, com foco em utilidade, privacidade local e experiências simples.</p>
    </header>

    <section class="page-section about-grid">
      <article class="about-block reveal">
        <h2>O que construo</h2>
        <p>Aplicativos Android/iOS — fitness, utilitários, finanças pessoais, organização e experimentos criativos. Muitos crescem em torno de dados no dispositivo e fluxos offline.</p>
        <p class="placeholder">[placeholder] Uma ou duas frases sobre a stack preferida (ex.: Flutter, Kotlin) e o tipo de problema que mais te motiva a abrir o editor.</p>
      </article>
      <article class="about-block reveal">
        <h2>Como trabalho</h2>
        <p>Prefiro produtos pequenos e bem definidos: uma dor clara, UX rápida, monetização honesta e docs legais no sítio.</p>
        <p class="placeholder">[placeholder] Hábitos de trabalho, ritmo de releases, ou o que evitas ao desenhar um app.</p>
      </article>
    </section>

    <section class="page-section about-block reveal">
      <h2>Gostos</h2>
      <p>Fora do código, o dia a dia mistura treino, música, café e curiosidade técnica.</p>
      <p class="placeholder">[placeholder] Música — géneros, artistas ou playlists que te acompanham a programar.</p>
      <p class="placeholder">[placeholder] Treino / powerlifting — o que treinas, com que frequência, porquê importa.</p>
      <p class="placeholder">[placeholder] Outros interesses (livros, hardware, viagem, cinema…) em 2–3 linhas.</p>
    </section>

    <section class="page-section about-block reveal">
      <h2>Contato</h2>
      <p>Aberturas a feedback, ideas e contactos profissionais.</p>
      <p class="placeholder">[placeholder] E-mail: voce@exemplo.com</p>
      <p class="placeholder">[placeholder] Links: GitHub · LinkedIn · X / Bluesky</p>
      <div class="cta-row">
        <a class="btn btn-primary" href="/projects/">Ver projetos</a>
      </div>
    </section>
  </main>
{footer()}
</body>
</html>
"""
    about_dir = ROOT / "about"
    about_dir.mkdir(exist_ok=True)
    (about_dir / "index.html").write_text(page)


def write_projects(projects: list[dict]) -> None:
    rows = []
    for p in projects:
        st = status_label(p["status"])
        if p["icon_url"]:
            icon = (
                f'<img class="project-icon" src="{esc(p["icon_url"])}" '
                f'alt="" width="48" height="48" loading="lazy">'
            )
        else:
            icon = (
                f'<span class="project-icon-fallback" aria-hidden="true">'
                f'{esc(initials(p["name"]))}</span>'
            )
        rows.append(
            f"""      <li>
        <a class="project-row reveal" href="/projects/{esc(p["slug"])}/">
          {icon}
          <div>
            <h2 class="project-name">{esc(p["name"])}</h2>
            <p class="project-tagline">{esc(p["tagline"])}</p>
          </div>
          <div class="project-meta">
            <span class="status status-{esc(st)}">{esc(st)}</span>
          </div>
        </a>
      </li>"""
        )

    page = f"""{head("Projetos — samir.tf", "Portfolio de apps e projetos publicados ou em documentação em samir.tf.")}
<body>
{nav("projects")}
  <main class="wrap">
    <header class="page-hero reveal">
      <p class="eyebrow">portfolio</p>
      <h1 class="display">Projetos</h1>
      <p class="lede" style="margin-top:1rem">{len(projects)} apps — publicados na Play Store e em desenvolvimento / documentação.</p>
    </header>
    <section class="page-section" aria-label="Lista de projetos">
      <ul class="project-list">
{chr(10).join(rows)}
      </ul>
    </section>
  </main>
{footer()}
</body>
</html>
"""
    projects_dir = ROOT / "projects"
    projects_dir.mkdir(exist_ok=True)
    (projects_dir / "index.html").write_text(page)

    for p in projects:
        write_project_page(p)


def write_project_page(p: dict) -> None:
    slug_dir = ROOT / "projects" / p["slug"]
    slug_dir.mkdir(parents=True, exist_ok=True)
    st = status_label(p["status"])
    if p["icon_url"]:
        icon = (
            f'<img class="project-hero-icon" src="{esc(p["icon_url"])}" '
            f'alt="" width="88" height="88">'
        )
    else:
        icon = (
            f'<span class="project-hero-icon-fallback" aria-hidden="true">'
            f'{esc(initials(p["name"]))}</span>'
        )

    highlights = "\n".join(f"          <li>{esc(h)}</li>" for h in p["highlights"])
    tags = "\n".join(f'        <span class="tag">{esc(t)}</span>' for t in p.get("tags", []))

    play = play_url(p.get("google_play_app_id"))
    ctas = []
    if play:
        ctas.append(
            f'<a class="btn btn-primary" href="{esc(play)}" '
            f'rel="noopener noreferrer" target="_blank">Google Play</a>'
        )
    ctas.append('<a class="btn btn-ghost" href="/projects/">Todos os projetos</a>')

    folder = p["folder"]
    legal = p.get("legal") or {}
    legal_bits = []
    if legal.get("about"):
        legal_bits.append(f'<a href="/{esc(folder)}/{esc(legal["about"])}">About</a>')
    if legal.get("privacy"):
        legal_bits.append(f'<a href="/{esc(folder)}/{esc(legal["privacy"])}">Privacidade</a>')
    if legal.get("terms"):
        legal_bits.append(f'<a href="/{esc(folder)}/{esc(legal["terms"])}">Termos</a>')
    legal_html = " · ".join(legal_bits)

    page = f"""{head(f'{p["name"]} — samir.tf', p["tagline"])}
<body>
{nav("projects")}
  <main class="wrap">
    <a class="back-link" href="/projects/">← Projetos</a>
    <header class="project-hero reveal">
      {icon}
      <div>
        <p class="eyebrow">{esc(st)}</p>
        <h1>{esc(p["name"])}</h1>
        <p class="lede">{esc(p["tagline"])}</p>
        <div class="tag-row">
{tags}
        </div>
        <div class="cta-row">
          {"".join(ctas)}
        </div>
      </div>
    </header>

    <section class="page-section reveal">
      <h2 class="section-title">Destaques</h2>
      <p class="section-lede">O essencial do produto — resumido a partir da documentação pública.</p>
      <ul class="highlight-list">
{highlights}
      </ul>
    </section>

    <section class="page-section reveal">
      <h2 class="section-title">Documentação</h2>
      <p class="section-lede">Páginas oficiais usadas pelas lojas e pelo app (texto legal completo).</p>
      <div class="legal-links">
        {legal_html}
      </div>
    </section>
  </main>
{footer()}
</body>
</html>
"""
    (slug_dir / "index.html").write_text(page)


def main() -> None:
    data = json.loads((ROOT / "projects.json").read_text())
    projects = data["projects"]
    write_index()
    write_about()
    write_projects(projects)
    print(f"Generated home, about, projects index, and {len(projects)} detail pages.")


if __name__ == "__main__":
    main()
