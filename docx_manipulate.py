# import the packages
import os
import warnings
from docx import Document
from docx2pdf import convert
from PyPDF2 import PdfMerger


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
    elif not docx_template_path.endswith('.docx'):
        raise TypeError("docx_template_path should be a docx file.")
    elif not new_docx_path.endswith('.docx'):
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
    elif not docx_template_path.endswith('.docx'):
        raise TypeError("docx_template_path should be a docx file.")
    elif not new_docx_path.endswith('.docx'):
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
    if not docx_path.endswith('.docx'):
        raise TypeError("docx_path should be a docx file.")

    # convert the docx to pdf
    convert(docx_path)

    # remove the docx if needed
    if keep == False:
        os.remove(docx_path)
        print(f'---------- {docx_path} converted to PDF successfully, original docx file removed.')
    else:
        print(f'---------- {docx_path} converted to PDF successfully, original docx file kept.')

#---

def merge_pdfs(pdf_list, output_path):
    """
    Merge multiple PDF files into a single PDF document.

    Parameters:
        pdf_list (list or str): A list of PDF file paths or a folder path containing PDF files.
        output_path (str): The path where the merged PDF will be saved. Must end with '.pdf'.

    Returns:
        None

    Raises:
        TypeError: If the input is not a list of PDF paths or a valid folder path,
                   or if any file in the original PDF list is not a PDF,
                   or if the output file path does not end with '.pdf',
                   or if the final PDF list for combination does not contain any PDF file.
        UserWarning: If the folder contains any non-PDF files.
    """

    # check the errors for file type
    if not output_path.endswith('.pdf'):
        raise TypeError("output_path should be a pdf file.")

    if isinstance(pdf_list, list):
        for file in pdf_list:
            if not file.endswith('.pdf'):
                raise TypeError(f"{file} is not a pdf file.")

    elif os.path.isdir(pdf_list):
        folder_path = pdf_list
        pdf_list = os.listdir(pdf_list)
        non_pdf_list = [file for file in pdf_list if not file.endswith('.pdf')]
        pdf_list = [folder_path + '/' + file for file in pdf_list if file.endswith('.pdf')]

        if len(non_pdf_list) == 1:
            warnings.warn(f"{len(non_pdf_list)} file in the folder is not a pdf file.")
        elif len(non_pdf_list) > 1:
            warnings.warn(f"{len(non_pdf_list)} files in the folder are not pdf files.")

    else:
        raise TypeError(f"{pdf_list} should be a list of pdf files or a valid folder path.")

    # check the length of the pdf_list
    if len(pdf_list) == 0:
        raise TypeError("There is no pdf file in the merged file list.")
    else:
        print('---------- merge the following pdf files:')
        for file in pdf_list:
            print(file)

    # merge the pdf files
    merger = PdfMerger()

    for pdf in pdf_list:
        merger.append(pdf)

    # save the merged pdf file to the output path; print reminder
    merger.write(output_path)
    merger.close()
    print(f'---------- {output_path} merged successfully.')
