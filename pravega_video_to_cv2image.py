import cv2
import gi
gi.require_version("Gst", "1.0")
from gi.repository import GObject, Gst

Gst.init(None)

pipeline_description=('pravegasrc name=src ! tsdemux ! h264parse ! avdec_h264 ! videoconvert ! appsink')
pipeline = Gst.parse_launch(pipeline_description)

#pravegasrc = pipeline.get_by_name('src')
#pravegasrc.set_property('controller', "tcp://127.0.0.1:9090")
#pravegasrc.set_property('stream', '%s/%s' % ('nxytest' , 'videotest'))
    
#print(pravegasrc)
print(cv2.getBuildInformation())
pipeline_description=('pravegasrc name=src ! tsdemux ! h264parse ! avdec_h264 ! videoconvert ! appsink').format(1280, 720)
video_capture = cv2.VideoCapture(pipeline_description ,cv2.CAP_GSTREAMER)

while True:      
        ret, frame = video_capture.read()
        if not ret:
            print('empty frame')
            break
        cv2.imshow(frame,'stream')