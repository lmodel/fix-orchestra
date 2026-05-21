"""Shared pytest fixtures and hooks for the fix-orchestra test suite."""
from __future__ import annotations

import pytest


def pytest_configure(config: pytest.Config) -> None:
    """Initialise the session-wide LinkML validation tally on the config object
    so both the ``fix_record_tally`` fixture and ``pytest_terminal_summary``
    reference the same mutable dict."""
    config._fix_record_tally: dict[str, int] = {"total": 0}  # type: ignore[attr-defined]


@pytest.fixture(scope="session")
def fix_record_tally(pytestconfig: pytest.Config) -> dict[str, int]:
    """Session-scoped mutable counter shared by all LinkML-validation tests.

    Tests append to ``tally["total"]``; the ``pytest_terminal_summary`` hook
    prints the grand total at the end of the run.
    """
    return pytestconfig._fix_record_tally  # type: ignore[attr-defined]


def pytest_terminal_summary(
    terminalreporter,  # type: ignore[no-untyped-def]
    exitstatus: int,
    config: pytest.Config,
) -> None:
    """Print a green grand-total line after the standard pytest summary."""
    tally: dict[str, int] = getattr(config, "_fix_record_tally", {"total": 0})
    if tally["total"] == 0:
        return
    terminalreporter.write_sep(
        "=",
        f"Total of {tally['total']:,} FIX records processed across all LinkML validation tests",
        green=True,
        bold=True,
    )
