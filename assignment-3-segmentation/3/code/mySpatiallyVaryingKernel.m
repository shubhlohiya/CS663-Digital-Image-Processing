function output_img = mySpatiallyVaryingKernel(image, image_no, alpha)
    [h,w,b] = size(image);
    %output_img = double(zeros(size(image)));
    %imshow(mat2gray(image));
    image = image ./ max(max(image));
    if image_no == 1
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
        imshow(mat2gray(mask));
        %negating the mask
        neg_mask = ~mask;
        mask = double(mask);
        neg_mask = double(neg_mask);
        
        %separating the foreground and background part
        background = image .* neg_mask;
        foreground = image .* mask;
        
        %imshow(mat2gray(background));
        
        %creating the kernel
        
        %[x,y] will be all possible combinations of indices in the given window
        %size, floor acts like Greatest integer function
        [x,y] = meshgrid(-floor(alpha): floor(alpha), -floor(alpha): floor(alpha));
        %calculating the spacial weights' matrix for the given window size 
        W_spc = exp(-(x.^2 + y.^2)/(2));  
        imshow(mat2gray(W_spc));
        
        for row = 1:h
            %to account for edge pixels
            row_min = max(row - alpha, 1);    
            row_max = min(row + alpha, h);
        
            for col = 1:w
                %to account for edge pixels
                col_min = max(col - alpha, 1);
                col_max = min(col + alpha, w);
                    
                %filter considering the corner cases
                W_spc_sub = W_spc((row_min:row_max)-row+alpha+1, (col_min:col_max)-col+alpha+1);
                
                radius = alpha;
                
                %finding the distance of foreground from the given pixel
                for i = max(row_min, row - alpha): min(row_max, row + alpha)
                    for j = max(col_min, col - alpha): min(col_max, col + alpha)
                        if mask(i,j) == 1
                            radius = min(radius, sqrt((row-i).^2 + (col-j).^2));
                        end
                    end
                end
                
                %making the elements outside the radius zero
                for i = 1:size(W_spc_sub,1)
                    for j = 1:size(W_spc_sub,2)
                        if (col-j)^2 +(row-i)^2 > radius^2
                            W_spc_sub(i,j) = 0;
                        end
                    end
                end
                
                
                %normalization constant
                K = sum(sum(W_spc_sub));
                %applying the blur filter on the backgroung image
                %disp(size(W_spc_sub));
                %disp(size(background((row_min:row_max)-row+alpha+1, (col_min:col_max)-col+alpha+1)));
                for i = 1:3
                    output_img(row,col,i) = sum(sum(W_spc_sub .* background((row_min:row_max)-row+alpha+1, (col_min:col_max)-col+alpha+1,i)))/K;
                    %imshow(mat2gray(output_img));
                
                end
        
        end
        
        end
        imshow(output_img);
        %removing the blurred foreground part
        %output_img = output_img .* neg_mask;
        %imshow(mat2gray(output_img));
        %adding the original foreground part
        %output_img = output_img + foreground;
        %imshow(mat2gray(output_img));
    end
end
    
    