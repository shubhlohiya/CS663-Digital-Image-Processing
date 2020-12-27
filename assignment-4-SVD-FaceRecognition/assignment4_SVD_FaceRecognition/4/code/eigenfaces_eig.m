function [ x_bar, X , V] = eigenfaces_eig(data)
    x_bar = mean(data, 2);
    X = data - x_bar;
    L = X'*X;
    [W, D] = eig(L);
    V = X*W;
    V = normc(V);
    [~, ind] = sort(diag(D), 'descend');
    V = V(:, ind);
    
    