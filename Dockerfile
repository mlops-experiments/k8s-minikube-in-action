FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy source code
COPY src/ src/
COPY requirements.txt .


# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose Streamlit default port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "src/app.py"]