import numpy as np
import scipy.signal as signal
import soundfile as sf

# Carregar arquivo de áudio
def load_audio(file_path):
    audio_data, sample_rate = sf.read(file_path)
    return audio_data, sample_rate

# Função para salvar arquivo de áudio
def save_audio(file_path, audio_data, sample_rate):
    sf.write(file_path, audio_data, sample_rate)

# Converter sinal estéreo em mono
def stereo_to_mono(signal):
    if signal.ndim == 2:
        return np.mean(signal, axis=1)
    else:
        return signal

# Realizar a convolução de dois sinais de áudio
def convolve_audio(signal1, signal2):
    return signal.convolve(signal1, signal2, mode='full')

# Carregar os sinais de áudio
audio_signal1, sample_rate1 = load_audio('Church Schellingwoude.wav')
audio_signal2, sample_rate2 = load_audio('audiovoz.wav')

# Converter os sinais estéreo em mono
audio_signal1 = stereo_to_mono(audio_signal1)
audio_signal2 = stereo_to_mono(audio_signal2)

# Verificar se os sinais têm a mesma taxa de amostragem
if sample_rate1 != sample_rate2:
    raise ValueError("Os sinais de áudio devem ter a mesma taxa de amostragem.")

# Realizar a convolução dos sinais de áudio
convolved_signal = convolve_audio(audio_signal1, audio_signal2)

# Salvar o sinal convolvido em um novo arquivo
save_audio('convolved_audio.wav', convolved_signal, sample_rate1)

print("Convolução concluída.")