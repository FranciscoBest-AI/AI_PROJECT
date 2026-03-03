# ==========================================
# video_generator.py
# ==========================================
from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip, CompositeVideoClip, TextClip

def create_video_from_images(image_paths, output_path, duration_per_scene=5, resolution=(720,1280), music_path=None, subtitles=None):
    clips = []
    for i, img in enumerate(image_paths):
        clip = ImageClip(img).set_duration(duration_per_scene).resize(newsize=resolution)
        if subtitles and i < len(subtitles):
            txt_clip = TextClip(subtitles[i], fontsize=24, color='white', font='Arial-Bold', method='caption', size=(resolution[0]-40,None)).set_position(('center', resolution[1]-100)).set_duration(duration_per_scene)
            clip = CompositeVideoClip([clip, txt_clip])
        clips.append(clip)
    
    video = concatenate_videoclips(clips, method="compose", padding=-0.5)
    if music_path:
        audio = AudioFileClip(music_path).subclip(0, video.duration)
        video = video.set_audio(audio)
    video.write_videofile(output_path, fps=24, codec='libx264', audio_codec='aac', threads=2, preset='ultrafast')