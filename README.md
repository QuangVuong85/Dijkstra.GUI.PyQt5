# Dijkstra.GUI.PyQt5
* [Python 3](https://www.python.org/)
* [PyQt5](https://pypi.org/project/PyQt5/)
* [Qt Designer](https://pypi.org/project/pyqt5-tools/)

# Reference
[1](https://www.learnpyqt.com/)

# Virtual Environment
[virtualenv](https://pypi.org/project/virtualenv/)

# Convert .ui to .py
Scripts\pyuic5.exe name_file_ui.ui -o name_file_py.py

# Build app for Windows use [PyInstaller](https://pyinstaller.readthedocs.io/en/stable/)
pyinstaller --clean --noconsole -F -n "name app" -i "icon_app.ico" name_main.py