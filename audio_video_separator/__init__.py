import tempfile
from pathlib import Path, PurePath
import shutil

import ffmpeg

import data_URI


def split_video(video_uri_or_file: str, fps: int = 2) -> tuple[str, list[str]]:
    if shutil.which("ffmpeg") is None:
        raise FileNotFoundError("ffmpeg not found in PATH")

    if not video_uri_or_file.startswith("data:"):
        video_uri = data_URI.from_file(video_uri_or_file)
    else:
        video_uri = video_uri_or_file

    with tempfile.TemporaryDirectory() as outdir:
        audio = PurePath(outdir) / "audio.mp3"
        with data_URI.as_tempfile(video_uri) as video_file:
            (
                ffmpeg.input(video_file)
                .output(
                    str(audio),
                    loglevel="error",
                    **{
                        # Use 64k bitrate for smaller file
                        "b:a": "64k",
                        # Only output one channel, again for smaller file
                        "ac": "1",
                    },
                )
                .run()
            )
            (
                ffmpeg.input(video_file)
                .output(
                    str(PurePath(outdir) / "frame-%04d.jpg"),
                    loglevel="error",
                    **{
                        # Use fps as specified, scale image to fit within 512x512
                        "vf": f"fps={fps},scale='if(gt(iw,ih),512,-1)':'if(gt(ih,iw),512,-1)'",
                        "q:v": "20",
                    },
                )
                .run()
            )
        images = list(Path(outdir).glob("*.jpg"))
        images.sort()
        return data_URI.from_file(audio), [data_URI.from_file(image) for image in images]
