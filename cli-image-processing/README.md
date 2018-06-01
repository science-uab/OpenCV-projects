# CLI Image processing app
## Author: Olariu Lucian

MIT License

This app reads all the images from a folder and applies 3 basic OpenCV operations on them. resize, grayscale and canny edge detection. It watches the image folder for new images and processes them also
The app also communicates with an esp that has been configured as a web server to indicate via two LED's when a job is in progress or when it is done.
   
### Installation instructions

Make sure you have installed python, opencv and virtualenv

1. Create a virtual environment using python `virtualenv` and `activate` it
    ```bash
    $ virtualenv --python=python3.6 --no-site-packages venv
    $ source venv/bin/activate
    ```

2. Install package dependencies
    ```bash
    pip install -r requirements.txt
    ```

3. Run the app
    ```bash
    python app.py
    ```

4. Enjoy

## Screenshots
1. App CLI output that is waiting for images
[CLI-output](https://i.imgur.com/xqHINjR.png)
<img src="https://i.imgur.com/xqHINjR.png">
2. Processing images output
[Processed](https://i.imgur.com/thY9Cnp.png)
<img src="https://i.imgur.com/thY9Cnp.png">
3. Resize
    1. Resized
        [Image](https://i.imgur.com/FoA6dHX.png)
        <img src="https://i.imgur.com/FoA6dHX.png">
    2. Original
        [Image](https://i.imgur.com/qSvIaTN.png)
        <img src="https://i.imgur.com/qSvIaTN.png">

4. Grayscale
[Grayscale](https://i.imgur.com/iC7UyOf.png)
<img src="https://i.imgur.com/iC7UyOf.png">

5. Canny edge detection
[Canny](https://i.imgur.com/OXjVfeg.png)
<img src="https://i.imgur.com/OXjVfeg.png">
