%% MyMainScript

tic;
%% Your code here
load("../data/barbara.mat");
image = imageOrig;
output_img = myBilateralFiltering(image, 1.8, 10, 7);

image = imread("../data/grass.png");
output_img = myBilateralFiltering(image, 0.77, 54, 7);

image = imread("../data/honeyCombReal.png");
output_img = myBilateralFiltering(image, 1, 37, 7);
toc;
