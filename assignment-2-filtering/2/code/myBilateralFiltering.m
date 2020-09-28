function output_img = myBilateralFiltering(image, sig_s, sig_i, window)
%setting the std deviation of idd noise to 5% of the range of intensities
%of the image
image = double(image);
figure()
subplot(1,3,1), imshow(mat2gray(image)), title('original image');
colorbar();
range_int = max(max(image)) - min(min(image));
st_dev = 0.05 * range_int;

%iid noise matrix of the size of the image
iid_noise = st_dev.*randn(size(image));

%corrupting the given image with idd noise
corrupt_img = image + iid_noise;
subplot(1,3,2), imshow(mat2gray(corrupt_img)), title('corrputed image');
colorbar();

%the spatial weights' matrix will be same irrespective of location in the image
%creating a matrix with all possible combinations of x and y
[x,y] = meshgrid(-floor(window/2):floor(window/2), -floor(window/2):floor(window/2));
%calculating the spatial weights
sp_w_G = exp(-(x.^2 + y.^2) / (2 * sig_s^2));
%initializing output image
output_img = double(zeros(size(image)));
[rows, columns] = size(image);

for row = 1:rows
    %to account for edge pixels
    row_min = max(row - floor(window/2), 1);
    row_max = min(rows, row + floor(window/2));
    
    for col = 1:columns
        %to account for edge pixels
        col_min = max(col - floor(window/2), 1);
        col_max = min(columns, col + floor(window/2));
        
        %intensity of current pixel
        int_curr = corrupt_img(row, col);
        
        %calculating the weights' matrix for the intensities around the
        %pixel under consideration
        int_w_G = exp(-(corrupt_img(row_min:row_max, col_min:col_max) - int_curr).^2 / (2 * sig_i^2));
       
        %subset of spacial weights' matrix corresponding to size of
        %intensity weights' matrix
        SP_W_G = sp_w_G((row_min:row_max)-row+floor(window/2)+1, (col_min:col_max)-col+floor(window/2)+1);
        %calculating the net weight corresponding to given window/pixel
        net_weight = int_w_G .* SP_W_G;
        %normalizing constant
        Wp = sum(sum(net_weight));
        
        %updated intensity of the pixel
        output_img(row, col) = sum(sum(net_weight .* corrupt_img(row_min:row_max, col_min:col_max))) / Wp; 
        
    end
end
subplot(1,3,3), imshow(mat2gray(output_img)), title('filtered image');
colorbar();

    %calculating RMSD
    diff = image - output_img;
    sum_sq = sum(sum(diff.^2));
    %number of pixels in images
    num_ele = size(image, 1) * size(image, 2);
    
    rmsd = sqrt(sum_sq ./ num_ele);
    disp(rmsd)
    
    %Spatial Gaussian
    figure()
    imshow(sp_w_G)
    
    
end
        