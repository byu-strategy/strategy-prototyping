# STRAT 490R - Chapter Outline Reference

## Overview

- **Total Chapters:** 12
- **Chapters with Quizzes:** 10 (Chapters 1-10)
- **Chapters without Quizzes:** 2 (Chapters 11-12, build/presentation weeks)
- **Format:** Each chapter integrates PM/Strategy + Build content

---

## Chapter Summary Table

| Ch | Title | Quiz | Read By | Focus |
|----|-------|------|---------|-------|
| 1 | Product Management in the AI Era | Q1 | Week 2 | PM history, AI disruption, CLI setup |
| 2 | Problems Worth Solving | Q2 | Week 3 | Why products fail, problem thinking |
| 3 | Problem Discovery | Q3 | Week 4 | JTBD, interviews, Git |
| 4 | Validating Opportunities | Q4 | Week 5 | Evaluation, commitment, Supabase intro |
| 5 | Building Your MVP | Q5 | Week 6 | MVP scoping, database, PRDs |
| 6 | Testing with Users | Q6 | Week 7 | Usability, iteration, APIs |
| 7 | Platform Strategy | Q7 | Week 8 | Web vs mobile, Capacitor |
| 8 | Measuring What Matters | Q8 | Week 9 | Metrics, analytics |
| 9 | Go-to-Market | Q9 | Week 10 | Distribution, launch, landing pages |
| 10 | Business Models | Q10 | Week 11 | Pricing, Stripe, monetization |
| 11 | Sustainable Code | – | Week 12 | Tech debt, testing, growth |
| 12 | Final Presentations | – | Week 14 | Storytelling, pitch, demo |

---

## File Structure

```
01-pm-ai-era.qmd                  ← Update existing
02-problems-worth-solving.qmd     ← New
03-problem-discovery.qmd          ← New
04-validating-opportunities.qmd   ← New
05-building-your-mvp.qmd          ← New
06-testing-with-users.qmd         ← New
07-platform-strategy.qmd          ← New
08-measuring-what-matters.qmd     ← New
09-go-to-market.qmd               ← Update existing
10-business-models.qmd            ← Update existing
11-sustainable-code.qmd           ← New
12-final-presentations.qmd        ← Update existing
```

---

## Supporting Files (Already Exist)

| File | Purpose | Status |
|------|---------|--------|
| index.qmd | Course welcome/syllabus | Exists - update as needed |
| 00-schedule.qmd | Daily schedule | Updated |
| 00-assessments.qmd | Grading, sprints, portfolio requirements | Needs update for new sprint structure |
| styles.css | Custom CSS for book pages | Exists |
| custom.scss | Custom SCSS for RevealJS slides | Exists |
| _header.html | Header includes | Exists |
| _footer.html | Footer includes | Exists |
| references.bib | Bibliography | Exists |

**Resource Files (Appendices):**

| File | Purpose | Status |
|------|---------|--------|
| 95-eng-checklist.qmd | Engineering checklist | Keep |
| 96-code-base-review.qmd | Code review guide | Keep |
| 97-resources.qmd | Additional resources | Update as needed |
| 98-tools.qmd | Tools reference | Merge into new AI tools content |
| 99-prompts.qmd | Prompt library | Update as needed |

**Portfolio Template:**
- https://github.com/byu-strategy/product-management-portfolio

---

## Detailed Chapter Outlines

### CH 1: PRODUCT MANAGEMENT IN THE AI ERA

**File:** `01-pm-ai-era.qmd` (update existing)
**Quiz:** Q1 - Thu Jan 15
**Reading before:** Week 2

#### PM / Strategy Content:
- **What is Product Management?**
  - The PM role defined
  - "CEO of the product" — and critiques
  - Core PM skills (strategy, customer insight, execution, communication)
- **History of Product Management**
  - P&G "Brand Men" (1931)
  - HP formalization (1940s)
  - Agile, Scrum, modern PM
  - Rise of APM programs
  - PM as sought-after career
- **The Product Trio**
  - PM + Designer + Engineer model
  - How AI is disrupting this model
- **AI-Powered PM vs AI Product PM**
  - Using AI as a PM (this course focus)
  - Building AI products
  - The new PM skillset
- **The Opportunity**
  - "Builder's high is back"
  - What we'll build this semester

#### Build Content:
- **The Command Line**
  - Why CLI matters in the AI era
  - Terminal basics (pwd, ls, cd, mkdir, rm, cp, cat, echo)
  - Package managers (Homebrew for Mac, winget for Windows)
  - File/folder naming conventions
  - Gotchas (spaces, case sensitivity, rm permanence)
- **VS Code Setup**
  - Installation
  - Terminal integration
  - Git Bash setup (Windows)
- **Claude Code**
  - What it is and why it matters
  - Installation and authentication
  - Installing dependencies (git, node, python)
  - First interaction
  - Explanatory mode
- **Your First App**
  - Building a simple Streamlit app
  - Experience the AI-assisted workflow

**Chapter Outcome:** Understand PM landscape + development environment fully set up

---

### CH 2: PROBLEMS WORTH SOLVING

**File:** `02-problems-worth-solving.qmd` (new)
**Quiz:** Q2 - Thu Jan 22
**Reading before:** Week 3

#### PM / Strategy Content:
- Why most products fail
- The idea trap (solutions without problems)
- Problem vs solution thinking
- You as the customer — finding problems you feel
- Problem journaling technique

#### Build Content:
- Terminal and CLI practice
- Claude Code basics continued
- Conversational coding introduction
- AI dev tools landscape overview (Lovable, Figma)
- Deploying your first prototype

#### Claude Code Block: Markdown Files
- CLAUDE.md for project context
- Project-specific vs global settings
- Memory management

**Chapter Outcome:** Understand why starting with problems matters + comfortable with basic deployment

---

### CH 3: PROBLEM DISCOVERY

**File:** `03-problem-discovery.qmd` (new)
**Quiz:** Q3 - Thu Jan 29
**Reading before:** Week 4

#### PM / Strategy Content:
- Jobs-to-be-Done framework
- Problem interviews (Mom Test approach)
- Asking good questions
- Interview synthesis techniques
- Building personas from research

#### Build Content:
- Git fundamentals (commits, branches, push/pull)
- Deployment with Vercel / GitHub Pages
- Version control workflow

#### Claude Code Block: Slash Commands
- Built-in commands (/help, /clear, /config)
- Creating custom slash commands
- Storing reusable prompts

**Chapter Outcome:** Know how to discover real problems + deploy code reliably

---

### CH 4: VALIDATING OPPORTUNITIES

**File:** `04-validating-opportunities.qmd` (new)
**Quiz:** Q4 - Thu Feb 5
**Reading before:** Week 5

#### PM / Strategy Content:
- Evaluating opportunities
- Frequency, intensity, willingness to pay
- Opportunity scoring frameworks
- Committing to a problem
- Avoiding premature commitment

#### Build Content:
- Frontend fundamentals (HTML, CSS basics)
- React introduction
- Client-side state and forms
- Supabase introduction and setup
- Authentication (email, OAuth)

#### Claude Code Block: Agents
- Subagents for parallel tasks
- Managing context window
- Task decomposition strategies

**Chapter Outcome:** Can evaluate which problems are worth solving + have auth working

---

### CH 5: BUILDING YOUR MVP

**File:** `05-building-your-mvp.qmd` (new)
**Quiz:** Q5 - Thu Feb 12
**Reading before:** Week 6

#### PM / Strategy Content:
- MVP scoping — what to build first
- Avoiding scope creep
- Feature vs product thinking
- The smallest thing that delivers value
- Writing effective user stories
- PRDs — what they are, when to use them
- AI-assisted PRD generation
- Feature prioritization frameworks

#### Build Content:
- Supabase database fundamentals
- Creating tables and schemas
- Row Level Security (RLS)
- CRUD operations
- Relations and queries
- Views and database functions

**Chapter Outcome:** Can scope an MVP + have data persistence working

---

### CH 6: TESTING WITH USERS

**File:** `06-testing-with-users.qmd` (new)
**Quiz:** Q6 - Thu Feb 19
**Reading before:** Week 7

#### PM / Strategy Content:
- Usability testing basics
- Running effective test sessions
- What to observe and ask
- Synthesizing feedback
- Iteration frameworks
- Responding to feedback without overreacting

#### Build Content:
- Supabase storage (file uploads)
- APIs and integrations overview
- HTTP fundamentals
- Third-party API integration

#### Claude Code Block: Skills
- Combining instructions + code
- Portable, reusable workflows
- Sharing skills across projects

**Chapter Outcome:** Can run user tests and iterate + integrate external services

---

### CH 7: PLATFORM STRATEGY

**File:** `07-platform-strategy.qmd` (new)
**Quiz:** Q7 - Thu Feb 26
**Reading before:** Week 8

#### PM / Strategy Content:
- Web vs mobile decision framework
- When mobile makes sense
- Distribution tradeoffs (web vs app stores)
- PWA as middle ground
- Platform-specific considerations

#### Build Content:
- Progressive Web App (PWA) setup
- Capacitor introduction
- Wrapping web apps for mobile
- Native alternatives overview (Swift, Kotlin, React Native, Flutter)

#### Claude Code Block: Hooks
- Automations that always run
- Pre/post commit hooks
- Validation, formatting, testing gates

**Chapter Outcome:** Can make informed platform decisions + set up automation

---

### CH 8: MEASURING WHAT MATTERS

**File:** `08-measuring-what-matters.qmd` (new)
**Quiz:** Q8 - Thu Mar 5
**Reading before:** Week 9

#### PM / Strategy Content:
- Product metrics fundamentals
- Leading vs lagging indicators
- Choosing what to measure
- Data-informed vs data-driven
- Avoiding vanity metrics
- Building a metrics dashboard

#### Build Content:
- Analytics implementation
- Event tracking setup
- Building dashboards
- Querying data with SQL basics
- Data visualization

**Chapter Outcome:** Have analytics live + understand what metrics matter

---

### CH 9: GO-TO-MARKET

**File:** `09-go-to-market.qmd` (update existing)
**Quiz:** Q9 - Thu Mar 12
**Reading before:** Week 10

#### PM / Strategy Content:
- Go-to-market strategy fundamentals
- Distribution channels
- Launch strategies
- Growth loops introduction
- Positioning and messaging
- Landing page best practices

#### Build Content:
- Landing page creation
- SEO basics (meta tags, structure)
- Supabase edge functions
- Serverless logic
- Conversion optimization basics

**Chapter Outcome:** Have landing page live + GTM plan ready

---

### CH 10: BUSINESS MODELS

**File:** `10-business-models.qmd` (update existing)
**Quiz:** Q10 - Thu Mar 19
**Reading before:** Week 11

#### PM / Strategy Content:
- Business model canvas
- Revenue models
- Pricing strategy
- When and how to charge
- Freemium vs paid vs hybrid
- Unit economics basics

#### Build Content:
- Stripe integration
- Payment flows
- Webhooks and Supabase integration
- Subscription logic

#### Claude Code Block: Plugins
- Sharing workflows with others
- Installing community plugins
- Creating your own plugins

**Chapter Outcome:** Understand business models + have payments working (if applicable)

---

### CH 11: SUSTAINABLE CODE (No Quiz)

**File:** `11-sustainable-code.qmd` (new)
**Reading before:** Week 12
**Purpose:** Build week focus

#### PM / Strategy Content:
- What is tech debt
- Strategic vs accidental debt
- When to pay it down vs ship
- Growth and retention fundamentals
- User lifecycle stages
- Onboarding optimization

#### Build Content:
- Code quality basics
- Linting and formatting
- Testing fundamentals
- Refactoring patterns
- Supabase realtime features
- Live subscriptions and presence

**Chapter Outcome:** Cleaner codebase + understand sustainable development

---

### CH 12: FINAL PRESENTATIONS (No Quiz)

**File:** `12-final-presentations.qmd` (update existing)
**Reading before:** Week 14
**Purpose:** Presentation prep

#### PM / Strategy Content:
- Storytelling for products
- Pitch structure
- Demo best practices
- Handling Q&A
- Retrospective frameworks

#### Build Content:
- Demo preparation
- Performance polish
- Edge case handling
- Final deployment checklist
- Production readiness

**Chapter Outcome:** Ready to present + product polished

---

## Quiz Schedule

| Quiz | Date | Covers Chapter | Topic |
|------|------|----------------|-------|
| 1 | Thu Jan 15 | Ch 1: PM in the AI Era | PM history, AI-powered PM, CLI basics |
| 2 | Thu Jan 22 | Ch 2: Problems Worth Solving | Why products fail, problem thinking |
| 3 | Thu Jan 29 | Ch 3: Problem Discovery | JTBD, interviews, Git |
| 4 | Thu Feb 5 | Ch 4: Validating Opportunities | Evaluation, commitment, Supabase intro |
| 5 | Thu Feb 12 | Ch 5: Building Your MVP | MVP scoping, database, PRDs |
| 6 | Thu Feb 19 | Ch 6: Testing with Users | Usability testing, APIs |
| 7 | Thu Feb 26 | Ch 7: Platform Strategy | Web vs mobile, Capacitor |
| 8 | Thu Mar 5 | Ch 8: Measuring What Matters | Product metrics, analytics |
| 9 | Thu Mar 12 | Ch 9: Go-to-Market | Distribution, launch strategies |
| 10 | Thu Mar 19 | Ch 10: Business Models | Pricing, monetization, Stripe |

---

## Claude Code Building Blocks Progression

| Block | Chapter | Week | Context |
|-------|---------|------|---------|
| Setup + basics | Ch 1 | 1-2 | First deployment |
| Markdown files | Ch 2 | 2-3 | Project context (CLAUDE.md) |
| Slash commands | Ch 3 | 3-4 | Reusable prompts for interviews/PRDs |
| Agents | Ch 4 | 4-5 | Parallel tasks for full-stack building |
| Skills | Ch 6 | 6-7 | Portable workflows for features |
| Hooks | Ch 7 | 7-8 | Automated validation, pre-commit |
| Plugins | Ch 10 | 10-11 | Sharing workflows |

---

## Supabase Progression

| Topic | Chapter | Week | Context |
|-------|---------|------|---------|
| Setup + auth | Ch 4 | 4-5 | First real product (v0.1) |
| Database, tables | Ch 5 | 5-6 | Data persistence |
| RLS, CRUD | Ch 5 | 5-6 | Security + operations |
| Relations, queries | Ch 5 | 5-6 | Complex data models |
| Views, functions | Ch 5 | 5-6 | Server-side logic |
| Storage | Ch 6 | 6-7 | File uploads |
| Edge functions | Ch 9 | 9-10 | Serverless logic |
| Webhooks | Ch 10 | 10-11 | Stripe integration |
| Realtime | Ch 11 | 11-12 | Live features |

---

## Chapter Template

Each chapter follows this structure:

```markdown
---
title: "Chapter Title"
---

## Why This Matters
Brief framing of the topic (1-2 paragraphs)

## Part 1: The Strategy
PM concepts, frameworks, examples
~15-20 min read

### [Topic 1]
### [Topic 2]
### [Topic 3]

## Part 2: Building It
Technical walkthrough, Claude Code techniques
~10-15 min read + code examples

### [Technical Topic 1]
### [Technical Topic 2]
### [Technical Topic 3]

## This Week's Sprint Work
How this applies to current sprint deliverables

## Key Concepts
Bulleted list of testable concepts (for quiz prep)
```

---

## Existing Files to Reuse/Update

| Existing File | Action | New File |
|---------------|--------|----------|
| 01-pm-ai-era.qmd | Update | 01-pm-ai-era.qmd |
| 02-git-deployment.qmd | Merge into | Ch 3 (03-problem-discovery.qmd) |
| 03-project-management.qmd | Merge into | Ch 5 (05-building-your-mvp.qmd) |
| 04-product-innovation.qmd | Merge into | Ch 2-3 |
| 04-value-prop-design.qmd | Merge into | Ch 3-4 |
| 05-go-to-market.qmd | Update | 09-go-to-market.qmd |
| 06-business-models.qmd | Update | 10-business-models.qmd |
| 07-internet-fundamentals.qmd | Merge into | Ch 6 (APIs section) |
| 08-software-engineering.qmd | Merge into | Ch 5, 11 |
| 09-ai-dev-platforms.qmd | Merge into | Ch 1 |
| 11-product-metrics.qmd | Update | 08-measuring-what-matters.qmd |
| 14-final-presentations.qmd | Update | 12-final-presentations.qmd |
