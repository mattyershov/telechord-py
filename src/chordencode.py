import scipy
import numpy as np

rate = 44100 # sample rate
duration = 0.3 # duration of tone in seconds
freq1 = 300
freq2 = 350
freq3 = 400
freq4 = 450
freq5 = 500
freq6 = 550
freq7 = 600
freq8 = 650

num_samples = max(1, int(rate * duration)) # ensures a non-empty function
t = np.linspace(0, num_samples / rate, num_samples, endpoint=False)

data = [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1] # length must be a multiple of 8
temp = []
split_data = [][]

count = 1
for i in range(0, len(data) / 8):
    temp.append(i)
    split_data.append(temp)



car1 = (np.sin(2 * np.pi * freq1 * t)).astype(np.float32)
car2 = (np.sin(2 * np.pi * freq2 * t)).astype(np.float32)
car3 = (np.sin(2 * np.pi * freq3 * t)).astype(np.float32)
car4 = (np.sin(2 * np.pi * freq4 * t)).astype(np.float32)
car5 = (np.sin(2 * np.pi * freq5 * t)).astype(np.float32)
car6 = (np.sin(2 * np.pi * freq6 * t)).astype(np.float32)

data = car1 + car2 + car3 + car4 + car5 + car6
scipy.io.wavfile.write("outputs/chord.wav", rate, data)