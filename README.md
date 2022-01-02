# Mooney

example backend for a personal transaction manager app in python

### How to run (for noobz)

- install linux 🙃 ([click here for easy guide](https://wiki.gentoo.org/wiki/Handbook:AMD64)) or do it youself on windows

- install python (^3.10) and poetry

- clone the repo and open terminal at project root (base folder, "mooney" in this case)

- [create and activate virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)

- install deps 
  ```bash
  poetry install
  ```

- run with uvicorn
    ```bash
    uvicorn app.main:app --reload
    ```
- run with gunicorn
    ```bash
    gunicorn app.main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 127.0.0.1:8000
    ```
    (this is how i use it, u can modify command according to your needs)

- open ```/docs``` path to open Swagger UI to test the backend
  
  (for eg. [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) or [http://localhost:8000/docs](http://localhost:8000/docs))