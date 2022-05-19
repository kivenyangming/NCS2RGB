import js2py
js2py.translate_file('cloor_translate.js', 'example.py')
from example import example
return_rgb = example.ncsToRgb("NCS S 0560-G80Y")
print(return_rgb)

# return_data0 = return_rgb[0]
# return_data1 = list(return_data0)
# R = return_data1[1]
# G = return_data1[2]
# B1 = return_data1[3]

