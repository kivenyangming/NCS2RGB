该项目可以直接通过NCS编码转化为对应的RGB值，调用cloor_translate.js通过js2py转化为example.py
RUN test.py
```
import js2py
js2py.translate_file('cloor_translate.js', 'example.py')
from example import example
return_rgb = example.ncsToRgb("NCS S 0560-G80Y")
print(return_rgb)
```
更改"NCS S 0560-G80Y" 即可得到该NCS对应的RGB


The project can be directly converted to the corresponding RGB value through NCS encoding,
call color_translate.js to convert to example.py through js2py
RUN test.py
```
import js2py
js2py.translate_file('cloor_translate.js', 'example.py')
from example import example
return_rgb = example.ncsToRgb("NCS S 0560-G80Y")
print(return_rgb)
```
Change "NCS S 0560-G80Y" to get the RGB corresponding to the NCS
