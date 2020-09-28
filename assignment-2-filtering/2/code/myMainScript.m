%% MyMainScript


tic;
%1
load("../data/barbara.mat");
image = imageOrig;
output_img = myBilateralFiltering(image, 1.9, 0.1, 7, 1);

image = imread("../data/grass.png");
output_img = myBilateralFiltering(image, 0.8, 0.18, 7, 1);

image = imread("../data/honeyCombReal.png");
output_img = myBilateralFiltering(image, 0.9, 0.16, 7, 1);

%2
load("../data/barbara.mat");
image = imageOrig;
output_img = myBilateralFiltering(image, 0.9*1.8, 0.1, 7, 0);

image = imread("../data/grass.png");
output_img = myBilateralFiltering(image, 0.9*0.77, 0.18, 7, 0);

image = imread("../data/honeyCombReal.png");
output_img = myBilateralFiltering(image, 0.9*0.88, 0.162, 7, 0);

%3
load("../data/barbara.mat");
image = imageOrig;
output_img = myBilateralFiltering(image, 1.1*1.8, 0.1, 7, 0);

image = imread("../data/grass.png");
output_img = myBilateralFiltering(image, 1.1*0.77, 0.18, 7, 0);

image = imread("../data/honeyCombReal.png");
output_img = myBilateralFiltering(image, 1.1*0.88, 0.162, 7, 0);

%4
load("../data/barbara.mat");
image = imageOrig;
output_img = myBilateralFiltering(image, 1.8, 0.9*0.1, 7, 0);

image = imread("../data/grass.png");
output_img = myBilateralFiltering(image, 0.77, 0.9*0.18, 7, 0);

image = imread("../data/honeyCombReal.png");
output_img = myBilateralFiltering(image, 0.88, 0.9*0.162, 7, 0);

%5
load("../data/barbara.mat");
image = imageOrig;
output_img = myBilateralFiltering(image, 1.8, 0.1, 1.1*7, 0);

image = imread("../data/grass.png");
output_img = myBilateralFiltering(image, 0.77, 0.18, 1.1*7, 0);

image = imread("../data/honeyCombReal.png");
output_img = myBilateralFiltering(image, 0.88, 0.162, 1.1*7, 0);
toc;