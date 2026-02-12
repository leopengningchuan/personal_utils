# SQL Related
A centralized reference for SQL syntax, functions, and query patterns commonly used in data analysis

## Table of Contents
- [Project Background](#project-background)
- [Project Goal](#project-goal)
- [Syntax](#syntax)
    - [General](#general)
    - [Math](#math)
    - [Date & Time](#date--time)
    - [String](#string)
- [Concepts](#concepts)
    - [What is Window function?](#what-is-window-function)
    - [Difference between star schema and snowflake schema](#difference-between-star-schema-and-snowflake-schema)
    - [Difference between INNER and OUTER JOINs](#difference-between-inner-and-outer-joins)
    - [Difference between relational and non-relational databases](#difference-between-relational-and-non-relational-databases)
    - [Difference between ROW_NUMBER(), RANK() and DENSE_RANK()](#difference-between-row_number-rank-and-dense_rank)
    - [Difference between CUBE() and ROLLUP()](#difference-between-cube-and-rollup)

## Project Background
This document serves as a personal knowledge base for SQL concepts, syntax, and query techniques frequently used in data analysis and analytics workflows. It consolidates common patterns, functions, and best practices encountered in real-world analytical tasks.

## Project Goal
The goal of this document is to provide a centralized and structured reference for SQL usage, enabling quick recall, clearer understanding, and consistent query writing for data exploration, transformation, and analysis.

## Syntax

### General
- `LIMIT 1 OFFSET 1` – Skip the first row and returns the next one
- `SUM(IF(flag_col = TRUE, 1, 0))` – Count rows where flag is true by summing 1s and 0s
- `OVER(ORDER BY date_col ROWS BETWEEN 2 PRECEDING AND 1 FOLLOWING)` – Window function preceding and following data
- `DELETE FROM table WHERE id IN ()` – Delete the rows in table where id meets the standard
- `CAST(str_col AS data_type)` – Change the column data type
- `BIT_AND() / BIT_OR()` – Perform logical operations on the corresponding bits of two integers
  
---

### Math
- `IFNULL(num_col, 0)` – Use 0 to substitute if the value is NULL
- `POWER(num_col, 3)` – Return the value raised to the 3rd power
- `SQRT(num_col)` – Return the square root of the value
- `LEAST(num_col), GREATEST(num_col)`– Return the minimal/maximal of the value
- `FLOORT(num_col), CEIL(num_col)`– Return the largest/smallest integer value that is less/greater than or equal to the value

---

### Date & Time

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

--- 

### String
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

## Concepts

### What is Window function?
A window function performs a calculation across a set of rows related to the current row, without collapsing the result set like GROUP BY. It uses the OVER() clause to define the window of rows.

---

### Difference between star schema and snowflake schema: 
In a star schema, dimension tables are denormalized and directly connected to the fact table.

In a snowflake schema, dimension tables are normalized into multiple related tables, forming a more complex structure.

---

### Difference between INNER and OUTER JOINs:

An INNER JOIN returns only the rows that have matching values in both tables.

An OUTER JOIN returns matching rows as well as unmatched rows from one or both tables, depending on the type (LEFT, RIGHT, or FULL).

---

### Difference between relational and non-relational databases:
Relational databases store structured data in tables with predefined schemas and relationships, typically using SQL.

Non-relational databases (NoSQL) store data in flexible formats such as key-value, document, column-family, or graph models, and often allow dynamic schemas.

---

### Difference between ROW_NUMBER(), RANK() and DENSE_RANK():
ROW_NUMBER() assigns a unique sequential number to each row.

RANK() assigns the same rank to tied rows but skips the next ranking value.

DENSE_RANK() assigns the same rank to tied rows without skipping subsequent ranking values.

---

### Difference between CUBE() and ROLLUP():
ROLLUP generates hierarchical subtotals from left to right in the GROUP BY clause.

CUBE generates all possible combinations of grouping columns, producing more subtotal combinations.