%% MyMainScript

tic;
%% input image 1: superMoonCrop.mat
figure(1)
load("../data/superMoonCrop.mat");
myUnsharpMasking(imageOrig, 1, 50);

% tuned hyperparameters: 
% std. dev of gaussian filter for smoothing: 1
% scaling factor of unsharp mask: 50

%% input image 2: superMoonCrop.mat
figure(2)
load("../data/lionCrop.mat");
myUnsharpMasking(imageOrig, 1, 10);

% tuned hyperparameters: 
% std. dev of gaussian filter for smoothing: 1
% scaling factor of unsharp mask: 10

%%
toc;
