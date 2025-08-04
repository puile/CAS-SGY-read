clear all
close all
fs = [42 21 10.5 5.25];
fs = fs*1e9;
dt = 1/(fs(2));
t = 0:dt:2047*dt;


% 设置输入和输出文件夹的路径
input_folder = 'G:\mayihang\弓村二区-01002_20250310_121549';
output_folder = 'G:\mayihang\弓村二区-01002_20250310_121549';
if ~exist(output_folder)
    mkdir(output_folder)
end

% 获取输入文件夹内所有的SGY文件
sgy_files = dir(fullfile(input_folder, '*.SGY'));

% 循环处理每个SGY文件
for i = 1:length(sgy_files)
    % 获取当前SGY文件的文件名
    filename = sgy_files(i).name;
    % 使用fileparts函数获取文件名和后缀
    [path, name, ext] = fileparts(filename);
    % 读取SGY文件
    
    try
        data = ReadSegy(fullfile(input_folder, filename));
        segyid = fopen(fullfile(input_folder, filename), 'r');
        fileheader = GetSegyHeader(segyid);
        fclose(segyid);
    catch exception
        % 捕捉错误并显示错误消息
        fprintf('发生错误：%s\n', filename);
        
        % 继续下一次循环
        continue;
    end
    data = data(:,1:end);
    [sample trace] = size(data);
    % 其他处理步骤...
    
    % 构造输出文件名
    if contains(name, '201650')
        if ~exist([output_folder,'/201650'])
            mkdir([output_folder,'/201650'])
        end
        output_filename_rad = fullfile([output_folder,'/201650'],  [name, '.RAD']);
        output_filename_rd3 = fullfile([output_folder,'/201650'], [name, '.RD3']);
    elseif contains(name, 'S0200')
        if ~exist([output_folder,'/S0200'])
            mkdir([output_folder,'/S0200'])
        end
        output_filename_rad = fullfile([output_folder,'/S0200'],  [name, '.RAD']);
        output_filename_rd3 = fullfile([output_folder,'/S0200'], [name, '.RD3']);
    end
    
    % 打开输出文件以进行写操作
    fid = fopen(output_filename_rad, 'w');
    
    % 写入元数据和数据到RAD文件
    % (请在这里添加之前的写入元数据和数据的代码)
    % 写入元数据

    % 定义元数据参数
    samples = sample;
    frequency = fileheader.ns*10;
    frequency_steps = 1;
    signal_position = 15;
    raw_signal_position = 15;
    distance_flag = 1;
    time_flag = 0;
    program_flag = 0;
    external_flag = 0;
    timewindow = fileheader.ns*fileheader.dt*1e-3;
    time_interval = timewindow/samples;
    distance_interval = 0.01;
    operator = '';
    customer = '';
    site = '';
    antennas = 0;
    antenna_orientation = '';
    antenna_separation = 0.0000;
    comment = '';

    stacks = 1;
    stack_exponent = 1;
    stacking_time = 0;
    last_trace = trace;
    stop_position =(trace+1)*distance_interval;
    system_calibration = 0;
    start_position = 0;

    fprintf(fid, 'SAMPLES:%d\n', samples);
    fprintf(fid, 'FREQUENCY:%f\n', frequency);
    fprintf(fid, 'FREQUENCY STEPS:%d\n', frequency_steps);
    fprintf(fid, 'SIGNAL POSITION:%d\n', signal_position);
    fprintf(fid, 'RAW SIGNAL POSITION:%d\n', raw_signal_position);
    fprintf(fid, 'DISTANCE FLAG:%d\n', distance_flag);
    fprintf(fid, 'TIME FLAG:%d\n', time_flag);
    fprintf(fid, 'PROGRAM FLAG:%d\n', program_flag);
    fprintf(fid, 'EXTERNAL FLAG:%d\n', external_flag);
    fprintf(fid, 'TIME INTERVAL:%f\n', time_interval);
    fprintf(fid, 'DISTANCE INTERVAL:%f\n', distance_interval);
    fprintf(fid, 'OPERATOR:%s\n', operator);
    fprintf(fid, 'CUSTOMER:%s\n', customer);
    fprintf(fid, 'SITE:%s\n', site);
    fprintf(fid, 'ANTENNAS:%d\n', antennas);
    fprintf(fid, 'ANTENNA ORIENTATION:%s\n', antenna_orientation);
    fprintf(fid, 'ANTENNA SEPARATION:%f\n', antenna_separation);
    fprintf(fid, 'COMMENT:%s\n', comment);
    fprintf(fid, 'TIMEWINDOW:%f\n', timewindow);
    fprintf(fid, 'STACKS:%d\n', stacks);
    fprintf(fid, 'STACK EXPONENT:%d\n', stack_exponent);
    fprintf(fid, 'STACKING TIME:%d\n', stacking_time);
    fprintf(fid, 'LAST TRACE:%d\n', last_trace);
    fprintf(fid, 'STOP POSITION:%f\n', stop_position);
    fprintf(fid, 'SYSTEM CALIBRATION:%d\n', system_calibration);
    fprintf(fid, 'START POSITION:%f\n', start_position);
    fclose(fid);
    
    fid1 = fopen(output_filename_rd3, 'w');
    
    % 写入数据到RD3文件
    fwrite(fid1, data, 'int16');
    
    fclose(fid1);
end
