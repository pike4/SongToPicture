# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 16:27:13 2015

@author: Definitely not Continuum
"""

import sys
import os
import traceback
import optparse
import time
import logging


def returnRGB(val):

    '''This converts a given wavelength of light to an 
    approximate RGB color value. The wavelength must be given
    in nanometers in the range from 380 nm through 750 nm
    (789 THz through 400 THz).

    Based on code by Dan Bruton
    http://www.physics.sfasu.edu/astro/color/spectra.html
    '''
    if(val > 0 and val < 1):
        wavelength = 380 + val * 370
    else:
        wavelength = 0
        
    gamma = 0.8


    wavelength = float(wavelength)
    if wavelength >= 380 and wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        G = 0.0
        B = (1.0 * attenuation) ** gamma
    elif wavelength >= 440 and wavelength <= 490:
        R = 0.0
        G = ((wavelength - 440) / (490 - 440)) ** gamma
        B = 1.0
    elif wavelength >= 490 and wavelength <= 510:
        R = 0.0
        G = 1.0
        B = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif wavelength >= 510 and wavelength <= 580:
        R = ((wavelength - 510) / (580 - 510)) ** gamma
        G = 1.0
        B = 0.0
    elif wavelength >= 580 and wavelength <= 645:
        R = 1.0
        G = (-(wavelength - 645) / (645 - 580)) ** gamma
        B = 0.0
    elif wavelength >= 645 and wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        R = (1.0 * attenuation) ** gamma
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0
    R *= 255
    G *= 255
    B *= 255
    return (int(R), int(G), int(B))


def main(options=None, args=None):

#    import ppm_dump
#    import png_canvas
    import canvas
    if options.ppm:
        canvas = canvas.ppm_canvas(371, 278)
        canvas.is_ascii = True
    else:
        canvas = canvas.png_canvas(371, 278)
    for wl in range(380, 751):
        r, g, b = wavelength_to_rgb(wl)
        for yy in range(0, 278):
            canvas.pixel(wl - 380, yy, r, g, b)
    sys.stdout.write(str(canvas))

if __name__ == '__main__':
    try:
        start_time = time.time()
        parser = optparse.OptionParser(
            formatter=optparse.TitledHelpFormatter(),
            usage=globals()['__doc__'],
            version='1'
        )
        parser.add_option(
            '-v', '--verbose', action='store_true',
            default=False, help='verbose output'
        )
        parser.add_option(
            '--png', action='store_true',
            default=True, help='Output as PNG.'
        )
        parser.add_option(
            '--ppm', action='store_true',
            default=False, help='Output as PPM ASCII (Portable Pixmap).'
        )
        (options, args) = parser.parse_args()
        #if len(args) < 1:
        #    parser.error ('missing argument')
        if options.verbose:
            print(time.asctime())
        exit_code = main(options, args)
        if exit_code is None:
            exit_code = 0
        if options.verbose:
            print(time.asctime())
            print('TOTAL TIME IN MINUTES: %f'
                  % ((time.time() - start_time) / 60.0))
        sys.exit(exit_code)
    except KeyboardInterrupt as e:  # The user pressed Ctrl-C.
        raise e
    except SystemExit as e:  # The script called sys.exit() somewhere.
        raise e
    except Exception as e:
        print('ERROR: Unexpected Exception')
        print(str(e))
        traceback.print_exc()
        os._exit(2)