# Python file automation sample

Original AI-assisted demonstration by ShortcutFactory. This is not a past client project.

## Run

Python 3, with no external packages or network calls:

```sh
python3 json_to_csv.py input.json output.csv
```

Input must be a JSON array of objects. Columns follow first-seen order. Missing/null fields become empty cells, nested objects and arrays become compact JSON, and Unicode, commas and newlines are handled by the standard CSV writer. Text that starts with a spreadsheet formula marker is prefixed with an apostrophe; this reduces formula execution risk, but is not a guarantee for every spreadsheet application. Numeric values remain numeric text.

The destination is overwritten, so choose a new filename. This small sample reads the whole input into memory and is not intended for very large exports. Errors return a nonzero exit code.

## Small custom automation work

JSON/CSV conversion, export cleanup, file renaming, or approved API integration. Small defined tasks start at EUR 30, with scope and a fixed quote agreed before work. Delivery includes run instructions and representative input/output checks. Bank transfer preferred.

Contact: peter.shortcutfactory@gmail.com. Please send dummy input, desired output, approximate size and deadline. Do not send passwords or private customer records.

Development is AI-assisted. No claim of independent human review or past client credits.
