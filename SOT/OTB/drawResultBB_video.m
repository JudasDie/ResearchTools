close all
clear
clc
warning off all;

addpath('./util');

pathRes = '.\results\results_TRE_CVPR13\';% The folder containing the tracking results
pathDraw = '.\tmp\videos\';% The folder that will stores the images with overlaid bounding box

if ~exist(pathDraw, 'dir')
   mkdir(pathDraw );
end

rstIdx = 1;

seqs=configSeqs;

trks=configTrackers;

if isempty(rstIdx)
    rstIdx = 1;
end

LineWidth = 1;

plotSetting;

lenTotalSeq = 0;
resultsAll=[];
trackerNames=[];

fps = 25;  % save fps 25~30

iptsetpref('ImshowBorder','tight');
% zzp: choose draw video, if all, annotated
% draw_videos = [];  


for index_seq=1:length(seqs)
    
    seq = seqs{index_seq};
    seq_name = seq.name;
    
     % debug for specific video
%     if ~strcmp(seq_name, 'skiing')
%         continue
%     end
    
%     fileName = [pathAnno seq_name '.txt'];
%     rect_anno = dlmread(fileName);

    % zzp video writer init
    videoName = [pathDraw, seq_name, '.avi'];
    if(exist('videoName','file'))
        delete videoName.avi
    end
      
    aviobj=VideoWriter(videoName);  % creat a video writer obj
    aviobj.FrameRate=fps;
    open(aviobj);    % Open file for writing video data
    
    seq_length = seq.endFrame-seq.startFrame+1; %size(rect_anno,1);
    lenTotalSeq = lenTotalSeq + seq_length;
    
    for index_algrm=1:length(trks)
        algrm = trks{index_algrm};
        name=algrm.name;
        trackerNames{index_algrm}=name;
               
        fileName = [pathRes seq_name '_' name '.mat'];
    
        load(fileName);
        
        res = results{rstIdx};
        
        if ~isfield(res,'type')&&isfield(res,'transformType')
            res.type = res.transformType;
            res.res = res.res';
        end
            
        if strcmp(res.type,'rect')
            for i = 2:res.len
                r = res.res(i,:);
               
                if (isnan(r) | r(3)<=0 | r(4)<=0)
                    res.res(i,:)=res.res(i-1,:);
                    %             results.res(i,:) = [1,1,1,1];
                end
            end
        end

        resultsAll{index_algrm} = res;

    end
        
    nz	= strcat('%0',num2str(seq.nz),'d'); %number of zeros in the name of image
    
%     pathSave = [pathDraw seq_name '_' num2str(rstIdx) '/'];
%     if ~exist(pathSave,'dir')
%         mkdir(pathSave);
%     end
    
    for i=1:seq_length
        image_no = seq.startFrame + (i-1);
        id = sprintf(nz,image_no);
        fileName = strcat(seq.path,id,'.',seq.ext);
        
        img = imread(fileName);
           
        imshow(img);
    

        text(10, 15, ['#' id], 'Color','y', 'FontWeight','bold', 'FontSize',24);
        
       %% write tracker name and line color in video
%         % base
%         % name
%         text(5, 200, 'SiamFC', 'Color','w', 'FontWeight','bold', 'FontSize',10);
%         text(110, 200, 'SiamRPN', 'Color','w', 'FontWeight','bold', 'FontSize',10);
%         text(225, 200, 'Staple', 'Color','w', 'FontWeight','bold', 'FontSize',10);
%         text(5, 220, 'SiamFC+', 'Color','w', 'FontWeight','bold', 'FontSize',10);
%         text(110, 220, 'SiamRPN+', 'Color','w', 'FontWeight','bold', 'FontSize',10);
%         text(225, 220, 'ECO-HC', 'Color','w', 'FontWeight','bold', 'FontSize',10);
%         
%         % represent color
%         rectangle('Position', [75, 200, 27, 1], 'EdgeColor', [0,0,1], 'LineWidth', LineWidth); % siamfc    [0,0,1]
%         hold on
%         rectangle('Position', [75, 220, 27, 1], 'EdgeColor', [1,0,0], 'LineWidth', LineWidth); % siamfc+    [1, 0, 0]
%         hold on
%         rectangle('Position', [185, 200, 27, 1], 'EdgeColor', [1,0,1], 'LineWidth', LineWidth); % siamrpn   [1,0,1]
%         hold on
%         rectangle('Position', [185, 220, 27, 1], 'EdgeColor', [136,0,21]/255, 'LineWidth', LineWidth); % siamrpn+  [[136,0,21]/255]  dark red
%         hold on
%         rectangle('Position', [285, 200, 27, 1], 'EdgeColor', [1,1,0], 'LineWidth', LineWidth); % staple    [1,1,0]
%         hold on
%         rectangle('Position', [285, 220, 27, 1], 'EdgeColor', [0,1,0], 'LineWidth', LineWidth); % eco-hc    [0,1,0]
%         hold on
% 
%         % jogging-2
%         % name
%         text(175, 280, 'SiamFC', 'Color','w', 'FontWeight','bold', 'FontSize',10);
%         text(275, 280, 'SiamRPN', 'Color','w', 'FontWeight','bold', 'FontSize',10);
%         text(390, 280, 'Staple', 'Color','w', 'FontWeight','bold', 'FontSize',10);
%         text(175, 300, 'SiamFC+', 'Color','w', 'FontWeight','bold', 'FontSize',10);
%         text(275, 300, 'SiamRPN+', 'Color','w', 'FontWeight','bold', 'FontSize',10);
%         text(390, 300, 'ECO-HC', 'Color','w', 'FontWeight','bold', 'FontSize',10);
%         
%         % represent color
%         rectangle('Position', [235, 280, 27, 1], 'EdgeColor', [0,0,1], 'LineWidth', LineWidth); % siamfc    [0,0,1]
%         hold on
%         rectangle('Position', [235, 300, 27, 1], 'EdgeColor', [1,0,0], 'LineWidth', LineWidth); % siamfc+    [1, 0, 0]
%         hold on
%         rectangle('Position', [345, 280, 27, 1], 'EdgeColor', [1,0,1], 'LineWidth', LineWidth); % siamrpn   [1,0,1]
%         hold on
%         rectangle('Position', [345, 300, 27, 1], 'EdgeColor', [136,0,21]/255, 'LineWidth', LineWidth); % siamrpn+  [[136,0,21]/255]  dark red
%         hold on
%         rectangle('Position', [445, 280, 27, 1], 'EdgeColor', [1,1,0], 'LineWidth', LineWidth); % staple    [1,1,0]
%         hold on
%         rectangle('Position', [445, 300, 27, 1], 'EdgeColor', [0,1,0], 'LineWidth', LineWidth); % eco-hc    [0,1,0]
%         hold on
        
       %%
        
        
        for j=1:length(trks)
            disp(trks{j}.name)            
           
            LineStyle = plotDrawStyle{j}.lineStyle;
            
            switch resultsAll{j}.type
                case 'rect'
                    rectangle('Position', resultsAll{j}.res(i,:), 'EdgeColor', plotDrawStyle{j}.color, 'LineWidth', LineWidth,'LineStyle',LineStyle);
                case 'ivtAff'
                    drawbox(resultsAll{j}.tmplsize, resultsAll{j}.res(i,:), 'Color', plotDrawStyle{j}.color, 'LineWidth', LineWidth,'LineStyle',LineStyle);
                case 'L1Aff'
                    drawAffine(resultsAll{j}.res(i,:), resultsAll{j}.tmplsize, plotDrawStyle{j}.color, LineWidth, LineStyle);                    
                case 'LK_Aff'
                    [corner c] = getLKcorner(resultsAll{j}.res(2*i-1:2*i,:), resultsAll{j}.tmplsize);
                    hold on,
                    plot([corner(1,:) corner(1,1)], [corner(2,:) corner(2,1)], 'Color', plotDrawStyle{j}.color,'LineWidth',LineWidth,'LineStyle',LineStyle);
                case '4corner'
                    corner = resultsAll{j}.res(2*i-1:2*i,:);
                    hold on,
                    plot([corner(1,:) corner(1,1)], [corner(2,:) corner(2,1)], 'Color', plotDrawStyle{j}.color,'LineWidth',LineWidth,'LineStyle',LineStyle);
                case 'SIMILARITY'
                    warp_p = parameters_to_projective_matrix(resultsAll{j}.type,resultsAll{j}.res(i,:));
                    [corner c] = getLKcorner(warp_p, resultsAll{j}.tmplsize);
                    hold on,
                    plot([corner(1,:) corner(1,1)], [corner(2,:) corner(2,1)], 'Color', plotDrawStyle{j}.color,'LineWidth',LineWidth,'LineStyle',LineStyle);
                otherwise
                    disp('The type of output is not supported!')
                    continue;
            end
        end        
%         imwrite(frame2im(getframe(gcf)), [pathSave  num2str(i) '.png']);
        writeVideo(aviobj, frame2im(getframe(gcf)));  % write video
    end
    close(aviobj);   % close video
    clf
end
