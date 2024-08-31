import time

import mediapipe as mp
from GymApp.scanner.ThreadedCamera import ThreadedCamera
import requests
from GymApp.scanner.utils import *

import base64

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
mp_pose = mp.solutions.pose

pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
pose_landmark_drawing_spec = mp_drawing.DrawingSpec(thickness=5, circle_radius=2, color=(0, 0, 255))  # color circles
pose_connection_drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1, color=(0, 255, 0))  # color lines
PRESENCE_THRESHOLD = 0.5
VISIBILITY_THRESHOLD = 0.5
performedRep = False


# def send_img(base64_encoded_image):
#     r = requests.post("http://127.0.0.1:5000/video_feed", data="data:image/jpeg;base64," + base64_encoded_image)
#     time.sleep(5)
#


class Chestpress():
    def __init__(self):
        pass

    def exercise(self, source):
        threaded_camera = ThreadedCamera(source)
        while True:
            success, image = threaded_camera.show_frame()
            if not success or image is None:
                continue
            image = cv2.flip(image, 1)
            image_orig = cv2.flip(image, 1)
            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
            results = pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            mp_drawing.draw_landmarks(
                image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                landmark_drawing_spec=pose_landmark_drawing_spec,
                connection_drawing_spec=pose_connection_drawing_spec)
            idx_to_coordinates = get_idx_to_coordinates(image, results)
            try:
                # shoulder - Elbow - wrist
                if 12 in idx_to_coordinates and 14 in idx_to_coordinates and 16 in idx_to_coordinates:  # right side of body

                    # Line rShoulder - rElbow
                    cv2.line(image, (idx_to_coordinates[12]), (idx_to_coordinates[14]), thickness=4,
                             color=(255, 0, 255))
                    l1 = np.linspace(idx_to_coordinates[12], idx_to_coordinates[14], 100)

                    # Line rElbow - rWrist
                    cv2.line(image, (idx_to_coordinates[14]), (idx_to_coordinates[16]), thickness=4,
                             color=(255, 0, 255))
                    l2 = np.linspace(idx_to_coordinates[14], idx_to_coordinates[16], 100)

                    # Angel upper - forearm
                    ang1 = ang((idx_to_coordinates[12], idx_to_coordinates[14]),
                               (idx_to_coordinates[14], idx_to_coordinates[16]))
                    # Text Angel upper - forearm
                    cv2.putText(image, "   " + str(round(ang1, 2)), (idx_to_coordinates[14]),
                                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                fontScale=0.6, color=(0, 255, 0), thickness=2)
                    center, radius, start_angle, end_angle = convert_arc(l1[80], l2[20], sagitta=15)
                    axes = (radius, radius)
                    draw_ellipse(image, center, axes, -1, start_angle, end_angle, 255)

                if 11 in idx_to_coordinates and 13 in idx_to_coordinates and 15 in idx_to_coordinates:  # left side of body
                    cv2.line(image, (idx_to_coordinates[11]), (idx_to_coordinates[13]), thickness=4,
                             color=(255, 0, 255))
                    cv2.line(image, (idx_to_coordinates[13]), (idx_to_coordinates[15]), thickness=4,
                             color=(255, 0, 255))
                    l1 = np.linspace(idx_to_coordinates[11], idx_to_coordinates[13], 100)
                    l2 = np.linspace(idx_to_coordinates[13], idx_to_coordinates[16], 100)
                    eang1 = ang((idx_to_coordinates[11], idx_to_coordinates[13]),
                                (idx_to_coordinates[13], idx_to_coordinates[15]))
                    cv2.putText(image, str(round(eang1, 2)), (idx_to_coordinates[13]),
                                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                fontScale=0.6, color=(0, 255, 0), thickness=2)
                    center, radius, start_angle, end_angle = convert_arc(l1[80], l2[20], sagitta=15)
                    axes = (radius, radius)
                    draw_ellipse(image, center, axes, -1, start_angle, end_angle, 255)

            except:
                pass

            try:
                # rhip - rknee - rheel
                if 26 in idx_to_coordinates and 30 in idx_to_coordinates and 24 in idx_to_coordinates:  # right side of body

                    # Line rhip - rknie
                    cv2.line(image, (idx_to_coordinates[24]), (idx_to_coordinates[26]), thickness=4,
                             color=(255, 0, 255))
                    l1 = np.linspace(idx_to_coordinates[24], idx_to_coordinates[26], 100)

                    # Line rheel - rfood.index
                    cv2.line(image, (idx_to_coordinates[26]), (idx_to_coordinates[30]), thickness=4,
                             color=(255, 0, 255))
                    l2 = np.linspace(idx_to_coordinates[26], idx_to_coordinates[30], 100)

                    # Angel rfemur - rfoot
                    angel = round(ang((idx_to_coordinates[24], idx_to_coordinates[26]),
                                      (idx_to_coordinates[26], idx_to_coordinates[30])))
                    # Text Angel rfemur - rfoot
                    cv2.putText(image, "   " + str(round(angel, 2)), (idx_to_coordinates[26]),
                                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                fontScale=0.6, color=(0, 255, 0), thickness=2)

                    center, radius, start_angle, end_angle = convert_arc(l1[80], l2[20], sagitta=15)
                    axes = (radius, radius)
                    draw_ellipse(image, center, axes, -1, start_angle, end_angle, 255)

                # lhip - lknee - lheel
                if 23 in idx_to_coordinates and 25 in idx_to_coordinates and 29 in idx_to_coordinates:
                    # Line rhip - rknie
                    cv2.line(image, (idx_to_coordinates[23]), (idx_to_coordinates[25]), thickness=4,
                             color=(255, 0, 255))
                    l1 = np.linspace(idx_to_coordinates[23], idx_to_coordinates[25], 100)

                    # Line rheel - rfood.index
                    cv2.line(image, (idx_to_coordinates[25]), (idx_to_coordinates[29]), thickness=4,
                             color=(255, 0, 255))
                    l2 = np.linspace(idx_to_coordinates[25], idx_to_coordinates[29], 100)

                    # Angel rfemur - rfoot
                    angel_lfemur_lfoot = round(ang((idx_to_coordinates[23], idx_to_coordinates[25]),
                                                   (idx_to_coordinates[25], idx_to_coordinates[29])))
                    # Text Angel rfemur - rfoot
                    cv2.putText(image, "   " + str(round(angel, 2)), (idx_to_coordinates[25]),
                                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                fontScale=0.6, color=(0, 255, 0), thickness=2)

                    center, radius, start_angle, end_angle = convert_arc(l1[80], l2[20], sagitta=15)
                    axes = (radius, radius)
                    draw_ellipse(image, center, axes, -1, start_angle, end_angle, 255)
            except:
                pass

            # try:
            #     # rshoulder - rhip
            #     if 12 in idx_to_coordinates and 24 in idx_to_coordinates:  # right side of body
            #
            #         # Line rshoulder - rhip
            #         cv2.line(image, (idx_to_coordinates[12]), (idx_to_coordinates[24]), thickness=4,
            #                  color=(255, 0, 255))
            #         l1 = np.linspace(idx_to_coordinates[12], idx_to_coordinates[24], 100)
            #
            #         # Angel rshoulder - rhip
            #         angel = round(ang((idx_to_coordinates[12], idx_to_coordinates[24])))
            #
            #         # Text Angel rshoulder - rhip
            #         cv2.putText(image, "   " + str(round(angel, 2)), (idx_to_coordinates[26]),
            #                     fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            #                     fontScale=0.6, color=(0, 255, 0), thickness=2)
            #
            #         if angel < 70 or angel > 120:
            #             print("Falsch R")
            #
            #         center, radius, start_angle, end_angle = convert_arc(l1[80], l2[20], sagitta=15)
            #         axes = (radius, radius)
            #         draw_ellipse(image, center, axes, -1, start_angle, end_angle, 255)
            #
            #
            #     # rshoulder - rhip
            #     if 11 in idx_to_coordinates and 23 in idx_to_coordinates:  # right side of body
            #
            #         # Line rshoulder - rhip
            #         cv2.line(image, (idx_to_coordinates[11]), (idx_to_coordinates[23]), thickness=4,
            #                  color=(255, 0, 255))
            #         l1 = np.linspace(idx_to_coordinates[11], idx_to_coordinates[23], 100)
            #
            #         # Angel rshoulder - rhip
            #         angel = round(ang((idx_to_coordinates[11], idx_to_coordinates[23])))
            #
            #         # Text Angel rshoulder - rhip
            #         cv2.putText(image, "   " + str(round(angel, 2)), (idx_to_coordinates[11]),
            #                     fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            #                     fontScale=0.6, color=(0, 255, 0), thickness=2)
            #
            #         center, radius, start_angle, end_angle = convert_arc(l1[80], l2[20], sagitta=15)
            #         axes = (radius, radius)
            #         draw_ellipse(image, center, axes, -1, start_angle, end_angle, 255)
            #
            # except:
            #     pass

            try:
                # rEar - rShoulder
                if 8 in idx_to_coordinates and 12 in idx_to_coordinates:  # right side of body

                    cv2.line(image, (idx_to_coordinates[8]), (idx_to_coordinates[12]), thickness=4,
                             color=(255, 0, 255))
                    l1 = np.linspace(idx_to_coordinates[8], idx_to_coordinates[12], 100)

                    # Angel
                    angel = round(ang((idx_to_coordinates[8], idx_to_coordinates[12]),
                                      (idx_to_coordinates[8], idx_to_coordinates[12])))

                    # Text Angel
                    cv2.putText(image, "   " + str(round(angel, 2)), (idx_to_coordinates[26]),
                                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                fontScale=0.6, color=(0, 255, 0), thickness=2)

                    center, radius, start_angle, end_angle = convert_arc(l1[80], l2[20], sagitta=15)
                    axes = (radius, radius)
                    draw_ellipse(image, center, axes, -1, start_angle, end_angle, 255)

                    center, radius, start_angle, end_angle = convert_arc(l1[80], l2[20], sagitta=15)
                    axes = (radius, radius)
                    draw_ellipse(image, center, axes, -1, start_angle, end_angle, 255)
            except:
                pass

            #  cv2.imshow('Image', rescale_frame(image, percent=100))
            # _, img_encoded = cv2.imencode('.jpg', image)
            # base64_encoded_image = base64.b64encode(img_encoded).decode('utf-8')
            # send_img(base64_encoded_image)

            r = requests.post("http://127.0.0.1:5000", data="test")
            time.sleep(10)

            if cv2.waitKey(5) & 0xFF == 27:
                break

        pose.close()
