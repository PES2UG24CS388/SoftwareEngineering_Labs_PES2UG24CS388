# Lab 5: Static Code Analysis — Reflections

**Name:** R. Pooja  
**SRN:** PES2UG24CS388

## 1. What is static code analysis, and why is it useful?

Static code analysis examines source code without executing it to identify potential bugs, security vulnerabilities, and style violations. It helps developers detect problems early, before the software is deployed. In this lab, Pylint, Bandit, and Flake8 helped identify different categories of issues in the scholarship disbursement program.

## 2. What did you learn from Pylint, Bandit, and Flake8?

Pylint helped identify code-quality and maintainability problems, such as mutable default arguments, missing docstrings, and naming violations. Bandit identified potentially unsafe patterns, including SQL query construction and shell command execution. Flake8 checked Python formatting and style conventions, such as line length and comparisons with `None`. Together, the tools provided complementary views of the program's quality.

## 3. Which issues were most important to fix, and why?

The SQL injection risk was important because unsafe query construction can allow input to interfere with database operations. The mutable default argument was also important because it could cause unexpected sharing of data between function calls. Removing unnecessary shell execution and improving exception handling made the program safer and easier to maintain. Input validation and checks against duplicate disbursement also improved reliability.

## 4. How did static analysis improve the program, and what are its limitations?

Static analysis improved the readability, consistency, and security of the program by identifying issues that could be corrected before execution. The Pylint score increased from 5.00/10 to 9.77/10, and the updated Bandit scan reported no issues. However, static analysis cannot guarantee that a program is completely free of bugs or security vulnerabilities. Runtime testing and careful review are still necessary to verify the program's actual behaviour.

