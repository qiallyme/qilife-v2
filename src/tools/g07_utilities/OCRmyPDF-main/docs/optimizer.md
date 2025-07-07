% SPDX-FileCopyrightText: 2022 James R. Barlow
% SPDX-License-Identifier: CC-BY-SA-4.0

# PDF optimization

OCRmyPDF includes an image-oriented PDF optimizer. By default, the
optimizer runs with safe settings with the goal of improving compression
at no loss of quality. At higher optimization levels, lossy
optimizations may be applied and tuned. Optimization occurs after OCR,
and only if OCR succeeded. It does not perform other possible
optimizations such as deduplicating resources, consolidating fonts,
simplifying vector drawings, or anything of that nature.

:::{list-table} OCRmyPDF optimization settings
---
widths: 33 6 60
header-rows: 1
---

* - Optimization level
  - Shorthand
  - Description
* - ``--optimize 0``
  - ``-O0``
  - Disable most optimizations.
* - ``--optimize 1`` (default)
  - ``-O1``
  - Enables lossless optimizations, such as transcoding images to more
      efficient formats. Also compress other uncompressed objects in the
      PDF and enables the more efficient "object streams" within the PDF.
      (If ``--jbig2-lossy`` is issued, then lossy JBIG2 optimization is used.
      The decision to use lossy JBIG2 is separate from standard optimization
      settings.)
* - ``--optimize 2``
  - ``-O2``
  - All of the above, and enables lossy optimizations and color quantization.
* - ``--optimize 3``
  - ``-O3``
  - All of the above, and enables more aggressive optimizations and targets lower
      image quality.
:::

The exact type of optimizations performed will vary over time, and
depend on what third party tools are installed.

Despite optimizations, OCRmyPDF might still increase the overall file
size, since it must embed information about the recognized text, and
depending on the settings chosen, may not be able to represent the
output file as compactly as the input file.

## Optimizations that always occurs

OCRmyPDF will automatically replace obsolete or inferior compression
schemes such as RLE or LZW with superior schemes such as Deflate, and
convert monochrome images to CCITT G4. Since this is lossless, it always
occurs and there is no way to disable it. Other non-image compressed
objects are compressed as well.

## Fast web view

OCRmyPDF automatically optimizes PDFs for \"fast web view\" in Adobe
Acrobat\'s parlance, or equivalently, linearizes PDFs so that the
resources they reference are presented in the order a viewer needs them
for sequential display. This reduces the latency of viewing a PDF both
online and from local storage, in exchange for a slight increase in file
size.

To disable this optimization and all others, use
`ocrmypdf --optimize 0 ...` or the shorthand `-O0`.

Adobe Acrobat might not report the file as being \"fast web view\".

## Lossless optimizations

At optimization level `-O1` (the default), OCRmyPDF will also attempt
lossless image optimization.

If a JBIG2 encoder is available, then monochrome images will be
converted to JBIG2, with the potential for huge savings on large black
and white images, since JBIG2 is far more efficient than any other
monochrome (bi-level) compression. (All known US patents related to
JBIG2 have probably expired, but it remains the responsibility of the
user to supply a JBIG2 encoder such as
[jbig2enc](https://github.com/agl/jbig2enc). OCRmyPDF does not implement
JBIG2 encoding on its own.)

OCRmyPDF currently does not attempt to recompress losslessly compressed
objects more aggressively.

## Lossy optimizations

At optimization level `-O1`, `-O2` and `-O3`, OCRmyPDF will some attempt
loss image optimization.

If Ghostscript is used to create a PDF/A (the default), Ghostscript will
optimize some images by converting them to JPEG, which are lossy. If
`--output-type pdf` is used, there are no lossy optimizations. Ghostscript's
JPEG conversion is quite safe.

If `pngquant` is installed, OCRmyPDF will use it to perform quantize
paletted images to reduce their size.

The quality of JPEGs may be lowered, on the assumption that a lower
quality image may be suitable for storage after OCR.

It is not possible to optimize all image types. Uncommon image types may
be skipped by the optimizer.

OCRmyPDF provides `lossy mode JBIG2 <jbig2-lossy>`{.interpreted-text
role="ref"} as an advanced feature that additional requires the argument
`--jbig2-lossy`.
