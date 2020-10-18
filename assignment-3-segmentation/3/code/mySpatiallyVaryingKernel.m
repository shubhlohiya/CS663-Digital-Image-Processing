function output_img = mySpatiallyVaryingKernel(image, image_no, alpha)
    [h,w,b] = size(image);
    image = double(image);
    if image_no == 1
               
%         %doing image segmentation
%         hc = 0.2;
%         hs = 20;
%         n = 10;
%         result = myMeanShiftSegmentation(image, hc, hs, n, 1, 1);
%         %
%         %removing anomalies due to resizing of the image in mean shift
%         result = result(1:h,1:w,:);\
        
        % reading segmented image formed using above code to make it fast
        result = imread("../images/flower/segmented_image.png");        
        gray_img = rgb2gray(result);
        %creating mask for flower
        mask = gray_img > 110;
        %imshow(mat2gray(mask));
        %negating the mask
        neg_mask = ~mask;
        mask = double(mask);
        neg_mask = double(neg_mask);
        
        %separating the foreground and background part
        image = image/max(image, [], 'all');
        background = image .* neg_mask;
        %imshow(mat2gray(background));
        foreground = image .* mask;
        
        %imshow(mat2gray(background));
    end
    
    if image_no == 2
        
%         hc = 0.12;
%         hs = 30;
%         n = 15;
%         
%         pic = imread('../data/bird.jpg');
%         result = myMeanShiftSegmentation2(pic, hc, hs, n);
%         [labels,centres] = imsegkmeans(result,2);
%         clustered = label2rgb(labels,im2double(centres));

        clustered = imread("../images/bird/clustered_image.png");
        %converting the image to grayscale        
        gray_img = rgb2gray(clustered);
        %creating mask for flower
        initial_mask = gray_img > 100;
        initial_mask(1:180, 550:end) = 0;
        initial_mask(180:360,end-100:end) =0;
        initial_mask(end-150:end-50,end-315:end-275) = 0;
        initial_mask(210:450,110:285) = 0;
        initial_mask(430:500,340:450) = 0;
        initial_mask(310:350,280:382) = 0;
        initial_mask(1:25,300:420) = 0;
        mask = initial_mask;
        %negating the mask
        neg_mask = ~mask;
        mask = double(mask);
        neg_mask = double(neg_mask);
        
        %separating the foreground and background part
        image = image/max(image, [], 'all');
        background = image .* neg_mask;
        %imshow(mat2gray(background));
        foreground = image .* mask;
        end
        
        radius_mat = double(ones(size(mask))) * alpha;
        visited=zeros(size(mask));
        for radius = 1:alpha
            kernel = fspecial('disk',alpha+1-radius);            
            M = imfilter(mask, kernel); %matrix with convolution of mask and kernel
            for row = 1:h
                for col = 1:w
                    if visited(row,col)==0 && M(row,col) == 0 && mask(row,col) == 0
                        visited(row,col)=1;
                        radius_mat(row,col) = alpha + 1 - radius;
                    end
                end
            end
        end
        blurr_img = background; 
        for i = 1:10
        for radius = 1:alpha
            kernel = fspecial('disk',radius);
            M = imfilter(image, kernel);
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
       
    figure; colormap jet;
    set(gcf, 'Position', get(0, 'Screensize'));
    imagesc(output_img); title("Blurred Background Result"); daspect ([1 1 1]); axis tight; colorbar;
    
    radius_mat = radius_mat/alpha; %scaling
    
    figure; colormap jet;
    set(gcf, 'Position', get(0, 'Screensize'));
    imagesc(radius_mat); title("Radius variation of the disc kernel across the image"); 
    daspect ([1 1 1]); axis tight; colorbar;
end
        
    
    