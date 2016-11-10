# peaknormalise

A Python script to help you batch-normalise your audio files.

Say you have a bunch of audio files in a folder, and what you'd like to do is to
normalise the files in a way that preserves the relative volume differences
_within_ those files. That's where this script comes in!

## Requirements

[Sox](http://sox.sourceforge.net) is required and should be available on your
`PATH`. If you installed sox from Homebrew on a Mac, you should be all set.

## Usage

    ./normalise.py <peak dbFS level> [files]

e.g.

    ./normalise.py -1 ~/audio/*.aif

