%% MyMainScript


%% Baboon
tic;
hc = 30;
hs = 25;
n = 20;

pic = imread('../data/baboonColor.png');
result = myMeanShiftSegmentation(pic, hc, hs, n, 0, 1.2);
plotresult(pic, result);

toc;

% *Used Parameters*
% * Gaussian Kernel bandwidth for color features = 50 (For intensities between 0 and 255)
% * Gaussian Kernel bandwidth for the spatial features = 200
% * Number of iterations = 20
% * Learning rate = 1.2 (halved after half iterations are completed for better results)
% * Nearest neighbours (using knnsearch()) for gradient calculation = 400
% (random subset of 100 from those used each iteration to speed up results)

%% Flower
tic;
hc = 0.2;
hs = 20;
n = 10;

pic = imread('../data/flower.jpg');
result = myMeanShiftSegmentation(pic, hc, hs, n, 1, 1);
plotresult(pic, result);
toc;


% *Used Parameters*
% * Gaussian Kernel bandwidth for color features = 0.05 (For intensities scaled between 0 and 1)
% * Gaussian Kernel bandwidth for the spatial features = 500
% * Number of iterations = 10
% * Learning rate = 1 (halved after half iterations are completed for better results)
% * Nearest neighbours (using knnsearch()) for gradient calculation = 400
% (random subset of 100 from those used each iteration to speed up results)

%% Bird
tic;
hc = 50;
hs = 25;
n = 20;

pic = imread('../data/bird.jpg');
result = myMeanShiftSegmentation(pic, hc, hs, n, 1, 1);
plotresult(pic, result);
toc;


% *Used Parameters*
% * Gaussian Kernel bandwidth for color features = 0.1 (For intensities scaled between 0 and 1)
% * Gaussian Kernel bandwidth for the spatial features = 200
% * Number of iterations = 15
% * Learning rate = 1 (halved after half iterations are completed for better results)
% * Nearest neighbours (using knnsearch()) for gradient calculation = 400
% (random subset of 100 from those used each iteration to speed up results)

%%
