function [] = plotresult(img1, img2, img3)
    n = 256;
    colorscale =  [0:1/(n-1):1]';    
    fig = figure; colormap([colorscale,colorscale,colorscale]); colormap jet;
    set(gcf, 'Position', get(0, 'Screensize'));
    subplot(1,3,1), imagesc(img1), title('Original Image'), colorbar, daspect([1 1 1]), axis tight;
    subplot(1,3,2), imagesc(img2), title('Segmented Result'), colorbar, daspect([1 1 1]), axis tight;
    subplot(1,3,3), imagesc(img3), title('Clustered Result'), colorbar, daspect([1 1 1]), axis tight;
end