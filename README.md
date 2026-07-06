![Status Page Lint cover](assets/readme-cover.svg)

# Status Page Lint

> Review status page updates for timestamps, scope, and next-update promises

This is a review desk for incident communications. The useful part is not a dashboard; it is the tiny repeatable moment where vague records become specific findings.

## Finding catalog for `status-page-lint`

| Finding | Level | Why it matters |
| --- | --- | --- |
| `missing-time` | high | timestamp is missing |
| `unknown-scope` | medium | scope is unclear |
| `no-next-update` | low | next update time missing |

## Try the sample

```bash
git clone https://github.com/mertefekurt/status-page-lint.git
cd status-page-lint
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

```bash
status-page-lint examples/sample.txt
status-page-lint examples/sample.txt --json
```

## Reading the output

- Markdown is meant for humans reviewing a change.
- JSON is meant for CI, scripts, or saved reports.
- `--fail-on` lets the repo decide how strict a gate should be.
