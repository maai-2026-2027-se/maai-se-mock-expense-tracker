# Expense Tracker: task pool

Each expense is a dictionary with `person` (nonempty string), `category` (nonempty string), and `cents` (nonnegative integer). Use integer cents throughout; never convert to floating-point currency. Category/person labels in expense records are already canonical. No function may mutate the input.

All nine tasks are required for final acceptance. Each function lives in `app.py`. Inputs follow the data model above unless a task explicitly asks for validation. Return values are checked for equality; object identity matters only where new dictionaries are required. Reuse requirements are checked by peer review.

For every task: add at least one meaningful test in `tests/test_student_<ID>.py`, run the task checks, create its completion marker, and open a PR. Round two also requires a regression demonstration. Round three also requires the shared release-note edit described in `CONTRIBUTING.md`.

## E1 — Total expenses by category

Round 1 · `category_totals(expenses)`

Return a dictionary mapping every observed category to the sum of its cents. Empty input returns `{}`; keep zero-valued categories. Do not mutate records.

No earlier task dependency.

Acceptance tests: `tests/test_E1.py`.

Run: `python3 check.py --task E1`; then `python3 check.py --complete E1`.

## E2 — List the people who paid

Round 1 · `people(expenses)`

Return distinct person labels sorted with Python's normal string order. Match labels exactly; empty input returns `[]`.

No earlier task dependency.

Acceptance tests: `tests/test_E2.py`.

Run: `python3 check.py --task E2`; then `python3 check.py --complete E2`.

## E3 — Find the largest expense

Round 1 · `largest_expense(expenses)`

Return the record with the greatest cents, or `None` for empty input. For a tie, return the first such record in input order.

No earlier task dependency.

Acceptance tests: `tests/test_E3.py`.

Run: `python3 check.py --task E3`; then `python3 check.py --complete E3`.

## E4 — Fix fair bill splitting

Round 2 · `split_bill(cents, participants)`

Return `{person: share_in_cents}`. Sort unique participant labels with normal string order, split evenly, and give one extra cent to each of the first remainder participants. Shares must sum to cents. Raise `ValueError` for negative cents, an empty participant list, or duplicate labels. Assume integer cents and nonempty string labels.

No earlier task dependency.

Acceptance tests: `tests/test_E4.py`.

Run: `python3 check.py --task E4`; then `python3 check.py --complete E4`.

## E5 — Fix category normalization

Round 2 · `normalize_category(label)`

Strip leading/trailing whitespace and apply `casefold()`. Preserve internal whitespace. Raise `ValueError` if the result is empty. Assume a string input.

No earlier task dependency.

Acceptance tests: `tests/test_E5.py`.

Run: `python3 check.py --task E5`; then `python3 check.py --complete E5`.

## E6 — Fix inclusive amount filtering

Round 2 · `filter_expenses(expenses, minimum, maximum)`

Return expenses with `minimum <= cents <= maximum`, in input order. Raise `ValueError` when minimum is negative or maximum is below minimum. Assume integer bounds.

No earlier task dependency.

Acceptance tests: `tests/test_E6.py`.

Run: `python3 check.py --task E6`; then `python3 check.py --complete E6`.

## E7 — Calculate settlement balances

Round 3 · `balances(expenses, participants)`

Reuse `total_cents` and `split_bill`. Return paid cents minus assigned share for every participant, including people who paid nothing. Positive means money to receive; negative means money owed. Sum of balances must be zero. Raise `ValueError` for any payer outside participants, or any participant input invalid for `split_bill`.

Depends on: E4.

Acceptance tests: `tests/test_E7.py`.

Run: `python3 check.py --task E7`; then `python3 check.py --complete E7`.

## E8 — Build the expense summary

Round 3 · `summary(expenses)`

Reuse earlier functions. Return a dictionary with exactly `total_cents`, `categories`, `people`, and `largest`, containing the outputs of the corresponding earlier functions. Empty input uses 0, `{}`, `[]`, and `None`.

Depends on: E1, E2, E3.

Acceptance tests: `tests/test_E8.py`.

Run: `python3 check.py --task E8`; then `python3 check.py --complete E8`.

## E9 — Export expenses to CSV

Round 3 · `to_csv(expenses)`

Return CSV text with header `person,category,cents`, rows in input order, and LF (`\n`) line endings including a final newline. Use Python's `csv` module for commas, quotes, and embedded newlines. Empty input returns the header plus newline.

No earlier task dependency.

Acceptance tests: `tests/test_E9.py`.

Run: `python3 check.py --task E9`; then `python3 check.py --complete E9`.
