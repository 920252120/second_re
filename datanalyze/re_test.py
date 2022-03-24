import os
import re


path = r"C:\Users\LYQ\Desktop\datanalyze\test\2015"
file_name = "flowhour2015_2.csv"

pattern_str = r"(\d{4})_(1?[0-9])"
pattern = re.compile(pattern_str)
matchObj = re.search(pattern, file_name)
print("we find group(): {}".format(matchObj.group()))
print("we find group(1): {}".format(matchObj.group(1)))
print("we find group(2): {}".format(matchObj.group(2)))
print(type(matchObj.group(1)))
