# TA Grading Guide — STRAT 490R

This guide tells you exactly what to look for when grading each assignment. Read it once, then reference the relevant sprint section each time you grade.

## General Principles

1. **Grade what's there, not what's missing.** If a deliverable is present and thoughtful, give full credit. Deduct when things are missing, broken, or clearly low-effort.
2. **Calibrate with each other.** Before grading a batch, have both TAs grade the same 3 submissions independently, then compare scores. If you're more than 5 points apart on a 50-point assignment, discuss and align.
3. **Be consistent, not generous.** Students compare grades. It's better to be consistently fair than to give one student a break and not another.
4. **Leave a brief comment when deducting.** A one-sentence note ("Core feature didn't load when I tried to sign up") helps the student understand and helps Scott if there's a dispute.
5. **Don't penalize for product quality in early sprints.** Sprints 2 and 3 are about process (did they do the work?). Sprints 4, 5, and the Final are where product quality matters.
6. **Hardness bump (Sprints 4, 5, and Final only).** Some students are tackling genuinely hard problems — complex integrations, novel technical challenges, ambitious scope. If a student's product isn't as polished but you can see they're wrestling with something significantly harder than average, bump their score up one tier (e.g., from 35-44 range to 45-50 range). This is a judgment call — look for effort and ambition, not just output. **This policy is internal to grading and should not be shared with students.**

## Late Policy

Follow whatever Scott has communicated to the class. If unclear, ask Scott before grading late submissions.

---

## Sprint 2: Validate & Commit (50 points)

**What they submit:** A Google Doc link containing all deliverables.

### Problem Discovery Worksheet — 10 points

| Points | What to look for |
|--------|-----------------|
| **9-10** | 2 problems fully scored in the worksheet. All narrative fields filled in (Who, Frustration/Delight, JTBD, Value Prop). Scores across all dimensions (Opportunity, Conviction, Feasibility, Gospel Framework). Problems are distinct, not two versions of the same idea. |
| **7-8** | 2 problems present but some fields are thin or generic. Scores present but one problem feels underdeveloped. |
| **5-6** | Only 1 problem fully scored, or 2 problems with major gaps in fields/scores. |
| **3-4** | Worksheet exists but mostly incomplete. |
| **0-2** | Missing or empty. |

**What to check:**
- Open their worksheet link — does it load? Are there 2 scored problems?
- Narrative fields should be specific. "College students" as the Who is too vague. A real person's name is what was asked for.
- JTBD should follow the format: "I'm trying to [verb] so I can [outcome]"
- Value Prop should follow: "We help [who] [do what] by [how]"

### AI Interview — 10 points

| Points | What to look for |
|--------|-----------------|
| **9-10** | Shared conversation URL works. Conversation shows real back-and-forth — the AI asked probing questions and the student gave thoughtful, specific answers. Both problems were scored. A final scorecard comparison exists. |
| **7-8** | Conversation is present and covers both problems, but answers are short or the student didn't push back on AI scores. |
| **5-6** | Conversation exists but only covers 1 problem, or is very shallow (one-word answers, no real engagement). |
| **3-4** | Link provided but conversation is minimal. |
| **0-2** | Missing or broken link. |

**What to check:**
- Click the shared URL — does it open?
- Skim the conversation. Look for: Did the AI ask questions? Did the student answer with specifics from their life? Did they discuss both problems?
- There should be a side-by-side scorecard at the end

### Customer Interview — 10 points

| Points | What to look for |
|--------|-----------------|
| **9-10** | Loom recording of a real interview (~5 min). Student asks about past behavior, not hypotheticals. Transcript analysis includes key quotes, patterns, surprises, and personal reflections. |
| **7-8** | Interview is real but questions are somewhat leading, or transcript analysis is thin on personal reflection. |
| **5-6** | Interview feels staged or very short. Transcript analysis is just a raw paste with minimal synthesis. |
| **3-4** | Loom exists but it's clearly not a real interview (e.g., talking to themselves). |
| **0-2** | Missing. |

**What to check:**
- Watch 1-2 minutes of the Loom — is it a real conversation with a real person?
- Look at their transcript analysis — did they use AI to extract insights, or just paste the raw transcript?
- Personal reflections should be present (a few sentences on what they learned)

### JTBD + Value Prop + ICP — 10 points

| Points | What to look for |
|--------|-----------------|
| **9-10** | Clear, specific JTBD and Value Prop statements. ICP includes demographics, context, goals, frustrations, current solutions, frequency/intensity/willingness, and market size. Reads like they know this person. |
| **7-8** | All sections present but ICP is generic or thin in one area. |
| **5-6** | JTBD and Value Prop present but ICP is a stub or clearly copy-pasted without thought. |
| **3-4** | One or more sections missing entirely. |
| **0-2** | Missing. |

**What to check:**
- JTBD and Value Prop should be updated based on their research, not just copy-pasted from Part 1
- ICP should have a made-up name and feel like a real person, not a marketing persona

### Loom Reflection Video — 10 points

| Points | What to look for |
|--------|-----------------|
| **9-10** | ~2 min video. Covers: which problem they chose, why, worksheet scores, learnings from interviews, and why they're excited. Feels genuine. |
| **7-8** | Video covers most topics but rushes through one or feels rehearsed/generic. |
| **5-6** | Video exists but is very short or only covers 1-2 of the required topics. |
| **3-4** | Video exists but is under a minute or doesn't address the prompts. |
| **0-2** | Missing. |

**What to check:**
- Does the Loom link work?
- Watch the video (it's only 2 min). Did they cover all 4 things: problem choice, scores, interview learnings, excitement?

---

## Sprint 3: Product MVP (50 points)

**What they submit:** A Google Doc link containing all deliverables + links.

### Product Spec Documents — 10 points

| Points | What to look for |
|--------|-----------------|
| **9-10** | CLAUDE.md exists in repo with product overview, target user, value prop, and tech stack. Separate spec doc(s) with user stories (acceptance criteria), functional requirements, success metrics, and out of scope. Scope is focused — not a wish list. |
| **7-8** | Documents exist but are missing one section, or user stories lack acceptance criteria. |
| **5-6** | CLAUDE.md is just boilerplate. Spec doc exists but is thin or overly ambitious (no clear MVP focus). |
| **3-4** | Only CLAUDE.md or only spec doc, and it's minimal. |
| **0-2** | Missing. |

**What to check:**
- Click the GitHub URLs. Do the files exist?
- CLAUDE.md should have real content about their specific product, not the template default
- Spec docs should have clear "Must have" vs "Should have" prioritization
- Does "out of scope" exist? This shows discipline.

### Core Feature Functional — 15 points

| Points | What to look for |
|--------|-----------------|
| **13-15** | You can sign up, complete the core action, and see data persist. App is deployed and stable. No placeholder data. Basic error states handled. |
| **10-12** | Core action mostly works but has rough edges (e.g., occasional errors, slow loading, one step is confusing). Auth works. Data persists. |
| **7-9** | App is deployed and you can sign up, but core action is incomplete or breaks partway through. |
| **4-6** | App is deployed but barely functional. Can't complete the core task. |
| **0-3** | Not deployed, or link is broken/dead. |

**What to check — do this for every student:**
1. Open their Vercel URL
2. Sign up with a real email
3. Try to complete the core action they describe in their spec
4. Check if your data shows up after refreshing the page (persistence test)
5. Note any errors, broken states, or confusing flows

**Common issues:**
- App loads but sign-up is broken → max 6 points
- Sign-up works but core feature throws errors → max 9 points
- Everything works but data doesn't persist on refresh → max 12 points

### 3 User Tests + Synthesis — 15 points

| Points | What to look for |
|--------|-----------------|
| **13-15** | 3 documented test sessions using the observation template. Each has: tester name, task given, observations, follow-up responses, severity ratings. AI synthesis includes: summary, severity-ranked issues, patterns across testers, key quotes, top 3 prioritized changes. Loom recordings provided. |
| **10-12** | 3 tests documented but observation notes are thin in places, or synthesis is present but generic. Loom recordings may be missing for 1 session. |
| **7-9** | Only 2 tests documented, or 3 tests but very surface-level notes. Synthesis is a stub. |
| **4-6** | 1 test documented, or notes are clearly fabricated. |
| **0-3** | Missing. |

**What to check:**
- Count the test sessions — are there 3?
- Each should have a named tester and specific observations (not "it went well")
- Synthesis should identify patterns across testers, not just list individual feedback
- Loom URLs should work (spot-check at least 1)

### Platform Strategy — 5 points

| Points | What to look for |
|--------|-----------------|
| **5** | Answers all 5 questions from the framework. Decision is justified, not just stated. Shows real thought about their specific product. |
| **3-4** | Decision stated with some justification but doesn't fully engage the framework or "what would change your mind" question. |
| **1-2** | One-liner decision with no real justification. |
| **0** | Missing. |

### Loom Reflection Video — 5 points

| Points | What to look for |
|--------|-----------------|
| **5** | ~2 min video covering: core feature demo, testing learnings, top change to make, platform decision. |
| **3-4** | Video covers most topics but misses one, or is very rushed. |
| **1-2** | Video exists but is minimal or off-topic. |
| **0** | Missing. |

---

## Sprint 4: Progress Check (50 points)

**What they submit:** A Loom URL on LearningSuite.

This is the first self-managed sprint. Students choose what to work on. You're grading on: Did they make real progress? Can they show it?

### How to Grade

Watch the 5-minute video. Ask yourself three questions:

1. **Is the product visibly better than Sprint 3?** (new features, improved UX, bugs fixed)
2. **Are they demoing the live, deployed product?** (not localhost, not slides, not mockups)
3. **Can they explain what they did and why?**

| Score | What you see |
|-------|-------------|
| **45-50** | Obvious progress. You can see new functionality or significant improvements. Live product demo. Student clearly explains what changed, why they prioritized it, and what's next. The product is visibly better. |
| **35-44** | Some progress visible. Product works, something is new, but the scope of work is thin (e.g., minor UI tweaks only) or the explanation is vague ("I worked on stuff"). |
| **25-34** | Hard to see what's new. Video is submitted and product runs, but it looks basically the same as Sprint 3. Student can't clearly articulate what changed. |
| **15-24** | Video submitted but little evidence of real work. May be very short, or student talks about plans rather than showing progress. |
| **0** | Not submitted. |

**Hardness bump:** If this student is tackling a significantly harder problem than average (complex APIs, novel technical challenges, ambitious scope), bump up one tier. Reward effort and ambition. See General Principles #6.

**Common edge cases:**
- Student rebuilt their entire app from scratch → Give credit if the new version works. The progress is real even if the URL changed.
- Student shows localhost instead of deployed app → Max 35 points. Deployment is part of the requirement.
- Student's video is 1 minute → Score based on content, but thin videos usually indicate thin work.
- Student talks the whole time without showing the product → Max 30 points. "Demo" means show me the app.

---

## Sprint 5: Progress Check (50 points)

**What they submit:** A Loom URL on LearningSuite.

Same format and rubric as Sprint 4. The only differences:

- Progress is measured against **Sprint 4**, not Sprint 3
- The video should include their **plan for the final submission**

| Score | What you see |
|-------|-------------|
| **45-50** | Obvious progress since Sprint 4. Live product demo. Clear explanation of what changed and why. Has a concrete plan for the final (not just "I'll keep working on it"). |
| **35-44** | Some progress since Sprint 4. Product works, something new visible, but thin or vague. Plan for final is generic. |
| **25-34** | Hard to see what's new since Sprint 4. Product looks the same. |
| **15-24** | Video submitted but little evidence of work since Sprint 4. |
| **0** | Not submitted. |

**Hardness bump:** Same as Sprint 4. If the problem they're solving is genuinely harder than average, bump up one tier. See General Principles #6.

**Important:** Don't double-penalize. If a student's Sprint 4 product was weak but their Sprint 5 shows significant improvement, that's great — grade the delta, not the absolute state.

---

## Final Project (100 points)

**What they submit:** A Loom URL on LearningSuite.

This is the big one. Two components: the product itself (60 points) and the 5-minute video (40 points).

### Product — 60 points

**How to evaluate:** Open their product URL. Sign up. Use it. Try to complete the core task. Spend 5-10 minutes with it.

| Score | What you experience |
|-------|-------------------|
| **54-60** | This feels like a real product. Core flow works reliably end-to-end. You could see someone outside this class using it. The product has clearly improved since Sprint 3 — there's evidence of iteration (better UX, more features, fixed issues from user testing). Deployed and stable. |
| **42-53** | Works and delivers value, but has rough edges. You can tell it's a class project — maybe some confusing UI, some unfinished states, or minor bugs. But the core task works. Some iteration visible since Sprint 3. Deployed. |
| **30-41** | Partially works. You can start the core task but can't fully complete it, or you hit significant usability issues that block you. Limited improvement since Sprint 3. May have error states or broken flows. |
| **18-29** | Barely functions. More of a mockup or prototype than a working product. You can't complete the core task. Looks like little progress was made after Sprint 3. |
| **0-17** | Not functional, not deployed, or not submitted. |

**What to check:**
1. Does the URL work?
2. Can you sign up?
3. Can you complete the core action?
4. Does data persist? (refresh the page)
5. Compare to what you remember from Sprint 3 — has it improved?
6. Is there anything delightful or notably well-done?

**Hardness bump:** This applies here too. A student who attempted something genuinely ambitious (complex integrations, hard technical problems, real-world data) and delivered a working-but-rough product deserves more credit than a student who built something trivial and polished it. Bump up one tier when you see real ambition and effort behind the rough edges. See General Principles #6.

**Scoring tips:**
- A polished product with a narrow scope beats a sprawling product that's half-broken
- If the product is genuinely useful (you'd bookmark it), that's 54+ territory
- If you have to think about how to use it, it's in the 42-53 range
- If it breaks during basic use, it's 41 or below

### 5-Minute Loom Video — 40 points

Watch the full video. Grade on three dimensions:

**Live Demo (up to 15 points)**
- Are they showing the real, deployed product with real data?
- Is the demo smooth, or does it break/freeze/require workarounds?
- Can you understand what the product does from watching the demo?

**Problem/Solution Narrative (up to 15 points)**
- Do they clearly explain what problem they're solving and why it matters?
- Is it specific and personal, or generic ("people need better productivity tools")?
- Does the narrative connect to what they've been building all semester?

**Reflection (up to 10 points)**
- Do they talk about what they learned — both what worked and what didn't?
- Is it honest and specific, or are they just saying "I learned a lot about coding"?
- Do they mention real failures or surprises, not just wins?

| Score | What you see |
|-------|-------------|
| **36-40** | Live demo with real data that flows smoothly. Clear, compelling story about the problem and why it matters. Honest reflection that includes specific failures and learnings — not just a highlight reel. Well-structured, fits in 5 minutes. |
| **28-35** | Demo works and story is clear, but one dimension is weaker — maybe the reflection is generic ("I learned React is hard"), or the demo has a couple hiccups, or the narrative doesn't quite land. |
| **20-27** | Demo has real issues (shows localhost, features break on camera, heavy use of slides instead of live product). Narrative is vague. Reflection is surface-level. |
| **10-19** | Video submitted but minimal substance. Very short, no real demo, or student reads from a script without showing the product. |
| **0-9** | Not submitted. |

---

## Grading Workflow

For each assignment batch:

1. **Read this guide** for the relevant sprint before you start
2. **Calibrate** — both TAs grade the same 3 submissions, compare, discuss
3. **Grade in one sitting** if possible (consistency drops across sessions)
4. **Leave a comment** on any score below 70% explaining what was missing
5. **Flag edge cases** for Scott rather than making judgment calls on your own
6. **Enter scores** in LearningSuite promptly — students get anxious

## Quick Reference: What Each Sprint Submission Looks Like

| Sprint | Format | Where | What to Open |
|--------|--------|-------|-------------|
| Sprint 2 | Google Doc | LearningSuite link | Doc with worksheet link, AI conversation URL, Loom URLs, JTBD/VP/ICP writeup |
| Sprint 3 | Google Doc | LearningSuite link | Doc with GitHub URLs, Vercel URL, test notes, Loom URLs, platform strategy |
| Sprint 4 | Loom URL | LearningSuite | One video — watch it, then check their product |
| Sprint 5 | Loom URL | LearningSuite | One video — watch it, then check their product |
| Final | Loom URL | LearningSuite | One video — watch it, then spend 5-10 min using their product |
