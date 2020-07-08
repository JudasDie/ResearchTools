function [] = py2mat_f(video_path, tracker_name)
    % Details: this demo is used to change json results (python benchmark) to TRE(OPE), TRE(1)=OPE
    % video_path: python result saved path, eg: video_path = 'pyresults/siamincep23/'
    % tracker_name: suffix of saved tracker name, eg:  'SiamFC+'
    % usage: py2mat_f('pyresults/siamincep23/', 'SiamFC+')
    
    % video sequences
    % video_path = 'pyresults/siamincep23/';
    videos_dir = dir(video_path);
    videos = {videos_dir.name};
    videos = videos(3:end);

    % read txt and change
    % txt_path = 'F:\MATLABFILE\otb-toolkit\tracker_benchmark_v1.0\pyresults\siamres23\';

    for i = 1:length(videos)
       video = videos{i};
       txt_file = [video_path video];
    %    if strcmp(video, 'Skating2')
    %        continue
    %    end
       disp([num2str(i) ' now we are processing ' txt_file])
       video_name = strsplit(video, '.');
       video_name = video_name{1};

       if strcmp(video_name, 'jogging_1')
           video_name = 'jogging-1';
       elseif strcmp(video_name, 'jogging_2')
           video_name = 'jogging-2';
       elseif strcmp(video_name, 'human4_2')
           video_name = 'human4-2';
       elseif strcmp(video_name, 'skating2_2')
           video_name = 'skating2-2';
       elseif strcmp(video_name, 'skating2_1')
           video_name = 'skating2-1';
       end


       % reference struct
       refers = load(['F:\MATLABFILE\otb-toolkit\tracker_benchmark_v1.0\results\results_TRE_CVPR13\', video_name, '_ECO.mat']);

       res = load(txt_file);
       results{1}.res = res;
       results{1}.type = refers.results{1}.type;
       results{1}.len = refers.results{1}.len;
       results{1}.annoBegin = refers.results{1}.annoBegin;
       if strcmp(video_name, 'tiger1')
           results{1}.startFrame = 1;
       else
           results{1}.startFrame = refers.results{1}.startFrame;
       end
       results{1}.fps = 65.0;
       if isfield(results{1}, 'anno')
           results{1}.anno = refers.results{1}.anno;
       end

    %    % add anno
    %    try
    %        tr2_results = load(['../results/results_TRE_CVPR13/' lower(video) '_Struck' '.mat']);
    %        results{1}.anno = tr2_results.results{1}.anno;
    %    catch
    %        disp([])
    %    end

       % pop shiftType
       % results{1} = rmfield(results{1}, 'shiftType');

       saldir = 'results/results_TRE_CVPR13/';
%        tracker_name = 'SiamFC+';

       savePath = [saldir video_name '_' tracker_name '.mat'];
       save(savePath,'results');  
    end
end