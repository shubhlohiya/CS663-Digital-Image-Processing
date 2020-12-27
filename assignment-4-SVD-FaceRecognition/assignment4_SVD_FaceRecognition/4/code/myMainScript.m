%% ORL
tic;
ORL_path = "../../../ORL/";
[training, test] = get_dataset_ORL(ORL_path);
toc;

tic;
% using svd for decomposition
[x_bar, X, V] = eigenfaces_svd(training);

K = [1 2 3 5 10 15 20 30 50 75 100 150 170];
rates1 = zeros(size(K));
for k=1:length(K)
    V_hat = V(:, 1:K(k));
    alpha = V_hat'*X; % coefficients of training set data
    
    X_t = test-x_bar;
    beta = V_hat'*X_t; % coefficients of the test set data
    
    matched1 = 0;
    for i=1:size(beta,2)
        sq_dist = sum((alpha-beta(:,i)).^2,1);
        [~,closest_match1] = min(sq_dist);
        if(floor((i-1)/4) == floor((closest_match1-1)/6))
            matched1 = matched1 + 1;
        end
    end
    rates1(k) = 100.0*matched1/size(test,2);
end
figure, plot(K, rates1);
xlabel('k');
ylabel('Recognition rate (%)');
title('Recognition Rates using svd - ORL dataset');

toc;

tic;
% using eig for decomposition
[x_bar, X, V] = eigenfaces_eig(training);

K = [1 2 3 5 10 15 20 30 50 75 100 150 170];
rates1 = zeros(size(K));
for k=1:length(K)
    V_hat = V(:, 1:K(k));
    alpha = V_hat'*X; % coefficients of training set data
    
    X_t = test-x_bar;
    beta = V_hat'*X_t; % coefficients of the test set data
    
    matched1 = 0;
    for i=1:size(beta,2)
        sq_dist = sum((alpha-beta(:,i)).^2,1);
        [~,closest_match1] = min(sq_dist);
        if(floor((i-1)/4) == floor((closest_match1-1)/6))
            matched1 = matched1 + 1;
        end
    end
    rates1(k) = 100.0*matched1/size(test,2);
end
figure, plot(K, rates1);
xlabel('k');
ylabel('Recognition rate (%)');
title('Recognition Rates using eig - ORL dataset');

toc;
%% Yale
tic;
Yale_path = "../../../CroppedYale/";
[training, test] = get_dataset_Yale(Yale_path);
toc;

tic;
% using svd for decomposition
[x_bar, X, V] = eigenfaces_svd(training);

K = [1 2 3 5 10 15 20 30 50 60 65 75 100 200 300 500 1000];
rates1 = zeros(size(K));
rates2 = zeros(size(K));
for k=1:length(K)
    V_hat = V(:, 1:K(k));
    alpha = V_hat'*X; % coefficients of training set data
    
    X_t = test-x_bar;
    beta = V_hat'*X_t; % coefficients of the test set data
    
    matched1 = 0;
    matched2 = 0;
    for i=1:size(beta,2)
        temp = (alpha-beta(:,i)).^2;
        sq_dist1 = sum(temp,1);
        [~,closest_match1] = min(sq_dist1);
        if(floor((i-1)/20) == floor((closest_match1-1)/40))
            matched1 = matched1 + 1;
        end
        if (k>3)
            sq_dist2 = sum(temp(4:end, :),1);
            [~,closest_match2] = min(sq_dist2);
            if(floor((i-1)/20) == floor((closest_match2-1)/40))
                matched2 = matched2 + 1;
            end
        end        
    end
    rates1(k) = 100.0*matched1/size(test,2);
    rates2(k) = 100.0*matched2/size(test,2);
end
figure, plot(K, rates1, K, rates2);
xlabel('k');
ylabel('Recognition rate (%)');
title('Recognition Rates using svd - Yale dataset');
legend({'before removing top-3 eigenfaces','after removing top-3 eigenfaces'},'Location','southeast')

toc;