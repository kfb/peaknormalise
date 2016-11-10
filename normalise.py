#!/usr/bin/env python

"""Batch normalise audio files.

Requires `sox` from http://sox.sourceforge.net/sox.html.
"""

import os
import subprocess
import sys
import tempfile

from peaknormalise.log import log


def apply_gain(file, gain):
    """Apply a gain of `gain` dB to `file`."""
    log.info('Applying gain of %f to %s', gain, file)

    with tempfile.NamedTemporaryFile(delete=False, suffix='.aif') as tf:
        log.debug('Created temp file %s', tf.name)

        subprocess.check_output(
            ['sox', '-V3', '{}'.format(file), tf.name, 'gain', str(gain)],
            stderr=subprocess.STDOUT,
        )

        os.remove(file)
        os.rename(tf.name, file)


def peak_level(file):
    """Return the peak level of `file`."""
    log.info('Analysing %s...', file)
    output = subprocess.check_output(
        ['sox', file, '-n', 'stats'],
        stderr=subprocess.STDOUT,
    )

    # We know the peak level will be the fifth line
    line = output.split('\n')[4]

    # The overall peak is the second column
    overall_peak = float(line.split()[3])
    log.debug('Overall peak is %f', overall_peak)

    return overall_peak


if __name__ == '__main__':
    target = float(sys.argv[1])
    peaks = {}
    for f in sys.argv[2:]:
        try:
            peaks[os.path.abspath(f)] = peak_level(os.path.abspath(f))
        except subprocess.CalledProcessError:
            log.warning('Couldn\'t open %s', os.path.abspath(f))

    gain = target - max(peaks.values())

    for f in sys.argv[2:]:
        try:
            apply_gain(os.path.abspath(f), gain)
        except subprocess.CalledProcessError as e:
            log.warning('Couldn\'t open %s', os.path.abspath(f))
            log.exception(e)
