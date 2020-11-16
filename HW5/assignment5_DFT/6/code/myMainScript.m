


tic;
%% Your code here
k1 = [0 1 0; 1 -4 1 ; 0 1 0];
filter_1_N = zeros(N);
filter_1_N( (N-1)/2:(N+3)/2 , (N-1)/2:(N+3)/2 ) = k1;
fim_1 = fftshift(fft2(filter_1_N));
log_mag_filter_1 = log(1+abs(fim_1));

subplot(1,2,2);
daspect([1 1 1]); axis tight;
imshow(log_mag_filter_1, [min(log_mag_filter_1(:)) max(log_mag_filter_1(:))]);  
colormap('jet'); colorbar;
h = gca; h.Visible = 'on';
title('Log Magnitude of the Fourier Transform of Kernel 1')

figure;
s = surf(log_mag_filter_1 ,'FaceAlpha', 0.5); s.EdgeColor = 'none';
colormap('jet'); colorbar;
h = gca; h.Visible = 'on';
title('Surf Image of the Log Magnitude of the Fourier Transform of Kernel 1');



k2 = [-1 -1 -1; -1 8 -1 ; -1 -1 -1];
filter_2_N = zeros(N);
filter_2_N( (N-1)/2:(N+3)/2 , (N-1)/2:(N+3)/2 ) = k2;
fim_2 = fftshift(fft2(filter_2_N));
log_mag_filter_2 = log(1+abs(fim_2));

subplot(1,2,2);
daspect([1 1 1]); axis tight;
imshow(log_mag_filter_2, [min(log_mag_filter_2(:)) max(log_mag_filter_2(:))]);  
colormap('jet'); colorbar;
h = gca; h.Visible = 'on';
title('Log Magnitude of the Fourier Transform of Kernel 2')

figure;
s = surf(log_mag_filter_2 ,'FaceAlpha', 0.5); s.EdgeColor = 'none';
colormap('jet'); colorbar;
h = gca; h.Visible = 'on';
title('Surf Image of the Log Magnitude of the Fourier Transform of Kernel 2');


%% MyMainScript


toc;
