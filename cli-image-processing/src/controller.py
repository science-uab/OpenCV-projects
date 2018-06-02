import os
import settings
import cv2
import time
import requests


class App:

    original_images = []
    processed_images =[]
    original_images_paths = []
    cv_images = []
    resized_images = []
    grayscale_image = []
    canny_edge_detection = []

    def __init__(self):
        settings.load_env()
        print("CLI image processing app started. Awating images...")

    def run(self):
        self.original_images = self.get_original_images()
        self.get_processed()
        self.make_request(os.getenv("GREEN_LED"))
        if self.compute_diff():
            self.compute_abs_path_to_original_images()
            self.cv_read_images()
            self.cv_process_and_write_resize()
            self.cv_process_and_write_grayscale()
            self.cv_process_and_write_canny()
            self.write_processed()
            self.make_request(os.getenv("GREEN_LED"))

    def write_processed(self):
        path_to_processed_manifest = os.getenv("PROCESSED_IMAGES_MANIFEST")
        stream = open(path_to_processed_manifest, 'a')
        if self.original_images:
            for image in self.original_images:
                stream.write(image + ", ")
                print ("Image {} was processed successfully".format(image))
        stream.close()

    def get_processed(self):
        path_to_processed_manifest = os.getenv("PROCESSED_IMAGES_MANIFEST")
        stream = open(path_to_processed_manifest, 'r')
        data = stream.read().split(", ")
        self.processed_images = data

    def compute_diff(self):
        diff = list(filter(lambda x: x not in self.processed_images, self.original_images))
        if len(diff) > 0:
            self.make_request(os.getenv("YELLOW_LED"))
            self.original_images = diff
            for image in self.original_images:
                print("Image {} was found. Proceeding...".format(image))
                time.sleep(0.5)
                print("Stand by. Working ...")
                time.sleep(0.5)
            return True
        else:
            print("Awaiting new images to be processed...")
        return False

    def get_path_to_dir(self, env_path_var):
        abs_path = os.path.abspath(env_path_var)

        if not abs_path:
            raise FileNotFoundError

        return abs_path

    def get_original_images(self):
        self.original_images = os.listdir(self.get_path_to_dir(os.getenv("ORIGINAL_IMAGES_DIR")))
        if not self.original_images:
            print("There are no images to be processed")

        return self.original_images

    def compute_abs_path_to_original_images(self):
        if self.original_images:
            abs_path_to_original_images_folder = self.get_path_to_dir(os.getenv("ORIGINAL_IMAGES_DIR"))
            for image in self.original_images:
                self.original_images_paths.append(abs_path_to_original_images_folder + '/' + image)

    def cv_read_images(self):
        if self.original_images_paths:
            for image in self.original_images_paths:
                self.cv_images.append(cv2.imread(image, 1))

    def cv_process_and_write_resize(self):
        if self.cv_images:
            for image in self.cv_images:
                self.resized_images.append(cv2.resize(image, (int(os.getenv("WIDTH")), int(os.getenv("HEIGHT")))))

        if self.resized_images:
            i = 0
            for image in self.resized_images:
                write_name = os.getenv("PROCESSED_RESIZED_IMAGE_DIR") + "/_resized_" + self.original_images[i]
                cv2.imwrite(write_name, image)
                i += 1
                if i == len(self.original_images):
                    break

    def cv_process_and_write_grayscale(self):
        if self.cv_images:
            for image in self.cv_images:
                self.grayscale_image.append(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))

        if self.grayscale_image:
            i = 0
            for image in self.grayscale_image:
                write_name = os.getenv("PROCESSED_GRAYSCALE_IMAGE_DIR") + "/_grayscale_" + self.original_images[i]
                cv2.imwrite(write_name, image)
                i += 1
                if i == len(self.original_images):
                    break

    def cv_process_and_write_canny(self):
        if self.cv_images:
            for image in self.cv_images:
                self.canny_edge_detection.append(cv2.Canny(image, int(os.getenv("CANNY_MIN_VAL")), int(os.getenv("CANNY_MAX_VAL"))))

        if self.canny_edge_detection:
            i = 0
            for image in self.canny_edge_detection:
                write_name = os.getenv("PROCESSED_CANNY_EDGE_DETECTION_IMAGE_DIR") + "/_canny_" + self.original_images[i]
                cv2.imwrite(write_name, image)
                i += 1
                if i == len(self.original_images):
                    break

    def make_request(self, route):
        indicator_ip = os.getenv("INDICATOR_IP")
        full_route = "http://{}/{}".format(indicator_ip, route)
        requests.get(full_route)
