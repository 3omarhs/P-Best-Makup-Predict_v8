class Capture():
    def Image(self=1):
        import cv2
        import os

        files = os.listdir('../photos/Captured')  # your directory path
        count = len(files)
        # print('len: ' + str(count))

        video = cv2.VideoCapture(0)  # 1.creating a video object
        a = 0  # 2. Variable
        while True:  # 3. While loop
            a = a + 1
            check, frame = video.read()  # 4.Create a frame object
            # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)      # Converting to grayscale
            cv2.imshow("Tap Space to Capture..", frame)  # 5.show the frame!
            key = cv2.waitKey(1)  # 6.for playing
            if key % 256 == 32:  # SPACE pressed
                saveImageName = f"photos/Captured/img_{count}.jpg"
                showPic = cv2.imwrite(saveImageName, frame)  # 7. image saving
                break
        print('Photo Captured: '+str(showPic))
        video.release()  # 8. shutdown the camera
        # cv2.destroyAllWindows
        cv2.destroyWindow("Tap Space to Capture..")
        cv2.waitKey(1)
        return saveImageName
# print(Capture.Image())