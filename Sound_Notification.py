import platform

def notify_me():
    if platform.system() == "Windows":
        # print("Windows")
        import winsound
        duration = 1000  # milliseconds
        freq = 440  # Hz
        winsound.Beep(freq, duration)
    elif platform.system() == "Darwin":
        # print("Mac")
        import os
        os.system('afplay /System/Library/PrivateFrameworks/ScreenReader.framework/Versions/A/Resources/Sounds/AnimationFlyToDownloads.aiff')
        
if __name__ =="__main__":
    notify_me()