import requests

def download(url):
	response = requests.get(url, stream=True)
	try:
		with open('video.mp4', 'wb') as out_file:
			print("writing to file")
			shutil.copyfileobj(response.raw, out_file)
			del response
			print("Downloaded")

	except:
		print("Failed")
download('https://drive.google.com/file/d/1hSu3z818ra45tjsmN1mf2tDqF1m_kt3D/view?usp=sharing')