#mood response module
def mood_response(mood):
    responses = {
        'happy': "I'm glad to hear you're feeling happy! 😊",
        'sad': "I'm sorry you're feeling sad. I hope things get better soon. 😔",
        'excited': "That's great! Excitement is wonderful! 🎉",
        'angry': "I'm sorry to hear that. Take a deep breath and try to calm down. 😠",
        'bored': "Sometimes a change of activity can help with boredom. Try something new! 😐"
    }
    return responses.get(mood.lower(), "Sorry, I don't recognize that mood.")