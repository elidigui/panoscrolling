
# import the necessary packages
import cv2
import PanoScrolling
import unittest as ut
import os
import hashlib

def hash_a_file(file):
  BS=65536
  #hasher=hashlib.md5()
  hasher=hashlib.sha1()
  with open(file,'rb') as afile:
    buf=afile.read(BS)
    while len(buf)>0:
      hasher.update(buf)
      buf = afile.read(BS)
  return(hasher.hexdigest())    

class TestLoadserie(ut.TestCase):
  """ Test  Lot's methods """
  def setUp(self):
      """ Set test up """
      self.cas = ".." + os.sep +".."+ os.sep +"cas"

  def test_cropped(self):
      """ load the image and show it"""
      chem=self.cas+ os.sep +"cas01"+ os.sep
      ima=chem+"socoro.jpg"
      crop=chem+"socoro_cropped.jpg"
      temp=chem+"tmp.jpg"
      image = cv2.imread(ima)
      cropped = image[70:170, 440:540]
      #cv2.imshow("cropped", cropped)
      #cv2.waitKey(0)
      cv2.imwrite(temp,cropped)
      a=hash_a_file(temp)
      b = hash_a_file(crop)
      self.assertEqual(a,b,"Crop is not the same")
    
# List of TestSuites:
suite1 = ut.TestLoader().loadTestsFromTestCase(TestLoadserie)
alltests = ut.TestSuite([suite1])

# Execution of tests:
for suite_ in alltests:
    ut.TextTestRunner(verbosity=2).run(suite_)

if __name__ == '__main__':
    ut.main()
