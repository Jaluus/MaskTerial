import numpy as np
from pycocotools.mask import encode


class Flake:
    """
    This class is used to store the information of a flake.
    """

    def __init__(
        self,
        mask: np.ndarray,
        thickness: str,
        size: int,
        mean_contrast: np.ndarray,
        center: tuple,
        max_sidelength: int,
        min_sidelength: int,
        false_positive_probability: float = 0,
        entropy: float = -1,
    ):
        """
        Initialize a flake object.

        Args:
            mask (np.ndarray): The mask of the flake, a 2D array with 1s and 0s indicating the flake and background respectively.
            thickness (str): The name of the layer the flake is from.
            size (int): The size of the flake in pixels.
            mean_contrast (np.ndarray): The mean contrast of the flake in BGR as defined in "https://arxiv.org/abs/2306.14845".
            center (tuple): The center of the flake in pixels relative to the top left corner of the image.
            max_sidelength (int): The maximum sidelength of the flake in pixels, measured using a rotated bounding box.
            min_sidelength (int): The minimum sidelength of the flake in pixels, measured using a rotated bounding box.
            false_positive_probability (float, optional): The probability of the flake being a false positive. Defaults to 0.
            entropy (float, optional): The Shannon entropy of the flake. Defaults to -1.
        """
        self.mask = mask
        self.thickness = thickness
        self.size = size
        self.mean_contrast = mean_contrast
        self.center = center
        self.max_sidelength = max_sidelength
        self.min_sidelength = min_sidelength
        self.aspect_ratio = round(max_sidelength / (min_sidelength + 1e-5), 1)
        self.false_positive_probability = false_positive_probability
        self.entropy = entropy

    def to_dict(
        self,
        return_bbox: bool = False,
    ) -> dict:
        """
        Convert the flake object to a dictionary.

        Returns:
            dict: A dictionary representation of the flake object. The keys are the attributes of the flake object.
        """
        temp_dict = {
            "mask": encode(np.asfortranarray(self.mask)),
            "thickness": int(self.thickness),
            "size": int(self.size),
            "mean_contrast": [
                int(self.mean_contrast[i]) for i in range(len(self.mean_contrast))
            ],
            "center": [int(self.center[0]), int(self.center[1])],
            "max_sidelength": int(self.max_sidelength),
            "min_sidelength": int(self.min_sidelength),
            "aspect_ratio": float(self.aspect_ratio),
            "false_positive_probability": float(self.false_positive_probability),
            "entropy": float(self.entropy),
        }

        # calculate the bbox of the flake from the mask
        if return_bbox:
            rows = np.any(self.mask, axis=1)
            cols = np.any(self.mask, axis=0)
            rmin, rmax = np.where(rows)[0][[0, -1]]
            cmin, cmax = np.where(cols)[0][[0, -1]]
            temp_dict["bbox"] = [
                int(cmin),
                int(rmin),
                int(cmax - cmin),
                int(rmax - rmin),
            ]

        print(temp_dict)

        return temp_dict

    def __repr__(self) -> str:
        """The string representation of the flake object.

        Returns:
            str: A string representation of the flake object.
        """
        return f"Flake(thickness={self.thickness}, size={self.size:5.0f}px, max_sidelength={self.max_sidelength:5.0f}px, min_sidelength={self.min_sidelength:5.0f}px, false_positive_probability={self.false_positive_probability:3.1%})"
