"""Expense Tracker: a small standard-library-only teaching project."""
import csv
import io
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
    """E3: Find the largest expense. See TASKS.md for the complete contract."""
    raise NotImplementedError("Implement E3: Find the largest expense")


def split_bill(cents, participants):
    """E4: Fix fair bill splitting. See TASKS.md for the complete contract."""
    return {person: cents // len(participants) for person in participants}


def normalize_category(label):
    normalized = label.strip().casefold()
    if not normalized:
        raise ValueError("Category must not be empty")
    return normalized


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
