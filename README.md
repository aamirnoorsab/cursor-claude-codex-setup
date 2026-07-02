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





