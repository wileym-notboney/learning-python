# Git Cheatsheet — Week 1

You only need 6 commands all week. That's it.

---

## The Daily Loop

### Start of day — create your branch
```bash
git checkout main
git checkout -b day-3-data-structures
```
Replace `day-3-data-structures` with the day you're starting.
Branch names used this week:
- `day-1-foundations`
- `day-2-control-flow`
- `day-3-data-structures`
- `day-4-functions`
- `day-5-oop`
- `day-6-apis`
- `day-7-capstone`

---

### During the day — check what you've changed
```bash
git status
```
Shows which files you've modified. Run this whenever you're curious.

---

### End of day — save your work

**Stage your files** (tell git what to include):
```bash
git add week-1/day-3-data-structures/my-work/
```

**Commit** (save a snapshot with a message):
```bash
git commit -m "day 3: data structures — worksheet and lab complete"
```

---

### If you want to see what you wrote today
```bash
git diff main...day-3-data-structures
```
Shows everything you added compared to the starting point.

---

### If you need to go back to main
```bash
git checkout main
```

---

## What NOT to worry about this week

- Pushing to GitHub (optional, not required for eval)
- Merging branches
- Merge conflicts
- `git pull`, `git fetch`, `git rebase`
- Anything that sounds scary

The only thing that matters is: **branch → work → add → commit → evaluate.**

---

## If Something Goes Wrong

**"I'm on the wrong branch"**
```bash
git checkout the-branch-you-want
```

**"I committed something I didn't mean to"**
— Tell Claude Code what happened. Don't try to fix it yourself yet.

**"git is complaining about something"**
— Copy the error message and tell Claude Code. It's almost certainly fine.
