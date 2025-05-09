# import the packages
from docx import Document

# define the function of replacing the template placeholder with invoice information
def populate_docx_table(item_dict, docx_template_path, new_docx_path):
    """
    Populate a Word docx document table using placeholder keys and a data dictionary.

    Parameters:
        doc_path (str): Path to the input Word template.
        data_dict (dict): Dictionary with keys matching placeholders in the doc.
        output_path (str): Path to save the updated document

    Returns:
        None
    """

    # check the errors for file type
    if isinstance(item_dict, dict) == False:
        raise Exception("item_dict should be a dictionary.")
    elif docx_template_path[-5:] != '.docx':
        raise Exception("docx_template_path should be a docx file.")
    elif new_docx_path[-5:] != '.docx':
        raise Exception("new_docx_path should be a docx file.")

    # open the template docx
    doc = Document(docx_template_path)

    # replace the placeholder in the docx for all the invoices information
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
