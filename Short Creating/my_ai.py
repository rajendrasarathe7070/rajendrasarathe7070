from flask import Flask, request, send_file, render_template_string
import os
import uuid
import shutil
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from pytube import YouTube
app = Flask(__name__)

# Auto usage folder
BASE_FOLDER = "usage"
os.makedirs(BASE_FOLDER, exist_ok=True)

# HTML + CSS inside Python
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
<title>YouTube Clip Cutter</title>
<style>
body{background:#0f172a;color:white;font-family:Arial;text-align:center;padding:50px}
input,button{padding:10px;margin:10px;font-size:16px;border-radius:6px;border:none}
button{background:#22c55e;color:black;cursor:pointer}
.box{background:#111827;padding:30px;border-radius:12px;width:400px;margin:auto}
</style>
</head>
<body>

<div class="box">
<h2>🎥 YouTube Clip Cutter</h2>

<form method="POST">
<input type="text" name="url" placeholder="YouTube Video Link" required><br>
<input type="text" name="times" placeholder="Time slices (e.g 10-20,30-50)" required><br>
<button type="submit">Process</button>
</form>

<p>{{msg}}</p>
</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    msg = ""
    if request.method == "POST":
        try:
            url = request.form["url"]
            times = request.form["times"]

            # unique session folder
            session_id = str(uuid.uuid4())
            session_folder = os.path.join(BASE_FOLDER, session_id)
            os.makedirs(session_folder, exist_ok=True)

            # ---- YouTube Download (Disabled for safety) ----
             
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            video_path = stream.download(output_path=session_folder, filename="video.mp4")

            # Demo placeholder video path
            video_path = "sample.mp4"  # replace with real video

            clips = []
            slices = times.split(",")

            for i, t in enumerate(slices):
                start, end = map(int, t.split("-"))
                clip_name = f"clip_{i}.mp4"
                clip_path = os.path.join(session_folder, clip_name)

                ffmpeg_extract_subclip(video_path, start, end, targetname=clip_path)
                clips.append(clip_path)

            msg = f"{len(clips)} clips created successfully!"

            # After sending clips, delete folder (auto cleanup)
            # shutil.rmtree(session_folder)

        except Exception as e:
            msg = f"❌ Error: {str(e)}"

    return render_template_string(HTML_PAGE, msg=msg)

if __name__ == "__main__":
    app.run(debug=True)