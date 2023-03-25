

class YKMaskToImage:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "mask": ("MASK",),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "mask_to_image"

    CATEGORY = "mask"

    def mask_to_image(self, mask):
        return (mask.unsqueeze(0).unsqueeze(-1).expand(-1, -1, -1, 3),)
