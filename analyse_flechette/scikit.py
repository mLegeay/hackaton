import imageio
import numpy as np
from skimage.measure import compare_ssim as ssim
import matplotlib.pyplot as plt
from os.path import exists
from skimage import io, color, img_as_float
from skimage.feature import corner_peaks, plot_matches, canny
import cv2


class VideoIntrouvableException(Exception):
    pass


class VideoFormatException(Exception):
    pass


class FlechetteSciKit(object):

    def __init__(self, fichier):

        if exists(fichier) is False:
            raise VideoIntrouvableException('Désolé, mais le fichier "{0}" est introuvable !'.format(fichier))

        self._fichier = fichier
        self._video = imageio.get_reader(self._fichier, 'ffmpeg')

        self._meta = self._video.get_meta_data()
        self._nframes = self._meta['nframes']

        self._image_a = self._video.get_data(5)
        self._image_b = self._video.get_data(self._nframes-1)

    @staticmethod
    def mse(image1, image2):
        err = np.sum((image1.astype("float") - image2.astype("float")) ** 2)
        err /= float(image1.shape[0] * image1.shape[1])

        # return the MSE, the lower the error, the more "similar" the two images are
        return err

    @property
    def nframes(self):
        return self._nframes

    @property
    def fichier(self):
        return self._fichier

    @property
    def meta(self):
        return self._meta

    @property
    def coeff_ssim(self):
        return ssim(self._image_a, self._image_b, multichannel=True)

    @property
    def coeff_mse(self):
        return FlechetteSciKit.mse(self._image_a, self._image_b)

    def coeff_ssim_n(self, image_id):
        """
        Récupère le coeff SSIM image début avec image choisie
        :param image_id: Numéro de la frame vidéo
        :return: Coeff SSIM [-1, 1]
        :rtype: float
        """
        return ssim(self._image_a, self._video.get_data(image_id), multichannel=True)

    def diff_n(self, image_id, seuil=200):

        (score, diff) = ssim(
            color.rgb2gray(img_as_float(self._image_a)),
            color.rgb2gray(img_as_float(self._video.get_data(image_id))),
            full=True)

        ar_diff = (diff * 255).astype("uint8")

        thresh = cv2.threshold(ar_diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        cv2.imshow("tresh", thresh)
        cv2.waitKey(0)
        return ar_diff

    def evolution_ssim(self):
        r = list()
        for i in range(6, self._nframes-1, 5):
            r.append(ssim(self._image_a, self._video.get_data(i), multichannel=True))
        return r

    def evolution_ssim_plot(self):

        frames = list(range(6, self._nframes-1))
        ssim_coeffs = self.evolution_ssim()

        fig, ax = plt.subplots()

        ax.add_artist(plt.Line2D(frames, ssim_coeffs))

        plt.show()

    def get_cases_rouges(self):
        image = img_as_float(self._image_a)

        black_mask = color.rgb2gray(image) < 0.1
        distance_red = color.rgb2gray(1 - np.abs(image - (1, 0, 0)))
        distance_red[black_mask] = 0

        return corner_peaks(distance_red, threshold_rel=0.9, min_distance=50)

    def cases_rouges_plot(self):
        image = img_as_float(self._image_a)

        black_mask = color.rgb2gray(image) < 0.1
        distance_red = color.rgb2gray(1 - np.abs(image - (1, 0, 0)))
        distance_red[black_mask] = 0

        coords_red = self.get_cases_rouges()

        f, ((ax0, ax1), (ax2, ax3)) = plt.subplots(2, 2, figsize=(15, 10))
        ax0.imshow(image)
        ax0.set_title('Input image')
        ax1.imshow(image)
        ax1.set_title('Marker locations')
        ax1.plot(coords_red[:, 1], coords_red[:, 0], 'ro')

        ax1.axis('image')
        ax2.imshow(distance_red, interpolation='nearest', cmap='gray')
        ax2.set_title('Distance to pure red')
        plt.show()

    def comparaison_plot(self):
        # setup the figure
        fig = plt.figure('Comparaison FIG')
        plt.suptitle("MSE: %.2f, SSIM: %.2f" % (self.coeff_mse, self.coeff_ssim))

        # show first image
        ax = fig.add_subplot(1, 2, 1)
        plt.imshow(self._image_a, cmap=plt.cm.get_cmap('gray'))
        plt.axis("off")

        # show the second image
        ax = fig.add_subplot(1, 2, 2)
        plt.imshow(self._image_b, cmap=plt.cm.get_cmap('gray'))
        plt.axis("off")

        # show the images
        plt.show()
