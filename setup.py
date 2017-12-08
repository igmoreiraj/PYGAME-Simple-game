import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = "C:\\Program Files\\Python35\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Program Files\\Python35\\tcl\\tk8.6"

executables=[cx_Freeze.Executable("D&D.py")]

cx_Freeze.setup(
    name="Dragons and Dungeons",
    options={"build_exe":{"packages":["pygame"],
                          "include_files":["cav2.jpg","dungeon2.jpg"]}},
    executables = executables
    )
