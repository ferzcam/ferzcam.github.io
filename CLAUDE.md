# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Personal academic website for Fernando Zhapa-Camacho, built with Jekyll and hosted on GitHub Pages (`ferzcam.github.io`). Content (publications, talks, news, etc.) is stored as Markdown files in Jekyll collections and rendered by Liquid templates.

## Commands

Serve the site locally:

```
bundle exec jekyll serve
```

Regenerate the CV PDF (run from the `cv/` directory):

```
cd cv && ./get_cv.sh
```

`get_cv.sh` runs the Python scripts in `cv/scripts/` to generate `*_py.tex` files, compiles `cv.tex` with `xelatex`, and moves the output to `assets/cv.pdf` (the file served via the site's CV download link). It requires Python (with PyYAML) and a XeLaTeX installation.

## Architecture

### Content lives in Jekyll collections

Defined in `_config.yml`, each collection is a directory of Markdown files with YAML front matter:

- `_preprints/` — unpublished papers (rendered with a "Preprint" badge).
- `_selected_publications/` — featured papers; shown on both the home page (`index.html`) and `papers.html`.
- `_publications/` — additional papers; shown only under "Additional Publications" on `papers.html`.
- `_talks/`, `_upcoming_talks/` — talks, rendered by `talks.html`.
- `_news/` — home-page news feed (`collection: events`); supports an optional `eventurl` to make the headline a link.
- `_awards/`, `_outreach/`, `_teaching/` — additional content sections.

When a preprint is published, move its file from `_preprints/` to `_selected_publications/` (or `_publications/`) and add `venue:` and `paperurl:` to the front matter. Publication entries support these front-matter keys: `title`, `authors`, `date` (`'Mon YYYY'`), `venue`, `venueurl`, `paperurl`, `arxiv`, `codeurl`, `pubicon`.

The author string `Fernando Zhapa-Camacho` is bolded automatically by the templates (and CV scripts) — keep the name spelled exactly that way in `authors`.

### Pages and templates

`index.html` (home), `papers.html`, and `talks.html` are the top-level pages; navigation is driven by `header_pages` in `_config.yml`. Shared markup is in `_includes/` and the single layout in `_layouts/default.html`. Styles are in `_sass/`.

### The CV shares the website's data

The scripts in `cv/scripts/` (`publications.py`, `talks.py`, `honors.py`, `teaching.py`, `extracurricular.py`) read the same collection Markdown files (e.g. `../../_selected_publications`, `../../_publications`) and emit LaTeX into `cv/cv/*_py.tex`. As a result, updating a publication's front matter and rerunning `get_cv.sh` keeps the website and the CV PDF in sync. Hand-edited LaTeX (e.g. `cv/cv/education.tex`, header fields in `cv/cv.tex`) is not generated from collections and must be edited directly.

## Notes

- `*.md~` files are editor backups; Jekyll ignores them. Do not treat them as content.
- The `_site/` directory is generated output — never edit it by hand.
