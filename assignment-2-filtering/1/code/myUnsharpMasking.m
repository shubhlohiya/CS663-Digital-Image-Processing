function myUnsharpMasking(image, sigma, s)

% Fsize is smoothing filter size
% sigma is the std deviation of smoothing filter
% s is the scaling factor

smoothing_filter = fspecial('gaussian', 3, sigma);
unsharp_mask = image - imfilter(image, smoothing_filter);
sharp_image = image + s*unsharp_mask;

subplot(1,2,1), imshow(image)
subplot(1,2,2), imshow(sharp_image)
% colorbar()