# ResearchTools
Design for analysing and visiualizing tracking and segmentation methods. Make research easier.

## News
:boom: Release initial version (most scripts are used for object tracking now).

## Contents
##### Single Object Tracking (SOT)
- For OTB
  - [py2mat_f.m]() Transform `txt` results to `.mat` for OTB official toolkit.
  - [mat2txt.py]() Transform `.mat` results to `txt`.
  - [drawResultBB.m]() Draw predicted bounding boxes on images and save in image format.
  - [drawResultBB_video.m]() Draw predicted bounding boxes on images and save in video format.
  - [blank2comma.py]() Transform result format form [x y w h] to [x,y,w,h].
  - [vot_analysis_boxgraph.py]

- For VOT
  - [eao_draw.py](): Draw eaos of multiple trackers (python version).
  - [gen_lost_excel.py](): Generate target lost information for each video in VOT (for multiple trackers).
  - [checklost.py](): Summarize lost information for each tracker.
  - [vot_analysis_boxgraph.py](): Draw box graph to analysz hyper-parameter influence.  
  - [calc_daivs_vot20.py](): Summary of target infomation in VOT and DAVIS, including target size, target size change ratio, motion pixels, video length. 

  <div align=center>
  <img src="https://i.postimg.cc/6Qs9M36L/eao-VOT2017.png" width="60%" height="30%" />
</div>

- For Analysing

  - [speed_eao.py](): Draw speed vs performance comparasion figures, as in Fig.1 of [Ocean](https://github.com/researchmm/TracKit).
  - [merge_videos.py](): Merge several videos to one.
  - [summary.py](): Summarize network structure details, e.g. parameter numbersm, network complexity (FLOPS), keras format summary. 











