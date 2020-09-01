A1=imread("barbaraSmall.png");
A=double(A1);
[rows,columns]=size(A);
nr=3*rows-2;
nc=2*columns-1;
k=0;
B=zeros(nr,nc);
for i=1:nr
    for j=1:nc
        if mod(i,3) == 1
            if mod(j,2) == 1
                oi=fix(i/3);
                oj=fix(j/2);
                
                B(i,j)=A(oi+1,oj+1);
            else
                B(i,j)=-1;
            end
        else
            B(i,j)=-1;
        end
    end
end
der=zeros(nr,nc,3);
%Populating the derivative matrix( axis 1 is dx, 2 is dy, 3 is dxy) 
 for i=1:3:nr
     for j=1:2:nc
         x=0;y=0;
         if j==1 && B(i,j)~=-1
             der(i,j,1)=(B(i,j+2)-B(i,j))/2;
             if i==1
                 der(i,j,3)=B(i+3,j+2)/6;
             elseif i==nr
                 der(i,j,3)=B(i-3,j+2)/6;
             else
                 der(i,j,3)=(B(i+3,j+2)-B(i-3,j+2))/24;
             end
             x=1;
         elseif j==nc && B(i,j)~=-1
             der(i,j,1)=(B(i,j)-B(i,j-2))/2;
             if i==1
                 der(i,j,3)=-B(i+3,j-2)/6;
             elseif i==nr
                 der(i,j,3)=-B(i-3,j-2)/6;
             else
                 der(i,j,3)=(B(i-3,j-2)-B(i+3,j-2))/24;
             end
             
             x=1;
         end
         if i==1 && B(i,j)~=-1
             der(i,j,2)=(B(i+3,j)-B(i,j))/3;
             if j~=1 && j~=nc
                 der(i,j,3)=(B(i+3,j+2)-B(i+3,j-2))/4;
             end
             y=1;
         elseif i==nr && B(i,j)~=-1
             der(i,j,2)=(B(i,j)-B(i-3,j))/3;
             if j~=1 && j~=nc
                 der(i,j,3)=(B(i-3,j-2)-B(i-3,j+2))/4;
             end
             y=1;
         end
         if x~=1
            der(i,j,1)=(B(i,j+2)-B(i,j-2))/4;
         end
         if y~=1
             der(i,j,2)=(B(i+3,j)-B(i-3,j))/6;
         end
         if x~=1 && y~=1
             der(i,j,3)=((B(i+3,j+2)+B(i-3,j-2))-(B(i+3,j-2)+B(i-3,j+2)))/24;
         end
         
     end
 end

coeff=[1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ; 
       1 0 0 0 2 0 0 0 4 0 0 0 8 0 0 0 ;
       1 3 9 27 0 0 0 0 0 0 0 0 0 0 0 0 ;
       1 3 9 27 2 6 18 54 4 12 36 108 8 24 72 216;
       0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0;
       0 0 0 0 1 0 0 0 4 0 0 0 12 0 0 0;
       0 0 0 0 1 3 9 27 0 0 0 0 0 0 0 0;
       0 0 0 0 1 3 9 27 4 12 36 108 12 36 108 324;
       0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
       0 1 0 0 0 2 0 0 0 4 0 0 0 8 0 0;
       0 1 6 27 0 0 0 0 0 0 0 0 0 0 0 0;
       0 1 6 27 0 2 12 54 0 4 24 108 0 8 48 216;
       0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0;
       0 0 0 0 0 1 0 0 0 4 0 0 0 12 0 0;
       0 0 0 0 0 1 6 27 0 0 0 0 0 0 0 0;
       0 0 0 0 0 1 6 27 0 4 24 72 0 108 12 324]; 
for i=4:3:nr
    for j=1:2:(nc-2)
        pp=[B(i,j);B(i,j+2);B(i-3,j);B(i-3,j+2);der(i,j,1);der(i,j+2,1);der(i-3,j,1);der(i-3,j+2,1);der(i,j,2);der(i,j+2,2);der(i-3,j,2);der(i-3,j+2,2);der(i,j,3);der(i,j+2,3);der(i-3,j,3);der(i-3,j+2,3)];
        R=coeff\pp;
        %disp(R);
        for o=0:3
            for p=0:2
                
                if B(i-o,j+p)==-1
                    inp=[1;o;(o^2);(o^3);p*1;p*o;p*(o^2);p*(o^3);(p^2)*1;(p^2)*o;(p^2)*(o^2);(p^2)*(o^3);(p^3)*1;(p^3)*o;(p^3)*(o^2);(p^3)*(o^3)];
                    
                    B(i-o,j+p)=transpose(R)*inp;
                    
                end
            end
        end
    end
end
%disp(B);
%C=B(1:4,1:3);
%disp(C);
%imshow(B,[0,255]);
% h1 = subplot(1,2,1);
% imshow(A1);
% axis on;
% colorbar;
% title("Original");
% h2= subplot(1,2,2);
imshow(double(B),[0,255]);
% axis on;
% colorbar;
% title("Cubic Interpolation");
% linkaxes([h2,h1]);
