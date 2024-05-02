from django.db import models

import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, FinishReason
import vertexai.preview.generative_models as generative_models
import os
from dotenv import load_dotenv

load_dotenv()


class Generator:

    def __init__(self, text_prompt):
        self.text_prompt = text_prompt
        self.generation_config = {
            "max_output_tokens": 8192,
            "temperature": 1,
            "top_p": 0.95,
        }
        self.safety_settings = {
            generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        }

    def generate(self):
        vertexai.init(project=os.getenv("VERTEXAI_PROJECT"), location=os.getenv("VERTEXAI_LOCATION"))
        model = GenerativeModel(os.getenv("VERTEXAI_GENERATIVEMODEL"))
        responses = model.generate_content(
            ["""Kirk insists on a heightened standard for the task: \" """, self.text_prompt, """ Showcase your solution with meticulous detail through polished PlantUML C4 code.\” """],
            generation_config=self.generation_config,
            safety_settings=self.safety_settings,
            )
        return responses