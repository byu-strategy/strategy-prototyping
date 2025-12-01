# Sprint 4: Code Base Teardown & Architecture Analysis

**Learning Objectives**

By completing this assignment, you will:

1. **Reverse engineer** your own application to deeply understand its architecture
2. **Document** how all components work together using visual diagrams
3. **Teach back** your understanding through clear verbal explanation

**Expected Time Required**: 3-4 hours (2-3 hours analysis/documentation, 1 diagramming and video explanation)

**Points**: 40 points (8% of your grade)

**Overview**

You've built an MVP with a frontend, backend, database, and payment integration. Now it's time to **deepen your understanding of what you've created**.

This assignment asks you to:

1. **Dissect** your codebase using Claude Code. 
2. **Create an annotated architecture diagram** showing how everything connects
3. **Record a 2-3 minute video** walking through your diagram and explaining your app's architecture

**Why This Matters**: As a product manager working with engineers, you need to understand system architecture to make informed decisions about features, technical debt, scalability, and resource allocation. This assignment bridges the gap between "I built something with AI" and "I understand how systems work."

**Step 1: Code Base Analysis (AI-Assisted)**

Use Claude Code to analyze your codebase. Run the following 4 prompts to save the responses as markdown files. **Then read the newly created markdown files carefully, take the time to ask your preferred AI follow-up questions about things you don't understand.**

**Prompt 1: Project Structure Analysis**

```markdown
Analyze my project structure and provide:
1. A complete list of all directories and their purposes
2. The role of each major file in the codebase
3. Which files are frontend, backend, configuration, or deployment-related
4. A count of total lines of code (excluding dependencies/node_modules)

Format this as a clear outline I can reference and save it as a new markdown file called code-base-analysis.md. Explain things simply to a brand new beginner who is on a fast track to becoming a world class engineer.
```

**Prompt 2: Data Flow Analysis**

```markdown
Trace the complete data flow in my application:
1. What happens when a user first loads the app? (step-by-step)
2. What happens when a user performs the main action in my app? (trace from UI click to database and back)
3. Where does user authentication happen?
4. Where does payment processing happen?
5. What data is stored in the database and why?

Show me the flow with specific file names and function names. Save this as a new markdown file called data-flow-analysis.md. Explain things simply to a brand new beginner who is on a fast track to becoming a world class engineer.
```

**Prompt 3: Architecture Pattern Identification**

```markdown
Analyze my application architecture and identify:
1. What architectural pattern am I using? (e.g., MVC, client-server, serverless, monolith)
2. How is my code organized? (e.g., by feature, by layer, mixed)
3. What are the main components/modules and how do they interact?
4. Which parts of my code handle which responsibilities? (UI, business logic, data access, authentication, payments)
5. Are there any architectural anti-patterns or code smells I should be aware of?

Explain in terms I can understand as a product manager learning technical concepts. Save this as a new markdown file called architecture-pattern.md
```

**Prompt 4: Dependency Mapping**

```markdown
Create a comprehensive list of:
1. All external services my app depends on (Vercel, Supabase, Stripe, etc.)
2. All major libraries/packages and what they do
3. All API endpoints in my backend (list each route and its purpose)
4. All database tables and their relationships
5. Any third-party integrations

For each dependency, explain WHY it's needed and what would break if it failed. Save this as a new markdown file called dependency-mapping.md
```

**Step 2: Create an Architecture Diagram of your App**

Now use what you've learned from the AI responses to create a **visual architecture diagram**. You have two options:

**Option A: AI-Generated Diagram**

**Run the following prompt in Claude Code**

```markdown
Based on our analysis, create a visual architecture diagram for my application using Mermaid syntax.

The diagram should show:
1. Frontend components (user interface, forms, displays)
2. Backend API routes and their purposes
3. Database tables and what data they store
4. External services (Vercel, Supabase, Stripe, etc.)
5. Data flow arrows showing requests and responses
6. Authentication flow
7. Payment flow

Use the engineering landscape diagram style with clear sections for:
- Application Architecture (Frontend/Backend)
- Languages & Frameworks used
- External Services
- Database Schema
- Request/Response flows

Make it detailed enough to explain to a technical interviewer.
```

The AI will generate Mermaid code. Then ask:

```markdown
Convert this Mermaid diagram to a visual format I can export as a PNG or PDF.
OR
Show me how to render this Mermaid code as an image using an online tool.
```

**Option B: Manual Diagram Creation**

If you prefer to create the diagram manually, use any of the following tools or another one you prefer:

- [Mermaid Live Editor](https://mermaid.live/) - paste Mermaid code, export as PNG
- [Excalidraw](https://excalidraw.com/) - hand-drawn style diagrams
- [draw.io](https://app.diagrams.net/) - professional diagrams
- PowerPoint/Google Slides - if you prefer manual creation

M



**Visual Style:**
- Use arrows to show direction of data flow
- Include labels and short descriptions where needed for clarity
- Make it visually clear and uncluttered

**Step 3: Video Walkthrough and Explanation**

Create a **2-3 minute video recording with screen share** where you walk through your architecture diagram and explain your application's architecture.

**Recording Tools (choose one):**

- **Loom** (recommended) - Free, easy, browser-based recording
- **Zoom** - Record yourself with screen share
- **QuickTime** (Mac) - Built-in screen recording

**What to Cover in Your Video**

Your video should address the following (think of it as teaching this to a classmate who hasn't seen your app):

**Introduction** (15-20 seconds)

- Brief description of what your app does

**Architecture Overview** (30-40 seconds)

- Screen share your diagram and explain the main sections

**Data Flow Walkthrough** (60-80 seconds)
Pick ONE main user action and trace it through the entire system:

**Example**: "Let me explain what happens when a user signs up and makes their first purchase..."

1. **User Action**: "User clicks 'Sign Up' on the frontend"
2. **Frontend → Backend**: "The form sends a POST request to my `/api/signup` endpoint"
3. **Authentication**: "The backend uses Supabase Auth to create the user account"
4. **Database**: "User data is stored in the `users` table with their email and password"
5. **Payment Flow**: "When they click 'Subscribe', we redirect to Stripe Checkout"
7. **Backend → Database**: "The backend updates the `subscriptions` table with their payment status"
8. **Response → Frontend**: "The user is redirected back to the app and sees their dashboard"

**Key Insights** (20-30 seconds)

- Mention one thing you learned from doing this analysis
- Mention one architectural decision you discovered about your app and why it matters
- Optional: Mention one thing you'd improve if you rebuilt this

**Submission**

Submit via LearningSuite:

1. **Video Link** - A file containing your video or a link to it
2. **Analysis Files** - All 4 markdown files: `code-base-analysis.md`, `data-flow-analysis.md`, `architecture-pattern.md`, `dependency-mapping.md`

**Note**: Your architecture diagram should be shown in your video, so no separate diagram file is needed.

**Grading Rubric (40 Points Total)**

| **Category** | **Description** | **Points** |
|--------------|-----------------|------------|
| **Analysis Files** | All 4 markdown files submitted with comprehensive analysis showing deep investigation of codebase | **0-20** |
| **Technical Understanding in Video** | Demonstrates clear understanding of architecture and accurately traces data flow through system | **0-10** |
| **Diagram Quality (shown in video)** | Diagram is visible, comprehensive, and clearly shows frontend, backend, database, services, and data flows | **0-10** |
| | | **Total: 40** |

This assignment assesses:

- **Learning Outcome 4**: Create a digital product that delivers value to a target customer group
  - By demonstrating deep understanding of your own product's technical architecture
  - By documenting system design decisions
  - By communicating technical concepts clearly

**Remember**: The goal of this assignment is not to prove your app is perfectly architected. The goal is to demonstrate that you **understand how software systems work** by analyzing, documenting, and explaining the system you've built.

This is a critical skill for product managers who need to have technical conversations with engineering teams, make informed decisions about features and timelines, and understand the implications of architectural choices.
