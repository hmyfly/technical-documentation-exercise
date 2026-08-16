# Part 4: Adoption Strategy

## The Problem

You've built DOC-SKILL-001 (Part 2) and proven it works with a checker (Part 3) that finds real bugs in production docs. But now you need multiple product teams to adopt this standard—and none of them report to you. You have no authority to mandate it. How do you drive adoption across an organization where incentives aren't aligned and competing priorities rule?

The answer: **lead with evidence, not mandates.** Show teams that the standard solves their problems, make adoption trivial, celebrate early wins, and let social proof do the work.

---

## The Five-Point Playbook

**1. Lead with Their Data, Not Your Vision**

Don't hold meetings about documentation quality. Instead, run the checker on one team's existing docs and show up with three concrete errors: missing scaffolding table, no entry point for examples, broken onboarding flow. Let them see the violations. Frame it as: "Your docs have these gaps. Here's a tool that catches them automatically. Want to try it?"

People adopt tools that solve *their* problems, not organizational problems. The checker is a gift that finds bugs they didn't know existed.

**2. Remove Every Friction Point**

Make adoption a three-step copy-paste:
```bash
python3 part3_docs_checker.py my-docs.md --json
cp template-how-to-guide.md my-new-guide.md
cp .github/workflows/docs-validate.yml your-repo/.github/workflows/
```

Propose: "Add the checker to CI going forward. Existing docs get a grace period. No rewrite required today." Provide an escape hatch (`# DOC-SKIP: checker`) so teams can override specific violations. This gives them control and prevents "that tool is too strict" complaints.

**3. Handle the Team That Doesn't Care**

One team will ignore it entirely. Dig into *why*: Are they too busy? Don't see the value? Don't trust the tool?

- **Too busy:** "Your dev team spends 2 hours onboarding per person because docs are unclear. The checker + template saves 30 minutes per person, per year." (Frame it as time saved, not new work.)
- **Don't see value:** Let a junior engineer try to follow their guide. Watch them struggle. They'll see the problem immediately.
- **Don't trust the tool:** Allow explicit rejection of violations. If they mark the same rule as false positive three times, that rule probably needs refinement. Listening to pushback builds credibility.

If a team genuinely blocks org-wide adoption despite these efforts, escalate—but only with clear data: "Team X's docs have 8 critical violations. New hires spend 40% longer onboarding than teams using the standard." Leadership intervenes when ROI is undeniable, not when you're just frustrated.

**4. Find Your First Fan and Amplify Them**

One team will "get it" immediately. Maybe they already care about docs quality. Partner with them for Weeks 3–4. Once they're live and seeing improvements, celebrate them publicly: "Team A reduced onboarding bugs by 40% in the first month. Check out their improved guides." Show before/after. Make adopters heroes. Social proof beats mandates every time.

**5. Measure Impact, Not Compliance**

Wrong metric: "X% of teams are using the checker."

Right metrics:
- **Violations caught per week** (trending down = continuous improvement)
- **Doc-to-first-code latency** (time from page load to working example, target <5 minutes)
- **New hire onboarding time** (measure now, target 20% reduction by Week 12)
- **"Docs are clear" rating** (post-launch survey)

When people see these trending in the right direction, they don't adopt because they have to—they adopt because the value is real and visible.

---

## The Nine-Week Timeline (with Checkpoints)

| Weeks | Action | Success Criteria | If This Fails |
|-------|--------|------------------|---------------|
| 1–2 | Run checker on 5 high-traffic docs; share violations with each team | 3+ teams express interest in trying the standard | Violations are being dismissed as false positives → Rule refinement needed; move to Week 3 with lower false positive bar |
| 3–4 | Partner with one early-adopter team; help them implement in CI | Team reports checker working, adopts for new docs going forward | Adopter finds checker blocking too much → Calibrate rules based on feedback; build false positive suppression into tool |
| 5–6 | Showcase adopter's improvements; publish metrics dashboard | 20% reduction in new-hire onboarding time OR 2+ additional teams interested | No visible improvement yet → Extend timeline to Week 8; measure again |
| 7–8 | Open adoption to all teams; provide templates and training | 50% of teams have integrated checker into CI (new docs only) | Adoption stalling → Identify blockers; one-on-one outreach to resistant teams |
| 9+ | Monitor metrics; iterate rules based on feedback; celebrate adopters | 75%+ of teams using checker; false positive rate <5%; org-wide violations trending down | Violations spiking → Investigate whether new rules are too strict; community vote on controversial rules |

**Key insight:** This trades speed for durability. You won't hit 100% adoption in nine weeks, but the teams that do adopt will *stay* adopted because the value is real.

---

## What Can Go Wrong (and How to Fix It)

**Early adopter finds false positives** → Checker loses credibility org-wide. *Fix:* During Week 3–4, calibrate rules aggressively. Get false positive rate below 5% before scaling to Week 7–8.

**Leadership sees no ROI by Week 8** → Adoption stalls before reaching critical mass. *Fix:* Show interim metrics (Week 5–6 survey results, before/after onboarding time) before making the business case. Frame in leadership terms: "Faster onboarding = faster shipping."

**Resistant team refuses adoption and influences others** → Political blocker. *Fix:* Make adoption opt-in, not mandatory. Celebrate early adopters loudly enough to create FOMO. One resistant team doesn't block progress if ten others are winning.

**Checker becomes stale; rules drift from reality** → Tool loses trust. *Fix:* Tie checker rules to Part 2 (living style guide). Automate a diff check in CI: if Part 2 and Part 3 diverge, fail the build. Rules stay in sync or nobody ships.

---

## The Core Insight

You're not trying to force compliance. You're trying to make documentation quality *obvious* and *easy*. Once that happens, teams don't adopt because they're mandated to—they adopt because it solves the problem they already have: "How do I write docs that actually help people?"

That's durable adoption.
