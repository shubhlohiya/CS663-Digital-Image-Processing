%% Original image

tic;
img = imread('../data/barbara256.png');
figure, imagesc(img), colormap('gray'), axis image, title('Original image');
%% Ideal low pass filter
D = 40;
[result, H] = ideal_low_pass_filter(img, D);
figure, imagesc(uint8(abs(result))), title('Ideal Low Pass Filter: D = 40'), axis image,colormap('gray');
figure, imagesc(H, [min(min(H)) max(max(H))]); colormap(jet); colorbar, axis image, title('Ideal Filter with D = 40');

D = 80;
[result, H] = ideal_low_pass_filter(img, D);
figure, imagesc(uint8(abs(result))), title('Ideal Low Pass Filter: = 80'), axis image, colormap('gray');
figure, imagesc(H, [min(min(H)) max(max(H))]); colormap(jet); colorbar, axis image, title('Ideal Filter with D = 80');
%% Gaussian low pass filter
sigma = 40;
[result, H] = gaussian_low_pass_filter(img, sigma);    
figure, imagesc(uint8(abs(result))), title('Gaussian Low Pass Filter: sigma = 40'), axis image, colormap('gray')
figure, imagesc(H, [min(min(H)) max(max(H))]); colormap(jet); axis image, colorbar, title('Gaussian Filter with Sigma = 40');

sigma = 80;
[result, H] = gaussian_low_pass_filter(img, sigma);
figure, imagesc(uint8(abs(result))), title('Gaussian Low Pass Filter: sigma = 80'), axis image, colormap('gray')
figure, imagesc(H, [min(min(H)) max(max(H))]); colormap(jet); axis image, colorbar, title('Gaussian Filter with Sigma = 80');
toc;
%% Observations
%
% 1) Image blurring is seen in both the cases  
% 2) The ringing artifacts are clearly visible when ideal low-pass filter is used (especially with larger D) whereas they are negligible when gaussian low-pass filter is used
%
