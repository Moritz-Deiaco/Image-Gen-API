# Image Generation API 🖼️

The Image Generation API is a powerful tool that allows you to effortlessly create stunning images by simply using a simple JSON syntax. With this API, you can generate various shapes like rectangles, ellipses, and polygons, as well as add customizable text to your images. It's designed to provide a seamless and intuitive image generation experience.

## Features ✅

### 1. Shape Generation 🔳🔵🔺

The API offers support for creating different shapes, including:

- Rectangles: Design and customize rectangles with specific dimensions and colors. 🟨🔳🎨
- Ellipses: Generate ellipses with adjustable parameters like width, height, and fill color. 🟩🔵🔸
- Polygons: Create polygons of varying sides and styles, adding uniqueness to your images. 🟧🔺🔹
- Text: Write on your image with 3 diffrent font styles and change the text, with your code. 📑
- Images: Paste your favorite images and change them easily with your code. 🖼️

### 2. Text Integration 🆎📝

Easily incorporate text into your generated images. You can dynamically modify the content of the text using the HTTP ID provided in the JSON file. This feature enables you to personalize each image, making it ideal for personalized messages or dynamic content generation. 🆒💬💭

### 3. Simple JSON Syntax 🧾🤖

The Image Generation API is designed for ease of use. By utilizing a straightforward JSON syntax, you can effortlessly define the attributes of shapes and text elements, making image generation a breeze, even for those new to the API. 🧩📄🤝

## How to Use 🛠️

To generate an image, simply construct a JSON file with the desired specifications for shapes and text elements. Then, submit your JSON request to the API endpoint, and it will return the corresponding image based on your specifications.

Here's an example of the JSON syntax:

```json
{
  "size": {
    "width": 2000,
    "height": 2000
  },
  "background-color": {
    "R": 0,
    "G": 0,
    "B": 0
  },
  "geometry": {
    "rect_0": {
      "x": 10,
      "y": 10,
      "width": 40,
      "height": 40,
      "color": {
        "r": 255,
        "g": 100,
        "b": 0
      }
    },
    "rect_1": {
      "x": 5,
      "y": 5,
      "width": 40,
      "height": 40,
      "color": {
        "r": 255,
        "g": 100,
        "b": 0
      }
    },
    "ellipse": {
      "x": 200,
      "y": 100,
      "width": 400,
      "height": 400,
      "color": {
        "r": 0,
        "g": 255,
        "b": 0
      }
    },
    "polygon": {
      "x": 200,
      "y": 100,
      "radius": 200,
      "sites": 8,
      "rotation": 90,
      "color": {
        "r": 0,
        "g": 100,
        "b": 0
      }
    },
    "text": {
      "x": 200,
      "y": 100,
      "size": 40,
      "text": "jklsajflksdjf",
      "words_per_line": 20,
      "httpid": "text_1",
      "align": "right",
      "color": {
        "r": 255,
        "g": 255,
        "b": 255
      },
      "font_style": "monospace"
    },
    "image": {
      "httpid": "image_1",
      "image_url": "https://picsum.photos/200/300",
      "width": 200,
      "height": 300,
      "x": 10,
      "y": 10,
      "transparent": false
    }
  }
}
```

## Get Started 🚀

Start using the Image Generation API today to unlock your creativity and effortlessly produce dynamic images for various use cases. Whether you're designing personalized greeting cards, generating visual content for social media, or enhancing your application's visuals, this API has you covered.

**API Endpoint:** `https://api.example.com/image/generate`

For detailed usage instructions and supported parameters, refer to the API documentation.

Enhance your applications with vibrant and personalized images using the Image Generation API! 🖼️🚀
