"""

WebcamBeam - Kamil Krawczyk, 2016
Determines size of beam on CMOS detector (webcam).

"""

import numpy as np
from PIL import Image

if len.sys.argv == 2:
    filename = sys.argv[1]
else:
    print('Usage: python main.py <filename in directory>')

# open the image and place into array
webcamImg = Image.open(filename)
webcamArr = np.array(webcamImg)



