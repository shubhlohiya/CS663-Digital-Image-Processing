function myPatchBasedFiltering(image, sig_i , show, gaussian)

    %adding iid noise to the image
    %calculating the standard deviation as 5% of range of image intensities
    std_dev = 0.05 * (max(max(image)) - min(min(image)));
    %iid noise from normal distribution with mean zero and std. deviation
    %as calculated above
    iid_noise = std_dev .* randn(size(image));
    %adding the noise to given image
    corrupt_image = image + iid_noise;
    
    
    % patch based filtering
    window = 25;
    patch_size = 9; 
    img = corrupt_image;
    img_size = size(img);
    
    output_img = zeros([img_size(1),img_size(2)]);
    
    
    padding = floor(window/2) + floor(patch_size/2);
    % Boundary Condition to account for edge patches and windows
    img_padded = padarray(img, [padding, padding], 'replicate');
        
        
    
    % pass through all the pixels of the padded image starting with the
    % pixels excluding outer rows and columns = half the padding size
    for i = 1+ padding:img_size(1)+ padding               
        for j = 1+ padding: img_size(2)+ padding
            
            % finding boundaries of window around the pixel. either 
            % 1)window lies completely in the padded image or 
            % 2)it may cross the padded image in which case we limit the
            % boundary pixels as below
            
            i_min = max(i - floor(window/2), 1);    
            i_max = min(i + floor(window/2), size(img_padded,1));
            j_min = max(j - floor(window/2), 1);
            j_max = min(j + floor(window/2), size(img_padded,2));
            
            
            window_center = [(i_min + i_max)/2, (j_min + j_max)/2];
            
            % Base pixel= center of window
            % in case 1) this will be different from pixel i,j but will be lie
            % on the original image
            % in case 2) this will be same as pixel i,j
            baseXmin = max(window_center(1) - floor(patch_size/2), 1);
            baseXmax = min(window_center(1) + floor(patch_size/2), size(img_padded,1));
            
            baseYmin = max(window_center(2) - floor(patch_size/2), 1);
            baseYmax = min(window_center(2) + floor(patch_size/2), size(img_padded,2));
            
            % patch centred at center of window
            basepatch = img_padded(baseXmin:baseXmax, baseYmin:baseYmax);
            basepatch = basepatch .* gaussian;

            % weight matrix for pixels in the window for calculating
            % intensity at 
            weights = zeros([i_max - i_min + 1, j_max - j_min + 1]);
            
            % pass over the window pixels to compare patches with the basePatch
            
            for px = i_min:1:i_max              
                for py = j_min:1:j_max
                    
                    % boundary of patch to be compared
                    patchXmin = max(px - floor(patch_size/2), 1);    
                    patchXmax = min(px + floor(patch_size/2), size(img_padded,1));

                    patchYmin = max(py - floor(patch_size/2), 1);    
                    patchYmax = min(py + floor(patch_size/2), size(img_padded,2));

                    patch = img_padded(patchXmin:patchXmax, patchYmin:patchYmax);
                    patch = patch .* gaussian; 

                    % Compute weight matrix for the window by gaussian on
                    % intern patch intensity-based distance
                    weights(px - i_min + 1, py - j_min + 1) = exp(-sum(sum((basepatch - patch) .^ 2))/sig_i^2);
                    
                end
            end

            % Compute actual intensity of center pixel of the window using weights
            % of patches
            output_img(i - padding,j - padding) = sum(sum(weights .* img_padded(i_min:i_max, j_min:j_max )))/sum(sum(weights));
            
           
            
            
        end
    end
   
     if show == 1
        figure();
        set(gcf, 'Position', get(0, 'Screensize'));
        subplot(1,3,1), imshow(mat2gray(image)), title('original image');
        subplot(1,3,2), imshow(mat2gray(corrupt_image)), title('corrupted image');
        subplot(1,3,3), imshow(mat2gray(output_img)), title('Patch Filtered Image');
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
    
            
            
          
       
end
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
