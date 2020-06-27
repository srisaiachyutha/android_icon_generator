import sys
import os
from  PIL import Image
from datetime import datetime
def create_image(path, image , folder, size):
	new_image = image.resize(size)
	path = os.path.join(path,folder)
	os.mkdir(path)
	os.chdir(folder)
	new_image.save('ic_launcher.png')
	os.chdir('..')

def help(image_path):
	try:
		timestamp = None
		if image_path.endswith('.png'):
			image = Image.open(image_path)
		else:
			timestamp = datetime.timestamp(datetime.now())
			image = Image.open(image_path)
			image.save(str(timestamp)+'.png')
			image = Image.open(str(timestamp)+'.png')

	except Exception as e:
		print('#############################################################')
		print('#                                                           #')
		print('#   The image you have given may not be present in that     #')
		print('#   exact location  or file that not exists.                #')
		print('#                                                           #')
		print('#############################################################')
		exit()
	current_directory = os.getcwd()

	dir_name = 'android_launcher_images'
	path = os.path.join(current_directory,dir_name)
	os.mkdir(path)
	os.chdir(dir_name)
		
	create_image(path,image,'mipmap-hdpi',(72,72))
	create_image(path,image,'mipmap-mdpi',(48,48))
	create_image(path,image,'mipmap-xhdpi',(96,96))
	create_image(path,image,'mipmap-xxhdpi',(144,144))
	create_image(path,image,'mipmap-xxxhdpi',(192,192))

	os.chdir('..')
	if timestamp:
		os.remove(str(timestamp)+'.png')
	print('#############################################################')
	print('#                                                           #')
	print('#   Successfully created the images in                      #')
	print('#   Directory :   android_launcher_images                   #')
	print('#                                                           #')
	print('#############################################################')
	exit()

def main():
	if len(sys.argv)<2:
		print('#############################################################')
		print('#                                                           #')
		print('#   Please send the image path as an file argument to       #')
		print('#   create the images for it.                               #')
		print('#                                                           #')
		print('#############################################################')
		exit()
	else:
		help(sys.argv[1])



if __name__ == '__main__':
	main()
