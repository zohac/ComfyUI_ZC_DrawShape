from .nodes.zc_draw_shape_factory import ZcDrawShapeFactory

# Set the web directory,
# any .js file in that directory will be loaded by the frontend as a frontend extension
# WEB_DIRECTORY = "./somejs"

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "ZcDrawShape": ZcDrawShapeFactory
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "ZcDrawShape": "ZC DrawShape Node"
}
