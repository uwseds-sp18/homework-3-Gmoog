
# coding: utf-8

# In[1]:


import unittest
from Homework_3 import create_dataframe
# define class to run tests on this function
class Homework3Test(unittest.TestCase):

    dframe = create_dataframe("/Users/Gaz/Documents/Sqlite/class.db")
    n = dframe.shape[0]
    
    def test_noofrows(self):
        # test to check the count of total rows
        self.assertEqual(self.n,35950)
        
    def test_columnnames(self):
        # test to check if the column names are as required
        col = self.dframe.columns.tolist()
        mylist = ['video_id','category_id','language']
        self.assertListEqual(col,mylist)
        
    def _test_columnkey(self,col):
        # test to check whether a combination of columns is key
        unique_count = len(self.dframe.groupby(col))
        self.assertEqual(unique_count,self.n)
    
    def test_columnkey(self):
        # check which column combinations form a unique key
        #colname1 = ['video_id']
        #colname2 = ['video_id','category_id']
        colname3 = ['video_id','category_id','language']
        #self._test_columnkey(colname1)
        #self._test_columnkey(colname2)
        self._test_columnkey(colname3)
    
    def test_invalidpath(self):
        # test to check whether the value exception is raised for an invalid file name
        self.assertRaises(ValueError,create_dataframe,"invalid_path")
            
    
if __name__=='__main__':
    unittest.main()



