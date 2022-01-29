import math
import os

import cv2
import matplotlib.pyplot as plt
import numpy as np
import skimage.measure as measure


def features_extraction(features_list, reading_path, writing_path, mode="MRI"):
    reading_path_f = os.listdir(reading_path)
    writing_path_f = os.listdir(writing_path)
    counter = 100000
    img_data_arr = []

    for image in writing_path_f:
        os.remove(writing_path + '/' + image)

    for image in reading_path_f:
        if mode == "MRI":  # filters for MRI
            img = cv2.imread(reading_path + '/' + image, 0)
            lower_white = np.array([6], dtype=np.uint8)
            upper_white = np.array([255], dtype=np.uint8)
            thresh = cv2.inRange(img, lower_white, upper_white)  # binarization
            median = cv2.medianBlur(thresh, 5)  # medial filter
            kernel = np.ones((5, 5), np.uint8)  # box sizes
            closing = cv2.morphologyEx(median, cv2.MORPH_CLOSE, kernel,
                                       iterations=3)  # morphological closure operation
        else:  # filters for CT
            img = cv2.imread(reading_path + '/' + image, 0)
            lower_white = np.array([6], dtype=np.uint8)
            upper_white = np.array([255], dtype=np.uint8)
            thresh = cv2.inRange(img, lower_white, upper_white)
            median = cv2.medianBlur(thresh, 7)
            kernel = np.ones((5, 5), np.uint16)
            closing = cv2.morphologyEx(median, cv2.MORPH_CLOSE, kernel, iterations=3)

        labels = measure.label(closing)  # labelling
        features = measure.regionprops(labels)  # features extraction
        plt.figure(figsize=(6, 6), dpi=100)
        plt.imshow(closing, cmap=plt.cm.gray)
        y0, x0 = features[0].centroid  # designation of the center of the area found
        plt.plot(x0, y0, '.r', markersize=15)
        minr, minc, maxr, maxc = features[0].bbox  # determining the size of the area found
        bx = (minc, maxc, maxc, minc, minc)
        by = (minr, minr, maxr, maxr, minr)
        plt.plot(bx, by, '-b', linewidth=5)

        area = features[0].filled_area  # determining the filled area
        perimeter = features[0].perimeter  # designation of the circuit
        if perimeter != 0:
            circularity = 4 * math.pi * (area / (perimeter * perimeter))  # determination of circularity
        counter += 1
        filename = str(counter) + '.png'

        if area > 10000:  # sorting out noise with insignificant area
            plt.plot(bx, by, '-r', linewidth=5)  # display the limits of the found area
            width_mri = maxc - minc  # specifying the width
            height_mri = maxr - minr  # specifying the height

            for x in features_list:
                if x[0] == filename:
                    intersection_point = round(x[1], 3)  # rewriting the point of intersection
                    break
            parameters_to_be_saved = [filename, intersection_point, area, circularity, width_mri, height_mri, x0,
                                      y0]  # creating a list of parameters to be saved
            img_data_arr.append(parameters_to_be_saved)  # adding a list to the feature table
        else:
            plt.plot(bx, by, '-y', linewidth=5)

        plt.savefig(writing_path + "/" + filename)
        plt.close()

    print("DONE - feature detection")
    return img_data_arr
