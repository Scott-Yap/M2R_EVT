import junix

import json

with open("garch_model/GARCH_DOGE.ipynb", "r") as f:
    notebook_dict = json.load(f)

with open("garch_model/GARCH_DOGE.ipynb", "w") as f:
    json.dump(notebook_dict, f)

junix.export_images(
    filepath="garch_model/GARCH_DOGE.ipynb",
    output_dir="garch_model/doge_images",
)
