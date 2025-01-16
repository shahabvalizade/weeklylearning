Install on system level:
sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0
sudo apt install gir1.2-webkit2-4.1

check if gi is working:
python -c "import gi; print('gi module is working')"

run:
python3 simplebrowser.py