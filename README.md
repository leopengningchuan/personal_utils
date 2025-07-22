# personal_utils
Reusable Python utilities for file, text, and data tasks

## Table of Contents
- [Project Background](#project-background)
- [Project Goal](#project-goal)
- [File Structure](#file-structure)
- [Instructions](#instructions)
  - [Using the Utils](#using-the-utils)
  - [Packages Used](#packages-used)
  - [docx_utils](#docx_utils)
    - [populate_docx_table](#populate_docx_table)
    - [populate_docx_paragraph](#populate_docx_paragraph)
  - [pdf_utils](#pdf_utils)
    - [convert_docx_pdf](#convert_docx_pdf)
    - [merge_pdfs](#merge_pdfs)
  - [email_utils](#email_utils)
    - [validate_email](#validate_email)
    - [format_valid_emails](#format_valid_emails)
    - [windows_outlook_send_email](#windows_outlook_send_email)
- [Note and Reference](#note_and_reference)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Project Background
In day-to-day Python development, it's common to write and reuse similar utility functions for tasks like file handling, string formatting, and data processing. Scattering these snippets across different projects can lead to duplication, inconsistency, and maintenance difficulties.

To address this, this repository was created as a personal centralized utility library for commonly used functions. It improves development efficiency by providing a lightweight, reusable toolkit that can be easily imported across multiple projects.

## Project Goal
This project aims to provide a lightweight, reusable Python utility library to support automation, data processing, and scripting tasks across multiple projects with consistent and maintainable code.

## File Structure
Configuration & Metadata:
- `README.md` – project overview
- `LICENSE.txt` – license information
- `.gitignore` – git ignore config
- `.gitattributes` – git attributes config

Core Logic:
- `docx_utils.py` – DOCX related utility functions
- `pdf_utils.py` – PDF related utility functions
- `email_utils.py` – email related utility functions
- `bind_utils.sh` – script to add utils submodule

Note & Reference:
- `NOTE_AND_REFERENCE.md` – notes and references

## Instructions

### Using the Utils
To use functions from `personal_utils`, run the `bind_utils.sh` script to add it as a Git submodule:

```bash
chmod +x bind_utils.sh

./bind_utils.sh
```

This will add the submodule to the `utils/` folder and initialize it automatically.

To update the submodule to the latest version from its remote repository, run the following command from the root of the project:

```bash
git submodule update --remote --merge
```

### Packages Used
- `os`, `warnings`, `logging`, `typing`, `platform`: core Python libraries for basic system operations
- `docx`: for reading and editing DOCX files
- `docx2pdf`: for converting DOCX files into PDF files
- `PyPDF2`: for merging multiple PDF files into one
- `win32com`: for Outlook email automation on Windows

### docx_utils

#### populate_docx_table
This function replaces placeholders in a DOCX file table using values from a Python dictionary. It requires three inputs: a dictionary with placeholder-value pairs, the path to a DOCX template, and the output path for the generated file. The function iterates through all table cells and replaces any exact matches with corresponding values from the dictionary. Only table content is affected — paragraph text outside tables will remain unchanged. Basic input validation is included to ensure file types and dictionary structure are correct.

> [!NOTE]  
> Handling Placeholder Substitution Issues in DOCX Template

When using DOCX templates, placeholders (e.g., `UNITPRICE1`) may not always be stored as a single contiguous string. Instead, DOCX templates can split them into multiple runs (e.g., `UNIT PRICE 1`), especially if the placeholder is manually typed letter-by-letter or if formatting changes occur mid-text. This makes accurate substitution difficult.

To address this, there are two possible solutions:
- Best Practice: Always paste the full placeholder (e.g., `UNITPRICE1`) into the DOCX template instead of typing it character by character. This helps DOCX templates treat it as a single run.
- Programmatic Workaround: Merge all runs in a paragraph into one string, perform substitutions on the combined text, and then rewrite the paragraph with the updated content. However, this method overwrites the original formatting of the paragraph.

Here’s the code implementation of the workaround:

```python
def populate_docx_table(item_dict, docx_template_path, new_docx_path):

    # open the template DOCX
    doc = Document(docx_template_path)

    # replace the placeholder in the DOCX for all the invoices information
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for para in cell.paragraphs:

                    # combine all the run as a full text
                    full_text = ''.join([run.text for run in para.runs])

                    if full_text in item_dict.keys():
                        full_text = item_dict[full_text]

                    # clear the para
                    para.clear()
                    para.add_run(full_text)

    # save the DOCX to the new_docx_path; log reminder
    doc.save(new_docx_path)
    logging.info(f"DOCX generated — Path: {new_docx_path}")
```

---

#### populate_docx_paragraph
This function replaces placeholders in a DOCX file paragraph text using values from a Python dictionary. It requires three inputs: a dictionary with placeholder-value pairs, the path to a DOCX template, and the output path for the generated file. The function iterates through all paragraphs and replaces any exact matches with corresponding values from the dictionary. Only paragraphs content is affected — tables will remain unchanged. Basic input validation is included to ensure file types and dictionary structure are correct.

---

### pdf_utils

#### convert_docx_pdf
This function converts a DOCX file to a PDF format. It requires the path to the input DOCX file and a Boolean flag indicating whether to keep the original file. By default, the original DOCX file is preserved after conversion. If set to `False`, the file will be deleted after the PDF is generated. The function performs basic input validation and uses the `docx2pdf` library to execute the conversion.

---

#### merge_pdfs
This function merges multiple PDF files into a single PDF file. It accepts either a list of PDF file paths or a folder containing PDF files, validates the input format and file types, and then combines the PDFs in the specified order. If a folder is provided, it filters out non-PDF files and optionally raises a warning. The merged output is saved to a user-defined path, and basic checks ensure the output file ends with `.pdf` and that the source files are valid.

> [!CAUTION]  
> DependencyError: PyCryptodome is required for AES algorithm

This error means encrypted files require the `pycryptodome` library while working with PDFs (e.g., using `PyPDF2`). To resolve the dependency and allow the script to process encrypted PDFs properly, the required package can be installed by running:

```python
pip install pycryptodome
```

---

### email_utils

#### validate_email
This function checks whether a given string is a valid email address using a regular expression. It ensures that the input matches a standard email format, including a username, the "@" symbol, a domain name, and a valid top-level domain. It returns `True` if the input is valid, otherwise `False`.

---

#### format_valid_emails
This function validates and formats one or more email addresses. If a single valid email is provided as a string, it returns the string. If a list of valid email addresses is given, it checks each one and returns a semicolon-separated string of all valid entries. Raises a `ValueError` if any address is invalid.

---

#### windows_outlook_send_email
This function automates the process of sending emails through the Windows Outlook desktop client using the `win32com.client` module. It supports multiple recipients in the To, CC, and BCC fields, and allows file attachments. All email addresses are validated and properly formatted before being passed to Outlook. The function checks for input validity, handles both single string and list input formats, and logs the result of the operation. Only works on Windows systems with Microsoft Outlook installed.

## Note and Reference
See [NOTE_AND_REFERENCE.md](https://github.com/leopengningchuan/personal_utils/blob/main/NOTE_AND_REFERENCE.md) for curated resources and reusable utilities that support documentation and development workflows.

## Acknowledgements
- Thanks to Microsoft Word for providing a flexible document format that allows for easy templating.
- Thanks to the Python community for the powerful libraries that made this project possible, including:
  - [`python-docx`](https://pypi.org/project/python-docx/)
  - [`docx2pdf`](https://pypi.org/project/docx2pdf/)
  - [`PyPDF2`](https://pypi.org/project/PyPDF2/)
  - [`pycryptodome`](https://pypi.org/project/pycryptodome/)
  - [`pywin32`](https://pypi.org/project/pywin32/)

## License
This project is licensed under the MIT License - see the [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/leopengningchuan/personal_utils?tab=MIT-1-ov-file) file for details.
