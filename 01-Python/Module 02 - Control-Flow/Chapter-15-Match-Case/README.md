# Chapter 15 - `match-case`

## 🎯 Learning Objectives

By the end of this chapter, you will:

- Understand `match-case`
- Compare it with `if-elif`
- Write cleaner multi-option programs
- Apply it in menus and command routing

---

# What is `match-case`?

`match-case` compares one value against multiple exact values.

Syntax:

```python
match variable:
    case value1:
        ...
    case value2:
        ...
    case _:
        ...
```

`case _:` acts as the default case.

---

# Example

```python
day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case _:
        print("Invalid")
```

---

# When to Use

Use `match-case` when checking:

- Menu options
- Commands
- Roles
- Status values
- Fixed choices

---

# When NOT to Use

Do not use `match-case` for:

- Numeric ranges
- Comparisons (`>`, `<`, `>=`, `<=`)
- Complex Boolean logic

Use `if-elif` instead.

---

# `if-elif` vs `match-case`

| `if-elif` | `match-case` |
|-----------|--------------|
| Best for comparisons and ranges | Best for exact values |
| Flexible conditions | Cleaner for menus and commands |

---

# AI Connection

AI assistants often route commands.

Example:

```python
match intent:
    case "translate":
        ...
    case "summarize":
        ...
    case "code":
        ...
```

---

# Key Takeaways

- `match-case` compares one value to many exact values.
- `case _:` is the default case.
- Use `match-case` for menus and command routing.
- Use `if-elif` for ranges and comparisons.

---

# Interview Questions

1. What is `match-case`?
2. When should you use it?
3. What is the purpose of `case _:`?
4. Why can't `match-case` replace every `if` statement?

---

# Assignment

- Weekday Finder
- Calculator Menu
- Traffic Signal
- User Role Router
- AI Command Router

---

# Summary

- `match-case` makes code cleaner when checking fixed values.
- It complements `if-elif`; it does not replace it.
- It is commonly used in menus, interpreters, and command-based applications.