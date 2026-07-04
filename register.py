from database import DatabaseManager

from name_dialog import NameDialog
import cv2
import os
import face_recognition
import pickle


class RegisterFace:

    def open_camera(self):

        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            return "camera_error"

        while True:

            ret, frame = cap.read()

            if not ret:
                break

            # Instruction panel
            cv2.rectangle(frame, (10, 10), (320, 85), (40, 40, 40), -1)

            cv2.putText(
                frame,
                "[S] Save Face",
                (20, 38),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                "[Q] Cancel",
                (20, 70),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 255),
                2
            )
            cv2.imshow("Register Face", frame)

            key = cv2.waitKey(1)

            # Press S to save image
            if key == ord('s'):
                dialog = NameDialog()

                if dialog.exec_():
                    name = dialog.name_edit.text().strip()

                    if name == "":
                        continue
                else:
                    continue



                # Convert captured image to RGB
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                encodings = face_recognition.face_encodings(rgb_frame)

                if len(encodings) == 0:
                    cap.release()
                    cv2.destroyAllWindows()
                    return "no_face"

                new_encoding = encodings[0]

                # Check if encodings file already exists
                if os.path.exists("encodings/encodings.pkl"):

                    with open("encodings/encodings.pkl", "rb") as file:
                        data = pickle.load(file)

                    matches = face_recognition.compare_faces(
                        data["encodings"],
                        new_encoding,
                        tolerance=0.45
                    )

                    if True in matches:
                        cap.release()
                        cv2.destroyAllWindows()
                        return "duplicate"

                # Save image
                if not os.path.exists("images"):
                    os.makedirs("images")

                image_path = f"images/{name}.jpg"

                cv2.imwrite(image_path, frame)

                db = DatabaseManager()
                db.insert_person(name, image_path)
                db.close()

                cap.release()
                cv2.destroyAllWindows()
                return "success"

                



                

            # Press Q to quit
            elif key == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                return "cancelled"

