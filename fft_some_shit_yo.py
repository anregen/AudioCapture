import scipy.io.wavfile as wavio
import numpy.fft as nfft
import numpy
import matplotlib.pyplot as plt

poop, samples = wavio.read('/home/carl/Downloads/audiocheck.net_sin_1000Hz_-3dBFS_3s.wav')
length = len(samples)
t = numpy.arange(0, (length/poop), (1/poop))
kitty = nfft.fft(samples)
frek = nfft.fftfreq(t.shape[-1], 1/poop)

plt.plot(frek, kitty.real)
plt.show()
