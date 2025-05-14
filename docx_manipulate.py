# import the packages
from docx import Document
import os
from docx2pdf import convert

# define the function of replacing the template placeholder in tables with item dictionary information
def populate_docx_table(item_dict, docx_template_path, new_docx_path):
    """
    Populate a Word docx document table using placeholder keys and a data dictionary.

    Parameters:
        item_dict (dict): Dictionary with keys matching placeholders in the template.
        docx_template_path (str): Path to the input template.
        new_docx_path (str): Path to save the updated document.

    Returns:
        None

    Raises:
        TypeError: If the input types are invalid (dictionary and sting for docx file).
        FileNotFoundError: If the template file does not exist or cannot be opened.
    """

    # check the errors for file type
    if isinstance(item_dict, dict) == False:
        raise TypeError("item_dict should be a dictionary.")
    elif docx_template_path[-5:] != '.docx':
        raise TypeError("docx_template_path should be a docx file.")
    elif new_docx_path[-5:] != '.docx':
        raise TypeError("new_docx_path should be a docx file.")

    # open the template docx
    try:
        doc = Document(docx_template_path)
    except:
        raise FileNotFoundError("Error: template file not found or is not a valid .docx file.")

    # replace the placeholder in the docx for all item_dict information
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for para in cell.paragraphs:
                    for run in para.runs:
                        if run.text in item_dict.keys():
                            run.text = item_dict[run.text]

    # save the docx to the docx path; print reminder
    doc.save(new_docx_path)
    print(f'---------- {new_docx_path} generated successfully.')

#---

# define the function of replacing the template placeholder in paragraphs with item dictionary information
def populate_docx_paragraph(item_dict, docx_template_path, new_docx_path):
    """
    Populate a Word docx document paragraph using placeholder keys and a data dictionary.

    Parameters:
        item_dict (dict): Dictionary with keys matching placeholders in the template.
        docx_template_path (str): Path to the input template.
        new_docx_path (str): Path to save the updated document.

    Returns:
        None

    Raises:
        TypeError: If the input types are invalid (dictionary and sting for docx file).
        FileNotFoundError: If the template file does not exist or cannot be opened.
    """

    # check the errors for file type
    if isinstance(item_dict, dict) == False:
        raise TypeError("item_dict should be a dictionary.")
    elif docx_template_path[-5:] != '.docx':
        raise TypeError("docx_template_path should be a docx file.")
    elif new_docx_path[-5:] != '.docx':
        raise TypeError("new_docx_path should be a docx file.")

    # open the template docx
    try:
        doc = Document(docx_template_path)
    except:
        raise FileNotFoundError("Error: template file not found or is not a valid .docx file.")

    # replace the placeholder in the docx for all the item_dict information
    for para in doc.paragraphs:
        for run in para.runs:
            for key in item_dict.keys():
                if key in run.text:
                    run.text = run.text.replace(key, item_dict[key])

    # save the docx to the docx path; print reminder
    doc.save(new_docx_path)
    print(f'---------- {new_docx_path} generated successfully.')

#---

def convert_docx_pdf(docx_path, keep = True):
    """
    Convert a Word docx document to a PDF file.

    Parameters:
        docx_path (str): Path to the input docx file.
        keep (bool, optional): Whether to keep the original docx file after conversion. Defaults to True.

    Returns:
        None

    Raises:
        TypeError: If the input path is not a docx file.
    """

    # check the errors for file type
    if docx_path[-5:] != '.docx':
        raise TypeError("docx_path should be a docx file.")

    # convert the docx to pdf
    convert(docx_path)

    # remove the docx if needed
    if keep == False:
        os.remove(docx_path)
        print(f'---------- {docx_path} converted to PDF successfully, original docx file removed.')
    else:
        print(f'---------- {docx_path} converted to PDF successfully, original docx file kept.')
