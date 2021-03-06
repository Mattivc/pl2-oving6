from sensobs.sensob import Sensob
from PIL import Image, ImageOps, ImageStat
import numpy as np

class RedDetector(Sensob):

    def __init__(self, cameraSensor):
        super().__init__()
        self.camera = cameraSensor
        self.value = 0.0
        self.confidence = 0.0
        self.active = False

    def _get_image(self):
        return self.camera.get_value()

    def _apply_image_transforms(self, image):
        """
        :param image: Image
        :return: Image
        """
        _, c, _ = image.split()
        im = ImageOps.invert(c)
        self.confidence = ImageStat.Stat(im)._getmean()[0] / 255.0
        print(self.confidence)
        im = im.point(lambda x: x**2 * (512/(255**2)) - 180)

        return im

    def find_mean_x_value(self, M):
        """
        range [-5, 5]
        :return:
        """
        shape = M.shape
        v = np.dot(M.T, np.ones((shape[0], 1)))
        n = len(v)

        center_of_mass = sum([i*v[i] for i in range(n)]) / np.sum(v)
        return ((center_of_mass - n *0.5) / n) * 100

    def update(self):
        self.active = not self.active
        if not self.active:
            return

        image = self._get_image()

        im = self._apply_image_transforms(image)
        data = np.asarray(im, dtype=np.uint8)

        self.value = self.find_mean_x_value(data)

    def get_red_position(self):
        return self.value

    def get_confidence(self):
        return self.confidence
