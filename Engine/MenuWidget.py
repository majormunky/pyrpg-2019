from __future__ import absolute_import
import pygame
from Engine.Text import text_surface

class MenuWidget:
	def __init__(self, list_items, x, y, text_color=(0, 0, 0), disabled_color=(200, 200, 200), font_size=40):
		self.x = x
		self.y = y
		self.font_size = font_size
		self.list_items = list_items
		self.disabled_items = []
		self.item_images = {}
		self.current_item = 0
		self.text_color = text_color
		self.disabled_color = disabled_color
		self.menu_height = 0
		self.title = None
		self.render_images()

	def disable_item(self, menu_name):
		if menu_name in self.list_items:
			self.disabled_items.append(menu_name)
		self.render_images()

	def set_title(self, text):
		self.title = text_surface(text, font_size=self.font_size, color=self.text_color)

	def render_images(self):
		for item in self.list_items:
			if item in self.disabled_items:
				color = self.disabled_color
			else:
				color = self.text_color
			self.item_images[item] = text_surface(item, self.font_size, color)

	def handle_key(self, key):
		new_item = int(self.current_item)
		if key == pygame.K_UP:
			if self.current_item == 0:
				new_item = len(self.list_items) - 1
			else:
				new_item -= 1
		elif key == pygame.K_DOWN:
			if self.current_item == len(self.list_items) - 1:
				new_item = 0
			else:
				new_item += 1
		if new_item != self.current_item:
			if self.list_items[new_item] not in self.disabled_items:
				self.current_item = new_item

	def get_current_item(self):
		return self.list_items[self.current_item]

	def get_current_index(self):
		return self.current_item

	def draw(self, canvas):
		base_y = self.y
		if self.title:
			canvas.blit(self.title, (self.x, base_y))
			base_y += self.title.get_rect().height
		for index, item in enumerate(self.list_items):
			canvas.blit(self.item_images[item], (self.x, base_y))
			if self.current_item == index:
				pygame.draw.rect(canvas, self.text_color, (self.x - 20, base_y + 5, 10, 10))
			base_y += self.item_images[item].get_height()