import ollama
from deepeval.test_case import LLMTestCase
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCaseParams
from deepeval.models import OllamaModel


# 01 Define the question
question = "What is the capital of Sri Lanka?"

# 02 Get response from the AI
response = ollama.chat(
    model = "llama3.2",
    messages = [
        {
            "role" : "User",
            "content" : question
        }
    ]
)

actual_answer = response["message"]["content"]

# 03 Create DeepEval TestCase
test_case = LLMTestCase(
    input = question,
    actual_output = actual_answer,
    expected_output = "The Capital of Sri Lanka is Sri Jayawardhanapura kotte."
)

# 04 Create GEval Metric
metric = GEval(
    name = "Check Actual and Expected",
    criteria = "Compare the actual answer with the expected answer.",
    evaluation_params=[
        LLMTestCaseParams.ACTUAL_OUTPUT,
        LLMTestCaseParams.EXPECTED_OUTPUT,
    ],
    model=OllamaModel(model="llama3.2"),
)

# 05 Run the metric
metric.measure(test_case);

# 06 Display
print("Score:", metric.score);
print("Reason:", metric.reason);