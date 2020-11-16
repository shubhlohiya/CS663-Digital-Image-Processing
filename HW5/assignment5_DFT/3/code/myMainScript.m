tic;
%% Original Image
img = load("../data/image_low_frequency_noise.mat").Z;
figure, imagesc(img), colormap('gray'), daspect([1 1 1]), title('Original image'), axis tight;

%% Zero padding

dim = length(img);
pad_img=cat(2,zeros([dim,dim/2]),img, zeros([dim,dim/2]));
pad_img=cat(1,zeros([dim/2,2*dim]),pad_img,zeros([dim/2,2*dim]));
figure, imagesc(pad_img), colormap('gray'), daspect([1 1 1]), title('Original image (padded)'), axis tight;

%% DFT of image
F_img = fftshift(fft2(pad_img));
figure, daspect([1 1 1]), imagesc(log(abs(F_img)+1)), axis tight, colormap('jet');
title('Log Discrete Fourier Transform of the image');
%% Make notch filter
% Notch positions (from impixelinfo)
x1=[234 279];
y1=[244 269];
k = 7; % notch size
F_prime = F_img(:, :);
for i=1:length(x1)
    x = x1(i); y = y1(i);
    F_prime(x-k:x+k, y-k:y+k) = 0;
end
figure, daspect([1 1 1]), imagesc(log(abs(F_prime)+1)), axis tight, colormap('jet');
title('Log Discrete Fourier Transform of the image after applying notch filter');
%% Restored Image
restored = abs(ifft2(ifftshift(F_prime)));
figure, imagesc(restored(129:384,129:384)), colormap('gray'), daspect([1 1 1]), title('Restored image'), axis tight;
toc;