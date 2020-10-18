function output_img = mySpatiallyVaryingKernel(image, segmented_img, image_no, alpha)
        figure();
        if image_no == 1
            [h,w,b] = size(image);
            image = double(image);
            %disp(size(image));
            subplot(1,4,1), imshow(mat2gray(image)), title('original image');
            result = segmented_img;
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
            subplot(1,4,2), imshow(mat2gray(mask)), title('mask');
            neg_mask = double(neg_mask);
        
            %separating the foreground and background part
            image = image./max(max(image));
            background = image .* neg_mask;
            subplot(1,4,3), imshow(mat2gray(background)), title('background image');
            %imshow(mat2gray(background));
            foreground = image .* mask;
            subplot(1,4,4), imshow(mat2gray(foreground)), title('background image');
        end
        
        if image_no == 2
            [h,w,b] = size(image);
            image = double(image);
            %disp(size(image));
            subplot(1,4,1), imshow(mat2gray(image)), title('original image');
            
            %removing anomalies due to resizing of the image in mean shift
            result = segmented_img;
            %disp(size(result));
            %converting the image to grayscale
            %imshow(result);
            gray_img = rgb2gray(result);
            %creating mask for flower
            mask = gray_img > 100;
            mask(1:180, 550:end) = 0;
            mask(180:360,end-100:end) =0;
            mask(end-150:end-50,end-315:end-275) = 0;
            mask(210:450,110:285) = 0;
            mask(430:500,340:450) = 0;
            mask(310:350,280:382) = 0;
            mask(1:25,300:420) = 0;
            %negating the mask
            neg_mask = ~mask;
            mask = double(mask);
            subplot(1,4,2), imshow(mat2gray(mask)), title('mask');
            neg_mask = double(neg_mask);
        
            %separating the foreground and background part
            image = image./max(max(image));
            background = image .* neg_mask;
            subplot(1,4,3), imshow(mat2gray(background)), title('background image');
            %imshow(mat2gray(background));
            foreground = image .* mask;
            subplot(1,4,4), imshow(mat2gray(foreground)), title('foreground image');
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
        blurr_img = background; 
        for i = 1:10
        for radius = 1:alpha
            kernel = fspecial('disk',radius);
            kernel = kernel;
            M = imfilter(blurr_img(:,:,:), kernel);
            for row = 1:h
                for col = 1:w
                    if mask(row,col) == 0 && radius_mat(row,col) == radius
                        blurr_img(row,col,:) = M(row,col,:);
                    end
                end
            end
        end
           waitbar(double(i)/double(5));     
        end
       
       %imshow(mat2gray(blurr_img));
       output_img = blurr_img + foreground;
       imshow(mat2gray(output_img));
end
        
    
    