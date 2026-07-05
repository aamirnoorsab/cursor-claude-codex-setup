\# Cursor + Claude Code + Codex Setup



This repo documents setting up Cursor IDE with the Claude Code and Codex agent add-ons, as part of a technical screening task.



\## Environment



\- OS: Windows

\- IDE: Cursor



\## Tools Installed



1\. \*\*Cursor IDE\*\* — downloaded and installed from cursor.com

2\. \*\*Node.js (LTS) + npm\*\* — required before installing either agent CLI; not present on the system initially

3\. \*\*Claude Code\*\* — installed globally via npm (`@anthropic-ai/claude-code`), authenticated with an Anthropic account

4\. \*\*Codex\*\* — installed globally via npm (`@openai/codex`), authenticated with a ChatGPT account

5\. \*\*Git\*\* — required for cloning/pushing this repo; not present on the system initially



\## Steps Completed



1\. Installed Cursor IDE.

2\. Attempted to install the Claude Code and Codex extensions via Cursor's built-in "Plugins" marketplace (under Customize). This did not work — that marketplace lists unrelated third-party integrations (AWS, dbt Labs, etc.), not Claude Code or Codex.

3\. Checked the standard VS Code-style Extensions panel (Ctrl+Shift+X, and View menu). This Cursor build doesn't expose a classic Extensions view at all — the UI has been redesigned around Plugins, Tools \& MCPs, and Rules/Skills/Subagents instead.

4\. Fell back to installing both agents as CLI tools via npm, run from Cursor's integrated terminal. This is a fully supported, standard way to use both tools inside an IDE.

5\. Installed Node.js (LTS) after discovering `npm` wasn't recognized — the system had no Node.js runtime.

6\. Hit a PowerShell execution policy error blocking npm's script (`npm.ps1 cannot be loaded because running scripts is disabled`). Resolved with:

```powershell

&#x20;  Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

```

7\. Installed Claude Code:
npm install -g @anthropic-ai/claude-code

8. Authenticated Claude Code — hit a backend bug where an active Claude Pro subscription was not recognized during OAuth login ("Claude Max or Pro is required to connect to Claude Code"), despite the correct account and an active, paid plan. This is a known, reported issue (matches multiple open reports on Anthropic's GitHub issue tracker — a backend entitlement sync bug, not a local configuration problem). Logging out and retrying resolved it on a subsequent attempt.

9\. Verified Claude Code with a test prompt (`what is 2+2` → correct response).

10\. Installed Codex:

npm install -g @openai/codex

11\. Authenticated Codex via ChatGPT sign-in (paid plan, different email than the one used for Claude Code — handled by explicitly selecting the correct account during the browser OAuth step rather than the pre-filled default).

12\. Verified Codex with the same test prompt.

13\. Installed Git — not present on the system initially, installed via git-scm.com with default options.

14\. Created this public GitHub repository, cloned it locally, opened it in Cursor.



\## Issues Ran Into and How They Were Solved



| Issue | Fix |

|---|---|

| Ctrl+Shift+X / View menu didn't open an Extensions panel | This Cursor version doesn't have one; used CLI installs instead |

| `npm` not recognized | Node.js wasn't installed; installed Node.js LTS |

| PowerShell blocked `npm.ps1` from running | Changed execution policy to `RemoteSigned` for current user |

| Claude Code rejected an active Pro subscription during login | Known backend entitlement bug (confirmed against public issue reports); resolved by logging out and re-authenticating |

| `git` not recognized | Git wasn't installed; installed Git for Windows with default settings |



\## Notes



This setup is directly relevant to the role: the company's own product integrates with Claude Code, Codex, and Cursor via an MCP server, so being able to install, authenticate, and troubleshoot these tools firsthand is a practical rather than academic exercise.




---

# Step 2 — Research Project: AI-Powered SEO Content Production

## What This Is

A research collection on **AI-Powered SEO Content Production** (GEO / AEO / AI search visibility): 10 expert sources, with their recent content collected and organized to support building a real playbook later.

Topic chosen because it is the most active and fastest-moving area of search marketing right now — the shift from ranking in traditional search to being cited by AI answer engines (ChatGPT, Google AI Overviews, Perplexity, Gemini).

## What I Collected

- **`research/sources.md`** — 10 experts with profile/site links and a one-line justification each.
- **`research/youtube-transcripts/`** — 5 transcripts pulled via the YouTube Transcript API (Python), one per expert who publishes strong long-form video/conference content.
- **`research/linkedin-posts/`** — 5 files (one per expert) containing their strongest recent LinkedIn posts on AI search, manually collected.
- **`research/other/key-themes.md`** — a synthesis of the recurring patterns, agreements, and disagreements across all 10 sources.

## The 10 Experts and Why They Were Chosen

Selection prioritized **original, evidence-backed contribution over reach or commentary**. Each source either publishes original research, ships a practitioner framework, or brings measurement rigor — not "first Google result" listicles.

| Expert | Why chosen | Collected via |
|---|---|---|
| Kevin Indig | Original clickstream/AI-search research; "Visibility Layer" and "Trust Stack" frameworks | YouTube transcript |
| Lily Ray | Original citation measurement; anti-hype myth-busting on GEO/AEO/LLMO | YouTube transcript |
| Marie Haynes | Deep Google ranking/EEAT expertise (consulted by Google's Danny Sullivan) | YouTube transcript |
| Wil Reynolds | Measurement angle: AI visibility vs. business impact | YouTube transcript |
| Rand Fishkin | Zero-click strategy, brand-association-through-language, SparkToro research | YouTube transcript |
| Aleyda Solís | 10 AI-readiness characteristics framework; original polls; strong curation | LinkedIn posts |
| Mike King (iPullRank) | Relevance Engineering, Agentic RAG, content-chunking — deep technical original work | LinkedIn posts |
| Dan Petrovic (Dejan AI) | Trained an LLM from scratch; original brand-authority-in-LLM-memory research | LinkedIn posts |
| Tim Soulo (Ahrefs) | Largest-scale AI-search research in the set (1B+ data points, 14 studies) | LinkedIn posts |
| Kaleigh Moore | Getting-started AEO strategy; AI-search job-market research | LinkedIn posts |

## Method Notes

**Collection was matched to each expert's primary channel.** Five experts publish strong long-form video (conference talks, podcast interviews) — their content was collected as YouTube transcripts via the `youtube-transcript-api` Python library. The other five publish primarily in written/long-form on LinkedIn — their posts were collected manually.

**LinkedIn was collected manually, not scraped.** Automated LinkedIn scraping violates their Terms of Service, so posts were copied by hand from public profiles. This is slower but avoids the ToS/account risk of scraping.

**Attribution is kept clean.** Where an expert shared or analyzed someone else's work (e.g., Aleyda sharing MJ Cachón's eye-tracking study, or Mike King sharing Ben Wills' ranking-factors study), it is labeled as a share/analysis, not presented as the expert's own original research.

**Quality over volume.** 2–4 strong, on-topic items per expert rather than padding to a fixed number. Where a source drifts off-topic (e.g., a podcast wandering into unrelated territory), only the on-topic portions are treated as relevant, and this is noted.

## Repo Structure

```
research/
  sources.md                    # 10 experts, links, justifications
  youtube-transcripts/          # 5 transcripts (one per video)
  linkedin-posts/               # 5 files (one per expert)
  other/
    key-themes.md               # cross-source synthesis
get_transcripts.py              # script used to pull YouTube transcripts via API
```

## Technical Note on Transcript Collection

Transcripts were pulled programmatically using the `youtube-transcript-api` Python library (see `get_transcripts.py`). The script takes a dictionary of `{label: video_id}` pairs, fetches each transcript via the API, and writes a clean text file per video into `research/youtube-transcripts/`. Video IDs were extracted from standard and short-form YouTube URLs.