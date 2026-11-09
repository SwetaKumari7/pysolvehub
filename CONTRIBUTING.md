# Contributing to PySolveHub

Thank you for considering a contribution! Beginners are welcome. Please ask questions if anything is unclear.

## 1. Choose an issue

- Check existing issues before starting work.
- For a substantial change, comment on the issue and wait for a maintainer to assign or acknowledge it.
- If you want to add a new problem, explain its topic and source first.
- Avoid starting duplicate work.

## 2. Set up the project

```bash
git clone https://github.com/<YOUR-GITHUB-USERNAME>/pysolvehub.git
cd pysolvehub
python -m venv .venv
```

Activate the environment:

```bash
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

## 3. Create a branch

```bash
git checkout -b add-array-solution
```

Use a descriptive branch name, such as `fix-palindrome-edge-case` or `docs-improve-readme`.

## 4. Add or update a solution

Follow the folder structure and `docs/SOLUTION_TEMPLATE.md`.

A good solution should:
- Use clear names and readable logic.
- Include a source link, not a copied problem statement.
- Explain the approach in your own words.
- State time and space complexity accurately.
- Include tests for normal and edge cases.
- Avoid unnecessary dependencies.

## 5. Run checks

```bash
python -m pytest
```

Please make sure tests pass before opening a pull request.

## 6. Open a pull request

- Push your branch to your fork.
- Open a PR against the `main` branch of this repository.
- Complete the pull request template.
- Link the issue using `Closes #<issue-number>` when applicable.
- Explain what changed and how you tested it.

## Review process

A maintainer may ask questions or request changes. Please respond respectfully and push updates to the same branch. A PR is merged only after review and required checks pass.

## Important contribution rules

- Submit original code and explanations, and respect the license and terms of external problem platforms.
- Do not include passwords, API keys, personal data, or other secrets.
- Do not add generated or unverified claims about performance.
- One focused PR is easier to review than a PR containing unrelated changes.
- Be kind to other contributors.

Thank you for helping make PySolveHub useful!
