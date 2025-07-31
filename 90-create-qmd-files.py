# Minimal script to create .qmd files with a YAML header

files = {
    "01-pm-ai-era.qmd": "AI Era PM & LLM Intro",
    "02-llms-prompt-engineering.qmd": "LLMs & Prompting",
    "03-product-innovation-process.qmd": "Product Innovation",
    "04-value-prop-validation.qmd": "Value Prop & Prototyping",
    "05-project-management-jira.qmd": "Jira & Project Mgmt",
    "06-collaboration-git-triad.qmd": "Git & Team Dynamics",
    "07-internet-fundamentals.qmd": "Internet Basics & APIs",
    "08-software-design-principles.qmd": "Software Design Principles",
    "09-ai-dev-platforms.qmd": "AI Dev Tools Overview",
    "10-build-feedback-1.qmd": "Build Session 1",
    "11-product-metrics.qmd": "Product Metrics",
    "12-build-feedback-2.qmd": "Build Session 2",
    "14-final-presentations.qmd": "Final Presentations"
}

for filename, title in files.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"""---
title: "{title}"
---
""")

