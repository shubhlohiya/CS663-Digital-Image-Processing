%% MyMainScript
%we shall be directly using the segmented images from quesion 2 of the
%assignment
tic;
%% Your code here

pic = double(imread('../data/flower.jpg'));
pic_seg = double(imread('../data/clustered_flower.png'));
output_img = mySpatiallyVaryingKernel(pic, pic_seg,1,20);


toc;
