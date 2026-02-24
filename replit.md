# replit.md

## Overview

This is a Python-based financial/mathematical computation project that calculates asset depreciation using two different methods:

1. **Straight-Line Depreciation** - Computes equal annual depreciation amounts over a fixed period (uniform distribution of cost over useful life).
2. **Declining Balance (Accelerated) Depreciation** - Uses a coefficient-based method where depreciation decreases each year as the accumulated depreciation grows.

The project computes depreciation schedules for an asset with an initial cost of 100,000 over 5 years, outputs results in tabular format, and generates a line chart comparing the two methods.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

This is a single-file Python script (`main.py`) with no complex architecture. It follows a linear procedural flow:

1. **Symbolic Math Layer** — Uses SymPy to define depreciation formulas symbolically before substituting concrete values. This allows formulas to be expressed cleanly and reused, though for this scale a simpler numeric approach would also work.

2. **Data Processing Layer** — Uses Pandas to organize computed depreciation values (annual amounts and residual values) into DataFrames for clean tabular output.

3. **Visualization Layer** — Uses Matplotlib to plot residual asset values over time for both depreciation methods side-by-side, saving the result as `plot1.png`.

### Key Design Decisions

- **SymPy for formula representation**: Depreciation formulas are defined symbolically and then evaluated with `.subs()`. This adds clarity to the math but introduces a heavier dependency than necessary for pure numeric computation.
- **Output as saved PNG**: The chart is saved to a file (`plot1.png`) rather than displayed interactively, making it suitable for headless/server environments like Replit.
- **No modular structure**: Everything lives in one file with no functions or classes. If extending this project, consider refactoring into functions for each depreciation method.

## External Dependencies

### Python Packages

| Package | Purpose |
|---------|---------|
| `sympy` | Symbolic mathematics — defines and evaluates depreciation formulas |
| `pandas` | Data organization — creates tabular output of depreciation schedules |
| `matplotlib` | Visualization — generates comparison line chart of depreciation methods |

### No External Services

There are no databases, APIs, authentication systems, or third-party service integrations. All computation is local and self-contained.