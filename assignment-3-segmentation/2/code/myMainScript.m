%% MyMainScript


%% Baboon
tic;
hc = 0.06;
hs = 25;
n = 15;

pic = imread('../data/baboonColor.png');
result = myMeanShiftSegmentation(pic, hc, hs, n);
[labels,centres] = imsegkmeans(result,20);
clustered = label2rgb(labels,im2double(centres));
plotresult(pic, result, clustered);
toc;

% *Used Parameters*
% * Gaussian Kernel bandwidth for color features = 0.06 (For intensities scaled between 0 and 1)
% * Gaussian Kernel bandwidth for the spatial features = 25
% * Number of iterations = 15
% * Learning rate = 1 (halved after half iterations are completed for better results)
% * Nearest neighbours (using knnsearch()) for gradient calculation = 400
% (random subset of 100 from those used each iteration to speed up results)
% * Number of colors in clustered result = 20

%% Flower
tic;
hc = 0.2;
hs = 20;
n = 15;

pic = imread('../data/flower.jpg');
result = myMeanShiftSegmentation(pic, hc, hs, n);
[labels,centres] = imsegkmeans(result,10);
clustered = label2rgb(labels,im2double(centres));
plotresult(pic, result, clustered);
toc;


% *Used Parameters*
% * Gaussian Kernel bandwidth for color features = 0.08 (For intensities scaled between 0 and 1)
% * Gaussian Kernel bandwidth for the spatial features = 25
% * Number of iterations = 15
% * Learning rate = 1 (halved after half iterations are completed for better results)
% * Nearest neighbours (using knnsearch()) for gradient calculation = 400
% (random subset of 100 from those used each iteration to speed up results)
% * Number of colors in clustered result = 10

%% Bird
tic;
hc = 0.12;
hs = 30;
n = 15;

pic = imread('../data/bird.jpg');
result = myMeanShiftSegmentation(pic, hc, hs, n);
[labels,centres] = imsegkmeans(result,10);
clustered = label2rgb(labels,im2double(centres));
plotresult(pic, result, clustered);
toc;


% *Used Parameters*
% * Gaussian Kernel bandwidth for color features = 0.12 (For intensities scaled between 0 and 1)
% * Gaussian Kernel bandwidth for the spatial features = 30
% * Number of iterations = 15
% * Learning rate = 1 (halved after half iterations are completed for better results)
% * Nearest neighbours (using knnsearch()) for gradient calculation = 400
% (random subset of 100 from those used each iteration to speed up results)
% * Number of colors in clustered result = 10

%%
