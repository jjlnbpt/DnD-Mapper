# DnD Map Display

First install the libraries:
```bash
pip install -r requirements.txt
```
Then to run:
```bash
python renderMap.py <image_file>
```

Depending on the map and monitor that you are using, you will need to adjust these settings.

```python
# MONITOR SETTINGS
# Get that information from this site: https://www.whatismyscreenresolution.org/
monitor_width = 1883
monitor_height = 934
monitor_width_inches = 19.6
monitor_height_inches = 9.7

# MAP SETTINGS
# Enter this information based on the map you are using
cells_per_row = 42
cells_per_column = 34
```
You can check your screen resolution [here](https://www.whatismyscreenresolution.org/)
