"""Where GOLEM writes.

Build products (jsonl, csv, the review viewers) are derived artifacts, not source, and
they can contain the full prompt corpus including the private half. They therefore go to
an output directory that is git-ignored by default and never inside the package.

    GOLEM_OUT=/somewhere golem-build     # override
    golem-build                          # default: ./out relative to the working dir
"""

from __future__ import annotations

import os
from pathlib import Path

OUT = Path(os.environ.get("GOLEM_OUT", Path.cwd() / "out"))


def out(*parts: str) -> Path:
    OUT.mkdir(parents=True, exist_ok=True)
    return OUT.joinpath(*parts)
