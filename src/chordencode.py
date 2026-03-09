import scipy
import numpy as np

# Old hardcoded frequencies
# freq1:float=300,
# freq2:float=350,
# freq3:float=350,
# freq4:float=400,
# freq5:float=450,
# freq6:float=500,
# freq7:float=550,
# freq8:float=600

data = [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1] # length must be a multiple of 8, otherwise data will be cut off

def format_data(data:list):
    temp = []
    data_split = []
    
    if (len(data) % 8 != 0):
        print("WARNING: Length of binary data is not a multiple of 8! Data will be cut off!")
    for i in range(0, len(data) // 8):
        for j in range(8 * i, 8 * i + 8):
            temp.append(data[j])
        data_split.append(temp)
        temp = []
    print(data_split)
    return data_split

def encode_chord(data:list, spacing:int, start_af:int=300, rate:int=44100, duration:float=0.3):
    num_samples = max(1, int(rate * duration)) # ensures a non-empty function
    t = np.linspace(0, num_samples / rate, num_samples, endpoint=False)

    car1 = (np.sin(2 * np.pi * (start_af + spacing*1) * t)).astype(np.float32)
    car2 = (np.sin(2 * np.pi * (start_af + spacing*2) * t)).astype(np.float32)
    car3 = (np.sin(2 * np.pi * (start_af + spacing*3) * t)).astype(np.float32)
    car4 = (np.sin(2 * np.pi * (start_af + spacing*4) * t)).astype(np.float32)
    car5 = (np.sin(2 * np.pi * (start_af + spacing*5) * t)).astype(np.float32)
    car6 = (np.sin(2 * np.pi * (start_af + spacing*6) * t)).astype(np.float32)
    car7 = (np.sin(2 * np.pi * (start_af + spacing*7) * t)).astype(np.float32)
    car8 = (np.sin(2 * np.pi * (start_af + spacing*8) * t)).astype(np.float32)

    data = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8
    scipy.io.wavfile.write("outputs/chord.wav", rate, data)

def main():
    format_data(data)

if __name__=="__main__":
    main()