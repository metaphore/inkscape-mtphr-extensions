#!/usr/bin/env python

import coloreffect
import inkex
import mtphr_commons

class C(coloreffect.ColorEffect):
    def __init__(self):
        coloreffect.ColorEffect.__init__(self)		
        self.OptionParser.add_option("-n", "--nhue",
            action="store", type="int",
            dest="n", default=0,
		    help="Hue")
        self.OptionParser.add_option("-l", "--lightness",
            action="store", type="float",
            dest="l", default=1.0,
		    help="Lightness")
        self.OptionParser.add_option("-s", "--saturation",
            action="store", type="float",
            dest="s", default=1.0,
		    help="Saturiation")

    def colmod(self, r, g, b):
        hls = mtphr_commons.rgb_to_hls(r, g, b)
        h = hls[0] + self.options.n
        if h < 0:
            h = h + 255
        if h > 255:
            h = h - 255
        l = max(0.0, min(hls[1] * self.options.l, 255))
        s = max(0.0, min(hls[2] * self.options.s, 255))
        
        rgb = mtphr_commons.hls_to_rgb (h, l, s)
		
        return '%02x%02x%02x' % (rgb[0], rgb[1], rgb[2])

	
c = C()
c.affect()