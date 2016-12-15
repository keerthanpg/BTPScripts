import os
from PIL import Image

yourpath = 'C:\Users\KEERTHANA\Desktop\jaffe'
for root, dirs, files in os.walk(yourpath, topdown=False):
    for name in files:        
        print(os.path.join(root, name))
        if os.path.splitext(os.path.join(root, name))[1].lower() == ".tiff":
            if os.path.isfile(os.path.splitext(os.path.join(root, name))[0] + ".jpg"):
                print "A jpeg file already exists for %s" % name
            
            # If a jpeg is *NOT* present, create one from the tiff.
            else:
                #Image.open('old.jpeg').convert('RGB').save('new.jpeg')
                outfile = os.path.splitext(os.path.join(root, name))[0] + ".jpg"
                try:
                    im = Image.open(os.path.join(root, name))
                    if im.mode == 'P':
                        im.convert('RGB')
                    print "Generating jpeg for %s" % name
                    im.thumbnail(im.size)
                    im.save(outfile, "JPEG", quality=100)
                except Exception, e:
                    print e


                    
    
