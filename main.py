import tkinter as tk
import requests

def get_webpage(url):
  """Fetches the HTML content of a website using requests."""
  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-200 status codes
    return response.text
  except requests.exceptions.RequestException as e:
    return f"Error: {e}"  # Handle network errors

def display_webpage(url):
  """Fetches and displays the HTML content in the UI."""
  content = get_webpage(url)
  # Process and format the HTML content (basic formatting for readability)
  formatted_content = content.replace("<br>", "\n")  # Replace br tags with newlines

  # Create a tkinter window and label to display the content
  root = tk.Tk()
  root.title(f"Simple Browser - {url}")
  label = tk.Label(root, text=formatted_content)
  label.pack()
  root.mainloop()

def main():
  """Entry point for user input and webpage display."""
  root = tk.Tk()
  root.title("Simple Browser")

  url_label = tk.Label(root, text="Enter URL:")
  url_label.pack()

  url_entry = tk.Entry(root)
  url_entry.pack()

  def browse_button_click():
    url = url_entry.get()
    display_webpage(url)

  browse_button = tk.Button(root, text="Browse", command=browse_button_click)
  browse_button.pack()

  root.mainloop()

if __name__ == "__main__":
  main()
