%% MyMainScript

%% Flower
tic;
pic = double(imread('../data/flower.jpg'));
output_img = mySpatiallyVaryingKernel(pic,1,20);
toc;

%% Bird
tic;
pic = double(imread('../data/bird.jpg'));
output_img = mySpatiallyVaryingKernel(pic,2,40);
toc;
%% Display kernels - bird
kernel_display(8);
kernel_display(16);
kernel_display(24);
kernel_display(32);
kernel_display(40);
%% Display kernels - flower
kernel_display(4);
kernel_display(8);
kernel_display(12);
kernel_display(16);
kernel_display(20);