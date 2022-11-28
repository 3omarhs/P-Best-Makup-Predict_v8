import cv2


img = cv2.imread('photos/img.png', cv2.IMREAD_UNCHANGED)
img = cv2.resize(img, (1000, 700), interpolation=cv2.INTER_AREA)

########################################
button = (200, 50), (200,300), "Train"    ##(width, height), (startWidth, startHeight)
button1 = (200, 50), (600,300), "Run"    ##(width, height), (startWidth, startHeight)
ButtonTextColor = (0, 0, 0)
ButtonBgColor = (255, 255, 255)
Buttonfont = cv2.FONT_HERSHEY_TRIPLEX  # font for left click event
but = -1

class RTbuttons():
    cv2.putText(img, 'Choose Run Type:', (150,120), Buttonfont, 1, ButtonTextColor, 2)

    cv2.rectangle(img, (button[1][0], button[1][1]), (button[1][0] + button[0][0], button[1][1] + button[0][1]), ButtonBgColor, -1)
    cv2.putText(img, button[2], (button[1][0] + 30, button[1][1] + button[0][1] - 15), Buttonfont, 1, ButtonTextColor, 2)

    cv2.rectangle(img, (button1[1][0], button1[1][1]), (button1[1][0] + button1[0][0], button1[1][1] + button1[0][1]), ButtonBgColor, -1)
    cv2.putText(img, button1[2], (button1[1][0] + 30, button1[1][1] + button1[0][1] - 15), Buttonfont, 1, ButtonTextColor, 2)

    def mouse_click(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:  # to check if left mouse button was clicked
            if x >= button[1][0] and x <= button[1][0]+button[0][0] and y >= button[1][1] and y <= button[1][1]+button[0][1]:
                global but
                but = 1
                cv2.destroyAllWindows()

            elif x >= button1[1][0] and x <= button1[1][0]+button1[0][0] and y >= button1[1][1] and y <= button1[1][1]+button1[0][1]:
                but = 2
                cv2.destroyAllWindows()

    def __init__(self):
        cv2.imshow('image', img)
        cv2.setMouseCallback('image', RTbuttons.mouse_click)
        cv2.waitKey(0)

    def getbuttonPressed(self=''):
        RTbuttons()
        return but


    cv2.destroyAllWindows()     # close all the opened windows.





# print(buttons.getbuttonPressed())