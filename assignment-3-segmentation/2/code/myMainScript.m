%% MyMainScript


%% Baboon
tic;
hc = 0.07;
hs = 200;
n = 10;

pic = double(imread('../data/baboonColor.png'));
result = uint8(myMeanShiftSegmentation(pic/255, hc, hs, n)*255);
plotresult(uint8(pic), result);

toc;

% *Used Parameters*
% * Gaussian Kernel bandwidth for color features = 0.07 (For intensities scaled between 0 and 1)
% * Gaussian Kernel bandwidth for the spatial features = 200
% * Number of iterations = 10
% * Learning rate = 1 (halved after half iterations are completed for better results)
% * Nearest neighbours (using knnsearch()) for gradient calculation = 400
% (random subset of 100 from those used each iteration to speed up results)

%% Flower
tic;
hc = 0.06;
hs = 500;
n = 10;

pic = double(imread('../data/flower.jpg'));
result = uint8(myMeanShiftSegmentation(pic/255, hc, hs, n)*255);
plotresult(uint8(pic), result);
toc;


% *Used Parameters*
% * Gaussian Kernel bandwidth for color features = 0.06 (For intensities scaled between 0 and 1)
% * Gaussian Kernel bandwidth for the spatial features = 500
% * Number of iterations = 10
% * Learning rate = 1 (halved after half iterations are completed for better results)
% * Nearest neighbours (using knnsearch()) for gradient calculation = 400
% (random subset of 100 from those used each iteration to speed up results)

%% Bird
tic;
hc = 0.1;
hs = 200;
n = 15;

pic = double(imread('../data/bird.jpg'));
result = uint8(myMeanShiftSegmentation(pic/255, hc, hs, n)*255);
plotresult(uint8(pic), result);
toc;


% *Used Parameters*
% * Gaussian Kernel bandwidth for color features = 0.1 (For intensities scaled between 0 and 1)
% * Gaussian Kernel bandwidth for the spatial features = 200
% * Number of iterations = 15
% * Learning rate = 1 (halved after half iterations are completed for better results)
% * Nearest neighbours (using knnsearch()) for gradient calculation = 400
% (random subset of 100 from those used each iteration to speed up results)

%%
