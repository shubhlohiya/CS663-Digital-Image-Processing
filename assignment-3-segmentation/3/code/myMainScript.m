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
%%
