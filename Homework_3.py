
# coding: utf-8

# In[3]:


import pandas as pd
import sqlite3
import pathlib
def create_dataframe(file_path):
    # connect to the database in sqlite3
    # commented the try-except block for unit test file to check exception raised.
    #try:
        if pathlib.Path(file_path).exists() is False:
            raise ValueError("File not Found")
        conn = sqlite3.connect(file_path)
        # run the query and return the results in a dataframe
        df = pd.read_sql_query("select video_id,category_id,'us' as language from USvideos UNION select video_id,category_id,'fr' as language from FRvideos UNION select video_id,category_id,'gb' as language from GBvideos UNION select video_id,category_id,'de' as language from DEvideos UNION select video_id,category_id,'ca' as language from CAvideos;", conn)
        return df
    #except ValueError:
     #   print("No valid file found at the path provided!!")

