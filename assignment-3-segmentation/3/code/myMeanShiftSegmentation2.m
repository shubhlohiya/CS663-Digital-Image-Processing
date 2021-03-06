function [segmented_img] = myMeanShiftSegmentation(img, hc, hs, n)
    % img - original image
    % hc - bandwidth parameter for color space
    % hs - spatial bandwidth parameter
     
    img = double(imresize(imgaussfilt(img,1), 0.5))/255; % smooth, resize and scale to 0-1
    
    [h,w,d] = size(img);	
	[x,y] = meshgrid(1:w,1:h);
    
    full_dim_img = img; % full_dim_img is the representation img in a color-spatial-hyperspace
    full_dim_img(:,:, d+1) = x;
    full_dim_img(:,:, d+2) = y;
    full_dim_img = double(reshape(full_dim_img, [h*w, d+2]));
    
    step_size = 1;
    k = 400; % number of neighbours
     
    for i=1:n
        neighbours = knnsearch(full_dim_img, full_dim_img, 'K', k);
        for j=1:h*w
            grad = get_grad(full_dim_img(j,:),full_dim_img(neighbours(j,randperm(400,100)),:), hc, hs);
            full_dim_img(j,:) = full_dim_img(j,:) + step_size*grad;
        end
        
%         if i%2==0
%             progress_pic = uint8(reshape(full_dim_img(:, 1:d), h, w, d)*255);
%             imshow(progress_pic);
%         end
        
        if i==floor(n/2)
            step_size = step_size/2;
        end
        waitbar(double(i)/double(n));
    end
    segmented_img = uint8(imresize(reshape(full_dim_img(:, 1:d), h, w, d), 2)*255);    
end

function grad = get_grad(pixel, neighbours, hc, hs)
    spatial_dist_sq = sum((neighbours(:, end-1:end) - pixel(end-1:end)).^2, 2);
    sweights = exp(-spatial_dist_sq/(2*hs^2));
    
    color_dist_sq = sum((neighbours(:, 1:end-2) - pixel(1:end-2)).^2, 2);
    cweights = exp(-color_dist_sq/(2*hc^2));
    
    weights = sweights.*cweights;    
    grad = sum(neighbours.*repmat(weights, 1, length(pixel)))/sum(weights)-pixel;
end
    
    
        
        
        
        