function [result, H] = gaussian_low_pass_filter(img, sigma)
% function to implement gaussian low-pass filter

    [h, w] = size(img);
%     pad_img=cat(2,zeros([dim,dim/2]),img, zeros([dim,dim/2]));
%     pad_img=cat(1,zeros([dim/2,2*dim]),pad_img,zeros([dim/2,2*dim]));
    pad_img = img;
    imgfft = fft2(pad_img);
    imgfft_shift = fftshift(imgfft);
  
    H = zeros(size(imgfft));
    for u=1:h
       for v=1:w
           if((u-128)^2 + (v-128)^2 <= sigma^2)
               H(u,v) = exp(-((u-128)^2 + (v-128)^2)/(2*sigma^2));
           end
       end
    end
    result = ifft2(ifftshift(imgfft_shift.*H));    
    H = log(abs(H)+1);
end
%  Note: Padding gave worse results so I removed it. Padding is more important with convolution in spatial domain 
% Code with padding below
% function [result, H] = gaussian_low_pass_filter(img, sigma)
% % function to implement gaussian low-pass filter
% 
%     [h, w] = size(img);
%     dim = length(img);
%     pad_img=cat(2,zeros([dim,dim/2]),img, zeros([dim,dim/2]));
%     pad_img=cat(1,zeros([dim/2,2*dim]),pad_img,zeros([dim/2,2*dim]));
% %     pad_img = img;
%     imgfft = fft2(pad_img);
%     imgfft_shift = fftshift(imgfft);
%   
%     H = zeros(size(imgfft));
%     for u=1:2*h
%        for v=1:2*w
%            if((u-256)^2 + (v-256)^2 <= sigma^2)
%                H(u,v) = exp(-((u-256)^2 + (v-256)^2)/(2*sigma^2));
%            end
%        end
%     end
%     result = ifft2(ifftshift(imgfft_shift.*H));    
%     H = log(abs(H)+1);
% end