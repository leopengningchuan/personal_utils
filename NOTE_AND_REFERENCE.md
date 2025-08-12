# Note and Reference
Curated resources and reusable utilities for general programming, documentation, and development workflows

## Table of Contents
- [Project Background](#project-background)
- [Project Goal](#project-goal)
- [Note](#note)
  - [SQL Related](#sql-related)
- [Reference](#reference)
  - [Markdown Related](#markdown-related)
  - [GitHub & Version Control](#github--version-control)

## Project Background
This document collects essential tools, reference materials, and workflow notes that support software development tasks. It serves as a personal knowledge base aimed at strengthening documentation, automation, and overall programming proficiency.

## Project Goal
To provide a centralized reference hub for commonly used techniques and websites across various programming languages and development environments.

## Note

### SQL Related
- `LIMIT 1 OFFSET 1` – Skips the first row and returns the next one
- `SUM(IF(flag = TRUE, 1, 0))` – Counts rows where flag is true by summing 1s and 0s
- `OVER(ORDER BY visited_on ROWS BETWEEN 2 PRECEDING AND 1 FOLLOWING)` – Window function preceding and following data
- `IFNULL(value, 0)` – Uses 0 to subustitute if the value is NULL
- `POWER(value, 3)` & `SQRT(value)` – Returns the value raised to the 3rd power and the square root of the value
- `DATEDIFF(DAY, start_date, end_date)` – Calculates the days between start_date and end_date
- `TIMESTAMPDIFF(SECOND, start_timestamp, end_timestamp)`– Calculates the seconds between start_timestamp and end_timestamp
- `DATE_ADD(date, INTERVAL 10 DAY)` – Gets the 10 days later of date
- `MONTHNAME(date)` & `DAYNAME(date)` – Gets the month name and day name of the date
- `WEEKDAY(date)` – Gets the weekday index (0 = Monday, 6 = Sunday) for the date
- `LEFT(date, 7)` – Gets the year and for the date
- `REPLACE(col, ' ', '')` – Removes the space in the col
- `SUBSTR("test_data", 5, 3)` – Returns a substring starting at position 5 with length 3
- `DELETE FROM table WHERE id IN ()` – Delete the rows in table where id meets the standard

## Reference

### Markdown Related
- [Markdown Guide: Basic Syntax](https://www.markdownguide.org/basic-syntax/) – Common formatting styles for Markdown documents.
- [readme.so](https://readme.so) – Visual tool for generating clean and readable README files.
- [shields.io](https://shields.io) – Generate custom badges for documentation, build status, and version info.
- [Mathematics in R Markdown](https://rpruim.github.io/s341/S19/from-class/MathinRmd.html) – LaTeX math expressions in Markdown.
- [Open Source Initiative](https://opensource.org) – Official resource for open source licensing and governance.

### GitHub & Version Control
- [GitHub Basics (in CN)](https://blog.csdn.net/u011296485/article/details/83717493) – Step-by-step GitHub usage tutorial in Chinese, covering commits, branches, and pull requests.
