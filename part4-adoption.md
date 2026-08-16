# Part 4: Adoption Strategy
---

## The Approach: Lead with Value, Not Mandates

### 1. Lead with Evidence, Not Evangelism

**Don't:** Hold meetings saying "You should use this standard because documentation matters."

**Do:** Show up with specific data from *their* docs:
- Run the checker on one team's existing how-to guides
- Show them the 3 ERRORs the checker found (from Test 2: missing scaffolding table, no entry point, etc.)
- Let them see their docs flagged for real problems
- Frame it: "Your docs have these gaps. Here's a tool that catches them automatically."

**Why this works:** People adopt tools that solve *their* problems, not organizational problems. The checker isn't a burden; it's a gift that finds bugs they didn't know existed.

---

### 2. Make It Friction-Free to Adopt

**Remove every barrier to getting started:**

```bash
# One command to validate their docs
python3 part3_docs_checker.py my-docs.md --json

# One template to follow
cp template-how-to-guide.md my-new-guide.md

# One GitHub Actions workflow to add
cp .github/workflows/docs-validate.yml your-repo/.github/workflows/
```

**Start small:** Don't ask them to rewrite all their docs at once. Propose: "Add the checker to your CI. Going forward, new docs follow the standard. Existing docs get a grace period."

**Provide escape hatches:** Add a `# DOC-SKIP: checker` comment to explicitly skip checks if needed. This gives teams control and prevents "that tool is too strict" complaints.

---

### 3. Address the Ignorer Team (The One That Doesn't Care)

**Scenario:** One team's docs are messy, they know it, they don't care. They have a backlog and "docs quality" isn't on it.

**Don't:** Complain to leadership. That signals you can't drive adoption.

**Do:** Find the real lever:
- Dig into why they ignore it. Is it: too busy? Don't see the value? Don't trust the checker?
- For "too busy": Frame it as saving time. "Your dev team spends 2 hours onboarding per person because your docs are unclear. The checker + template saves 30 minutes per person, per year."
- For "don't see value": Run the checker on their docs. Show them real violations. Let a junior engineer try to follow their guide and struggle. They'll see the problem.
- For "don't trust the tool": Let them reject violations explicitly. Build in a review step: "Is this a real problem?" If they mark it as false positive 3x, it's probably a rule that needs refinement, not a team that's being stubborn.

**The nuclear option (use only if necessary):** If a team genuinely blocks adoption org-wide, escalate up—but *only* with data: "Team X's docs have 8 unfixed violations. New onboarded engineers report X issue because Y is missing. Here's the cost." Let leadership decide if it's worth forcing. (But this should be rare if you've done steps 1–2 well.)

---

### 4. Build Momentum with Early Adopters

**Find the team that gets it first.** Maybe they already care about docs quality. They'll adopt, find value, tell other teams. Use them as your proof:

- **Public wins:** Celebrate when teams adopt. "Team A is now using DOC-SKILL-001. They reduced onboarding docs bugs by 40% in the first month."
- **Showcase improvements:** Show the before/after of a team's docs after adopting the standard.
- **Make adopters heroes:** Send a message to the org: "Team B just joined DOC-SKILL-001. Check out their improved guides."

Social proof beats mandates every time.

---

### 5. Measure Adoption, Not Compliance

**Wrong metric:** "X% of teams are using the checker."

**Right metrics:**
- Violations caught and fixed per week (trending down = improvement)
- Doc-to-run latency (time from page load to first code execution)
- New hire onboarding time with updated docs vs. old docs
- "Docs are clear" rating in post-launch surveys

When people see these metrics trending in the right direction, they *want* to adopt.

---

## Summary: The Adoption Playbook

1. **Show value first** — Run the checker on their existing docs, show real violations
2. **Make it easy** — One command, one template, one workflow
3. **Provide control** — Allow teams to mark violations as false positives; refine rules based on feedback
4. **Lead with early adopters** — Find one team that cares, let them prove the value
5. **Use data, not mandates** — Let metrics speak; leadership only intervenes with clear ROI
6. **For the ignorer team** — Understand why they're ignoring it, address the real blocker (time, trust, or value), and only escalate if it blocks org-wide adoption

**The core insight:** You're not trying to force compliance. You're trying to make docs quality *obvious* and *easy*. Once that happens, teams adopt not because they have to, but because it solves their problem.

---

## Implementation Timeline

| Week | Action | Goal |
|------|--------|------|
| 1-2 | Run checker on 5 high-traffic docs, share results with each team | Establish value with data |
| 3-4 | Partner with one early-adopter team, help them implement | Proof of concept |
| 5-6 | Showcase their improvements, publish metrics | Social proof |
| 7-8 | Open adoption to all teams, provide templates + training | Scale |
| 9+ | Monitor metrics, refine rules based on feedback, celebrate adopters | Iterate |

This approach trades speed for durability. You might not get 100% adoption fast, but the teams that *do* adopt will stay adopted because the value is real.
