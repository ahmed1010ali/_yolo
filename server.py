from model import YoloModel
from PIL import Image
import io 
from fastapi.responses import StreamingResponse
from fastapi import FastAPI, UploadFile, File


app = FastAPI()
model = YoloModel()


@app.get("/")
async def root ():
    return{"message": "hello from fastapi"}


@app.post("/process_image/")
async def process_image (file: UploadFile = File(...)):
    image_data = await file.read()
    input_image = Image.open(io.BytesIO(image_data))

    output_image = model.predict(input_image)

    output_buffer  = io.BytesIO()
    output_image.save(output_buffer, format="JPEG")
    output_buffer.seek(0)
    return StreamingResponse(output_buffer, media_type="image/jpeg")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
