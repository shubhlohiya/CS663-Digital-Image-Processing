%% Get SVD
A = randn(6,4);
[U, S, V] = mySVD(A);

%% Proving that $USV^{T} = A$

disp(U*S*transpose(V));
disp(A);

% thus USV' and A can clearly been seen to be equal