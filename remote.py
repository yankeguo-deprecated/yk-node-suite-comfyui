class YMSaveImageToS3:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "images": ("IMAGE",),
                "configs": ([],),
            }
        }
