With the rise of Generative AI applications, traditional software testing methods are no longer sufficient for validating AI outputs. DeepEval offers a structured framework to evaluate and test LLM-powered applications by assessing key metrics such as response quality, accuracy, and relevance.
Firstly, we can understand how LLM evaluation works, and learn how it can be used to build reliable AI-powered applications.
DeepEval is an open-source, python native evaluation framework designed for unit testing and measuring the quality, reliability and regressions of large language model (LLM) applications, RAG pipelines and AI agents.

We can do various type of testing using DeepEval. 

Correctness Testing, Answer Relevancy Testing, Hallucination Testing, Safety Testing, Bias Testing, Summarization Testing

then we should  configure Ollama and Llama 3.2 to run a local Large Language Model (LLM) environment for AI testing with DeepEval. 

next, we should download and install ollama to our machine. then, we can download a model and use it by running it through Ollama. 

Go to the ollama.com website -> Click Models -> search and select llama3.2

for download the llama3.2 , Go to the PowerShell and type, "ollama pull llama3.2" and enter.

for check whether it is download successfully, we can check that using "ollama list" command.

After that we will see how to run downloaded llama3.2. use this command. "ollama run llama3.2"

then we can ask any question , before that we can add website link which we needed to use. 

eg-: Give me test cases for https://staging.coachtribe.co/auth/register

next enter, 
It's start Automatically write test cases for particular part.



