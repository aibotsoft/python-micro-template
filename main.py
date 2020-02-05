from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.api_route("/api_route")
def non_operation():
    return {"message": "Hello World"}


def non_decorated_route():
    return {"message": "Hello World"}


app.add_api_route("/non_decorated_route", non_decorated_route)


if __name__ == '__main__':
    print('hello')
