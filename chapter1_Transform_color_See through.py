from skimage.transform import ProjectiveTransform
from skimage.io import imread
import numpy as np
import matplotlib as plt

im_src=imread('test_4.png')
height,width,dim =im_src.shape
im_dst=np.zeros((height,width,dim))

pt=ProjectiveTransform()
src=np.array([[295,174],[540,146],[400,777],[60,422]])
dst=np.array([[0,0],[height-1,0],[height-1,width-1],[0,width-1]])

x,y=np.mgrid[:height,:width]
dst_indices=np.hstack((x.reshape(-1,1),y.reshape(-1,1)))
src_indices=np.round(pt.inverse(dst_indices),0).astype(int)
valid_idx=np.where((src_indices[:,0]<height)&(src_indices[:,1]<width
                                              &(src_indices[:,0]>=0)&(src_indices[:,1]>=0)))
dst_indices_valid=dst_indices[valid_idx]
src_indices_valid=src_indices[valid_idx]

im_dst[dst_indices_valid[:,0],dst_indices_valid[:,1]]=im_src[src_indices_valid[:,0],src_indices_valid[:,1]]