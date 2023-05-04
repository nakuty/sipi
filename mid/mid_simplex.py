from back.simplex import simplex
import eel


@eel.expose
def mid_simplex(func_input, input_min_max, input_count_ogr, input_ogr) -> str:
    return simplex(func_input, input_min_max, input_count_ogr, input_ogr)
