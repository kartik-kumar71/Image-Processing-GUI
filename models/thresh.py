import cv2

class Thresh_image():
    def __init__(self,t1,t2,th,im_path):
        self.t1 = t1
        self.t2 = t2
        self.th = eval(th)
        self.image = cv2.imread(im_path)

    def threshold():
        thresh = cv2.threshold(self.image,t1,t2,self.th)
        return cv2.cvtColor(thresh,cv2.COLOR_BGR2RGB)

    def blur():
        pass