from abc import ABC, abstractmethod

class LLM(ABC):
    
    def __init__(self, name):
        self.name = name
        
    @abstractmethod
    def generate(self, prompt):
        pass
        
class OpenAIModel(LLM):
    def __init__(self, name):
        super().__init__(name)
    def generate(self, prompt):
        return f"OpenAIModel {prompt}"
    
class GeminiModel(LLM):
    def __init__(self, name):
        super().__init__(name)
    def generate(self, prompt):
        return f"GeminiModel {prompt}"

    
class AnthropicModel(LLM):
    def __init__(self, name):
        super().__init__(name)
    def generate(self, prompt):
        return f"AnthropicModel {prompt}"

    
# models = [OpenAIModel(), GeminiModel(), AnthropicModel()]

class ModelManager:
    
    def __init__(self):
        self.models = []
    
    def add_model(self, model):
        self.models.append(model)
    
    def list_models(self):
        return [model.name for model in self.models]
    
    def get_model(self, name):
        for model in self.models:
            if model.__class__.__name__ == name:
                return model
        raise ValueError(f"{name} not found")
    
    def generate(self, name, prompt):
        model = self.get_model(name)
        return model.generate(prompt)
            

manager = ModelManager()

manager.add_model(OpenAIModel("openai"))
manager.add_model(GeminiModel("gemini"))
manager.add_model(AnthropicModel("claude"))

allModels = manager.list_models()

print(allModels)
# response = manager.generate("GeminiModel", "Explain RAG")

# print(response)