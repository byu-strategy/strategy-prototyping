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
- **Output**: Static HTML website generated to `_book/` directory (configured in `_quarto.yml`)
- **Assets**: Images stored in `images/` directory, copied to output during build
- **Python Engine**: Project uses Jupyter for python code execution (Python 3.12+)
- **Deployment**: Automated via GitHub Actions to GitHub Pages on push to main branch

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
- All chapters are defined in `_quarto.yml` under the `book.chapters` section with three parts: "Course Information", "Topics", and "Resources"
- Chapter files follow naming convention: `##-topic-name.qmd`
- When adding new chapters, update both the file and the YAML configuration
- Two versions exist for some files since two different course sections are taught (e.g., `00-schedule-sandbox.qmd`). APM stands for Associate Product Manager and Sandbox refers to students building their own companies. 

### Creating Presentation Slides
- The project supports RevealJS slide decks from chapter content
- Slide files use naming convention: `##-topic-name-slides.qmd`
- Slide format configuration includes:
  ```yaml
  format:
    revealjs:
      theme: [default, custom.scss]
      slide-number: true
      chalkboard: true
  ```
- Custom slide styling defined in `custom.scss` with BYU branding (navy #002E5D, royal blue #0057B8)
- Render slides with: `quarto render ##-topic-name-slides.qmd`

### File References
- Internal links between chapters use relative paths: `[Link Text](file.qmd)`
- Cross-references to assessments use anchors: `[Link](00-assessments.qmd#section-id)`
- All file references in content must match exactly with actual filenames

## Important Notes

- The project uses Quarto's book format with HTML output
- Bibliography references use `references.bib` with `informs.csl` style
- Custom CSS styling in `styles.css` for book pages
- Custom SCSS styling in `custom.scss` for RevealJS slides (BYU color scheme)
- Header/footer includes via `_header.html` and `_footer.html`
- Python code execution disabled by default (`execute: eval: false` in config)
- When renaming chapter files, update all references in `_quarto.yml`, schedule, assessments, and cross-links
- GitHub Actions workflow (`.github/workflows/publish.yml`) automatically builds and deploys to GitHub Pages on push to main