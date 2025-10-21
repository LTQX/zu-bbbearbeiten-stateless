#!/usr/bin/env python3
import re
import sys
from pathlib import Path


def main() -> int:
    msg_path = Path(sys.argv[1])
    message = msg_path.read_text(encoding="utf-8").strip()

    # Conventional Commit erlaubt (feat|fix|chore|docs|refactor|test)
    cc_ok = re.match(
        r"^(feat|fix|chore|docs|refactor|test)(\(.+\))?:\s.+",
        message,
    )

    # Oder eine Issue-Referenz (closes #12, fix #3, #7, ...)
    issue_ok = re.search(
        r"(?:close[sd]?|fix|resolve[sd]?)\s*#\d+|#\d+",
        message,
        re.IGNORECASE,
    )

    if cc_ok or issue_ok:
        return 0

    print(
        "Commit-Message nicht erlaubt.\n"
        "- Erwarte z. B. 'feat: …' oder 'closes #12'.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
