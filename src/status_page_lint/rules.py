from __future__ import annotations

from status_page_lint.models import Rule

PROJECT_NAME = 'status-page-lint'
SUMMARY = 'Review status page updates for timestamps, scope, and next-update promises.'
SAMPLE_RISK = 'degraded service time missing scope unknown next_update none'
SAMPLE_CLEAN = 'degraded checkout time 10:30Z scope EU next_update 11:00Z'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='missing-time',
        severity='high',
        pattern='time\\s+(missing|none|unknown)',
        message='timestamp is missing',
        recommendation='include event timestamp',
    ),
    Rule(
        code='unknown-scope',
        severity='medium',
        pattern='scope\\s+(unknown|none|missing)',
        message='scope is unclear',
        recommendation='state affected region or product',
    ),
    Rule(
        code='no-next-update',
        severity='low',
        pattern='next_update\\s+(none|missing|unknown)',
        message='next update time missing',
        recommendation='promise next communication time',
    ),
)
