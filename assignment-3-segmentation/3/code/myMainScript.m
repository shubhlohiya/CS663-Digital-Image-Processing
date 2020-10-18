%% MyMainScript
%we shall be directly using the segmented images from quesion 2 of the
%assignment
tic;
%% Your code here

pic = double(imread('../data/flower.jpg'));
output_img = mySpatiallyVaryingKernel(pic,1,20);


toc;
