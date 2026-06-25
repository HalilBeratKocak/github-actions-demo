# GitHub Actions CI Demo

A minimal Python project used to demonstrate a collaborative GitHub workflow
(pull requests + code review) and Continuous Integration with **GitHub Actions**.

## What's inside

| File | Purpose |
|------|---------|
| `calculator.py` | The application code (a tiny calculator). |
| `test_calculator.py` | Automated unit tests (pytest). |
| `.github/workflows/ci.yml` | The GitHub Actions pipeline that runs the tests on every push and pull request. |
| `requirements.txt` | Python dependencies (just pytest). |

## Run the tests locally (optional)

```bash
pip install -r requirements.txt
pytest -v
```

All tests should pass.

---

## How to produce the "Failure (Red)" run for your report

The CI pipeline turns **red** whenever a test fails. To simulate a bug:

1. Open `calculator.py`.
2. Change the `add` function so it is wrong, e.g.:
   ```python
   def add(a, b):
       return a - b   # <-- BUG: should be a + b
   ```
3. Commit and push (ideally on a branch / in a pull request).
4. The `test_add` test will fail, and the Actions run will show a **red ❌**.
   → Screenshot this for your report.

To get the **green ✅** run again, revert that line back to `return a + b`,
commit and push.
