#!/usr/bin/env python
import pickle

from openpyxl.workbook import Workbook

class WorkbookCreator():
    """Parses input pickle data and outputs an Excel workbook"""
    
    def __init__(self):
        """Constructor - Creates the workbook"""
        self.wb = Workbook()
        self.ws = self.wb.active
        

    def setTitles(self):
        """Set title names and formatting
        Sets the sheet and column titles
        """
        self.ws.title = "Task Data"

        self.ws['A1'] = "Task Name" # content
        self.ws['B1'] = "Set Part Name" # entity[code]
        self.ws['C1'] = "Parent Build Name" # sg_parent_build
        self.ws['D1'] = "Start Date" # start_date
        self.ws['E1'] = "End Date" # due_date


    def parseEntry(self, entry):
        """Parses the entry and adds it to the next row of the worksheet

        Args:
            entry -- The current data entry object to parse
        """
        # Get the next row of the worksheet to populate
        nextRow = self.ws.max_row + 1

        # Verify the values exist before setting them to their cell
        # Task Name
        self.ws.cell(row=nextRow, 
                     column=1, 
                     value=entry['content'] if entry['content'] else '')

        # Set Part Name
        self.ws.cell(row=nextRow, 
                     column=2, 
                     value=entry['entity']['code'][0] if entry['entity'] else '')

        # Parent Build Name
        self.ws.cell(row=nextRow, 
                     column=3, 
                     value=entry['sg_parent_build']['code'] if entry['sg_parent_build'] else '')

        # Start Date
        self.ws.cell(row=nextRow, 
                     column=4, 
                     value=entry['start_date'] if entry['start_date'] else '')

        # End Date
        self.ws.cell(row=nextRow, 
                     column=5, 
                     value=entry['due_date'] if entry['due_date'] else '')


    def importAndParse(self, pickle_file):
        """Imports and parses the data from the file

        Args:
            pickle_file -- name of input pickle file
        """
        # Import data
        with open(pickle_file, 'rb') as f:
            data = pickle.load(f)
        
        # Sort and parse data
        for entry in data:
            self.parseEntry(entry)


    def saveFile(self, output):
        """Saves the workbook to the output file

        Args:
            output -- name of output file
        """
        self.wb.save(output)


def main():
    wb = WorkbookCreator()
    wb.setTitles()

    pickle_file = 'test_data.pkl' 
    wb.importAndParse(pickle_file)

    wb.saveFile('output.xlsx')


if __name__ == '__main__':
    main()
