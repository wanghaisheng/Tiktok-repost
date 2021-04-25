# This class deals with the formatting and editing of the video before uploading.
from moviepy.editor import *
import time


class Video:
    def __init__(self, dir, caption, user):
        self.dir = dir
        self.clip = VideoFileClip(self.dir)
        self.font = "Arial"
        self.font_size = 80
        self.caption = caption
        self.tiktok_dim = (1080, 1920)
        self.bg = "black"
        self.color = "white"
        self.userPreference = user
        '''
        if self.start_time is None:
            self.start_time = 0
        else:
            self.start_time = start_time
        if self.end_time is None:
            self.end_time = self.clip.duration
        else:
            self.end_time = end_time
        '''


    def customCrop(self, start_time, end_time):
        templist = sorted([start_time, end_time])
        start_time, end_time = templist[0], templist[1]
        if end_time > self.clip.duration:
            end_time = self.clip.duration
        self.clip = VideoFileClip(self.dir)
        self.dir = os.path.join(self.userPreference.video_save_dir, "post-processed") + ".mp4"
        self.clip = self.clip.subclip(t_start=start_time, t_end=end_time)
        self.clip.write_videofile(self.dir)


    def createVideo(self):
        self.clip = self.clip.resize(width=1080)  # Ignore error.
        base_clip = ColorClip(size=(1080, 1920), color=[10, 10, 10], duration=self.clip.duration)
        OFFSET = -20
        bottom_meme_pos = 960 + (((1080 / self.clip.size[0]) * (self.clip.size[1])) / 2) + OFFSET
        top_meme_pos = 960 - (((1080 / self.clip.size[0]) * (self.clip.size[1])) / 2) - OFFSET
        to_pos = 1920 / 6
        memeOverlay = TextClip(txt=self.caption, bg_color=self.bg, color=self.color, size=(900, None), kerning=-1,
                               method="caption", font=self.font, fontsize=self.font_size,
                               align="center")  # stroke_color="black", stroke_width=2.5
        memeOverlay = memeOverlay.set_duration(self.clip.duration)
        self.clip = CompositeVideoClip([base_clip, self.clip.set_position(("center", "center")), memeOverlay.set_position(("center", bottom_meme_pos))])
        self.dir = os.path.join(self.userPreference.video_save_dir, "processed") + ".mp4"
        self.clip.write_videofile(self.dir, fps=24)


