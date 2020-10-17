function [] = plotresult(img1, img2)
    n = 256;
    colorscale =  [0:1/(n-1):1]';    
    fig = figure; colormap([colorscale,colorscale,colorscale]); colormap jet;
    set(gcf, 'Position', get(0, 'Screensize'));
    subplot(1,2,1), imagesc(img1), title('Original Image'), colorbar, daspect([1 1 1]), axis tight;
    subplot(1,2,2), imagesc(img2), title('Segmented Result'), colorbar, daspect([1 1 1]), axis tight;
    impixelinfo();
end