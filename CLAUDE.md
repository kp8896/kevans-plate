# CLAUDE.md

Guidance for AI assistants working in this repository.

## What this is

**Kevan's Plate** is a single-page, client-side dashboard that visualizes Microsoft
To Do / Outlook Tasks through an Eisenhower priority matrix, a filterable task table,
and a weekly roadmap. It reads tasks live from the **Microsoft Graph API** (browser
auth via MSAL) and enriches them with structured metadata parsed out of a `[PLATE]`
block embedded in each task's notes/body.

The `[PLATE]` blocks are intended to be written by an AI assistant integration
("Donna") that runs intake on raw Outlook tasks. This repo contains only the frontend
viewer — there is no Donna code here.

The whole application is **one file**: `index.html` (HTML + CSS + vanilla JS, no build
step). Treat it as the single source of truth.

## Repository layout

```
index.html   The entire application: markup, inline <style>, inline <script>
README.md     One-line description
```

There is **no build system, no package manager, no test suite, no backend, and no
dependencies to install.** The only external runtime dependencies are two CDN loads:

- `@azure/msal-browser@3` (Microsoft auth) — `<script>` in `<head>`
- Google Fonts (`Syne`, `DM Mono`)

## Running & testing

- **Run locally:** serve the directory over HTTP (MSAL redirect auth will not work from
  a `file://` URL). For example: `python3 -m http.server 8000` then open
  `http://localhost:8000`. Opening `index.html` directly will break sign-in.
- **Auth requires** a real Microsoft account and network access. The Azure app
  registration (`clientId` / `tenantId`) is hardcoded near the top of the `<script>`
  (`startAuth()` and the boot IIFE) and in `initMSAL`. The MSAL `redirectUri` is derived
  from the current URL, so the exact origin you serve from must be registered as a
  redirect URI in Azure AD, or login will fail.
- **Verifying UI changes** without Microsoft auth is awkward because rendering is driven
  by live Graph data. To test rendering logic in isolation, populate the global
  `allTasks` array in the console and call `renderAll()`.
- **There is no lint/format/test command.** Verify changes by loading the page in a
  browser and exercising the three views (Matrix / All Tasks / Roadmap).

## Architecture (all inside `index.html`)

The page has three top-level states, toggled by `display`:
`#loading`, `#auth-screen`, and `#app`. Within `#app`, three **views** (`.view`) —
`view-matrix`, `view-all`, `view-roadmap` — are switched by `switchView()`.

Data flow, roughly top to bottom in the `<script>`:

1. **Auth** — `initMSAL` / `startAuth` / `getToken` / `signOut` wrap MSAL redirect
   flow. Tokens are held in the module-level `accessToken` and requested for the
   `Tasks.ReadWrite` Graph scope. The boot IIFE at the bottom handles the redirect
   callback, then shows either the auth screen or the app.
2. **Fetch** — `graphFetch(url, options)` is the single Graph HTTP wrapper: injects the
   bearer token, retries once on `401` by refreshing the token. `getAllOutlookTasks()`
   walks every To Do list, paginates via `@odata.nextLink`, tags each task with its
   `_listName`, and drops `completed` tasks.
3. **Parse** — `parsePlate(body)` extracts the `[PLATE]...[/PLATE]` block and reads
   `KEY: value` lines. `parseConfig(body)` does the same for a `[CONFIG]...[/CONFIG]`
   block found on a task whose title contains "donna config". `getQuadrant(plate)` maps
   urgency/importance to an Eisenhower quadrant.
4. **Load** — `loadTasks()` orchestrates fetch → parse → normalize into the global
   `allTasks` array of `{ id, title, status, pct, due, plate, quadrant, listName,
   rawBody }`, then calls `renderAll()`.
5. **Render** — `renderAll()` fans out to `renderStats`, `renderMatrix`,
   `renderAllTasks`, and `renderRoadmap`. Rendering is done by building HTML strings and
   assigning `innerHTML`. User-supplied text must pass through `escHtml()`.
6. **Interaction** — `setFilter`, `filterSearch`, `switchView`, `openModal`/`closeModal`
   read from `allTasks` and re-render; no framework, no reactive state.

Module-level state: `msalInstance`, `accessToken`, `allTasks`, `activeFilter`,
`searchQuery`, `scheduleConfig`.

## Domain model: the `[PLATE]` block

Each Outlook task's body may contain a block like:

```
[PLATE]
URGENCY: High
IMPORTANCE: High
CATEGORY: DW-AI
EFFORT_HRS: 4
DELEGATE: No
DELEGATE_TO:
ROADMAP_WEEK: 2026-W28
REVIEW_DATE: 2026-07-17
[/PLATE]
```

Parsed fields (see `parsePlate`): `urgency`, `importance`, `category`, `effortHrs`,
`delegate`, `delegateTo`, `roadmapWeek`, `reviewDate`. Tasks without a `[PLATE]` block
are treated as **"unstructured"** and shown separately.

**Quadrant logic** (`getQuadrant`): urgent = urgency is `High`; important = importance is
`High` or `Medium`.
- urgent + important → `do-first`
- important, not urgent → `schedule`
- urgent, not important → `delegate`
- neither → `backlog`

**Categories** drive badge colors (CSS classes `cat-<CATEGORY>`, non-alphanumerics
replaced with `-`) and roadmap placement. Known categories referenced in code:
`DW-AI`, `DW-Jolted`, `LT`, `MT`, `OP`, `RD`, `ST`, `YZ`. The set
`['DW-AI', 'DW-Jolted', 'RD', 'ST']` is treated as **deep work** in the roadmap.

## The `[CONFIG]` block

A task titled to include "donna config" can carry a `[CONFIG]...[/CONFIG]` block parsed
by `parseConfig` into `scheduleConfig`: `WFH_DAYS` (e.g. `Tue, Fri`), `OOO_DATES`
(ISO `YYYY-MM-DD`, comma-separated), and `REVIEW_CADENCE`. This drives the roadmap's
WFH/office/OOO day tagging. Defaults: WFH `Tue`/`Fri`, review cadence `Friday`.

## Roadmap specifics (`renderRoadmap`)

- Shows Mon–Fri of the current week, but **rolls to next week once it's Thu/Fri**
  (`dayOfWeek >= 4`) so the view stays actionable.
- Tasks land on the roadmap by matching `plate.roadmapWeek` to the ISO week
  (`getISOWeek`) of the displayed Monday.
- Fixed recurring meetings are hardcoded in `fixedBlocks` (keyed by day index, 0=Mon).
  WFH days get deep-work blocks + a buffer; office days get admin blocks.
- `DAY_NAME_TO_INDEX` maps `Mon`..`Fri` to `0`..`4`.

## Conventions & gotchas

- **Vanilla JS only.** No frameworks, no bundler, no npm. Keep everything in
  `index.html` unless there's a strong reason to split it.
- **Rendering is string-concatenation + `innerHTML`.** Always wrap any task-derived
  string in `escHtml()` before interpolating it, exactly as existing code does — this is
  the only XSS guard.
- **Styling is a CSS custom-property design system** defined in `:root` (dark theme,
  color tokens like `--red`/`--blue`/`--green`, fonts `--font-head` Syne /
  `--font-mono` DM Mono). Reuse these tokens rather than hardcoding colors, and follow
  the existing badge/quadrant class naming.
- **Secrets:** the hardcoded `clientId`/`tenantId` are public Azure AD app-registration
  identifiers (a SPA client ID is not a secret), but still avoid committing anything that
  is actually sensitive. There is no server-side secret in this repo.
- **Graph scope** is `Tasks.ReadWrite`; the app currently only reads. Adding write
  operations should reuse `graphFetch`.
- Task completion filtering happens in `getAllOutlookTasks` (excludes `completed`); the
  "donna config" task is filtered out of `allTasks` in `loadTasks`.

## Git workflow

- The default branch is `main`. History shows the app is edited by uploading a full
  replacement `index.html`, so expect large single-file diffs.
- Make focused commits with clear messages. Only open a pull request when explicitly
  asked.
