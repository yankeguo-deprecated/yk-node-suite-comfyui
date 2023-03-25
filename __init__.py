from .utils import print_success
from .image import *
from .mask import *

NODE_CLASS_MAPPINGS = {
    "YKImagePadForOutpaint": YKImagePadForOutpaint,
    "YKMaskToImage": YKMaskToImage,
}

print_success("loaded")
