function [ x_bar, X , V] = eigenfaces_svd(data)
    x_bar = mean(data, 2);
    X = data - x_bar;
    [V,D,~] = svd(X,'econ');
    V = normc(V);
    [~, ind] = sort(diag(D), 'descend');
    V = V(:, ind);