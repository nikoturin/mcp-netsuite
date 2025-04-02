import asyncio
import streamlit as st
import os
from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_community.chat_models import ChatOllama
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-4o",temperature=0, openai_api_key=os.getenv('OPENAI_API_KEY'))
# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="python",
    args=["/opt/mcp/server/server.py"],
)

async def run_client_poc(user_input):
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read,write) as session:
            # Initialize the connection
            await session.initialize()

            # Get tools
            tools = await load_mcp_tools(session)

            # Create and run the agent
            agent = create_react_agent(model, tools)
            agent_response = await agent.ainvoke({"messages": user_input})
            return agent_response

st.set_page_config(
    page_title="MCP",
)

st.title("STREAMLIT + OPENAI + MCP + NETSUITE")

# Campo de entrada de texto para el usuario
user_input = st.text_input("Búsqueda información de Transacciones:")

# Botón para enviar el mensaje
if st.button("Enviar"):
    # Obtener la respuesta del modelo Mistral
    response=asyncio.run(run_client_poc(user_input),debug=True)
    st.text_area("Respuesta:", value=response, height=200)
    #Mostrar la respuesta en la interfaz

# Instrucciones para el usuario
st.markdown("### Instrucciones:")
st.markdown("- Escribe tu mensaje en el campo de texto.")
st.markdown("- Haz clic en el botón 'Enviar' para obtener una respuesta.")
st.markdown("Beta Versión para Naviera++")
