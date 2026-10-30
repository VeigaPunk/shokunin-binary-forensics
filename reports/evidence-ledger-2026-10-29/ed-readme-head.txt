# Epistemic Deconstructor

[![License](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-v7.16.7-green.svg)](CHANGELOG.md)
[![Tests](https://img.shields.io/badge/Tests-885%20passing-brightgreen.svg)](tests/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](src/scripts/)
[![Sponsored by Electi](https://img.shields.io/badge/Sponsored%20by-Electi-red.svg)](https://www.electiconsulting.com)

**Turn "I don't know how this works" into a quantified, validated model of how it works.**

Epistemic Deconstructor is a [Claude](https://claude.com/claude-code) skill. You hand Claude a black box; it runs a structured scientific investigation — Bayesian hypothesis tracking, falsification tests, parametric model fitting, conformal prediction — and writes every step to disk so context-window loss can't erase progress. The deliverable is a validated predictive model with parameter uncertainty bounds, not a summary document. Because every hypothesis, probe, and update is persisted to a session directory, a context-window reset mid-analysis is a non-event: the next turn resumes from disk, not from memory.

You don't run the tools by hand. You talk to Claude; Claude adopts the orchestrator role, picks a depth tier, and drives the whole protocol for you.

### What it sounds like

**Engineering — black-box reverse engineering.**

> *"Help me figure out how this API's rate limiter works — I only have request/response logs."*

Claude seeds three competing mechanisms (token bucket / sliding window / leaky bucket) with priors, designs differential probes (burst vs. steady traffic), fits a parametric model with capacity and refill-rate uncertainty, and returns allow/reject predictions with conformal intervals plus a head-to-head comparison against a "count requests" baseline.

**Security — side-channel investigation.**

> *"Does this login endpoint leak whether a username exists through response-time variance?"*

Claude seeds H1 timing oracle, H2 rate-limit artifact, H3 network jitter; runs timed enumeration vs. non-enumeration probes; the falsification gate forbids any hypothesis from crossing 0.80 posterior without a disconfirming test, and a standing adversarial hypothesis tracks the possibility that the signal is measurement noise.

**Forecasting — calibration audit.**

> *"I have a sales forecast from our demand planner — can you tell me whether it beats a naive baseline, and where its intervals are honest?"*

Claude runs walk-forward cross-validation, compares against a seasonal naive, produces conformal prediction intervals with guaranteed marginal coverage, and returns a calibrated assessment of where the planner's intervals are over- or under-confident at each horizon.

Every Claude response carries a state line, so progress is visible at a glance:

```
[STATE: Phase 2 | Tier: STANDARD | Active Hypotheses: 3 | Lead: H2 (78%) | Confidence: Medium]
```
