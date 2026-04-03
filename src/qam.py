import numpy as np
import scipy
import sounddevice as sd


def qam16_format(data:int):
    chunks = []
    iq_values = []
    data = str(data)
    chunks = [data[i:i+4] for i in range(0, len(data), 4)]
    print(chunks)
    for i in chunks:
        I = int(i[0:2], 2)
        Q = int(i[2:4], 2)
        print(I, Q)
        iq_values.append((I, Q))
    return iq_values


def encode(iq_values:list, carr_af:int=300, rate:int=44100, duration:float=0.2):
    
    full_wave = []
    num_samples = max(1, int(rate * duration)) # ensures a non-empty function
    t = np.linspace(0, num_samples / rate, num_samples, endpoint=False)
    seq = []

    # iq = qam16_format(1010010111110110)

    for i in iq_values:
        I = i[0]
        Q = i[1]
        iq_wave = I * np.sin(2 * np.pi * carr_af * t) + Q * np.cos(2 * np.pi * carr_af * t)
        full_wave.append(iq_wave)

    cont_wave = np.concatenate(full_wave).astype(np.float32)
    sd.play(cont_wave, rate, blocking=True)
    scipy.io.wavfile.write("outputs/qam.wav", rate, cont_wave)

def main():
    data = 1010010111110110
    encode(qam16_format(data))

if __name__ == "__main__":
    main()