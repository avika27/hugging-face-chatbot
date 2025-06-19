Project Name- Chatbot With Hugging face 
(This project includes  making a Chatbot  using Hugging Face and Langchain . We have used the pipeline function () for completing the task of  text genaeration and it also includes  the CLI environment where chatbot can continously takes the input from users and  gracefully exit when it is not required and with the help of Langchain  it  also has a sliding window  where we store the last  5 interactions and based on that chatbot responds  )

Features:-
 Built  Using Hugging Face and  Langchain 
 Has a sliding window for storing upto last 5 interactions (Memory Block)
 Has a CLI for user interaction 
 Gracefully  terminates when user  types "exit" ,"bye"
 Simple and Clean  mmodular code structure   



Install Dependencies :- (Install the required Python packages)
[pip install langchain langchain_huggingface transformers huggingface_hub python-dotenv]

 Setting up the environment for huggingface API  key:-
(created a .env file in the same  directory where all my other  python files is being stored so  that  our huggingface API  key remainns secret )

[HUGGINGFACE_API_KEY=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
DB_PASSWORD=@lambo2703]

Run the chatbot  :-
 ( for running the  chatbot  use  this  command)
 {python interface.py}


 Sample  interaction Examples:-

 🤖 Chatbot is ready! Type your message (type 'exit' to quit):

You: what is the capital of India?
🤖 Chatbot: Delhi

You: what is apple?
🤖 Chatbot: Apple is a fruit.







  

---
