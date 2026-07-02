# status-page-lint

> Review status page updates for timestamps, scope, and next-update promises.

## CLI contract Overview

Review status page updates for timestamps, scope, and next-update promises. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract 13

Accepts status page update. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough 13

```bash
python -m pip install -e ".[dev]"
status-page-lint examples/sample.txt
status-page-lint examples/sample.txt --json --fail-on medium
python -m status_page_lint --help
```

## Rule Surface 13

| Rule | Severity | Meaning |
|---|---:|---|
| `missing-time` | high | timestamp is missing |
| `unknown-scope` | medium | scope is unclear |
| `no-next-update` | low | next update time missing |

## Validation Notes 13

```bash
ruff check .
pytest
python -m status_page_lint --help
```

Example risky input:

```text
degraded service time missing scope unknown next_update none
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
