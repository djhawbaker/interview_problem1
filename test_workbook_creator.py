#!/usr/bin/env python
import unittest

from workbook_creator import WorkbookCreator 

class TestWorkbookCreator(unittest.TestCase):
    """Class to test the dictionary to Excel script"""
    # A set of valid sample values to use as a base
    valid_test_values = {'due_date' : '2016-12-08',
                         'entity' : {
                            'code' : ['Test Prop 1'],
                            'type' : 'CustomEntity18', 
                            'id': 3194}, 
                         'content' : 'design',
                         'sg_status_list' : None,
                         'id': 144909,
                         'type' : 'Task',
                         'start_date': '2016-12-05',
                         'sg_parent_build': {
                            'code': "Horace's Home",
                            'type': 'CustomEntity18',
                            'id': 2291}
                         }

    def setUp(self):
        """Setup test fixture: Instantiate the class to test"""
        self.wb = WorkbookCreator()
    
    def testContent(self): 
        """Test standard and obscure values for the content field"""
        self.wb.parseEntry(self.valid_test_values)

        # Verify the value got set to the correct cell
        self.assertEqual(self.wb.ws['A2'].value, self.valid_test_values['content'])

    def testContentNone(self):
        """Test Null values"""
        # Copy the values to modify
        test_values = dict(self.valid_test_values) 
        test_values['content'] = None
        self.wb.parseEntry(test_values)
        self.assertEqual(self.wb.ws['A2'].value, '')

    @unittest.skip("TODO")
    def testContentObscure(self):
        """Test obscure values"""
        self.assertTrue(True)

    def testEntity(self):
        """Test standard and obscure values for the entity field"""
        self.wb.parseEntry(self.valid_test_values)

        # Verify the value got set to the correct cell
        self.assertEqual(self.wb.ws['B2'].value, 
                         self.valid_test_values['entity']['code'][0])

    def testEntityNone(self):
        """Test Null values"""
        # Copy the values to modify
        test_values = dict(self.valid_test_values) 
        test_values['entity'] = None
        self.wb.parseEntry(test_values)
        self.assertEqual(self.wb.ws['B2'].value, '')

    @unittest.skip("TODO")
    def testEntityObscure(self):
        """Test obscure values"""
        self.assertTrue(True)

    def testParentBuild(self):
        """Test standard and obscure values for the sg_parent_build field"""
        self.wb.parseEntry(self.valid_test_values)

        # Verify the value got set to the correct cell
        self.assertEqual(self.wb.ws['C2'].value, 
                         self.valid_test_values['sg_parent_build']['code'])

    def testParentBuildNone(self):
        """Test Null values"""
        # Copy the values to modify
        test_values = dict(self.valid_test_values) 
        test_values['sg_parent_build'] = None
        self.wb.parseEntry(test_values)
        self.assertEqual(self.wb.ws['C2'].value, '')

    @unittest.skip("TODO")
    def testParentBuildObscure(self):
        """Test obscure values"""
        self.assertTrue(True)

    def testStartDate(self):
        """Test standard and obscure values for the start_date field"""
        self.wb.parseEntry(self.valid_test_values)

        # Verify the value got set to the correct cell
        self.assertEqual(self.wb.ws['D2'].value, 
                         self.valid_test_values['start_date'])

    def testStartDateNone(self):
        """Test Null values"""
        # Copy the values to modify
        test_values = dict(self.valid_test_values) 
        test_values['start_date'] = None
        self.wb.parseEntry(test_values)
        self.assertEqual(self.wb.ws['D2'].value, '')

    @unittest.skip("TODO")
    def testStartDateObscure(self):
        """Test obscure values"""
        self.assertTrue(True)

    def testDueDate(self):
        """Test standard and obscure values for the due_date field"""
        self.wb.parseEntry(self.valid_test_values)

        # Verify the value got set to the correct cell
        self.assertEqual(self.wb.ws['E2'].value, 
                         self.valid_test_values['due_date'])

    def testDueDateNone(self):
        """Test Null values"""
        # Copy the values to modify
        test_values = dict(self.valid_test_values) 
        test_values['due_date'] = None
        self.wb.parseEntry(test_values)
        self.assertEqual(self.wb.ws['E2'].value, '')

    @unittest.skip("TODO")
    def testDueDateObscure(self):
        """Test obscure values"""
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
