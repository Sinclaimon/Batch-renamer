import pytest
from renamer_lib import get_renamed_file_path, get_logger

@pytest.fixture
def logger():
    return get_logger(True)

@pytest.mark.parametrize("existing_name, string_to_find, string_to_replace, prefix, suffix, expected", [
    ("grass_file_01.ma", "_file_01", "", "M_", "", "M_grass.ma"),
    ("metal_file_01.ma", "_file_01", "", "M_", "", "M_metal.ma"),
    ("rock_file_final_new_02.ma", ("_file_final_new_02", "_file_final_new"), "", "M_", "", "M_rock.ma"),
    ("hello_world.txt", "hello_world", "NOTE_hello_world", "", "_TEMP", "NOTE_hello_world_TEMP.txt"),
    ("lorem_ipsum.txt", "lorem_ipsum", "NOTE_lorem_ipsum", "", "_TEMP", "NOTE_lorem_ipsum_TEMP.txt"),
    ("texture_grass_color.png", ("texture", "tex"), "T", "", "_C", "T_grass_C.png"),
    ("texture_metal_diffuse.png", ("texture", "tex"), "T", "", "_C", "T_metal_C.png"),
    ("tex_rock_diffuse.png", ("texture", "tex"), "T", "", "_C", "T_rock_C.png")
])
def test_get_renamed_file_path(logger, existing_name, string_to_find, string_to_replace, prefix, suffix, expected):
    result = get_renamed_file_path(logger, existing_name, string_to_find, string_to_replace, prefix, suffix)
    assert result == expected, f"Expected {expected}, but got {result}"