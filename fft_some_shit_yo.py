import scipy.io.wavfile as wavio
import numpy.fft as nfft
import numpy
import matplotlib.pyplot as plt


discontinuity_eval()


def fft_that_file():
    poop, samples = wavio.read('/home/carl/Downloads/audiocheck.net_sin_1000Hz_-3dBFS_3s.wav')
    length = len(samples)
    t = numpy.arange(0, (length/poop), (1/poop))
    kitty = nfft.fft(samples)
    frek = nfft.fftfreq(t.shape[-1], 1/poop)
    plt.plot(frek, kitty.real)
    plt.show()


def discontinuity_eval():
    # 1 cycle, 1kHz
    fundamental = 1000
    resolution = 100
    phase_shift = 0
    sample_rate = fundamental*resolution
    t = numpy.arange(0,1/fundamental, 1/sample_rate)
    wave = numpy.sin(2*numpy.pi*fundamental*t + phase_shift)
    kitty = nfft.fft(wave)
    freqs = nfft.fftfreq(t.shape[-1], 1/sample_rate)
    plt.plot(t, wave)
    plt.plot(freqs, kitty)
    plt.show()
