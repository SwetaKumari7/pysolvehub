# PySolveHub

**Learn. Solve. Share. Contribute.**

PySolveHub is a beginner-friendly, community-driven collection of Python problem-solving examples. Contributors can add solutions, improve explanations, write tests, fix mistakes, and help make programming practice more accessible.

## What you'll find

- Python solutions organized by topic
- Clear explanations and complexity analysis
- Small, readable examples
- Tests for checking solution behavior
- Beginner-friendly issues for first-time contributors

## Getting started

1. Browse the topic folders in [`solutions/`](solutions/).
2. Read the problem's `README.md` or the comments/docstring in its solution.
3. Run the tests locally.
4. Want to contribute? Read [`CONTRIBUTING.md`](CONTRIBUTING.md).

### Run locally

```bash
# Create a virtual environment
python -m venv .venv

# Windows PowerShell:
.\.venv\Scripts\Activate.ps1

# Windows Command Prompt:
.venv\Scripts\activate.bat

# macOS/Linux:
source .venv/bin/activate

# Install dependencies
python -m pip install -r requirements-dev.txt

# Run tests
python -m pytest
```

## Current topics

| Topic | Examples |
|---|---|
| Arrays | Two Sum |
| Strings | Palindrome check |

More topics will be added through reviewed contributions.

## Solution standards

Each contribution should include:

- A link to the original problem or a clearly stated original exercise
- An independently written explanation (do not copy copyrighted problem statements)
- A readable Python implementation
- Time and space complexity, with a brief justification
- Tests covering normal cases and useful edge cases

See [`docs/SOLUTION_TEMPLATE.md`](docs/SOLUTION_TEMPLATE.md).

## Ways to contribute

You don't need to be an expert. You can:

- Add a new solution
- Improve an explanation
- Add missing tests or edge cases
- Fix a bug or typo
- Improve documentation

Look for issues labeled `good first issue` or `help wanted`.

## Community

Please be respectful and constructive. Read our [Code of Conduct](CODE_OF_CONDUCT.md).

## License

This project is licensed under the MIT License. See [`LICENSE`](LICENSE).
