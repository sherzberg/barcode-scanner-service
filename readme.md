Barcode Scanner Service
=======================

This is a simple web service that will take a posted image and 
return some json with barcode information if it can find any.

This webservice uses Flask, Pillow, and [ZBar](http://zbar.sourceforge.net/).

Usage
-----

```bash
$ curl -F file=@/full/path/to/barcode.png barcode-scanner.herokuapp.com/image
