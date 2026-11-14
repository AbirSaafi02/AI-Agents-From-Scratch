from src.llm import LLM
from src.agent import TinyAgent

llm = LLM(model="qwen2.5:7b")
agent = TinyAgent(llm=llm)

response = agent.run("What is 2 + 2?")
print("Answer:", response)
print("\nTrajectory:", agent.trajectory.runs)