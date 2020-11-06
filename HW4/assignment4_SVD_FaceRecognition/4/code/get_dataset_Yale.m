function [training, test] = get_dataset_Yale(path)
    training = [];
    test = [];
    
    allFolders = {dir(path).name};
    
    for i = 3:length(allFolders)
        folder = path + allFolders{i} + "/";
        allFiles = {dir(folder).name};
        for j = 3:62
            file = folder + allFiles{j};
            img = double(imread(file))/255;
            if j<=42
                training = [training, img(:)];
            else
                test = [test, img(:)];
            end
        end
    end
end