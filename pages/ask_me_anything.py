import streamlit as st

from clarifai.client.auth import create_stub
from clarifai.client.auth.helper import ClarifaiAuthHelper
from clarifai.client.user import User
from clarifai.modules.css import ClarifaiStreamlitCSS

st.set_page_config(layout="wide")
ClarifaiStreamlitCSS.insert_default_css(st)

# This must be within the display() function.
auth = ClarifaiAuthHelper.from_streamlit(st)
stub = create_stub(auth)
user_app_id = auth.get_user_app_id_proto()
user_app = User(user_id=user_app_id.user_id).app(app_id=user_app_id.app_id)

st.title("Ask Me Anything")

workflow_id = os.environ['CLARIFAI_WORKFLOW_ID']
if not workflow_id:
    all_workflows = user_app.list_workflows()
    all_workflow_ids = []
    for workflow in all_workflows:
        all_workflow_ids.append(workflow.id)
    workflow_id = st.selectbox("Assistant", all_workflow_ids)

detail = st.checkbox("Detail Answers",
                     help="Request the assistant to provide more details when providing answers",
                     value=True)

messages = st.container(height=200)
if prompt := st.chat_input("Ask something"):
    messages.chat_message("user").write(prompt)
    if detail:
        prompt += "\nPlease provide more details when providing answer."
    with st.spinner(text="Predicting..."):
        answer_response = user_app.workflow(workflow_id).predict_by_bytes(
            input_bytes=bytes(prompt, 'utf-8'),
            input_type='text',
        )
    answer = answer_response.results[0].outputs[-1].data
    if answer.text:
        answer = answer.text
        if answer.raw:
            answer = answer.raw
    messages.chat_message("assistant").write(answer)

