受到 [BV1hu411m713](https://www.bilibili.com/video/BV1hu411m713) 启发做来练练手的东西。

## 原理
1. 用 `video_to_frame.py` 把原视频转换为帧
2. 用 `frame_color.py` 把每一帧的亮度分类存入 `temp.json`
3. 用 `process.py` 每一帧切成30*30的小块，然后按照小块的亮度在 `temp.json` 找符合的随机一个帧。
4. 把那个找到的帧贴到原处。如果亮度为纯黑和纯白则不做处理。
5. 最后用 Pr 把 `result` 中的帧组合成视频输出