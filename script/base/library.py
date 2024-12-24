import bpy

def get_package_name():
    return __package__.replace(".script.base", "")

def get_preference():
    preferences = bpy.context.preferences
    return preferences.addons[get_package_name()].preferences

def get_preference_path():
    return get_preference().gmic_path

def get_preference_isRTL():
    return get_preference().graph_layout

def create_enum(items = []):
    enum_items = []
    index = 0
    for item in items:
        enum_items.append((str(index), item, ""))
        index += 1
    return enum_items

def color_channels():
    return ["All",
        "RGBA [All]",
        "RGB [All]",
        "RGB [Red]",
        "RGB [Green]",
        "RGB [Blue]",
        "RGBA [Alpha]",
        "Linear RGB [All]",
        "Linear RGB [Red]",
        "Linear RGB [Green]",
        "Linear RGB [Blue]",
        "YCbCr [Luminance]",
        "YCbCr [Blue-Red Chrominances]",
        "YCbCr [Blue Chrominance]",
        "YCbCr [Red Chrominance]",
        "YCbCr [Green Chrominance]",
        "Lab [Lightness]",
        "Lab [ab-Chrominances]",
        "Lab [a-Chrominance]",
        "Lab [b-Chrominance]",
        "Lch [ch-Chrominances]",
        "Lch [c-Chrominance]",
        "Lch [h-Chrominance]",
        "HSV [Hue]",
        "HSV [Saturation]",
        "HSV [Value]",
        "HSI [Intensity]",
        "HSL [Lightness]",
        "CMYK [Cyan]",
        "CMYK [Magenta]",
        "CMYK [Yellow]",
        "CMYK [Key]",
        "YIQ [Luma]",
        "YIQ [Chromas]",
        "RYB [All]",
        "RYB [Red]",
        "RYB [Yellow]",
        "RYB [Blue]"
    ]
