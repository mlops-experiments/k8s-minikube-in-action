# k8s-minikube-in-action
Deployment of app in mini kube 


## To view streamlit app on a browser, run with 

```bash
streamlit run src/app.py
```

## Build docker image
```bash
docker build -t my-streamlit-app .
```

## Run the container, mapping port 8501
```bash
docker run -p 8501:8501 my-streamlit-app
```bash