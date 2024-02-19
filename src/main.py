import asyncio
import time
import webbrowser
from web_app import MyApp
import sqlalchemy

async def run_flask_app():
    my_app = MyApp()
    my_app.app.run(debug=True, port=5005, use_reloader=False)

def open_browser():
    url = "http://localhost:5005"
    webbrowser.open(url)

def run_web_app():
    # Create an event loop
    loop = asyncio.get_event_loop()

    try:
        # Run Flask app in an asynchronous event loop
        flask_task = loop.create_task(run_flask_app())

        # Wait for a moment to ensure the Flask app is up and running
        time.sleep(1)

        # Open the browser
        open_browser()

        # Run the event loop until the task completes
        loop.run_until_complete(flask_task)
    except KeyboardInterrupt:
        print("GoodBye !!!")
    finally:
        # Close the event loop
        loop.close()

def run():

    run_web_app()


if __name__ == '__main__':
    run()

    print("sqlalchemy version:  ", sqlalchemy.__version__)
