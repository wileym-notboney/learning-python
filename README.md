# Python Curriculum — Week 1

A 7-day beginner Python curriculum built around a real capstone project:
a command-line tool that controls your Home Assistant smart home.

By the end of the week you'll type commands like this in your terminal and
watch your actual lights respond:

```bash
home lights bedroom off
home sensors temperature
home scene "evil tv"
```

---

## Table of Contents

1. [What's in this repo](#whats-in-this-repo)
2. [Before you start — one-time setup](#before-you-start--one-time-setup)
3. [The week at a glance](#the-week-at-a-glance)
4. [How each day works](#how-each-day-works)
5. [The daily git ritual](#the-daily-git-ritual)
6. [How evaluations work](#how-evaluations-work)
7. [Setting up the capstone project](#setting-up-the-capstone-project)
8. [Troubleshooting](#troubleshooting)

---

## What's in this repo

```
learning_python/
├── week-1/
│   ├── day-1-foundations/
│   ├── day-2-control-flow/
│   ├── day-3-data-structures/
│   ├── day-4-functions/
│   ├── day-5-oop/
│   ├── day-6-apis/
│   └── day-7-capstone/
├── cheatsheets/
│   ├── syntax.md          ← Python quick reference
│   ├── git-cheatsheet.md  ← the 6 git commands you need all week
│   └── ha-api-reference.md ← Home Assistant API reference for the capstone
└── home-cli/              ← the capstone project (Day 7)
```

Each day folder looks like this:

```
day-1-foundations/
├── README.md      ← start here — concepts explained with examples
├── resources.md   ← videos, articles, and docs to read/watch
├── worksheet.md   ← fill-in exercises to check your understanding
├── lab/
│   ├── lab.md           ← the coding challenge for the day
│   └── solution/        ← reference solution (peek if you're stuck)
└── my-work/
    └── notes.md         ← YOUR notes, worksheet answers, and lab code go here
```

**The only folder you write in is `my-work/`.** Everything else is read-only
curriculum material.

---

## Before you start — one-time setup

You only need to do this once, before Day 1.

### 1. Check that Python is installed

Open your terminal and run:

```bash
python3 --version
```

You should see something like `Python 3.13.x`. If you see an error, download
Python from [python.org](https://www.python.org/downloads/).

### 2. Install `uv`

`uv` is a modern Python package manager — it handles installing libraries and
managing your Python environment. It's what the industry uses.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then close and reopen your terminal so the new command is available. Verify it
worked:

```bash
uv --version
```

### 3. Clone this repo (if you haven't already)

If you're reading this on GitHub and haven't downloaded the repo yet:

```bash
git clone git@github.com:wileym-notboney/learning-python.git
cd learning-python
```

If you already have it locally, just `cd` into it:

```bash
cd /Users/skeletor/DEV/learning_python
```

### 4. Verify your setup

Run this to confirm Python works through `uv`:

```bash
uv run python --version
```

You should see a Python version printed. You're ready.

---

## The week at a glance

| Day | Topic | Capstone connection |
|-----|-------|---------------------|
| 1 | Foundations — variables, types, print/input | Understanding the data HA sends back |
| 2 | Control Flow — if/elif, loops, comprehensions | Filtering devices by state or type |
| 3 | Data Structures — lists, dicts, sets | Parsing real HA JSON responses |
| 4 | Functions & Modules | Organizing CLI commands as clean functions |
| 5 | Classes & OOP | Modeling HA devices as Python objects |
| 6 | HTTP, APIs & Files | Calling the HA REST API with `httpx` |
| 7 | Capstone Build Day | Building `home-cli` end to end |

Each day builds on the one before it. Don't skip ahead.

---

## How each day works

Follow this order every day. It's not arbitrary — each step prepares you for
the next one.

### Step 1 — Create your branch

Before you do anything else, create a git branch for the day. This keeps your
work organized and makes evaluations possible.

```bash
git checkout main
git checkout -b day-1-foundations
```

Replace `day-1-foundations` with the name for the day you're starting (see the
full list in `cheatsheets/git-cheatsheet.md`).

### Step 2 — Read the README

Open `week-1/day-N-<topic>/README.md`. This is the lesson for the day. It
explains the concepts in plain English with code examples. Read it fully before
doing anything else.

### Step 3 — Check the resources

Open `resources.md` for the day. It has hand-picked videos and articles. You
don't need to consume everything — skim the list and watch or read what looks
useful for solidifying the concepts from the README.

### Step 4 — Work through the worksheet

Open `worksheet.md`. This is a series of fill-in-the-blank and predict-the-
output exercises. Do it in your `my-work/notes.md` file — write your answers
there, not in the worksheet itself.

To run Python snippets as you work through it:

```bash
uv run python
```

This opens an interactive Python session. Type code and hit Enter to run it.
Type `exit()` when you're done.

### Step 5 — Do the lab

Open `lab/lab.md`. This is the main coding challenge for the day. You'll
write a Python script from scratch.

Save your script in `my-work/` — for example, `my-work/status.py` for Day 1.

To run your script:

```bash
uv run python week-1/day-1-foundations/my-work/status.py
```

If you get stuck, re-read the README hints in the lab file. If you're really
stuck, peek at `lab/solution/` — but try for at least 20 minutes first.

### Step 6 — Fill in your notes

Open `my-work/notes.md` and jot down:
- What clicked today
- What confused you
- Any questions you have

This is the most important input for your evaluation. Even a few bullet points
help a lot.

### Step 7 — Commit and evaluate

See [The daily git ritual](#the-daily-git-ritual) and
[How evaluations work](#how-evaluations-work) below.

---

## The daily git ritual

Git is how you save your work and how evaluations happen. You only need 4
commands. Do them in this order at the end of every day.

### 1. Make sure you're on the right branch

```bash
git status
```

The first line will say something like `On branch day-1-foundations`. If it
says `main`, you need to switch first:

```bash
git checkout day-1-foundations
```

### 2. Stage your work

This tells git which files to include in your save. Always stage the
`my-work/` folder for the day you just finished:

```bash
git add week-1/day-1-foundations/my-work/
```

### 3. Commit — take the snapshot

```bash
git commit -m "day 1: foundations — worksheet and lab complete"
```

The message in quotes is for your future self. Keep it in the format above,
just swap out the day number and topic.

### 4. Evaluate

Tell Claude Code:

```
evaluate day 1
```

That's it. Claude reads your `my-work/` folder, checks your work against the
lab requirements, and gives you feedback.

---

### Branch names for the whole week

| Day | Branch name |
|-----|-------------|
| 1 | `day-1-foundations` |
| 2 | `day-2-control-flow` |
| 3 | `day-3-data-structures` |
| 4 | `day-4-functions` |
| 5 | `day-5-oop` |
| 6 | `day-6-apis` |
| 7 | `day-7-capstone` |

---

## How evaluations work

At the end of each day, after you've committed your work, say:

```
evaluate day N
```

Claude Code will:
1. Read your `my-work/` folder on the branch you just committed
2. Compare your work against the lab requirements for the day
3. Give you specific, written feedback on what you got right and where to dig deeper
4. Flag anything to review before moving to the next day

**You do not need a perfect score to move on.** The point is to learn, not to
pass a test. Even if something didn't click, the evaluation will tell you exactly
what to focus on.

Day 7 evaluation is different — it's a full week retrospective. Claude reviews
all your day branches together and gives you a recommendation for what to work
on next.

---

## Setting up the capstone project

The `home-cli` project lives in the `home-cli/` folder. You won't touch it
until Day 7, but here's how to get it running when that day comes.

### 1. Navigate into the project

```bash
cd home-cli
```

### 2. Create your `.env` file

The CLI needs to know where your Home Assistant is and how to authenticate with
it. Copy the example file:

```bash
cp .env.example .env
```

Then open `.env` in a text editor and fill in your values:

```
HA_URL=http://your-home-assistant-ip:8123
HA_TOKEN=your_long_lived_access_token
```

**How to get your token:**
1. Open Home Assistant in your browser
2. Click your username in the bottom-left corner
3. Scroll to "Long-Lived Access Tokens" at the bottom
4. Click "Create Token", give it a name (e.g. `home-cli`), copy it

### 3. Install dependencies

```bash
uv sync
```

This downloads and installs all the libraries the project needs (`typer`,
`httpx`, `python-dotenv`).

### 4. Verify it works

```bash
uv run home --help
```

You should see a list of available commands. If you see that, you're ready for
Day 7.

### 5. Run the tests

```bash
uv run pytest
```

---

## Troubleshooting

### "command not found: uv"

Close and reopen your terminal after installing `uv`. If that doesn't fix it:

```bash
source ~/.zshrc
```

### "command not found: python" or "command not found: python3"

Use `uv run python` instead of `python` directly. This ensures you're using
the right version.

### "I accidentally edited a curriculum file (not my-work/)"

Don't panic. Run this to see what changed:

```bash
git diff
```

To undo changes to a specific file you didn't mean to touch:

```bash
git checkout -- week-1/day-1-foundations/worksheet.md
```

### "I'm on the wrong branch"

```bash
git checkout the-branch-you-want
```

If you did work on the wrong branch and need to move it, tell Claude Code what
happened — don't try to fix git yourself yet.

### "git commit failed with a pre-commit hook error"

Read the error message carefully — it usually tells you exactly what to fix.
Copy the error and tell Claude Code if you're unsure.

### "I can't figure out the lab"

1. Re-read the README for the day — the answer is usually in the concepts section
2. Re-read the hints in the lab file
3. Open `lab/solution/` and study the solution — then close it and write your own version from scratch
4. Ask Claude Code: describe what you tried and what happened

### "Something in git went wrong and I don't know what"

Run:

```bash
git status
git log --oneline
```

Copy the output and tell Claude Code. Don't run any git commands you're not
sure about — the situation is almost always recoverable.

---

## A note on looking at solutions

The `lab/solution/` folders exist for when you're genuinely stuck, not as a
shortcut. The best learning happens when you struggle with a problem, make
attempts, and then look at the solution to compare approaches.

Copying the solution and committing it defeats the purpose of the evaluation
system — the eval looks at whether you understood the concepts, not just whether
the code is correct.

Try first. Struggle a little. Then look.
