# Lab 5: Static Code Analysis — Issues and Fixes

**Name:** R. Pooja  
**SRN:** PES2UG24CS388  
**Repository:** L5_20_scholarship_disbursement

## Issues Identified and Fixed

| Issue | Type | Original Finding | Description | Fix Approach |
|---|---|---|---|---|
| Mutable default argument | Bug / Code quality | Pylint W0102 | Using `audit=[]` as a default argument can cause the same list to be shared across function calls. | Changed the default to `None` and created a new list inside the function. |
| SQL injection risk | Security | Bandit B608 | Building SQL queries using string formatting can allow unsafe input to alter a query. | Used parameterized SQL queries with `?` placeholders. |
| Shell command execution | Security | Bandit B605, B607 | `os.system()` executes a shell command and introduces unnecessary security risk. | Removed shell execution and used Python logging for the archive message. |
| Broad exception handling | Code quality / Security | Bandit B110, Pylint W0718 | Catching every exception and ignoring it can hide errors. | Removed the unnecessary exception-handling block. |
| Global variable modification | Maintainability | Pylint W0603 | Modifying a global total makes program state harder to track and maintain. | Calculated the disbursed total directly from the database. |
| Inconsistent return values | Bug / Code quality | Pylint R1710 | A function may return an amount for a valid award but return `None` when the award is missing. | Added explicit `None` returns for missing or already-disbursed awards. |
| Comparison with `None` | Style | Pylint C0121, Flake8 E711 | Comparing a value with `None` using `==` is not the recommended Python style. | Replaced `scheme == None` with `scheme is None`. |
| Non-standard function naming | Style | Pylint C0103 | `bySchemeCount` does not follow Python's snake_case naming convention. | Renamed the function to `by_scheme_count`. |
| Missing documentation | Maintainability | Pylint C0114, C0116 | Missing module and function docstrings make code harder to understand. | Added descriptive docstrings. |
| Long lines and SQL formatting | Style | Pylint C0301, Flake8 E501 | Long lines reduce readability and violate line-length conventions. | Split SQL statements and expressions across multiple lines. |
| Missing input validation | Reliability | Improvement identified during review | Invalid student names, schemes, or award amounts could be accepted. | Added checks for empty names/schemes and invalid or negative amounts. |

## Verification

- Pylint score improved from **5.00/10 to 9.77/10** before the final naming-warning cleanup.
- Bandit reported **No issues identified** after the changes.
- Flake8 was used to check formatting and style; its final output should be reviewed after the fixes.

