# Pravega_video_example

本案例展示使用Pravega传输视频。使用Python语言开启传输和接收。

## 安装Pravega

在一个终端，启用Pravega。

```
wget https://github.com/pravega/pravega/releases/download/v0.9.0/pravega-0.9.0.tgz
# or
#curl -OL https://github.com/pravega/pravega/releases/download/v0.9.0/pravega-0.9.0.tgz
tar zxvf pravega-0.9.0.tgz
cd pravega-0.9.0
./bin/pravega-standalone
```

在另一个终端，进入pravega-0.9.0文件夹。创建Scope和Stream。

```
./bin/pravega-cli
> scope create examples
> stream create examples/mystream1
```

## 使用Python将视频送入Pravega

```
python video_file_to_pravega.py --pravega-scope examples --pravega-stream mystream1 --source-uri /home/yjw/wifi-ble1.mp4
```

例如
```
python video_file_to_pravega.py --source-uri https://www.freedesktop.org/software/gstreamer-sdk/data/media/sintel_trailer-480p.webm
```