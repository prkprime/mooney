# Mooney

Example backend for a personal transaction manager app in python

### How to run

- Please note, some instructions may vary if you're not using Linux

- Install python (^3.10) and poetry 

- Clone the repo and open terminal at project root (base folder, "mooney" in this case)

- [Create and activate virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)

- Install deps 
  ```bash
  poetry install
  ```

- Run with uvicorn
    ```bash
    uvicorn app.main:app --reload
    ```
- Run with gunicorn
    ```bash
    gunicorn app.main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 127.0.0.1:8000
    ```
    (this is how I use it, you can modify the command according to your needs)

- Open ```/docs``` path to open Swagger UI to test the backend
  - [Swagger](http://localhost:8000/docs)
  - You can also check out [ReDoc](http://localhost:8000/redoc) for an alternative way to view the documentation
