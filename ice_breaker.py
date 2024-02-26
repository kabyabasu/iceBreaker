# from typing import Tuple
# from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
# from agents.twitter_lookup_agent import lookup as twitter_lookup_agent
# from chains.custom_chains import (
#     get_summary_chain,
#     get_interests_chain,
#     get_ice_breaker_chain,
# )
# from third_parties.linkedin import scrape_linkedin_profile

# from third_parties.twitter import scrape_user_tweets
# from output_parsers import (
#     summary_parser,
#     topics_of_interest_parser,
#     ice_breaker_parser,
#     Summary,
#     IceBreaker,
#     TopicOfInterest,
# )


# def ice_break_with(name: str) -> Tuple[Summary, IceBreaker, TopicOfInterest, str]:
#     linkedin_username = linkedin_lookup_agent(name=name)
#     linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username)

#     twitter_username = twitter_lookup_agent(name=name)
#     tweets = scrape_user_tweets(username=twitter_username)

#     summary_chain = get_summary_chain()
#     summary_and_facts = summary_chain.run(
#         information=linkedin_data, twitter_posts=tweets
#     )
#     summary_and_facts = summary_parser.parse(summary_and_facts)

#     interests_chain = get_interests_chain()
#     interests = interests_chain.run(information=linkedin_data, twitter_posts=tweets)
#     interests = topics_of_interest_parser.parse(interests)

#     ice_breaker_chain = get_ice_breaker_chain()
#     ice_breakers = ice_breaker_chain.run(
#         information=linkedin_data, twitter_posts=tweets
#     )
#     ice_breakers = ice_breaker_parser.parse(ice_breakers)

#     return (
#         summary_and_facts,
#         interests,
#         ice_breakers,
#         linkedin_data.get("profile_pic_url"),
#     )

from dotenv import load_dotenv
import os

from langchain.chains import LLMChain
# from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

if __name__ == "__main__":
    print("Hello LLM")

    # # Attempt to get the environment variable, provide a default value or handle the error if not found
    # my_token = os.environ.get('My_Token', None)

    # if my_token is None:
    #     print("Error: 'My_Token' environment variable is not set.")
    #     # You can also set a default value or exit the script here
    # else:
    #     print(my_token)

    load_dotenv()
    # print(os.environ['My_Token'])
    information  = " Elon Reeve Musk (/ˈiːlɒn/; EE-lon; born June 28, 1971) is a businessman and investor. He is the founder, chairman, CEO, and CTO of SpaceX; angel investor, CEO, product architect, and former chairman of Tesla, Inc.; owner, executive chairman, and CTO of X Corp.; founder of the Boring Company and xAI; co-founder of Neuralink and OpenAI; and president of the Musk Foundation. He is the second wealthiest person in the world, with an estimated net worth of US$232 billion as of December 2023, according to the Bloomberg Billionaires Index, and $182.6 billion according to Forbes, primarily from his ownership stakes in Tesla and SpaceX.[5][6][7]\
        A member of the wealthy South African Musk family, Elon was born in Pretoria and briefly attended the University of Pretoria before immigrating to Canada at age 18, acquiring citizenship through his Canadian-born mother. Two years later, he matriculated at Queen's University at Kingston in Canada. Musk later transferred to the University of Pennsylvania, and received bachelor's degrees in economics and physics. He moved to California in 1995 to attend Stanford University, but dropped out after two days and, with his brother Kimbal, co-founded online city guide software company Zip2. The startup was acquired by Compaq for $307 million in 1999, and, that same year Musk co-founded X.com, a direct bank. X.com merged with Confinity in 2000 to form PayPal."
    
    summary_template = """ 
     given the information {information} about a person, I want to create:

     1. a short summary in one sentence.
     2. two interesting facts about them.
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"],template=summary_template)

    llm = ChatOpenAI(temperature = 0, model_name = "gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    result = chain.invoke(input={"information":information})

    print(result)
