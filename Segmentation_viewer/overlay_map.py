#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 00:25:14 2017

@author: wjcheon-ml
"""
#%%
class viewer_for_segmentation:
    def __init__(self):
        from PIL import Image
        import matplotlib.pyplot as plt
        
    def draw(self, dicom_,roi_true_,roi_predicted_, alpha_roi_predicted_=0.5, alpha_roi_sum_=0.7, accuracy_=0.0):
        
        result_blending_roi = Image.blend(roi_true_, roi_predicted, alpha=alpha_roi_predicted_)
        result = Image.blend(dicom_imgs, result_blending_roi, alpha=alpha_roi_sum_)
        plt.imshow(result)
        if roi_predicted_ is not None:
            plt.title('Liver segmentation')
        if alpha_roi_sum_ is not None:
            plt.title('Liver segmentation \n (True:alpha={}, Predicted:alpha={})'.format(alpha_roi_predicted_,alpha_roi_sum_))
        if accuracy_ is not None:
            plt.title('Liver segmentation \n (True:alpha={}, Predicted:alpha={}) \n Accuracy (dice metric): {}'.format(alpha_roi_predicted_,alpha_roi_sum_, accuracy_))
        return result

#%%
from PIL import Image
import matplotlib.pyplot as plt

#image load
dicom_imgs = Image.open('dicom_image.jpg')
roi_true = Image.open('true_Y.jpg')
roi_predicted = Image.open('predicted_Y.jpg')
# Image format conver form L to RGB
roi_predicted = roi_predicted.convert('RGB')

# Call class 
segview = viewer_for_segmentation()
#segimg = segview.draw(dicom_imgs,roi_true,roi_predicted)
#segimg = segview.draw(dicom_imgs,roi_true,roi_predicted,0.3,0.6)
segimg = segview.draw(dicom_imgs,roi_true,roi_predicted,0.3,0.6,0.916946)

#plt.imshow(segimg)
#%%
