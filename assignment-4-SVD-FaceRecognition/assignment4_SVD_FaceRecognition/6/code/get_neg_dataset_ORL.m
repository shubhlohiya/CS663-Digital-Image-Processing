function [neg_set] = get_neg_dataset_ORL(path)
    neg_set= [];
    
    for i = 33:40
        folder = path + "s" + num2str(i) + "/";
        for j = 1:10
            file = folder + num2str(j) + ".pgm";
            img = double(imread(file))/255;
            neg_set = [neg_set, img(:)];            
        end
    end
end