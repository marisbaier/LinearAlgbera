#!/bin/bash
manim-slides convert Intro chapter1.html
manim-slides convert CoordinatesAsScalars CoordinatesAsScalarsExample WhatIfWeChoseADifferentBasis ShowVaryingLinearCombinations NameLinearCombinations LinearCombinationsWithSumCopies UnluckyCase EvenMoreUnluckyCase chapter2.html

scp -r *.html chapter*_assets/ pool:public_html/
