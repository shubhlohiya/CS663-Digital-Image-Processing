function[] = kernel_display(alpha)
    h=fspecial('disk',alpha);
    maxi=max(h, [], 'all');
    h=h/maxi;
    
    figure;
    imshow(h);
    title("Spatial Kernel for dp = "+alpha);
    colorbar;
end