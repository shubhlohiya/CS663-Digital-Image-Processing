function output_img = myBilateralFiltering(image, sig_s, sig_i, window, show)

    %converting the image in double 
    image = double(image);
    %noramlizing the image pixels as we are using color bar from 0 to 1
    image= image / max(max(image));
    if show == 1
        figure();
        set(gcf, 'Position', get(0, 'Screensize'));
        subplot(1,3,1), imshow(mat2gray(image)), title('original image');
%         colorbar();
    end
    %adding iid noise to the image
    %calculating the standard deviation as 5% of range of image intensities
    std_dev = 0.05 * (max(max(image)) - min(min(image)));
    %iid noise from normal distribution with mean zero and std. deviation
    %as calculated above
    iid_noise = std_dev .* randn(size(image));
    %adding the noise to given image
    corrupt_image = image + iid_noise;
    if show == 1
        subplot(1,3,2), imshow(mat2gray(corrupt_image)), title('corrupted image');
%         colorbar();
    end
    %initializing the output image with all zeros
    output_img = double(zeros(size(image)));
    
    %the weights from the spacial gaussian matrix will be same irrespective
    %of the position of the pixel under consideration
    %[x,y] will be all possible combinations of indices in the given window
    %size, floor acts like Greatest integer function
    [x,y] = meshgrid(-floor(window/2): floor(window/2), -floor(window/2): floor(window/2));
    %calculating the spacial weights' matrix fir the given window size and standard deviation 
    W_spc = exp(-(x.^2 + y.^2)/(2 * sig_s^2));
    
    [rows, columns] = size(image);
   
    for row = 1:rows
        %to account for edge pixels
        row_min = max(row - floor(window/2), 1);    
        row_max = min(row + floor(window/2), rows);
        
        for col = 1:columns
            %to account for edge pixels
            col_min = max(col - floor(window/2), 1);
            col_max = min(col + floor(window/2), columns);
            
            %calculating the intensity weights' matrix corresponding the
            %pixel under consideration and, window size and given standard
            %deviation
            W_int = exp(-(corrupt_image(row_min:row_max, col_min:col_max) - corrupt_image(row,col)).^2 / (2 * sig_i^2));
            
            %taking the subset of the spacial weights matrix same size as
            %of intensity weight matrix
            W_spc_sub = W_spc((row_min:row_max)-row+floor(window/2)+1, (col_min:col_max)-col+floor(window/2)+1);
            
            %calculating the overall weights .i.e. product of the intensity and
            %spacial weights
            W_overall = W_spc_sub .* W_int;
            
            %the normalizing constant
            Wp = sum(sum(W_overall));
            
            %updating the intensity in the final image
            output_img(row,col) = sum(sum(W_overall .* corrupt_image(row_min:row_max, col_min:col_max))) / Wp;
            
        end
    end
    if show == 1
        subplot(1,3,3), imshow(mat2gray(output_img)), title('output image');
%         colorbar();
    end
    %Root Mean Squared Distance(RMSD)
    %number of elements/pixels in the image
    num_pix = size(image, 1) * size(image, 2);
    %sum of squares of differences between the pixel intensities of the
    %given two images
    SoS = sum(sum((image - output_img) .^ 2));
    %value to be returned
    rmsd = sqrt(SoS/num_pix);
    disp(rmsd);
    
    %showing the spatial gaussian
    if show == 1
        figure();
        imshow(mat2gray(W_spc));
    end
end