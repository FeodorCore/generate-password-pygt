from PyQt5 import uic

ui_file = "generate_password.ui"
py_file = "pattern_2.py"

with open(py_file, "w", encoding="utf-8") as fout:
    uic.compileUi(ui_file, fout)

print(f"Файл {py_file} создан из {ui_file}")
