import os
import tempfile
import subprocess

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


def save_image(image, name):
    try:

        path = os.path.join(tempfile.gettempdir(), name + ".png")

        if isinstance(image, bpy.types.Image):
            if(image.is_dirty):
                image.reload()
                image.file_format = "PNG"
        else:
            print("Output Node: Invalid input image.")
            raise Exception("Invalid input image")
        
        print(f"Output Node: Saving image to {path}")

        if(image.name == "Render Result" or image.name == "Viewer Node"):
            image.save_render(filepath=path)
        else:
            image.save(filepath=path)

        return path
    
    except:
        print("Failed to save image")
        return None


def run_gmic(command, name):
    try:

        output_path = os.path.join(tempfile.gettempdir(), name + ".png")

        gmic_path = get_preference_path()

        gmic_command = f"{gmic_path} {command} -o {output_path}"

        print(f"GMIC command: {gmic_command}")

        subprocess.run(gmic_command, shell=True, check=True)

        if os.path.exists(output_path):
                
            image = bpy.data.images.get(name)
            if image:
                image.reload()
            else:
                image = bpy.data.images.load(output_path, check_existing=True)
                image.name = name

            print(f"Output image loaded: {image.name}")
        else:
            raise Exception("Failed to load output image")

        return True

    except:
        print("Failed to execute GMIC command")
        return False



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
