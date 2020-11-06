function mySVD(A)

    AAT = A * transpose(A);
    ATA = transpose(A) * A;
    
    %calculating the eigenvectors and eigenvalues
    [U, U_eig] = eig(AAT);
    [V, V_eig] = eig(ATA);
    
    %sorting the eigenvalues and eigenvectord according to the convention
    %ph is just a place holder
    [ph, U_sort] = sort(diag(U_eig), 'descend');
    [ph, V_sort] = sort(diag(V_eig), 'descend');
    
    U = U(:, U_sort);
    V = V(:, V_sort);
    
    %S = U^T*A*V as A = U*S*V^T
    S = transpose(U) * A * V;
    
    %as S is always non negative, switching signs of eigen vectors
    %corrrecponding to negative values in S = transpose(U) * A * V 
    for i = 1:min(size(S,1), size(S, 2))
        if S(i,i) < 0
            U(:,i) = -U(:,i);
        end
    end
    
    %S is always non negative
    S = abs(S);  
    %prindting the values for verification
    disp(A);
    disp(U*S*transpose(V))
    %disp(A-U*S*transpose(V));
    

end

