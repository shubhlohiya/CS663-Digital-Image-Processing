%% MyMainScript

tic;
%% Gaussian Mask used for isotropic patches

% define the gaussian mask to make patches isotropic
    sigma = 1.6;    
    patch_size = 9; 
    [x,y] = meshgrid(-floor(patch_size/2):floor(patch_size/2),-floor(patch_size/2):floor(patch_size/2));
    gaussian = exp(-(x.^2 + y.^2)/(2*sigma^2));
% Barbara; Optimal sigma found= 0.15
 load("../data/barbara.mat");
 image = imageOrig;
     image = double(image);
%     %noramlizing the image pixels as we are using color bar from 0 to 1
     image= image / max(max(image));
 
 smoothing_filter = fspecial('gaussian', 5, 2/3); 
 image= imfilter(image, smoothing_filter); % Apply gaussian blur with 0.66 pixel width

 small_img = image(1:2:size(image,1), 1:2:size(image, 2));  % Shrink Image
 
 myPatchBasedFiltering(small_img, 0.15, 1, gaussian);
 myPatchBasedFiltering(small_img, 0.9*0.15, 0 , gaussian);
 myPatchBasedFiltering(small_img, 1.1*0.15, 0, gaussian);


%% Grass Optimal sigma found =0.15
grassimage = imread("../data/grass.png");
  %converting the image in double 
     grassimage = double(grassimage);
  %noramlizing the image pixels as we are using color bar from 0 to 1
     grassimage= grassimage / max(max(grassimage));
myPatchBasedFiltering(grassimage, 0.15, 1, gaussian); % Optimal Sigma i.e. sigma*=0.15

myPatchBasedFiltering(grassimage, 0.9*0.15, 0, gaussian);
myPatchBasedFiltering(grassimage, 1.1*0.15, 0, gaussian);
 
%% HoneyComb Optimal sigma found =0.162
honeyimage = imread("../data/honeyCombReal.png");
%  %converting the image in double 
     honeyimage = double(honeyimage);
%     %noramlizing the image pixels as we are using color bar from 0 to 1
     honeyimage= honeyimage / max(max(honeyimage));

myPatchBasedFiltering(honeyimage, 0.162, 1, gaussian); % Optimal Sigma i.e. sigma*=0.18
myPatchBasedFiltering(honeyimage, 0.9*0.162, 0, gaussian);
myPatchBasedFiltering(honeyimage, 1.1*0.162, 0, gaussian);

%% Gaussian mask
figure();
imshow(mat2gray(gaussian));

 
toc;

