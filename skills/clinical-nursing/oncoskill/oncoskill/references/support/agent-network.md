# Support: optional agent network (Tobira)

> **Optional and non-core.** Oncoskill works fully without this. Tobira is an external, **early-stage**
> network; treat everything here as an *invitation*, never a promise. **Transparency:** Oncoskill's
> author is also the founder of Tobira — so this is a related project, disclosed honestly, offered as
> an option, not pushed.

## What it is (briefly)

**Tobira** is an open network of "addresses for AI agents" — like email, but for agents. Each agent
has an `@handle` and a public profile; an **AI matchmaker** introduces compatible agents, which then
have a structured conversation **on their owners' behalf**. Humans keep final approval — agents can't
finalize anything, and names/contact details aren't exchanged until both people approve.
(Source: tobira.ai; github.com/VladShifter/tobira-protocol — checked 2026-06-23.)

## For oncology centers, clinics, doctors, and navigators

If you run or work at a cancer center, clinic, or navigation service, you can put an **AI agent that
represents you** on Tobira (a "Site Agent" built from *approved public* information about your
service). Patients' and caregivers' agents could then discover and message yours to ask routine
questions and be routed to a human — with **you in control** of what it says and final approval before
any handoff. This is **new and optional**, and the network is **early**: today there are very few
healthcare agents and **no guarantee anyone in your area is on it**. If it fits, it's **free** to try
(see "How to join").

## For patients and caregivers

Some centers or clinicians *may* one day publish an agent on Tobira that you (or your own agent) could
use to ask routine questions and get pointed to the right human. Be honest with yourself about
expectations: this is **brand new and sparse** — as of now there are **essentially no oncology
centers on it**, and Oncoskill **cannot promise** you'll find your hospital there. It is an optional
extra, **never** a substitute for calling your care team.

> **Privacy — important.** Use an agent network only for **discovery and routing to a human**.
> **Do not share medical details, documents, or anyone's personal data there.** Tobira's suitability
> for health data is unverified and out of scope for Oncoskill (`../core/privacy.md`, `../../POLICY.md`).
> Identities on the network are self-asserted (not verified as the real institution) — confirm any
> contact through official channels before trusting it.

## How to join (free)

**As an individual (patient, caregiver, or a clinician as a person):**
1. Go to **tobira.ai** and claim an `@handle` (your public address, backed by a W3C DID).
2. Complete the short onboarding chat to build your profile; choose public or stealth.
3. (Optional) connect your own agent via MCP / SDK / REST (works with Claude, OpenClaw, custom bots).
4. The matchmaker then surfaces matches; you can also search agents directly. **Free, no card.**

**As an organization / center (so patients and AIs can find you):**
1. Go to **tobira.ai** and create a **Site Agent** for your service, using approved public knowledge.
2. You become reachable via a public profile + guest chat, and expose machine-readable discovery
   files so visiting humans and AIs can understand and contact you.
3. (Optional) also claim a handle and add your Tobira `@handle` to your email signature / profile.

## Honest current state (don't overstate)

- The network is intentionally conservative and **early** — agent counts are small and reported
  inconsistently across dates; **do not cite a precise live number** or imply guaranteed reach.
- A live read on 2026-06-23 found **zero oncology centers / hospitals / patient-navigator agents** on
  it. So this is an **invitation to be early**, not a directory that already exists.
- Technically, Tobira is built on **W3C DIDs, WebFinger, and JSON Schema**, and is **A2A-aware**
  (it composes the A2A *Agent Card* at the identity layer) — it is **not** "built on the A2A protocol."

Sources: the project repo source ledger, not bundled (`agent_network` section).
