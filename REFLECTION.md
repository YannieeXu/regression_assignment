REFLECTION -- Assignment 3

1. Commit messages: manual vs AI

My hand-written commit messages are short and functional (e.g., "Add ai/ file listing to README.md"). The AI version would likely produce more descriptive messages with context, like "feat: add regression diagnostics with annotated plots for Python and R". For a project I would inherit a year from now, I prefer the AI style -- descriptive messages make it easier to understand the history without reading the diff.

2. AI code review

The AI code review caught a few real issues: it noted that the Python and R scripts could benefit from better error handling (try/except for missing files), and that plot annotation positioning should be consistent between the two implementations. It did not flag any false positives. The review was accurate but shallow -- it caught surface-level style issues rather than deep logic errors.

3. README comparison: manual vs README_AI.md

The manual README is more concise and includes exact output values. The AI-generated README is better structured with clearer setup instructions. For a new contributor, the AI version is more useful because it explains the diagnostics in plain terms and provides cleaner usage examples.

4. Habit to carry forward

Write more descriptive commit messages. The AI approach of explaining both the "what" and the "why" in commit messages makes the project history much more readable.
