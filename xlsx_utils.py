# import the packages
import os, warnings, logging
from typing import List, Dict, Union, Tuple, Sequence, Optional

import openpyxl

logging.basicConfig(
    level = logging.INFO,
    format = '[%(levelname)s] %(asctime)s — %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S'
)

# define the function of adjusting the column format of the worksheet in the workbook
def adjust_xlsx_columns(excel_path: str,
                        worksheet_name: str, 
                        col_num_format_list: Optional[Sequence[Tuple[Sequence[str], str]]] = None,
                        group_col_list: Optional[Sequence[Tuple[str, str, bool]]] = None) -> None:

    """
    Adjust a XLSX file's column number format using the column and format list.

    Parameters:
        docx_template_path (str): Path to the excel.
        worksheet_name (str): Excel worksheet name.
        col_num_format_list (list): list of columns need to be change number format.
        group_col_list (list): list of columns need to be grouped.

    Returns:
        None

    Raises:
        TypeError: If the input types are invalid.
        FileNotFoundError: If the template file does not exist or cannot be opened.
    """
    
    # check the errors for file type
    if not excel_path.endswith('.xlsx'):
        raise TypeError("excel_path should be a xlsx file.")
    elif isinstance(col_num_format_list, list) == False:
        raise TypeError("col_num_format_list should be a list.")
    elif isinstance(group_col_list, list) == False:
        raise TypeError("group_col_list should be a list.")
    
    # open the workbook and worksheet
    wb = openpyxl.load_workbook(excel_path)
    ws = wb[worksheet_name]

    # for all the columns
    for col in ws.columns:
        col_letter = col[0].column_letter
        max_length = 0

        # for all the cells under the column
        for cell in col:

            # get the maximal length of the column
            try:
                if cell.value:
                    max_length = max(max_length, len(str(cell.value)))
            except:
                pass
            

            # adjust the columns based on the column number format
            for col_num_format_group in col_num_format_list:
                col_num_list, format = col_num_format_group
            
                if col_num_format_list and col_letter in col_num_list:
                    cell.number_format = format

            # adjust the column according to the maximal length
            adjusted_width = max_length + 2.5
            ws.column_dimensions[col_letter].width = adjusted_width
    
    # adjust the group columns
    if group_col_list:
        for grp in group_col_list:
            start, end, hidden = grp
            ws.column_dimensions.group(start = start, end = end, hidden = hidden)

    # save the workbook to the excel_path; log reminder
    wb.save(excel_path)
    logging.info(f"XLSX adjusted — Path: {excel_path}")