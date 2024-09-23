import mediapipe as mp
from ScannerUtils.ThreadedCamera import ThreadedCamera
from ScannerUtils.utils import *
import cv2

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
mp_pose = mp.solutions.pose

pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
pose_landmark_drawing_spec = mp_drawing.DrawingSpec(thickness=5, circle_radius=2, color=(0, 0, 255))  # color circles
pose_connection_drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1, color=(0, 255, 0))  # color lines
PRESENCE_THRESHOLD = 0.5
VISIBILITY_THRESHOLD = 0.5
performedRep = False


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
            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
            results = pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            mp_drawing.draw_landmarks(
                image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                landmark_drawing_spec=pose_landmark_drawing_spec,
                connection_drawing_spec=pose_connection_drawing_spec)
            idx_to_coordinates = get_idx_to_coordinates(image, results)
            # try:  # Schulter - Ellenbogen - Hüfte
            #     if 12 in idx_to_coordinates and 14 in idx_to_coordinates and 24 in idx_to_coordinates:  # Rechte Körperhälfte
            #
            #         # Linie Rechts Schulter/Ellenbogen
            #         cv2.line(image, (idx_to_coordinates[12]), (idx_to_coordinates[14]), thickness=4,
            #                  color=(255, 0, 255))
            #         l1 = np.linspace(idx_to_coordinates[12], idx_to_coordinates[14], 100)
            #
            #         # Linie Rechts Ellebogen/Handgelenk
            #         cv2.line(image, (idx_to_coordinates[12]), (idx_to_coordinates[24]), thickness=4,
            #                  color=(255, 0, 255))
            #         l2 = np.linspace(idx_to_coordinates[12], idx_to_coordinates[24], 100)
            #
            #         # Winkel Rechts Ober/Unterarm
            #         angR = ang((idx_to_coordinates[14], idx_to_coordinates[12]),
            #                    (idx_to_coordinates[12], idx_to_coordinates[24]))
            #
            #         # Text Winkel Rechts Ober/Unterarm
            #         cv2.putText(image, "   " + str(round(angR, 2)), (idx_to_coordinates[14]),
            #                     fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            #                     fontScale=0.6, color=(0, 255, 0), thickness=2)
            #         center, radius, start_angle, end_angle = convert_arc(l1[80], l2[20], sagitta=15)
            #         axes = (radius, radius)
            #         draw_ellipse(image, center, axes, -1, start_angle, end_angle, 255)
            #
            #         if angR > 75:
            #             print(f"Linker Ellenbogen runter {angR}")
            #         if angR < 30:
            #             print(f"Linker Ellenbogen höher {angR}")
            #
            #     if 11 in idx_to_coordinates and 13 in idx_to_coordinates and 23 in idx_to_coordinates:
            #
            #         # Linie Links Schulter/Ellenbogen
            #         cv2.line(image, (idx_to_coordinates[11]), (idx_to_coordinates[13]), thickness=4,
            #                  color=(255, 0, 255))
            #         l1 = np.linspace(idx_to_coordinates[11], idx_to_coordinates[13], 100)
            #
            #         # Linie Links Ellebogen/Handgelenk
            #         cv2.line(image, (idx_to_coordinates[11]), (idx_to_coordinates[23]), thickness=4,
            #                  color=(255, 0, 255))
            #         l2 = np.linspace(idx_to_coordinates[11], idx_to_coordinates[23], 100)
            #
            #         # Winkel Links Ober/Unterarm
            #         angL = ang((idx_to_coordinates[13], idx_to_coordinates[11]),
            #                    (idx_to_coordinates[11], idx_to_coordinates[23]))
            #
            #         # Text Winkel Links Ober/Unterarm
            #         cv2.putText(image, str(round(angL, 2)), (idx_to_coordinates[13]),
            #                     fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            #                     fontScale=0.6, color=(0, 255, 0), thickness=2)
            #         center, radius, start_angle, end_angle = convert_arc(l1[80], l2[20], sagitta=15)
            #         axes = (radius, radius)
            #         draw_ellipse(image, center, axes, -1, start_angle, end_angle, 255)
            #
            #         if angL > 75:
            #             print(f"Linker Ellenbogen runter {angL}")
            #         if angL < 30:
            #             print(f"Linker Ellenbogen höher {angL}")
            # except:
            #     pass

            '''  
            try:
                # Schulter - Hüfte -  Knie
                if 12 in idx_to_coordinates and 24 in idx_to_coordinates and 26 in idx_to_coordinates:  # Rechte Körperhälfte

                    # Linie Rechts Schulter/Hüfte
                    cv2.line(image, (idx_to_coordinates[12]), (idx_to_coordinates[24]), thickness=4,
                             color=(255, 0, 255))
                    l1 = np.linspace(idx_to_coordinates[12], idx_to_coordinates[24], 100)

                    # Linie Rechts Hüfte/Knie
                    cv2.line(image, (idx_to_coordinates[24]), (idx_to_coordinates[26]), thickness=4,
                             color=(255, 0, 255))
                    l2 = np.linspace(idx_to_coordinates[24], idx_to_coordinates[26], 100)

                    # Winkel Rechts Schulter/Hüfte/Knie
                    angR = ang((idx_to_coordinates[12], idx_to_coordinates[24]),
                               (idx_to_coordinates[24], idx_to_coordinates[26]))

                    # Text Winkel Rechts Schulter/Hüfte/Knie
                    cv2.putText(image, "   " + str(round(angR, 2)), (idx_to_coordinates[24]),
                                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                fontScale=0.6, color=(0, 255, 0), thickness=2)
                    center, radius, start_angle, end_angle = convert_arc(l1[80], l2[20], sagitta=15)
                    axes = (radius, radius)
                    draw_ellipse(image, center, axes, -1, start_angle, end_angle, 255)

                if 11 in idx_to_coordinates and 13 in idx_to_coordinates and 15 in idx_to_coordinates:  # Linke Körperhälfte

                    # Linie Links Schulter/Hüfte
                    cv2.line(image, (idx_to_coordinates[11]), (idx_to_coordinates[23]), thickness=4,
                             color=(255, 0, 255))
                    l1 = np.linspace(idx_to_coordinates[11], idx_to_coordinates[23], 100)

                    # Linie Links Hüfte/Knie
                    cv2.line(image, (idx_to_coordinates[23]), (idx_to_coordinates[25]), thickness=4,
                             color=(255, 0, 255))
                    l2 = np.linspace(idx_to_coordinates[23], idx_to_coordinates[25], 100)

                    # Winkel Links Schulter/Hüfte/Knie
                    angL = ang((idx_to_coordinates[11], idx_to_coordinates[23]),
                               (idx_to_coordinates[23], idx_to_coordinates[25]))

                    # Text Winkel Links Schulter/Hüfte/Knie
                    cv2.putText(image, str(round(angL, 2)), (idx_to_coordinates[23]),
                                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                fontScale=0.6, color=(0, 255, 0), thickness=2)
                    center, radius, start_angle, end_angle = convert_arc(l1[80], l2[20], sagitta=15)
                    axes = (radius, radius)
                    draw_ellipse(image, center, axes, -1, start_angle, end_angle, 255)


            except:
                pass
            '''

            try:
                # Schulter - Ellenbogen - Handgelenk
                if 14 in idx_to_coordinates and 16 in idx_to_coordinates:  # Rechte Körperhälfte

                    # Linie Rechts Ellenbogen/Handgelenk
                    cv2.line(image, (idx_to_coordinates[14]), (idx_to_coordinates[16]), thickness=4,
                             color=(255, 0, 255))
                    l1 = np.linspace(idx_to_coordinates[14], idx_to_coordinates[16], 100)

                    # Linie Rechts Ellenbogen/Handgelenk
                    cv2.line(image, (idx_to_coordinates[14]), (idx_to_coordinates[16]), thickness=4,
                             color=(255, 0, 255))
                    l2 = np.linspace(idx_to_coordinates[14], idx_to_coordinates[16], 100)

                    # Winkel Rechts Schulter/Ellenbogen/Handgelenk
                    angR = ang((idx_to_coordinates[16], idx_to_coordinates[14]),
                               (idx_to_coordinates[14], idx_to_coordinates[16]))

                    # Text Winkel Rechts Schulter/Ellenbogen/Handgelenk
                    cv2.putText(image, "   " + str(round(angR, 2)), (idx_to_coordinates[14]),
                                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                fontScale=0.6, color=(0, 255, 0), thickness=2)
                    center, radius, start_angle, end_angle = convert_arc(l1[80], l2[20], sagitta=15)
                    axes = (radius, radius)
                    draw_ellipse(image, center, axes, -1, start_angle, end_angle, 255)

                if 13 in idx_to_coordinates and 15 in idx_to_coordinates:  # Linke Körperhälfte

                    cv2.line(image, (idx_to_coordinates[13]), (idx_to_coordinates[15]), thickness=4,
                             color=(255, 0, 255))
                    l1 = np.linspace(idx_to_coordinates[13], idx_to_coordinates[15], 100)

                    # Linie Links Ellenbogen/Handgelenk
                    cv2.line(image, (idx_to_coordinates[13]), (idx_to_coordinates[15]), thickness=4,
                             color=(255, 0, 255))
                    l2 = np.linspace(idx_to_coordinates[13], idx_to_coordinates[15], 100)

                    # Winkel Links Schulter/Ellenbogen/Handgelenk
                    angL = ang((idx_to_coordinates[15], idx_to_coordinates[13]),
                               (idx_to_coordinates[13], idx_to_coordinates[15]))

                    # Text Winkel Links Schulter/Ellenbogen/Handgelenk
                    cv2.putText(image, str(round(angL, 2)), (idx_to_coordinates[13]),
                                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                fontScale=0.6, color=(0, 255, 0), thickness=2)
                    center, radius, start_angle, end_angle = convert_arc(l1[80], l2[20], sagitta=15)
                    axes = (radius, radius)
                    draw_ellipse(image, center, axes, -1, start_angle, end_angle, 255)

            except:
                pass

            print( image)

        pose.close()
