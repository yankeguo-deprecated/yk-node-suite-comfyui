import torch


class YKImagePadForOutpaint:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "left": ("INT", {"default": 0, "min": 0, "max": 4096, "step": 64}),
                "top": ("INT", {"default": 0, "min": 0, "max": 4096, "step": 64}),
                "right": ("INT", {"default": 0, "min": 0, "max": 4096, "step": 64}),
                "bottom": ("INT", {"default": 0, "min": 0, "max": 4096, "step": 64}),
                "feathering": ("INT", {"default": 0, "min": 0, "max": 4096, "step": 1}),
            }
        }

    RETURN_TYPES = ("IMAGE", "MASK")
    FUNCTION = "expand_image"

    CATEGORY = "image"

    def expand_image(self, image, left, top, right, bottom, feathering):
        d1, d2, d3, d4 = image.size()

        new_image = torch.zeros(
            (d1, d2 + top + bottom, d3 + left + right, d4),
            dtype=torch.float32,
        )
        new_image[:, top:top + d2, left:left + d3, :] = image

        mask = torch.ones(
            (d2 + top + bottom, d3 + left + right),
            dtype=torch.float32,
        )

        if feathering > 0 and feathering * 2 < d2 and feathering * 2 < d3:
            # distances to border
            mi, mj = torch.meshgrid(
                torch.arange(d2, dtype=torch.float32),
                torch.arange(d3, dtype=torch.float32),
                indexing='ij',
            )
            distances = torch.minimum(
                torch.minimum(mi, mj),
                torch.minimum(d2 - 1 - mi, d3 - 1 - mj),
            )
            # convert distances to square falloff from 1 to 0
            t = (feathering - distances) / feathering
            t.clamp_(min=0)
            t.square_()

            mask[top:top + d2, left:left + d3] = t
        else:
            mask[top:top + d2, left:left + d3] = torch.zeros(
                (d2, d3),
                dtype=torch.float32,
            )

        return (new_image, mask)
