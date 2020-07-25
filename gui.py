import cv2

class Window():
    
    #callbacki do trackbarów, można je zmienić
    def firstTrackbarCallback(self,x):
        if(x != 0):
            cv2.setTrackbarPos(self.firstTrackbar,self.windowName, 0)

    def secondTrackbarCallback(self,x):
        if(x != 0):
            cv2.setTrackbarPos(self.secondTrackbar,self.windowName, 0)
        
    def thirdTrackbarCallback(self,x):
        if(x != 0):
            cv2.setTrackbarPos(self.thirdTrackbar,self.windowName, 0)

    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.windowName = 'frame'
        #nazwy okna i trackbarów, można zmienić
        self.firstTrackbar = 'firstTrackbar'
        self.secondTrackbar = 'secondTrackbar'
        self.thirdTrackbar = 'thirdTrackbar'
        self.setCamera()
        self.setTrackbars()

    def setCamera(self):
        cv2.namedWindow(self.windowName, cv2.WINDOW_AUTOSIZE)
        cv2.setWindowProperty(self.windowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)
        self.camera = cv2.VideoCapture(0)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)

    def setTrackbars(self):
        cv2.createTrackbar(self.firstTrackbar, self.windowName,0,1,self.firstTrackbarCallback)
        cv2.createTrackbar(self.secondTrackbar, self.windowName,0,1,self.secondTrackbarCallback)
        cv2.createTrackbar(self.thirdTrackbar, self.windowName,0,1,self.thirdTrackbarCallback)

    def start(self):
        try:
            ret, frame = self.camera.read()
            while(True):
                ret, frame = self.camera.read()
                cv2.imshow(self.windowName, frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        except KeyboardInterrupt:
            pass

    
    def __del__(self):
        self.camera.release()
        cv2.destroyAllWindows()
        