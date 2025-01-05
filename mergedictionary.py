# -*- coding: utf-8 -*-
"""mergedictionary.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jaPJDRWAkonDDGsWwspgYOLNys9hYtDJ

Merge Two Dictionaries
"""

# Input two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Merge the dictionaries
merged_dict = {**dict1, **dict2}

# Print the result
print(f"Merged dictionary: {merged_dict}")