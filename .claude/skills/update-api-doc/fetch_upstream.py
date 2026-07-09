#!/usr/bin/env python3
"""
Fetch a gptbots.ai API-reference doc page and print its cleaned main-content
text to stdout (or save with --out).

Usage:
    python3 fetch_upstream.py <url> [--nav-label "Sidebar Label"] [--out FILE]

Why this exists: gptbots.ai is server-rendered (Nuxt SSR), so a plain curl
gets the real page HTML -- no headless browser needed. BUT: for a handful of
high-traffic URLs, the CDN intermittently serves the marketing homepage
instead of the real page (same HTTP 200, same ~101175-byte payload, title
"Enterprise AI Agents: Cut Costs & Boost ROI | GPTBots.ai") regardless of
locale or User-Agent. This script detects that and retries; if it still
fails, it tells you to ask the user to paste the page content instead of
silently returning garbage.

Requires: beautifulsoup4, lxml (pip install beautifulsoup4 lxml if missing).
Must run with HTTPS_PROXY set and the CA bundle trusted (see SKILL.md) --
gptbots.ai is not reachable without the environment's outbound proxy allowing
it.
"""
import argparse
import os
import subprocess
import sys
import time

HOMEPAGE_TITLE_MARKER = "Cut Costs"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"


def fetch_html(url: str) -> str:
    proxy = os.environ.get("HTTPS_PROXY")
    cmd = ["curl", "-sS", "-A", UA, url]
    if proxy:
        ca_bundle = "/root/.ccr/ca-bundle.crt"
        cmd = ["curl", "-sS", "-x", proxy] + (["--cacert", ca_bundle] if os.path.exists(ca_bundle) else []) + ["-A", UA, url]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if result.returncode != 0:
        raise RuntimeError(f"curl failed (exit {result.returncode}): {result.stderr}")
    return result.stdout


def is_homepage_fallback(html: str) -> bool:
    return HOMEPAGE_TITLE_MARKER in html[:2000]


def extract_main(html: str, nav_label: str | None) -> str:
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, "lxml")
    for tag in soup(["script", "style"]):
        tag.decompose()
    text = soup.get_text("\n")
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    if nav_label:
        idx = None
        for i, l in enumerate(lines):
            if l == nav_label:
                idx = i
        if idx is not None:
            lines = lines[idx:]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("url")
    parser.add_argument("--nav-label", default=None, help="Sidebar label text to trim the page down to its main content (e.g. the page's H1). Omit to get the full extracted page.")
    parser.add_argument("--out", default=None, help="Write output to this file instead of stdout")
    parser.add_argument("--retries", type=int, default=4)
    args = parser.parse_args()

    html = None
    for attempt in range(args.retries):
        html = fetch_html(args.url)
        if not is_homepage_fallback(html):
            break
        print(f"[attempt {attempt + 1}/{args.retries}] got homepage fallback, retrying...", file=sys.stderr)
        time.sleep(2)
    else:
        print(
            "FAILED: this URL consistently returns the gptbots.ai homepage instead of "
            "real content (known CDN quirk on some high-traffic pages). Ask the user to "
            "paste the page content directly instead (their browser can see it fine).",
            file=sys.stderr,
        )
        sys.exit(1)

    content = extract_main(html, args.nav_label)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Wrote {len(content)} chars to {args.out}", file=sys.stderr)
    else:
        print(content)


if __name__ == "__main__":
    main()
