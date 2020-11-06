%% Reconstruction of face image from ORL using top-k eigenfaces
tic;
ORL_path = "../../../ORL/";
[training, test] = get_dataset_ORL(ORL_path);

% using eig for decomposition
[x_bar, X, V] = eigenfaces_eig(training);

img = double(imread(ORL_path+"s10/2.pgm"))/255;
img = img(:); %image for reconstruction

K = [2, 10, 20, 50, 75, 100, 125, 150, 175];

figure(1);
daspect([1 1 1]);
set(gcf, 'Position', get(0, 'Screensize'));
for k=1:length(K)
    V_hat = V(:,1:K(k));
    X_t = img - x_bar;
    beta = V_hat'*X_t;    
    % reconstruction
    r_img = x_bar + V_hat*beta;
    
    % plot it
    subplot(3, 3, k);
    imshow(reshape(r_img, 112, 92));
    title(['Reconstructed with k = ' num2str(K(k))]);
end
toc;
%% Display top-25 eigenfaces
tic;
figure(2);
set(gcf, 'Position', get(0, 'Screensize'));
daspect([1 1 1]);
for k=1:25
    eigenface = reshape(V(:, k), 112, 92);
    subplot(3,9,k);
    imagesc(eigenface);
    colormap('gray');
    title(['Eigenface #' num2str(k)]);
end
toc;