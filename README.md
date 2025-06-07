# personal_utils
Reusable Python utilities for file, text, and data tasks

## Table of Contents
- [Project Background](#project-background)
- [Project Goal](#project-goal)
- [File Structure](#file-structure)
- [Instructions](#instructions)
  - [Using the Utils](#using-the-utils)
  - [Packages Used](#using-the-utils)
  - [docx_manipulate.populate_docx_table](#docxmanipulatepopulatedocxtable)
  - [docx_manipulate.populate_docx_paragraph](#docxmanipulatepopulatedocxparagraph)
  - [docx_manipulate.convert_docx_pdf](#docxmanipulateconvertdocxpdf)
  - [docx_manipulate.merge_pdfs](#docxmanipulatemergepdfs)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Project Background
In day-to-day Python development, it's common to write and reuse similar utility functions for tasks like file handling, string formatting, and data processing. Scattering these snippets across different projects can lead to duplication, inconsistency, and maintenance difficulties.

To address this, this repository was created as a personal centralized utility library for commonly used functions. It improves development efficiency by providing a lightweight, reusable toolkit that can be easily imported across multiple projects.

## Project Goal
This project aims to provide a lightweight, reusable Python utility library to support automation, data processing, and scripting tasks across multiple projects with consistent and maintainable code.

## File Structure
- `README.md`
- `LICENSE.txt`
- `.gitignore`
- `docx_manipulate.py`
  - `populate_docx_table()`
  - `populate_docx_paragraph()`
  - `convert_docx_pdf()`
  - `merge_pdfs()`
- `bind_utils.sh`
- `NOTE_AND_REFERENCE.md`

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

---

### Packages Used
- `os`: for file path handling
- `warnings`: for raising warnings
- `docx`: for reading and editing Word docx files
- `docx2pdf`: for converting Word docx files into PDF files
- `PyPDF2`: for merging multiple PDF files into one

---

### docx_manipulate.populate_docx_table
This function replaces placeholders in a Word docx document table using values from a Python dictionary. It requires three inputs: a dictionary with placeholder-value pairs, the path to a Word docx template, and the output path for the generated file. The function iterates through all table cells and replaces any exact matches with corresponding values from the dictionary. Only table content is affected — paragraph text outside tables will remain unchanged. Basic input validation is included to ensure file types and dictionary structure are correct.

> [!NOTE]  
> Handling Placeholder Substitution Issues in Word Docx Template

When using Word docx templates, placeholders (e.g., `UNITPRICE1`) may not always be stored as a single contiguous string. Instead, Word docx templates can split them into multiple runs (e.g., `UNIT PRICE 1`), especially if the placeholder is manually typed letter-by-letter or if formatting changes occur mid-text. This makes accurate substitution difficult.

To address this, there are two possible solutions:
- Best Practice: Always paste the full placeholder (e.g., `UNITPRICE1`) into the Word docx template instead of typing it character by character. This helps Word docx templates treat it as a single run.
- Programmatic Workaround: Merge all runs in a paragraph into one string, perform substitutions on the combined text, and then rewrite the paragraph with the updated content. However, this method overwrites the original formatting of the paragraph.

Here’s the code implementation of the workaround:

```python
def populate_docx_table(item_dict, docx_template_path, new_docx_path):

    # open the template docx
    doc = Document(docx_template_path)

    # replace the placeholder in the docx for all the invoices information
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

    # save the docx to the docx path; print reminder
    doc.save(new_docx_path)
    print(f'---------- {new_docx_path} generated successfully.')
```

---

### docx_manipulate.populate_docx_paragraph
This function replaces placeholders in a Word docx document paragraph text using values from a Python dictionary. It requires three inputs: a dictionary with placeholder-value pairs, the path to a Word docx template, and the output path for the generated file. The function iterates through all paragraphs and replaces any exact matches with corresponding values from the dictionary. Only paragraphs content is affected — tables will remain unchanged. Basic input validation is included to ensure file types and dictionary structure are correct.

---

### docx_manipulate.convert_docx_pdf
This function converts a Word docx file to a PDF format. It requires the path to the input docx file and a Boolean flag indicating whether to keep the original file. By default, the original docx file is preserved after conversion. If set to `False`, the file will be deleted after the PDF is generated. The function performs basic input validation and uses the docx2pdf library to execute the conversion.

---

### docx_manipulate.merge_pdfs
This function merges multiple PDF files into a single PDF file. It accepts either a list of PDF file paths or a folder containing PDF files, validates the input format and file types, and then combines the PDFs in the specified order. If a folder is provided, it filters out non-PDF files and optionally raises a warning. The merged output is saved to a user-defined path, and basic checks ensure the output file ends with `.pdf` and that the source files are valid.

> [!CAUTION]  
> DependencyError: PyCryptodome is required for AES algorithm

This error means encrypted files require the `pycryptodome` library while working with PDFs (e.g., using `PyPDF2`). To resolve the dependency and allow the script to process encrypted PDFs properly, the required package can be installed by running:

```python
pip install pycryptodome
```

## License
This project is licensed under the MIT License - see the [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/leopengningchuan/personal_utils?tab=MIT-1-ov-file) file for details.

## Acknowledgements
- Thanks to Microsoft Word for providing a flexible document format that allows for easy templating.
- Thanks to the Python community for the powerful libraries that made this project possible, including:
  - [`python-docx`](https://pypi.org/project/docx2pdf/)
  - [`openpyxl`](https://pypi.org/project/docx2pdf/)
  - [`PyPDF2`](https://pypi.org/project/PyPDF2/)
  - [`pycryptodome`](https://pypi.org/project/pycryptodome/)
