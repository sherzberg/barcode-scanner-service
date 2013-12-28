from sys import argv
import zbar
from PIL import Image

import logging

logger = logging.getLogger(__file__)


def scan_image(image_fh):
    # create a reader
    scanner = zbar.ImageScanner()

    # configure the reader
    scanner.parse_config('enable')

    # obtain image data
    pil = Image.open(image_fh).convert('L')
    width, height = pil.size
    raw = pil.tostring()

    # wrap image data
    image = zbar.Image(width, height, 'Y800', raw)

    # scan the image for barcodes
    scanner.scan(image)

    barcodes = []
    # extract results
    for symbol in image:
        # do something useful with results
        barcode = {'type': str(symbol.type), 'symbol': symbol.data}
        barcodes.append(barcode)
        logger.debug(barcode)

    # clean up
    del(image)

    return {'total': len(barcodes), 'barcodes': barcodes}


if __name__ == '__main__':
    with open(argv[1]) as fh:
        result = scan_image(fh)
        print result
