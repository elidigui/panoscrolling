# import the necessary packages
import cv2
import os

class LoadSerie:
  """Load a serie of images and order them alphanumerically
  List all the file in a directory if:
  -all files are of the same type (png or jpg)
  -and named alphanumerically.
  It return the list """

  def __init__(self,dir):
    """init the object list"""
    self.dir=dir
    self.l=[]
    self.f_ok=["png","jpg","jpeg","bmp" ,"dib" ,"jpeg","jpg" ,"jpe" ,"jp2" ,"png" ,"pbm" ,"pgm" ,"ppm" ,"sr"  ,"ras" ,"tiff","tif"]
  
  def list_of_image(self):
    """List files in the directory dir"""
    l_=[]
    l=os.listdir(self.dir)
    for i in l:
      if os.path.splitext(i)[1][1:] not in self.f_ok:
        exit("The file %s have not the write format (%s)",i,self.f_ok)
      else:
        l_.append(i)
    return(l_)
    

class Scrolling:
  """Does a scrolling in a list of images"""
      
  def __init__(self,dir,xinit,yinit,xend,yend,ncropp,x_size,y_size):
    """Define the scrolling parametres"""
    self.dir=dir #Directory where images are.
    self.xi=xinit
    self.yi=yinit
    self.xe=xend
    self.ye=yend
    self.dir=LoadSerie(dir)
    self.ncropp=ncropp
    self.x_size=x_size
    self.y_size=y_size
    
  def calc_dn(self,n):
    """Define the path of the scrolling"""
    liste_image=self.dir.list_of_image()
    n_image=len(liste_image)
    if n>n_image:
      return(int(n/n_image))
    else:
      print("Number of display images greater then the number of initial images:%s",self.n_image)
   
  def calc_path(self,n_int,n):
    av=n/n_int
    x=self.xi+(self.xe-self.xi)*av
    y=self.yi+(self.ye-self.yi)*av
    return(x,y)
    
  def cropp_on_path(self):
    """Crop images from image in and write it down with a sequence name"""
    n_int=calc_dn(self.ncropp)
    liste_image=self.dir.list_of_image()
    n_image=len(liste_image)
    (x,y)=calc_path(n_int,0)
    i_im=0
    for n,i in enumerate(liste_image):
      if n%self.dn==0:
        i_im=i_im+1
        image = cv2.imread(i)
        cropped = image[x:y, x+self.x_size:x+self.y_size]
        (x,y)=calc_path(n)
        nom=i_im+".png"
        cv2.imwrite(nom,cropped)
    #cv2.imshow("cropped", cropped)
    #cv2.waitKey(0)
    #cv2.imwrite("../../cas/cas01/tmp.jpg",cropped)
