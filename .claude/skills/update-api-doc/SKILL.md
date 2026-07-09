---
name: update-api-doc
description: Add or update pages on the AltaBots OpenAPI doc site (openapi.altabots.ai) by pulling the equivalent page from the upstream GPTBots API reference and converting it to our OEM branding. Use when asked to update our API doc, sync API doc, add a new API page, or reflect a GPTBots API change in our docs.
---

Pulls one or more pages from the upstream GPTBots API reference (`https://www.gptbots.ai/docs/api-reference/...`), converts them to AltaBots OEM branding/URLs, writes them into `docs/`, updates `mkdocs.yml` nav and `docs/Changelog.md`, and pushes straight to `main` (which auto-deploys to `openapi.altabots.ai` via `.github/workflows/pages.yml`). The fetch harness is `.claude/skills/update-api-doc/fetch_upstream.py` — see "Step 2" below for how to drive it. All paths in this file are relative to the repo root.

## Step 0: get the URL(s) from the user

Ask the user for the upstream URL(s) they want added or updated, e.g.
`https://www.gptbots.ai/docs/api-reference/conversation-api/query-logtree`.
Don't guess a URL from a feature name — GPTBots' slugs don't always match
their nav labels (see Gotchas).

Skip this step if the user already pasted the URL(s) in their request.

## Step 1: fetch the upstream page

```bash
python3 .claude/skills/update-api-doc/fetch_upstream.py "<url>" --nav-label "<Sidebar Label>"
```

`--nav-label` is the sidebar text for that page (visible in the left nav on
gptbots.ai) — it trims the output down to the actual page content instead of
the full page-with-nav dump. If you don't know the exact label, omit the
flag and skim the full output; the real content starts after the first
`Last updated：` line.

**If the script exits 1 with "consistently returns the gptbots.ai
homepage"**: this is a known CDN quirk (see Gotchas) — stop retrying and
ask the user to open the URL in their own browser and paste the page text
into the chat. This has happened for `send-message-v2`,
`human-handoff-service`, and `user-overview` specifically, and is not
locale-dependent (tried both `en` and `zh_CN` paths, both fail the same
way). If they paste Simplified Chinese, that's fine — convert it like any
other content in Step 2, just translate it too.

Network note: gptbots.ai must be reachable through this environment's
egress proxy. If curl hangs or the proxy rejects the connection, the
environment's network policy needs `gptbots.ai` allowed — tell the user to
adjust it in their environment settings (see `/root/.ccr/README.md` for
proxy diagnostics), you cannot change it yourself.

## Step 2: convert to OEM content and write the file

Read the fetched text and produce the target `.md` file. Apply every rule
below — they were all discovered the hard way against real upstream pages
in prior syncs (see git log on this repo for examples of every rule in
action):

1. **URL parity.** The upstream URL path *is* the target path:
   `.../api-reference/<category-slug>/<page-slug>` → write to
   `docs/<category-slug>/<page-slug>.md` (mkdocs has `use_directory_urls:
   false`, so the `.md` filename becomes the URL suffix directly — no
   further renaming). Match upstream's slug exactly, including its own
   typos/inconsistencies (`delege-knowledge-doc`, `update-datebase`,
   `Set-User-Id` with capitals) — don't "fix" their spelling, URL parity
   beats tidiness.
2. **Follow the existing Markdown template.** Open a sibling file already
   in that category folder and match its structure: `_Last updated at:
   YYYY-MM-DD_` header, `# **Title**` / `## **Request Method**` / `##
   **Request URL**` / `## **Request Example**` / `## **Response**` /
   `## **Error Codes**` sections, pipe tables. Don't invent a new layout.
3. **Brand sweep.** `GPTBots`/`gptbots` → `AltaBots`/`altabots` everywhere,
   including inside JSON examples and error messages.
4. **Domain sweep.** `https://api-${endpoint}.gptbots.ai`,
   `https://api.gptbots.ai`, or any per-datacenter variant
   (`api-sg.gptbots.ai` etc.) → flat `https://altatech.ai` (no datacenter
   prefix — this OEM has one region). Any asset/example URL on
   `gptbots.ai`/`res.gptbots.ai` → `altatech.ai`.
5. **No Simplified Chinese or mainland idioms in examples.** Scan example
   JSON and prose for CJK; if it's Simplified Chinese or a
   mainland-specific term, replace with English (the doc's base language)
   or Traditional Chinese if the surrounding content is Chinese. Upstream's
   own examples have shipped Simplified Chinese before (`人工服务-售前`,
   `中国的历史`, even a sidebar label `查询用户CDP`) — always check, don't
   assume upstream is clean.
6. **Drop mainland-only integrations.** This OEM does not offer DingTalk
   (钉钉), WhatsApp by EngageLab, Sobot, Zoho Sales IQ, or WeChat Customer
   Service (微信客服). If a fetched page lists integration platforms (e.g.
   User Overview's anonymous-ID tables), omit rows for these five —
   everything else (Teams, LINE, Telegram, WhatsApp by Meta, Slack,
   Discord, Instagram, Facebook, Intercom, LiveChat, Livedesk, Zapier,
   etc.) stays.
7. **Skip History API and Client Plugin content** unless the user
   explicitly asks for it — these are out of scope for this OEM doc.
8. **`mkdocs.yml` nav placement.** Add the new entry inside the matching
   category block, in the **same relative order** upstream uses in its own
   sidebar (open the category's overview/sidebar on gptbots.ai to check
   order — don't just append to the end of the list). Category-level order
   in our nav also mirrors upstream: Agent API, Knowledge API, Workflow
   API, Database API, Models API, User API, Analytics API, Account API,
   History API. Note our nav labels diverge from upstream in two places on
   purpose: `conversation-api/` folder = "Agent API" label,
   `models-api/` folder = "Models API" label (upstream renamed the tab but
   not the URL slug — don't rename the folder to match).

## Step 3: update the Changelog and publish

Add a new dated entry to the **top** of `docs/Changelog.md` (below the
`# Changelog` heading, above the most recent existing entry), bumping the
version number. Keep it to **API-facing changes only** — new pages, new
request/response fields, changed endpoints. Do not mention internal
mechanics (URL renames, nav reordering, brand sweep) unless the user asks
for that level of detail. Example of the right altitude:

```markdown
## V1.7 · 2026-08-02
- Added Query LogTree API (Agent API).
- Added `retry_count` field to Workflow Test response.
```

Then build, verify, and push directly to `main`:

```bash
mkdocs build --strict          # must pass with zero warnings before pushing
git add docs/<new-or-changed-files> mkdocs.yml docs/Changelog.md
git commit -m "<concise summary of what changed>"
git push origin main
```

Pushing to `main` triggers `.github/workflows/pages.yml`, which builds and
deploys to `openapi.altabots.ai` automatically (takes ~1-2 minutes). You can
confirm the deploy succeeded before reporting back:

```bash
# via the github MCP tools, not raw gh CLI:
# mcp__github__actions_list method=list_workflow_runs, resource_id=pages.yml, workflow_runs_filter={"branch":"main"}
# check the newest run's head_sha matches your commit and conclusion == "success"
```

## Step 4: report back

Reply with:
- The live URL(s) for every page you added or updated, e.g.
  `https://openapi.altabots.ai/conversation-api/query-logtree.html`
  (path = `docs/<file>.md` with `.md` → `.html`, no other transformation).
- A one-line flag on **which ones are new vs. updated**, so the user knows
  what to actually read carefully vs. skim.
- If any source page couldn't be fetched (see Gotchas) and you had to ask
  for pasted content, say so explicitly rather than silently proceeding.

## Gotchas

- **gptbots.ai intermittently serves its homepage instead of the real
  page**, same HTTP 200, same ~101175-byte payload, title "Enterprise AI
  Agents: Cut Costs & Boost ROI | GPTBots.ai". Confirmed reproducible for
  `conversation-api/send-message-v2`, `conversation-api/human-handoff-service`,
  and `user-api/user-overview`, on both the `en` and `zh_CN` locale paths,
  across multiple User-Agents (desktop Chrome, mobile Safari) and 5+
  retries with delays. Not rate-limiting (other pages fetched fine in the
  same batch) — looks like a CDN cache issue on their end for specific
  high-traffic paths. `fetch_upstream.py` detects and reports this; don't
  try to work around it with more retries, ask the user to paste instead.
- **Upstream nav labels don't always match the page's actual H1.** E.g. the
  sidebar says "Get Bot Information" but the page content title is "Get
  Agent Information"; the sidebar says "Agent Quality" but the page title
  is "Agent Feedback Evaluation". Use the page's own H1/title for our doc's
  heading, not the sidebar label — but use the sidebar label to identify
  *which* page you're looking at when there's ambiguity.
- **Upstream itself ships bugs** — a numbered heading artifact
  ("1.Get Correlated Document"), an outright Simplified Chinese sidebar
  label ("查询用户CDP") on an otherwise-English site. Don't assume upstream
  content is clean; always run the brand/CJK checks even on pages you
  "just glanced at."
- **Category tab renames don't change the URL folder.** Upstream renamed
  "Conversation API" → "Agent API" and "Speech API" → "Models API" in their
  nav, but the URL slugs stayed `conversation-api/` and `models-api/`.
  Match the *label* to upstream's current nav text, match the *folder* to
  upstream's URL — they can legitimately disagree.

## Troubleshooting

- **`ModuleNotFoundError: No module named 'bs4'`**: `pip install
  beautifulsoup4 lxml`.
- **curl hangs / connection refused fetching gptbots.ai**: the sandbox's
  outbound network policy is blocking the domain. This is an environment
  setting, not something fixable from inside the session — tell the user
  to allow `gptbots.ai` in their environment's network policy.
- **`mkdocs build --strict` fails on a nav entry**: you added/renamed a
  `.md` file but didn't update `mkdocs.yml` (or vice versa) — the nav
  entry and the file on disk must match exactly, including case.
