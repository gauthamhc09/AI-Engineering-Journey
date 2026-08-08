# Chapter 19 – break, continue, and pass

## break

- Immediately exits the current loop.
- Execution continues after the loop.

Example:

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

---

## continue

- Skips the remaining statements in the current iteration.
- Continues with the next iteration.

Example:

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

## pass

- Placeholder statement.
- Does nothing.
- Used when Python requires a block of code.

Example:

```python
def future_function():
    pass
```

---

## Differences

| Keyword | Action |
|----------|--------|
| break | Exit the loop |
| continue | Skip current iteration |
| pass | Do nothing |

---

## Real Software Uses

- Stop searching after finding a result (`break`)
- Skip invalid records (`continue`)
- Placeholder for future implementation (`pass`)

---

## AI Applications

- Skip corrupt training data
- Stop searching after finding relevant context
- Build incomplete AI pipeline functions

---

## Best Practices

- Use `break` to improve efficiency.
- Use `continue` for filtering.
- Use `pass` only as a placeholder.

---

## Interview Questions

1. Difference between `break`, `continue`, and `pass`.
2. Why is `pass` required?
3. When would you use `continue`?

---

## Assignments

- Stop loop using `break`
- Skip values using `continue`
- Placeholder function with `pass`
- Password checker
- Menu-driven calculator