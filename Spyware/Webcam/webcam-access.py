from cv2 import VideoCapture, imwrite, destroyAllWindows
from cv2.typing import MatLike


def take_picture(path: str, camera_index) -> bool:
    camera = VideoCapture(camera_index)
    status, pic = camera.read()
    if status:
        save_picture(path, pic)
        camera.release()
        destroyAllWindows()
        return True
    return False


def save_picture(path: str, frame: MatLike) -> None:
    imwrite(path, frame)

if __name__ == '__main__':
    take_picture('Images/test1.png', 0)
    take_picture('Images/test2.png', 0)
    take_picture('Images/test3.png', 0)
    take_picture('Images/test4.png', 0)