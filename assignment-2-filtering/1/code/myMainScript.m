%% MyMainScript

tic;
%% Your code here

% input image: superMoonCrop.mat
figure(1)
load("../data/superMoonCrop.mat");
myUnsharpMasking(imageOrig, 1, 50);

% input image: superMoonCrop.mat
figure(2)
load("../data/lionCrop.mat");
myUnsharpMasking(imageOrig, 1, 20);

%%
toc;
