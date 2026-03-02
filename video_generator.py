from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip

def create_video_from_images(image_paths, output_path, duration_per_scene=7.5, music_path=None):
    clips = [ImageClip(img).set_duration(duration_per_scene).resize(height=1920).resize(width=1080) for img in image_paths]
    video = concatenate_videoclips(clips, method="compose")
    if music_path:
        audio = AudioFileClip(music_path).subclip(0, video.duration)
        video = video.set_audio(audio)
    video.write_videofile(output_path, fps=24)