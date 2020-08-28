import requests
from bs4 import BeautifulSoup as Bs
import shutil
import os
from PIL import Image

img_list = []
fail = set()

def get_images(i):
	page = requests.get(f'https://pamskenya.com/?page={i}').text
	soup = Bs(page,'lxml')
	img = soup.find_all('img', class_='centered-image')
	for im in img:
		img_list.append((im["src"],im['alt']))

		if not os.path.exists('./images'):
			os.makedirs('./images')

		for img in img_list:
			url = img[0]
			name = str(img[1]).strip()
			
			
			
			if not os.path.exists(f'./images/{name}.jpg'):
				print("getting file")
				response = requests.get(url, stream=True)
				try:
					with open(f'./images/{name}.jpg', 'wb') as out_file:
						print("writing to file")
						shutil.copyfileobj(response.raw, out_file)
						del response
						print("writing Done")

				except :
					fail.add(name)
					print(fail)
					pass


def resize_all():

	if not os.path.exists('./images/resized'):
			os.makedirs('./images/resized')

	for r,d,file in os.walk('./images'):
		for f in file:
			name = f.split('.')[0]

			if not os.path.exists(f'./images/resized/{name}_resized.jpg'):
				image = Image.open(f'./images/{f}')

				if not image.mode == 'RGB':
					new_image = image.convert('RGB')

				try:
					new_image = image.resize((600, 600))
					new_image.save(f'./images/resized/{name}_resized.jpg')

				except:
					print(name)
					pass

#resize_all()

'''i = 1
while i<3:
	get_images(i)
	i += 1'''
	