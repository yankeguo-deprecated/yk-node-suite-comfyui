from .image import *
from .mask import *

NODE_CLASS_MAPPINGS = {
    "YKImagePadForOutpaint": YKImagePadForOutpaint,
    "YKMaskToImage": YKMaskToImage,
}

print('\033[34mYK Node Suite: \033[92mLoaded\033[0m')
