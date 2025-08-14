
# Tech Spring Week Applications — Step‑by‑Step Guide

---

## 0) What success looks like
- 15–25 targeted applications (not spray-and-pray)
- A CV with *3–5 quantifiable bullets* (impact, numbers, users, speed)
- Public proof: 2 repos + 1 short write‑up (readme or blog)
- Interview‑ready: 20–30 DSA problems (topic‑tagged), 3 mini “systems” prompts, 8 behavioral stories
- Tracking: hit rate >25% OAs, >10% interviews

---

## 1) Two‑week fast start (do this first)
**Day 1–2 — Positioning**
- Define your **hook** (1 line): `I build X for Y to solve Z (with N users or N% improvement).`
- Choose 2 themes you’ll repeat everywhere:
  - *Builder with impact* (course platform, tooling)
  - *Sharer/leader* (this repo, tutoring)

**Day 3–5 — Proof‑of‑work**
- Publish one **tiny but real** tool:
  - e.g., `course-enrolment-stats-cli` (Node/Java) → reads CSV/MySQL, prints “top courses, avg enrolment”, runs <1s on 1k rows
  - Write a 150‑word README with sample input/output
- Add **before/after metrics** to your existing project (even with synthetic data):
  - “Refactor queries → 420ms → 130ms (3.2×) on 1k enrolments”

**Day 6–7 — CV draft v1**
- Use the **Impact‑First Bullet** formula below (Section 4).

**Week 2 — Distribution + OAs**
- Turn on **GitHub Insights → Traffic**; share repo in uni CS groups / LinkedIn.
- Start OA prep (see Section 6) and log accuracy + time.

---

## 2) Target list & tracker
Create a short, smart list instead of 80 low‑quality apps.

**Company buckets to cover**
- Big Tech (London/UK hubs), high‑growth product companies, quant/fintech, consulting tech, startups with real users.

## 3) What reviewers look for (and how to show it fast)
- **Evidence you ship:** live link, screenshots, CLI demo gif, repo with tests
- **Numbers:** users, speedup, LOC touched, PRs merged, visitors
- **Clarity over buzzwords:** show before/after; name the bottleneck and fix
- **Team signals:** tutoring outcomes, tiny leadership moments, documentation others used

---

## 4) CV bullets that get interviews
**Impact‑First Bullet (CAR)**
[Conclusion: impact/metric] by [Action: what you built/changed] using [Relevant tech], [Reasoning/constraint].

**Before → After examples**
- *Weak:* “Built course management forms.”
- *Strong:* “Cut enrolment mistakes to 0% by adding backend validation and server‑side sanitisation (Node/MySQL), enabling error‑free creation/edit of 100+ records.”

- *Weak:* “Wrote complex SQL queries.”
- *Strong:* “3.2× faster analytics (420ms→130ms) by replacing N+1 queries with indexed joins and pre‑aggregations for ‘popular courses’ dashboard (1k rows).”

- *Weak:* “Shared notes on GitHub.”
- *Strong:* “Curated 50+ CS/interview resources; reached 120+ unique visitors in 4 weeks via uni groups/LinkedIn; added runnable DSA snippets with tests.”

**Banned phrases:** “hard‑working”, “team player”, “fast learner”, “familiar with”, “exposed to”, “responsible for”. Replace with outcomes and numbers.

---

## 5) Cover letter in 5 sentences (fill‑in template)
1. **Hook:** `I build <what> used by <who>, delivering <metric>.`
2. **Why them (specific):** one product/team, one public tech detail you admire.
3. **Why you (proof):** 1–2 bullets from your CV with numbers that match their stack.
4. **Transfer:** `Here’s how that maps to your <team/product> this spring.`
5. **Close:** Ask for the interview; add links to repo/demo.

**Example openers**
- “I build tiny backend tools that make data visible—most recently cutting query time 3.2× on a course analytics dashboard used by student organisers.”

---

## 6) Online assessments (OAs) & coding prep
**Scope to cover (lightweight, spring‑week level):**
- Arrays/strings, hash maps/sets, two‑pointers, stacks/queues, BFS/DFS, basic recursion, sorting, simple greedy.
- Complexity: be able to say `O(n log n)` vs `O(n^2)` and why.

**Plan (10–14 days):**
- 25–30 problems total. Tag each: topic + time + result.
- Aim: **≥80% accuracy** on easy, **≥60%** on medium, **≤20 mins** each.

**Practice log template**
| Date | Problem | Topic | Time | Result | Note |
|---|---|---|---|---|---|
| 2025‑08‑20 | Two Sum | Hash Map | 8m | AC | Drew hashmap, watch off‑by‑one |

**Code hygiene (scores easy points):**
- Function name matches prompt, clear variable names, explain edge cases in 1‑2 comments, add 2 tests.

---

## 7) “Systems lite” you might get
**Prompts:** “Design a course signup service for 1k students”, “Rate‑limit enrolment attempts.”
**What to say (2–3 mins):**
- Entities (Course, User, Enrolment), endpoints (POST /enrol, GET /stats)
- Data model: `users`, `courses`, `enrolments (user_id, course_id, ts, UNIQUE(user_id, course_id))`
- Bottlenecks & fixes: indexing (`(course_id, ts)`), caching top‑N, input validation, idempotency
- Trade‑offs: simplicity now vs scale later

---

## 8) Behavioral stories (8 pack)
Use STAR but be concise (≤120 words).
- **Conflict:** “Team disagreed on schema; I proposed an index to satisfy both read and write needs.”
- **Ownership:** “Nobody owned error handling; I wrote validation middleware; bug rate → 0.”
- **Pressure:** “Wimbledon queue spike; triaged, re‑routed, resolved in 5 mins.”
- **Teaching:** “Tutored 3 students; avg grade +1 band in a term.”

**Template**
Situation/goal → Obstacle → Decision/trade‑off → Action (tools) → Result (metric) → What I learned.

---

## 9) Outreach that actually gets replies (templates)

**Alumni/engineer DM (LinkedIn/Email)**
Hi <Name>,
I’m a first‑year CS at <Uni>. I build small backend tools (recently 3.2× sped up analytics on a course platform).
I’m applying to <Company>’s Spring Week and would value 5 minutes of advice on how <team/product> evaluates early talent.
Happy to share a one‑pager repo link if useful. If there’s someone better to reach out to, I’d appreciate a nudge.

Thanks! — <Your Name> | GitHub <link>


**Recruiter follow‑up (after applying)**
Hi <Name>,
I’ve applied to <Program>. To share context: here’s a 120‑sec README showing a tool I built that cuts query time 3.2× on a small analytics workload (Node/MySQL, tests included).
If helpful, I can adapt it to a tiny API endpoint to match <Company>’s stack.

Best, <Your Name>


---

## 10) Portfolio checklist (fast wins)
- [ ] Repo has a **one‑screen README** (problem → solution → demo → tech → results)
- [ ] **`/tests`** directory or a simple JUnit/Node test file
- [ ] Screenshot or CLI gif
- [ ] `LICENSE`, `CONTRIBUTING.md` (signals maturity)
- [ ] Traffic analytics enabled; add a tiny **/metrics.md** log: visitors, shares

---

## 11) Subconscious bias traps (avoid these)
- **Apology/hedge words:** “just”, “only”, “tried to”, “helped with” → use “built/led/shipped”.
- **Assignment framing:** Don’t write “module coursework”; write the *problem and result*. Add “(assessed project)” at the end if needed.
- **No numbers:** Replace with proxy metrics (e.g., “tested on 1k synthetic rows”, “used by 12 peers”).
- **Laundry‑list skills:** Tie each skill to a result.
- **Formatting traps:** No photo, no DOB, no full address. Use PDF, standard fonts, file name like `Firstname-Lastname-CV.pdf`.

---
## 12) Quality bar (self‑check before applying)
- Would an engineer **learn something** from your README in 60 seconds?
- Can every bullet be **understood by a non‑technical recruiter** and still impress an engineer?
- If a reviewer remembers only **one line** about you, is
