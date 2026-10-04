"""Expense Tracker: a small standard-library-only teaching project."""
import csv  # noqa: F401 -- available for the round-three CSV task
import io  # noqa: F401 -- available for the round-three CSV task
import json


def total_cents(expenses):
    """Existing working behavior; preserve it while adding features."""
    return sum(expense["cents"] for expense in expenses)


def category_totals(expenses):
    """E1: Total expenses by category. See TASKS.md for the complete contract."""
    raise NotImplementedError("Implement E1: Total expenses by category")


def people(expenses):
    """E2: List the people who paid. See TASKS.md for the complete contract."""
    raise NotImplementedError("Implement E2: List the people who paid")


def largest_expense(expenses):
    return max(expenses, key=lambda expense: expense["cents"], default=None)


def split_bill(cents, participants):
    """E4: Fix fair bill splitting. See TASKS.md for the complete contract."""
    if cents < 0:
        raise ValueError("cents cannot be negative")

    if not participants:
        raise ValueError("participants cannot be empty")

    if len(participants) != len(set(participants)):
        raise ValueError("duplicate participant labels")

    participants = sorted(participants)

    base_share, remainder = divmod(cents, len(participants))

    return {
        person: base_share + (1 if i < remainder else 0)
        for i, person in enumerate(participants)
    }


def normalize_category(label):
    """E5: Fix category normalization. See TASKS.md for the complete contract."""
    result = label.strip().casefold()
    if not result:
        raise ValueError("category label is empty after normalization")
    return result


def filter_expenses(expenses, minimum, maximum):
    """E6: Fix inclusive amount filtering. See TASKS.md for the complete contract."""
    return [expense for expense in expenses if minimum < expense['cents'] < maximum]


def balances(expenses, participants):
    """E7: Calculate settlement balances. See TASKS.md for the complete contract."""
    raise NotImplementedError("Implement E7: Calculate settlement balances")


def summary(expenses):
    """E8: Build the expense summary. See TASKS.md for the complete contract."""
    raise NotImplementedError("Implement E8: Build the expense summary")


def to_csv(expenses):
    """E9: Export expenses to CSV. See TASKS.md for the complete contract."""
    raise NotImplementedError("Implement E9: Export expenses to CSV")


if __name__ == "__main__":
    example = [{'person': 'Ada', 'category': 'food', 'cents': 900}, {'person': 'Lin', 'category': 'travel', 'cents': 300}]
    print(json.dumps(example, indent=2))
    print("total_cents:", total_cents(example))
