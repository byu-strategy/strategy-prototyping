# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Quarto book project for **STRAT 490R - Creating Digital Products with AI: Strategy & Prototyping**, a BYU course taught by Scott Murff. The project generates a static website containing course materials, schedules, assessments, and chapter content.

## Architecture

### Content Structure
- **Course Information**: `index.qmd`, `00-schedule.qmd`, `00-assessments.qmd` - Core course logistics and grading
- **Topic Chapters**: Numbered `.qmd` files (01-14) covering course topics from AI/PM basics to final presentations
- **Resources**: `97-resources.qmd`, `98-tools.qmd`, `99-prompts.qmd` - Supplementary materials
- **Configuration**: `_quarto.yml` defines the book structure, chapters order, and output settings

### Build System
- **Primary tool**: Quarto (installed at `/usr/local/bin/quarto`)
- **Output**: Static HTML website generated to `docs/` directory
- **Assets**: Images stored in `images/` directory, copied to `docs/images/` during build

## Common Commands

### Build and Preview
```bash
# Build the entire book
quarto render

# Preview with live reload during development
quarto preview

# Build and serve locally
quarto serve
```

### Chapter Management
- All chapters are defined in `_quarto.yml` under the `book.chapters` section
- Chapter files follow naming convention: `##-topic-name.qmd`
- When adding new chapters, update both the file and the YAML configuration

### File References
- Internal links between chapters use relative paths: `[Link Text](file.qmd)`
- Cross-references to assessments use anchors: `[Link](00-assessments.qmd#section-id)`
- All file references in content must match exactly with actual filenames

## Important Notes

- The project uses Quarto's book format with HTML output
- Bibliography references use `references.bib` with `informs.csl` style
- Custom CSS styling in `styles.css`
- Header/footer includes via `_header.html` and `_footer.html`
- When renaming chapter files, update all references in `_quarto.yml`, schedule, assessments, and cross-links