from cv2 import VideoCapture, imwrite, destroyAllWindows
from cv2.typing import MatLike


def take_picture(path: str) -> bool:
    camera = VideoCapture(0)
    status, pic = camera.read()
    if status:
        save_picture(path, pic)
        camera.release()
        destroyAllWindows()
        return True
    return False


def save_picture(path: str, frame: MatLike) -> None:
    imwrite(path, frame)
