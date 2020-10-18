function [cornerimg] = myHarrisCornerDetector( image, s1, s2, k)
    
    imageInit=image;
     figure();
        set(gcf, 'Position', get(0, 'Screensize'));
        subplot(1,1,1), imshow(mat2gray(image)), title('Original Image');
    
    % Apply Gaussian smoothing to remove noise
    image = imgaussfilt(image,s1);
    
    % Calculate gradient along X and Y direction
    [Ix , Iy ] = gradient(image);
    
     figure();
        set(gcf, 'Position', get(0, 'Screensize'));
        subplot(1,2,1), imshow(mat2gray(Ix)), title('Derivative Along X');
        subplot(1,2,2), imshow(mat2gray(Iy)), title('Derivative Along Y');
    
    Ix2 = imgaussfilt ( Ix.^2 , s2);
    Iy2 = imgaussfilt ( Iy.^2 , s2);
    Ixy = imgaussfilt ( Ix .* Iy , s2);       
    
    eigen1 = zeros(size(image));
    eigen2 = zeros(size(image));
    cornerimg = zeros(size(image));
    
    for i = 2:(size(image,1)-1)
        for j = 2:(size(image,2)-1)
            
            A = [Ix2(i,j),Ixy(i,j); Ixy(i,j), Iy2(i,j)];
            
            cornerimg(i,j) = det(A) - (k*trace(A)^2);
            eigen = eig(A);
            eigen1(i,j) = eigen(1);
            eigen2(i,j) = eigen(2);
            
        end
    end
    
   
    
    figure();
        set(gcf, 'Position', get(0, 'Screensize'));
        subplot(1,2,1), displaycolormap(eigen1), title('Eigen Value 1');
        subplot(1,2,2), displaycolormap(eigen2), title('Eigen Value 2');
        
    
    figure();
        set(gcf, 'Position', get(0, 'Screensize'));
        subplot(1,1,1),displaycolormap(cornerimg), title('Harris Cornerness Measure');
    
    disp('Parameter values Used are -> Sigma 1 = 0.6, Sigma 2 = 1.3, k = 0.002');
    % cornerimg = (cornerimg>0.0001)*255;
    % superposed = imageInit + cornerimg;    
    
     
        
    
    
    
    















end


function displaycolormap(img)
    myNumOfColors = 200;
    myColorScale = [[0:1/(myNumOfColors-1):1]', [0:1/(myNumOfColors-1):1]', [0:1/(myNumOfColors-1):1]'];
    imagesc(img);
    colormap (myColorScale);
    colormap gray;
    daspect ([1 1 1]);
    colorbar

end