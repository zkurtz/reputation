"""Manage paths for the repute package."""

from pathlib import Path

CACHE_DIR = Path.home() / ".cache" / "repute"
GH_URL_BASE = "github.com/"
DEFAULT_CACHE_DURATION_DAYS = 10
