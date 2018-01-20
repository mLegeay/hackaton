import matplotlib.pyplot as plt
from skimage import data, filters
from scipy import ndimage as ndi

import matplotlib.patches as mpatches

from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import label2rgb

from analyse_flechette.Flechette import Flechette


class TreshAnalyse(object):

    @staticmethod
    def get_flechettes(tresh_2d, debug=False):

        flechettes = list()

        edges = filters.sobel(tresh_2d)
        fill_coins = ndi.binary_fill_holes(edges)

        low = 0.1
        high = 0.35

        # label image regions
        label_image = label(fill_coins)
        image_label_overlay = label2rgb(label_image, image=tresh_2d)

        if debug is True:
            fig, ax = plt.subplots(nrows=2, ncols=2, subplot_kw={'adjustable': 'box-forced'})

        for region in regionprops(label_image):
            # take regions with large enough areas
            if region.area >= 2000:
                # draw rectangle around segmented coins
                minr, minc, maxr, maxc = region.bbox

                flechettes.append(Flechette(minc, minr, maxc - minc, maxr - minr, region.area))

                if debug is True:
                    rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                              fill=False, edgecolor='red', linewidth=2)
                    ax[0, 1].add_patch(rect)

        if debug is True:

            lowt = (fill_coins > low).astype(int)
            hight = (fill_coins > high).astype(int)

            ax[0, 0].imshow(tresh_2d, cmap='gray')
            ax[0, 0].set_title('Original image')

            ax[0, 1].imshow(fill_coins, cmap='magma')
            ax[0, 1].set_title('Sobel edges')

            ax[1, 0].imshow(lowt, cmap='magma')
            ax[1, 0].set_title('Low threshold')

            #ax[1, 1].imshow(hight + hyst, cmap='magma')
            #ax[1, 1].set_title('Hysteresis threshold')

            for a in ax.ravel():
                a.axis('off')

            #print(edges)
            #print(type(edges))

            plt.tight_layout()

            plt.show()

        return flechettes