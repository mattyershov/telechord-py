import scipy
import scipy.fft
import numpy as np
from pydub import AudioSegment
from pydub.utils import make_chunks

def main():
    sample_rate = 44100

    _, input = scipy.io.wavfile.read("outputs/dualsine.wav")
    input_seg = AudioSegment.from_file("outputs/dualsine.wav", format="wav")
    chunks = make_chunks(input_seg, 300) #time in ms

    for i, chunk in enumerate(chunks):
        chunk.export(f"outputs/chunk{i}.wav", format="wav")
        
    N = len(input)
    window = scipy.signal.windows.hann(N)
    fft = np.fft.rfft(input * window)
    freqs = np.fft.rfftfreq(N, 1/sample_rate)

    mag = np.abs(fft) # magnitudes of bins

    # freq ranges
    f_min1 = 300
    f_max1 = 325
    f_min2 = 350
    f_max2 = 375
    f_min3 = 400
    f_max3 = 425
    f_min4 = 450
    f_max4 = 475
    f_min5 = 500
    f_max5 = 525
    f_min6 = 550
    f_max6 = 575

    # find indices in range
    idx1 = np.where((freqs >= f_min1) & (freqs <= f_max1))[0]
    idx2 = np.where((freqs >= f_min2) & (freqs <= f_max2))[0]
    idx3 = np.where((freqs >= f_min3) & (freqs <= f_max3))[0]
    idx4 = np.where((freqs >= f_min4) & (freqs <= f_max4))[0]
    idx5 = np.where((freqs >= f_min5) & (freqs <= f_max5))[0]
    idx6 = np.where((freqs >= f_min6) & (freqs <= f_max6))[0]

    # dominant frequency in range
    peak_idx1 = idx1[np.argmax(mag[idx1])]
    peak_idx2 = idx2[np.argmax(mag[idx2])]
    peak_idx3 = idx3[np.argmax(mag[idx3])]
    peak_idx4 = idx4[np.argmax(mag[idx4])]
    peak_idx5 = idx5[np.argmax(mag[idx5])]
    peak_idx6 = idx6[np.argmax(mag[idx6])]

    detected_freq1 = freqs[peak_idx1]
    detected_freq2 = freqs[peak_idx2]
    detected_freq3 = freqs[peak_idx3]
    detected_freq4 = freqs[peak_idx4]
    detected_freq5 = freqs[peak_idx5]
    detected_freq6 = freqs[peak_idx6]

    # actual values for each freq (frequency that each detected freq is above its range's minimum, all divided by 2 to eliminate amplified changes)
    val1 = (detected_freq1 - f_min1)/2
    val2 = (detected_freq1 - f_min2)/2
    val3 = (detected_freq1 - f_min3)/2
    val4 = (detected_freq1 - f_min4)/2
    val5 = (detected_freq1 - f_min5)/2
    val6 = (detected_freq1 - f_min6)/2

    print(f"Detected frequencies:\n{detected_freq1:.0f}\n{detected_freq2:.0f}\n{detected_freq3:.0f}\n{detected_freq4:.0f}\n{detected_freq5:.0f}\n{detected_freq6:.0f}")

if __name__ == "__main__":
    main()