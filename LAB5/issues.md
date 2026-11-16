# Static Code Analysis Issue Table

| Issue | Type | Line(s) Before Fix | Description | Fix Approach |
|---|---|---:|---|---|
| Shell command execution | Security - High | 56 | `os.system()` executes a shell command and can expose the program to command injection. | Replaced it with `subprocess.run()` using an argument list and an absolute executable path. |
| Unsafe deserialization | Security - Medium | 51 | `pickle.load()` can execute malicious code when loading untrusted data. | Replaced pickle serialization with JSON using `json.load()` and `json.dump()`. |
| Mutable default argument | Code quality | 9 | Using `guests=[]` as a default can share the same list between function calls. | Changed the default to `None` and initialized a new list inside the function. |
| Insecure random selection | Security | 72 | `random.choice()` was flagged by Bandit for using a standard pseudo-random generator. | Replaced it with `secrets.choice()` for winner selection. |
| Missing docstrings | Code quality | Multiple | Pylint reported missing module and function docstrings. | Added a module docstring and docstrings to all functions. |
| Naming conventions | Code style | Multiple | Pylint reported function and argument names that did not follow snake_case. | Renamed functions and arguments to snake_case and updated their references. |
| File encoding unspecified | Code quality | 50, 55 | Pylint warned that file encoding was not explicitly specified. | Added `encoding="utf-8"` to file operations. |
| Formatting violations | Formatting | 61, 66, 75, 79 | Flake8 reported spacing and blank-line violations. | Corrected whitespace and blank lines to comply with PEP 8. |
