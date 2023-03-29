"""import wx
import openai

# Set up the OpenAI API credentials
openai.api_key = "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"

# Define the emotions and their corresponding characters
emotion_to_character = {
    "happy": "Character A",
    "angry": "Character B",
    "sad": "Character C",
    "frustrated": "Character D",
    "anxious": "Character E",
    "calm": "Character F"
}

class MainWindow(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Bionic Owls AI Game Assist", size=(600, 400))
        
        panel = wx.Panel(self)

        # Create the UI elements
        text_label = wx.StaticText(panel, label="How do you feel?")
        self.text_ctrl = wx.TextCtrl(panel)
        button = wx.Button(panel, label="Get Character")

        # Bind the button to the click event handler
        self.Bind(wx.EVT_BUTTON, self.on_button_click, button)

        # Create the layout
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(text_label, 0, wx.ALL, 5)
        vbox.Add(self.text_ctrl, 0, wx.ALL|wx.EXPAND, 5)
        vbox.Add(button, 0, wx.ALL|wx.CENTER, 5)
        
        panel.SetSizer(vbox)
        
    def on_button_click(self, event):
        description = self.text_ctrl.GetValue()
        character = get_character_from_emotion(description)
        wx.MessageBox(f"The character corresponding to the emotion is {character}", "Result", wx.OK | wx.ICON_INFORMATION)

def get_character_from_emotion(description):
    # Use the GPT-3 model to analyze the description and identify the emotion
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="classify the following text as happy, angry, sad, frustrated, anxious or calm:\n" + description + "\nemotion:",
        max_tokens=1,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Extract the emotion from the OpenAI API response
    emotion = response.choices[0].text.strip().lower()

    # Return the character corresponding to the identified emotion
    return emotion_to_character.get(emotion, "Unknown character")

if __name__ == "__main__":
    app = wx.App()
    frame = MainWindow()
    frame.Show()
    app.MainLoop()
    
    
"""




import wx
import openai

# Set up the OpenAI API credentials
openai.api_key = "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"

# Define the emotions and their corresponding characters
emotion_to_character = {
    "happy": "RBO",
    "angry": "EnemyRobot",
    "sad": "NBO",
    "frustrated": "Character D",
    "anxious": "Character E",
    "calm": "Character F"
}

class MainWindow(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Bionic Owls AI Game Assist", size=(600, 400))
        
        panel = wx.Panel(self)

        # Create the UI elements
        text_label = wx.StaticText(panel, label="How do you feel?")
        self.text_ctrl = wx.TextCtrl(panel)
        self.character_label = wx.StaticText(panel, label="")
        button = wx.Button(panel, label="Get Character")

        # Bind the button to the click event handler
        self.Bind(wx.EVT_BUTTON, self.on_button_click, button)

        # Create the layout
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(text_label, 0, wx.ALL, 5)
        vbox.Add(self.text_ctrl, 0, wx.ALL|wx.EXPAND, 5)
        vbox.Add(button, 0, wx.ALL|wx.CENTER, 5)
        vbox.Add(self.character_label, 0, wx.ALL|wx.CENTER, 5)
        
        panel.SetSizer(vbox)
        
    def on_button_click(self, event):
        description = self.text_ctrl.GetValue()
        character = get_character_from_emotion(description)
        self.character_label.SetLabel(f"The character corresponding to the emotion is {character}")

def get_character_from_emotion(description):
    # Use the GPT-3 model to analyze the description and identify the emotion
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="classify the following text as happy, angry, sad, frustrated, anxious or calm:\n" + description + "\nemotion:",
        max_tokens=1,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Extract the emotion from the OpenAI API response
    emotion = response.choices[0].text.strip().lower()

    # Return the character corresponding to the identified emotion
    return emotion_to_character.get(emotion, "Unknown character")

if __name__ == "__main__":
    app = wx.App()
    frame = MainWindow()
    frame.Show()
    app.MainLoop()

