using UnityEngine;
using UnityEngine.UI;
using System.IO;

public class DataCollector : MonoBehaviour
{
    // The input field for the user to enter their prompt
    public InputField promptInputField;

    // The file to save the collected data
    public string dataFilePath;

    // Save the user's input to a file
    public void SaveData()
    {
        // Get the user's input from the input field
        string prompt = promptInputField.text;

        // Open the file for writing
        StreamWriter writer = new StreamWriter(dataFilePath, true);

        // Write the prompt to the file
        writer.WriteLine(prompt);

        // Close the file
        writer.Close();
    }
}
