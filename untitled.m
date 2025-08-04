clc
clear all


% 指定要搜索的文件夹路径
sourceFolder = 'E:\Mayihang\radar_kotianyuan\xsj3-7\fsbh1';
% 指定要将文件复制到的目标文件夹路径
destinationFolder = 'E:\Mayihang\Rardardata23.10.7';

% 使用dir函数列出源文件夹及其子文件夹中的所有文件
fileList = dir(fullfile(sourceFolder, '**', '*.SGY'));

% 遍历文件列表，逐个复制文件
for i = 1:length(fileList)
    % 获取当前文件的完整路径
    currentFile = fullfile(fileList(i).folder, fileList(i).name);
    
    % 构建目标文件的完整路径
    destinationFile = fullfile(destinationFolder, fileList(i).name);
    
    % 如果目标文件已存在，更改文件名
    counter = 1;
    while isfile(destinationFile)
        [path, name, ext] = fileparts(destinationFile);
        newName = sprintf('%s%d%s', name, counter, ext);
        destinationFile = fullfile(path, newName);
        counter = counter + 1;
    end
    
    % 使用copyfile函数复制文件
    copyfile(currentFile, destinationFile);
    
    % 可以选择删除原文件（复制后删除）：如果需要删除原文件，请取消下一行的注释
    % delete(currentFile);
end