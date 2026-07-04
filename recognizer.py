import cv2
import face_recognition
import pickle
import os


class FaceRecognizer:

    def __init__(self):

        if os.path.exists("encodings/encodings.pkl"):
            with open("encodings/encodings.pkl", "rb") as file:
                data = pickle.load(file)

            self.known_encodings = data["encodings"]
            self.known_names = data["names"]
        else:
            self.known_encodings = []
            self.known_names = []

    def create_encodings(self):

        self.known_encodings = []
        self.known_names = []

        images_folder = "images"

        if not os.path.exists(images_folder):
            print("Images folder not found!")
            return

        if not os.path.exists("encodings"):
            os.makedirs("encodings")

        for filename in os.listdir(images_folder):

            image_path = os.path.join(images_folder, filename)

            image = face_recognition.load_image_file(image_path)

            encodings = face_recognition.face_encodings(image)

            if len(encodings) > 0:

                self.known_encodings.append(encodings[0])
                self.known_names.append(os.path.splitext(filename)[0])

        data = {
            "encodings": self.known_encodings,
            "names": self.known_names
        }

        with open("encodings/encodings.pkl", "wb") as file:
            pickle.dump(data, file)

        print("Face encodings created successfully!")

    def recognize_faces(self):

        if len(self.known_encodings) == 0:
            print("No registered faces found!")
            return

        cap = cv2.VideoCapture(0)

        while True:

            ret, frame = cap.read()

            if not ret:
                break

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
            face_count = len(face_locations)
            recognized = False
            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

                matches = face_recognition.compare_faces(
                    self.known_encodings,
                    face_encoding
                )

                face_distances = face_recognition.face_distance(
                    self.known_encodings,
                    face_encoding
                )

                name = "Unknown Person"

                if len(face_distances) > 0:
                    best_match = face_distances.argmin()

                    if matches[best_match]:
                        name = self.known_names[best_match]
                        recognized = True

                if name == "Unknown Person":
                    color = (0, 0, 255)  # Red
                else:
                    color = (0, 255, 0)  # Green

                cv2.rectangle(
                    frame,
                    (left, top),
                    (right, bottom),
                    color,
                    2
                )

                cv2.putText(
                    frame,
                    name,
                    (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    color,
                    2
                )


            # Background panel
            cv2.rectangle(frame, (10, 10), (360, 110), (40, 40, 40), -1)

            # Face count
            cv2.putText(
                frame,
                f"Faces Detected : {face_count}",
                (20, 35),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 255),
                2
            )
            if face_count == 0:
                status = "No Face Detected"
                status_color = (0, 0, 255)  # Red

            elif recognized:
                status = "Face Recognized"
                status_color = (0, 255, 0)  # Green

            else:
                status = "Unknown Face Detected"
                status_color = (0, 255, 255)  # Yellow

            cv2.putText(
                frame,
                f"Status : {status}",
                (20, 65),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                status_color,
                2
            )

            
            cv2.putText(
                frame,
                "[Q] Exit Recognition",
                (20, 95),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 255, 255),
                2
            )
            cv2.imshow("Face Recognition", frame)

            if cv2.waitKey(1) == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()