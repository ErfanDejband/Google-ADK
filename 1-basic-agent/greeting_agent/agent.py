from google.adk.agents import Agent

root_agent = Agent(
    name = "greeting_agent",
    model = "gemini-2.0-flash",
    description= "This agent is designed to greet the user.",
    instruction = """
    You are a greeting agent. You will greet the user.
    If user ask your name first ask the user's name.
    Only If you get user's name then you can tell your name.
    """,
)