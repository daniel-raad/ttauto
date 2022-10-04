source venv/bin/activate

functions_framework --target=run_download

docker build -t "draad/tiktokcompiler" .
docker run draad/tiktokcompiler
