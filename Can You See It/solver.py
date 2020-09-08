import imageio
import numpy as np
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

VIDEO = 'Can_You_See_It.mp4'


def read_video():
	print('Processing video')
	vid = imageio.get_reader(VIDEO, 'ffmpeg')
	frames_count = vid.count_frames()
	data = np.zeros(frames_count)
	for i in range(frames_count):
		frame = vid.get_data(i)
		frame = rgb2gray(frame)
		data[i] = frame.min()

		p = 100 * (i + 1) / frames_count
		print(f'\rProgress: {p: 0.2f}%', end='', flush=True)
	return data


def main():
	data = read_video()
	img = np.reshape(data, [317, 1438])
	plt.imshow(img, cmap='gray')
	plt.show()


if __name__ == '__main__':
	main()
