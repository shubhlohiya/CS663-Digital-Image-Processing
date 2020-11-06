%% Strategy for people not in training set
% 
%  For people not in the training set, we expect the minimum of the errors of their image coefficients with respect to the coefficients of the training set
%  images to be on the higher side as they are not highly similar to any of the training set images. Wheareas, this minimum error across the training
%  set images will be lower for people who had their images in the training set. 
%  We calculate this error using squared euclidean distance between the coefficient vectors and classify a test image as negative if it's error is 
%  more than a threshold value. We do a grid search over the hyperparameters "k" and "threshold" and pick the one which gives the best (max) F-1 Score. 
%  Our choice of the F-1 score metric was due to our aim to balance the tradeoff between precision and recall. 
%  We used the training set of 32*6 images, and treated the (32*4 + 8*10) remaining images as a validation set (which was used to tune the value of threshold and k)
%  


%% Tuning

tic;
ORL_path = "../../../ORL/";
[training, test] = get_dataset_ORL(ORL_path);
negatives = get_neg_dataset_ORL(ORL_path);

% trainging
[x_bar, X, V] = eigenfaces_eig(training);


best_k = 20;
best_threshold = 30;
best_fscore = -inf;
for k=20:30
    V_hat = V(:, 1:k);
    alpha = V_hat'*X; % coefficients of training set data

    X_t = test-x_bar;
    beta = V_hat'*X_t; % coefficients of the test set data

    X_neg = negatives-x_bar;
    gamma = V_hat'*X_neg;    
%     y = [];
    for threshold = 30:2:70
        fn=0;
        for i=1:size(test, 2)
            sq_dist = sum((alpha-beta(:, i)).^2,1);
            if (min(sq_dist)>threshold)
                fn = fn+1;
            end
        end
        tp = size(test, 2)-fn;

        fp=0;
        for i=1:size(negatives, 2)
            sq_dist = sum((alpha-gamma(:, i)).^2,1);
            if (min(sq_dist)<threshold)
                fp = fp+1;
            end
        end
        p = tp/(tp+fp);
        r = tp/(tp+fn);
        fscore = 2*p*r/(p+r);
        if (fscore > best_fscore)
            best_k = k;
            best_threshold = threshold;
            best_fscore = fscore;            
        end
%         y = [y fscore];
    end
%     figure, plot(30:2:70, y)
end
toc;

%% Plot of F1-score for k=23 (best)
k = 23;
V_hat = V(:, 1:k);
alpha = V_hat'*X; % coefficients of training set data
X_t = test-x_bar;
beta = V_hat'*X_t; % coefficients of the test set data
X_neg = negatives-x_bar;
gamma = V_hat'*X_neg;
y = [];
for threshold = 30:2:70
    fn=0;
    for i=1:size(test, 2)
        sq_dist = sum((alpha-beta(:, i)).^2,1);
        if (min(sq_dist)>threshold)
            fn = fn+1;
        end
    end
    tp = size(test, 2)-fn;
    fp=0;
    for i=1:size(negatives, 2)
        sq_dist = sum((alpha-gamma(:, i)).^2,1);
        if (min(sq_dist)<threshold)
            fp = fp+1;
        end
    end
    p = tp/(tp+fp);
    r = tp/(tp+fn);
    fscore = 2*p*r/(p+r);
    y = [y fscore];
end
figure, plot(30:2:70, y);
xlabel("threshold");
ylabel("F1-score");
title("F1-score vs threshold for k=23");
%% Final hyperparameters

k = best_k;
threshold = best_threshold;

V_hat = V(:, 1:k);
alpha = V_hat'*X; % coefficients of training set data

X_t = test-x_bar;
beta = V_hat'*X_t; % coefficients of the test set data

X_neg = negatives-x_bar;
gamma = V_hat'*X_neg;    

fn=0;
for i=1:size(test, 2)
    sq_dist = sum((alpha-beta(:, i)).^2,1);
    if (min(sq_dist)>threshold)
        fn = fn+1;
    end
end

fp=0;
for i=1:size(negatives, 2)
    sq_dist = sum((alpha-gamma(:, i)).^2,1);
    if (min(sq_dist)<threshold)
        fp = fp+1;
    end
end

fprintf('Number of false positives is %d\n', fp);
fprintf('Number of false negatives is %d\n', fn);