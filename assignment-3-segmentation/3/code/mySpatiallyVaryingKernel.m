function output_img = mySpatiallyVaryingKernel(image, image_no, alpha)
    
    if image_no == 1
        [h,w,b] = size(image);
        image = double(image);
        %disp(size(image));
        %doing image segmentation
        hc = 0.2;
        hs = 20;
        n = 10;
        result = myMeanShiftSegmentation(image, hc, hs, n, 1, 1);
        
        %removing anomalies due to resizing of the image in mean shift
        result = result(1:h,1:w,:);
        %disp(size(result));
        %converting the image to grayscale
        %imshow(result);
        gray_img = rgb2gray(result);
        %creating mask for flower
        mask = gray_img > 110;
        %imshow(mat2gray(mask));
        %negating the mask
        neg_mask = ~mask;
        mask = double(mask);
        neg_mask = double(neg_mask);
        
        %separating the foreground and background part
        image = image./max(max(image));
        background = image .* neg_mask;
        %imshow(mat2gray(background));
        foreground = image .* mask;
        
        %imshow(mat2gray(background));
    end
    
    if image_no == 2
        [h,w,b] = size(image);
        image = double(image);
        %disp(size(image));
        %doing image segmentation
        hc = 0.2;
        hs = 20;
        n = 10;
        result = myMeanShiftSegmentation(image, hc, hs, n, 1, 1);
        
        %disp(size(result));
        %converting the image to grayscale
        %imshow(result);
        gray_img = rgb2gray(result);
        %creating mask for flower
        mask = gray_img > 110;
        %imshow(mat2gray(mask));
        %negating the mask
        neg_mask = ~mask;
        mask = double(mask);
        neg_mask = double(neg_mask);
        
        %separating the foreground and background part
        image = image./max(max(image));
        background = image .* neg_mask;
        %imshow(mat2gray(background));
        foreground = image .* mask;
        
        %imshow(mat2gray(background));
    end
        
        radius_mat = double(ones(size(mask))) * alpha;
        
        
        for radius = 1:alpha
            kernel = fspecial('disk',alpha+1-radius);
            %matrix with convolution of mask and kernel
            M = imfilter(mask, kernel);
            for row = 1:h
                for col = 1:w
                    if M(row,col) == 0 && mask(row,col) == 0
                        radius_mat(row,col) = alpha + 1 - radius;
                    end
                end
            end
        end
         
        for radius = 1:alpha
            kernel = fspecial('disk',radius);
            kernel = kernel;
            M = imfilter(background(:,:,:), kernel);
            for row = 1:h
                for col = 1:w
                    if mask(row,col) == 0 && radius_mat(row,col) == radius
                        blurr_img(row,col,:) = M(row,col,:);
                    end
                end
            end
               waitbar(double(radius)/double(alpha));     
            end
       
       %imshow(mat2gray(blurr_img));
       output_img = blurr_img + foreground;
       imshow(mat2gray(output_img));
end
        
    
    