# PPM-py-viewer
It's a simple ppm viewer in Python based on PyGame
### Don't use it 
It works ! Yes :)
But it's not compatible with every ppm files. This is ok :
```ppm
P3
3 2
255
255 255 0
255 0 255
0 255 255
0 0 255
255 0 0
0 255 0
```
But this is not compatible :
```ppm
P3
3 2
255
255 255 0 255 0 255 0 255 255
0 0 255 255 0 0 0 255 0
```
You cannot choose which file to upload without modifying the code, and also, there is no error handling (yet).

 ### But if you are crazy 
 Be sure you have PyGame installed and :
 ```
 git clone https://github.com/shika-blyat/py-ppm-viewer/
 cd py-ppm-viewer
 python main.py
```
