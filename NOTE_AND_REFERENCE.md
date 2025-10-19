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
General:
- `LIMIT 1 OFFSET 1` – Skip the first row and returns the next one
- `SUM(IF(flag_col = TRUE, 1, 0))` – Count rows where flag is true by summing 1s and 0s
- `OVER(ORDER BY date_col ROWS BETWEEN 2 PRECEDING AND 1 FOLLOWING)` – Window function preceding and following data
- `DELETE FROM table WHERE id IN ()` – Delete the rows in table where id meets the standard
- `CAST(str_col AS data_type)` – Change the column data type
- `BIT_AND() / BIT_OR()` – Perform logical operations on the corresponding bits of two integers

Math related:
- `IFNULL(num_col, 0)` – Use 0 to substitute if the value is NULL
- `POWER(num_col, 3)` – Return the value raised to the 3rd power
- `SQRT(num_col)` – Return the square root of the value
- `LEAST(num_col), GREATEST(num_col)`– Return the minimal/maximal of the value
- `FLOORT(num_col), CEIL(num_col)`– Return the largest/smallest integer value that is less/greater than or equal to the value

Date and Time related
- `DATEDIFF(DAY, start_date_col, end_date_col)` – Calculate the days between start_date and end_date
- `TIMESTAMPDIFF(SECOND, start_timestamp_col, end_timestamp_col)`– Calculate the seconds between start_timestamp and end_timestamp
- `DATE_ADD(date_col, INTERVAL 10 DAY)` – Get the 10 days later of date
- `DATE_SUB(date_col, INTERVAL 10 MONTH)` – Get the 10 months prior of date
- `MONTHNAME(date_col)` – Get the month name of the date
- `DAYNAME(date_col)` – Get the day name of the date
- `WEEKDAY(date_col)` – Get the weekday index (0 = Monday, 6 = Sunday) for the date
- `WEEK(date_col)` – Get the week sequence of the year for the date
- `TIME_FORMAT(timestamp_col, '%H:%i:%s')` – Return the timestamp based on the required time format
- `SEC_TO_TIME(timestamp_col)` – Return the timestamp based on the specified seconds
- `TIME(timestamp_col) BETWEEN '11:00:00' AND '14:00:00'` – Return the timestamp in the required range


String related:
- `LENGTH(str_col)` – Return the length of a string in bytes
- `CHAR_LENGTH(str_col)` – Return the length of a string in characters
- `LEFT(str_col, 7)` – Get the first 7 characters from left
- `GROUP_CONCAT(str_col ORDER BY str_col SEPARATOR ', ')` – Group the string with separator
- `REPLACE(str_col, ' ', '')` – Remove the space in the col
- `SUBSTR(str_col, 3, 4)` – Return a substring starting at position 5 with length 3
- `SUBSTRING_INDEX(str_col, '@', -1)` – Return a substring part after the last @
- `REGEXP '^[a-zA-z][a-zA-z0-9._-]*@test\\.com$'` – Return a string follows the REGEX expression
- `REGEXP_SUBSTR(str_col, '#[A-Za-z0-9_]+')'` – Return a string part that match the REGEX expression
- `str_col LIKE '@%_'` – Return a string that follows the pattern (`%` represents zero, one, or multiple characters; `_` represents one, single character)


## Reference

### Markdown Related
- [Markdown Guide: Basic Syntax](https://www.markdownguide.org/basic-syntax/) – Common formatting styles for Markdown documents.
- [readme.so](https://readme.so) – Visual tool for generating clean and readable README files.
- [shields.io](https://shields.io) – Generate custom badges for documentation, build status, and version info.
- [Mathematics in R Markdown](https://rpruim.github.io/s341/S19/from-class/MathinRmd.html) – LaTeX math expressions in Markdown.
- [Open Source Initiative](https://opensource.org) – Official resource for open source licensing and governance.

### GitHub & Version Control
- [GitHub Basics (in CN)](https://blog.csdn.net/u011296485/article/details/83717493) – Step-by-step GitHub usage tutorial in Chinese, covering commits, branches, and pull requests.
