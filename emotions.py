from emotions_dict import emotions

class Emotion(object):

    # match if a word is associated with an emotion
    def match_emotion(self, word):
        matched_emotions=[]
        for emo in emotions:
            if emo in word:
                matched_emotions.append(emotions[emo])
        return matched_emotions

    #text is a string
    def get_emotions_count(self, text):
        result=[]
        words = text.split(" ")
        for word in words:
            result.extend(self.match_emotion(word))
        
        emotion_count={}
        for x in set(result):
            emotion_count[x] = result.count(x)
        
        return emotion_count

    # prints detected emotions and their count in a text
    def get_emotions(self, text):
        emotion_count = self.get_emotions_count(text)
        output = ""
        
        for emo in emotion_count:
            output = output + emo+' : '+str(emotion_count[emo])+'; '
        
        return output