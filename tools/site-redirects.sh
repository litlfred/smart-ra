#!/usr/bin/env bash
# Forwarding pages at addresses the site used to serve — a build-instance-site
# source step (`bun run site:redirects <site dir>`).
#
# The first agent-run root publish (2026-10-11, bean n3h9) moved the
# "what changed" page from /review/ to /en/review/, where the document build
# now writes it. Links already shared to /review/ forward there.
set -euo pipefail
OUT=$(cd "${1:?usage: site-redirects.sh <site dir>}" && pwd)

redirect() { # <old dir> <new target, relative to the old dir>
  mkdir -p "$OUT/$1"
  cat > "$OUT/$1/index.html" <<HTML
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Moved</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="$2">
<meta http-equiv="refresh" content="0; url=$2">
</head>
<body><p>This page has moved to <a href="$2">$2</a>.</p></body>
</html>
HTML
}

redirect review ../en/review/
