import pygame
import os

assets = {}
asset_path = ['images']

def set_base_folder(path):
	global asset_path
	asset_path = path.split("/")

def base_folder():
	return os.path.join(*asset_path)

def load_images(image_list):
	for i in image_list:
		load_image(i)

def load_image(image_name):
	image_key = os.path.splitext(os.path.split(image_name)[-1])[0]
	if image_key in assets.keys():
		return assets[image_key]
	
	base_path = base_folder()
	image = pygame.image.load(os.path.join(base_path, image_name)).convert_alpha()

	if image:
		assets[image_key] = image
		return image
	else:
		return False

def get_image(image_name):
	if image_name in assets.keys():
		return assets[image_name]
	return False