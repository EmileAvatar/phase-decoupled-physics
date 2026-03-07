#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
print_utils.py — Unified console + file output for the PDTP solver.

All other modules receive a ReportWriter instance and call rw.print()/
rw.section()/rw.table() instead of using print() directly.  This ensures
every line goes to both the terminal AND the timestamped report file.
"""

import os
import sys
import datetime


class ReportWriter:
    """
    Writes to stdout and a timestamped file simultaneously.

    Usage:
        rw = ReportWriter(output_dir)
        rw.section("Title")
        rw.print("Some text")
        rw.table(["Col A", "Col B"], [["x", "y"], ["a", "b"]], [20, 10])
        rw.close()
    """

    def __init__(self, output_dir, label="report"):
        os.makedirs(output_dir, exist_ok=True)
        ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.path = os.path.join(output_dir, "{}_{}.txt".format(label, ts))
        self._file = open(self.path, "w", encoding="utf-8")
        self._write_both("PDTP Comprehensive Solver Report")
        self._write_both("Generated: {}".format(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        self._write_both("=" * 80)
        self._write_both("")

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def print(self, message=""):
        """Print a line to console and file."""
        self._write_both(str(message))

    def section(self, title, char="=", width=80):
        """Print a prominent section header."""
        bar = char * width
        self._write_both("")
        self._write_both(bar)
        self._write_both("  {}".format(title.upper()))
        self._write_both(bar)
        self._write_both("")

    def subsection(self, title):
        """Print a secondary header."""
        self._write_both("")
        self._write_both("--- {} ---".format(title))
        self._write_both("")

    def table(self, headers, rows, widths=None):
        """
        Print a fixed-width table.

        headers : list of str
        rows    : list of list (each inner list = one row of values)
        widths  : list of int (column widths); auto-computed if None
        """
        if widths is None:
            widths = [max(len(str(h)), max((len(str(r[i])) for r in rows), default=0))
                      for i, h in enumerate(headers)]

        # Header row
        header_line = "  " + "  ".join(
            str(h).ljust(w) for h, w in zip(headers, widths))
        sep_line = "  " + "  ".join("-" * w for w in widths)
        self._write_both(header_line)
        self._write_both(sep_line)
        for row in rows:
            line = "  " + "  ".join(
                str(v).ljust(w) for v, w in zip(row, widths))
            self._write_both(line)
        self._write_both("")

    def key_value(self, key, value, indent=2):
        """Print a key = value line."""
        self._write_both("{}{}  =  {}".format(" " * indent, key, value))

    def close(self):
        """Flush and close the output file."""
        self._write_both("")
        self._write_both("=" * 80)
        self._write_both("End of report. Saved to: {}".format(self.path))
        self._file.close()
        print()
        print("Report saved: {}".format(self.path))

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _write_both(self, line):
        sys.stdout.write(line + "\n")
        sys.stdout.flush()
        self._file.write(line + "\n")
        self._file.flush()
