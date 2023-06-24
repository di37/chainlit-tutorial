# Basic Chainlit Demo

This is just basic demo to show how LLM agents can be shown in crispy User Interface. Chainlit library helps us accomplishing that in seconds. Modify the code in `main.py` file and the python scripts in utils folder - `constants.py` and `helper.py`.

To spin up Chainlit on web browser

```bash
chainlit run main.py -w --port 3000
```

### Running the Image on Docker

- On the terminal command, run `sudo docker-compose up` for building and running the image.
- To stop running the image and delete its container: `sudo docker-compose down`.
- For any code changes and is to be reflected in the docker image: `sudo docker-compose build`.

### References

- Build Python LLM apps in minutes Using Chainlit ⚡️ - https://www.youtube.com/watch?v=tv7rn5AsxFY&t=580s
- Chainlit Documentation: https://docs.chainlit.io/langchain
