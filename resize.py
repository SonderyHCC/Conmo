import subprocess
import os

def resize_video(file_path, target_width=576, target_height=320):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"文件未找到：{file_path}")

    # 构造临时输出文件路径
    temp_file_path = file_path + ".tmp.mp4"

    # 使用 ffmpeg 缩放视频分辨率
    command = [
        "ffmpeg",
        "-i", file_path,
        "-vf", f"scale={target_width}:{target_height}",
        "-c:a", "copy",  # 保留原音频
        "-y",  # 自动覆盖输出文件
        temp_file_path
    ]

    # 执行命令
    subprocess.run(command, check=True)

    # 替换原始文件
    os.replace(temp_file_path, file_path)
    print(f"已将视频分辨率压缩为 {target_width}x{target_height}，并覆盖保存。")


# 示例调用
resize_video("./static/videos/multi-subject/Slow_Motion_Crash/original.mp4", 576, 320)