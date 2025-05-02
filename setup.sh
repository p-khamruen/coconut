#!/bin/bash
# สคริปต์ติดตั้ง ByteTrack

echo "Cloning ByteTrack repository..."
if [ ! -d "ByteTrack" ]; then
    git clone https://github.com/ifzhang/ByteTrack.git
else
    echo "ByteTrack directory already exists."
fi

cd ByteTrack

# แก้ไข requirements.txt ให้รองรับ onnx ที่ต้องการ
echo "Updating onnx version in ByteTrack requirements..."
sed -i 's/onnx==1.8.1/onnx==1.9.0/g' requirements.txt

# ติดตั้ง dependencies ของ ByteTrack
echo "Installing ByteTrack dependencies..."
pip install -r requirements.txt

# ติดตั้ง ByteTrack ในโหมดพัฒนา (develop)
echo "Running setup.py develop..."
python3 setup.py develop

# กลับไปยัง root ของ repository
cd ..
echo "ByteTrack setup complete."

