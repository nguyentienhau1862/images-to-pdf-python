from os import listdir, path, makedirs
from PIL import Image

def load_image(image_path = ""):
	try:
		image_size = (1970, 2786)
		return Image.open(image_path).convert("RGB").resize(image_size, Image.Resampling.LANCZOS)
	except:
		print("Error When Open Image:", image_path, KeyError, NameError)

def save_images_pdf(images = [], pdf_path = ""):
	try:
		if len(images) > 0:
			images[0].save(pdf_path, "PDF", bitmap_format="png", save_all=True, optimize=True, append_images=images[1:])
	except:
		print("Error When Merge Images To PDF", pdf_path, KeyError, NameError)

def is_image_file(image_path = ""):
	image_extensions = (".png", ".jpeg", ".jpg", ".bmp", ".webp", ".tiff", ".gif", ".rgb", ".pbm", ".pgm", ".ppm", ".rast", ".xbm", ".exr")
	return path.isfile(image_path) and image_path.lower().endswith(image_extensions)

if __name__ == "__main__":
	comics_dir = "D:/Privates"
	pdf_comics_dir = "D:/Downloads"

	if not path.isdir(comics_dir):
		makedirs(comics_dir)

	if not path.isdir(pdf_comics_dir):
		makedirs(pdf_comics_dir)

	for comic_name in listdir(comics_dir):
		comic_dir = path.join(comics_dir, comic_name)

		if path.isdir(comic_dir):
			print("Create Comic:", comic_name)

			pdf_path = path.join(pdf_comics_dir, comic_name + ".pdf")
			images = []

			for image_name in listdir(comic_dir):
				image_path = path.join(comic_dir, image_name)

				if is_image_file(image_path):
					images.append(load_image(image_path))
			
			save_images_pdf(images, pdf_path)

			print("Finish")
