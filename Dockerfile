from python:3.11.6
expose 8501
cmd mkdir -p /app
workdir /app
copy requirements.txt ./requirements.txt
run pip install -r requirements.txt
copy .. 
ENTRYPOINT ["streamlit", "run"]
CMD ["testdeployAzure.py"]