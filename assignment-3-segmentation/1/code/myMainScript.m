%% MyMainScript

tic;
%% Your code here

image = load('../data/boat.mat');
image = double(image.imageOrig)/255;

s1 = 0.6; % Sigma 1 
s2 = 1.3; % Sigma 2
k = 0.002;  % 

result = myHarrisCornerDetector( image, s1 , s2 , k );













toc;

% Color Map
function displaycolormap(img)
    myNumOfColors = 200;
    myColorScale = [[0:1/(myNumOfColors-1):1]' ,[0:1/(myNumOfColors-1):1]' ,[0:1/(myNumOfColors-1):1]' ];
    imagesc (single (phantom)); % phantom is a popular test image
    colormap (myColorScale);
    colormap jet;
    daspect ([1 1 1]);
    axis tight;
    colorbar

end