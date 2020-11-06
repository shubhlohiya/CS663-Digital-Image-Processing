function [training, test] = get_dataset_ORL(path)
    training = [];
    test = [];
    
    for i = 1:32
        folder = path + "s" + num2str(i) + "/";
        for j = 1:10
            file = folder + num2str(j) + ".pgm";
            img = double(imread(file))/255;
            if j<=6
                training = [training, img(:)];
            else
                test = [test, img(:)];
            end
        end
    end
end
        
    