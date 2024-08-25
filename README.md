![Clarifai logo](https://www.clarifai.com/hs-fs/hubfs/logo/Clarifai/clarifai-740x150.png?width=240)

# Ask Me Anything

Chat with a bot. Ask them anything about your data.

## Setup Locally
1. Install requirements
   ```commandlinet
   pip install -r requirements.txt
   ```
2. Setup environment variables or update `pages/ask_me_anything.py` to overwrite environment variables directly in the script
   ```python
    import os
    os.environ['CLARIFAI_USER_ID'] = 'USER-ID'
    os.environ['CLARIFAI_APP_ID'] = 'APP-ID'
    os.environ['CLARIFAI_PAT'] = 'PAT'
   ```

## How To Run Locally
1. `cd ~/PycharmProjects/clarifai-module-chat`
2. `streamlit run pages/ask_me_anything.py`
