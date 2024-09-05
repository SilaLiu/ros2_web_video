import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/pixbus/pix/robobus/HMI/web_video_ws/install/combined_launch'
